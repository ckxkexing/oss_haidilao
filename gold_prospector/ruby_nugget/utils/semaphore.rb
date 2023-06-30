module Semaphore

    def semaphore_log
      @semaphore_log ||= Mutex.new
      @semaphore_log
    end

    def semaphore_read
      @semaphore_read ||= Mutex.new
      @semaphore_read
    end
  
  end