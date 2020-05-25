import queue
import threading
import concurrent.futures


list_of_student_names = []


class Pipeline(queue.Queue):
    """

    Pipeline allows multiple element using the Queue
    between producer and consumer.

    """

    def __init__(self):
        super().__init__(maxsize=3)

    def set_message(self, student_name):
        self.put(student_name)

    def get_message(self):
        student_name = self.get()
        return student_name


def producer(pipeline, event, number):
    """
    
    Gets the student name(s) from the user(s). 
    
    """

    for _ in range(number):
        student_name = input("Student Name: ")
        pipeline.set_message(student_name)

    event.set()


def consumer(pipeline, event):
    """

    Store the student name(s) in a list.

    """

    while not event.is_set() or not pipeline.empty():
        student_name = pipeline.get_message()
        list_of_student_names.append(student_name)


def main():

    print("\nHow many student names do you wish to enter?")
    number = int(input())

    pipeline = Pipeline()
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event, number)
        executor.submit(consumer, pipeline, event)

    print(list_of_student_names)    


if __name__=="__main__":
    main()