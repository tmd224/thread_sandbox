import threading
import time

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def join(self, *args, **kwargs):
        self.stop()
        super(StoppableThread,self).join(*args, **kwargs)

    def run()
        print "Running Thread"
        while not self._stop_event.is_set():
            print "Still running!" 
            time.sleep(2)
        print "stopped"
        

def thread_func():
    print "Hello"
    
if __name__=="__main__":
    t1 = StoppableThread(target=thread_func)
    try:
        t1.start()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
        t1.join()
        
    