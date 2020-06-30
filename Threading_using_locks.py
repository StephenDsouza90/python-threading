import threading
import concurrent.futures


SENTINEL = object()
list_of_student_names = []


class Pipeline:
    """

    Pipeline allows a single element between producer and consumer.

    """

    def __init__(self):
        self.student_name = None
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def set_message(self, student_name):
        self.producer_lock.acquire()
        self.student_name = student_name
        self.consumer_lock.release()

    def get_message(self):
        self.consumer_lock.acquire()
        student_name = self.student_name
        self.producer_lock.release()
        return student_name


def producer(pipeline, number):
    """
    
    Gets the student name(s) from the user(s). 
    
    """

    for _ in range(number):
        student_name = input("Student Name: ")
        pipeline.set_message(student_name)

    # Send a sentinel message to tell consumer we are done
    pipeline.set_message(SENTINEL)


def consumer(pipeline):
    """
    
    Store the student name(s) in a list.
    
    """
    
    student_name = None
    while student_name is not SENTINEL:
        student_name = pipeline.get_message()
        if student_name is not SENTINEL:
            list_of_student_names.append(student_name)


def main():

    print("\nHow many student names do you wish to enter?")
    number = int(input())

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, number)
        executor.submit(consumer, pipeline)
    
    print(list_of_student_names)


if __name__=="__main__":
    main()