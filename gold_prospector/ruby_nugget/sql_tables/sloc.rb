
module Table_sloc

    def self.create_table(db)
        unless db.table_exists?(:sloc)
            db.create_table :sloc do
              column :owner, String
              column :repo, String
              column :commit, String
              column :sloc, Integer
            end
          end
    end

    def self.count(db)
        db[:sloc].count
    end

    def self.insert(db, owner, repo, commit, sloc)
        db[:sloc].insert(owner, repo, commit, sloc)
    end

    def self.all(db)
        db[:sloc].all
    end

end
