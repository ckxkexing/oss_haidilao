#!/usr/bin/env ruby

require 'yaml'
require 'sequel'
require 'rugged'
require 'parallel'
require 'thread'
require 'mongo'
require 'linguist'
require 'json'

require_relative 'utils/commits'
require_relative 'utils/files'
require_relative 'utils/lines'
require_relative 'utils/git'
require_relative 'utils/logger'
require_relative 'utils/semaphore'
require_relative 'utils/rugged_handler'
require_relative 'utils/comments'
require_relative 'utils/db'

require_relative 'utils/languages/go'

require_relative 'sql_tables/sloc'

class SlocExtraction
	include Lines
	include Files
	include Commits
	include Git
	include LoggerUtil
	include Semaphore
	include RuggedHandler
	include Comments
	include DB
	include Table_sloc

	THREADS = 1

    attr_accessor :config, :owner, :lang, :repo

    def initialize(owner, repo, lang)
        self.owner = owner
        self.repo  = repo
        self.lang = lang
        self.config = YAML.load_file("configs.yaml")

		# create table `sloc`
		Table_sloc.create_table(db)
    end 

	def run(argv = ARGV)
		leader
		log "finish"
	end

	def runner(commit)
		src_lines(commit)
	end

	# Process sloc for a commit in a repo
	# the function to start handling a repo commit
	def leader
		interrupted = false

        case lang
            when /dart/i then self.extend(DartData)
            when /sass/i then self.extend(SassData)
            when /php/i  then self.extend(PHPData)
            when /ruby/i then self.extend(RubyData)
            when /javascript/i then self.extend(JavascriptData)
            when /typescript/i then self.extend(TypescriptData)
            when /java/i then self.extend(JavaData)
            when /python/i then self.extend(PythonData)
            when /go/i then self.extend(GoData)
            when /c/i  then self.extend(CCData)
            when /shell/i then self.extend(ShellData)
            else 
				abort("Error: language missing")
        end

        cmts = get_repo_latest_commit(10)

        cmts_completed = Table_sloc.all(db).map{|x| x[:commit]}
        cmts = cmts.reject { |x| cmts_completed.include?(x) }

		do_sloc = Proc.new do |commit|
			begin
				r = runner(commit)
				Table_sloc.insert(db, owner, repo, commit, r)
				
				if r.nil?
				else
					log "#{commit} #{r}", 1
					r
			end
			rescue StandardError => e
			log "Error processing #{owner} #{repo} #{commit} :#{e.message}"
			log e.backtrace
			#raise e
			end
		end

		results = Parallel.map(cmts, :in_threads => THREADS) do |cmt|
			if interrupted
				raise Parallel::Kill
			end
			do_sloc.call(cmt)
		end
	end
end


sloc = SlocExtraction.new(ARGV[0], ARGV[1], ARGV[2])
sloc.run
