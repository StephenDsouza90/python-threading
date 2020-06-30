# Threading

In multi-threading, multiple things can happen simultaneously because every thread can execute a specific task. But as these threads run on a single processor, the program will only appear to be doing multiple things because they share the processing speed. Tasks that spend much of their time waiting for external events are good candidates for threading. As the task is waiting, it can temporarily be suspended allowing more processing speed for other tasks to run.

## The Producer-Consumer Problem

In an app, there could be multiple users sending or receving requests to and from the server. The app could also be storing or retriving data from the datebase. If the app runs on a single-thread, every task would be performed on this thread, therefore if the number of users increase, the app would run slow. 

To speed-up the app, multiple threads can be used where each thread performs a specific task. In multi-threading, the most common use case for threading is the **Producer-Consumer Problem**. The Producer `producer()` listens for incomming requests from the users, it accepts the requests and stores it in a Pipeline. The Pipeline is the bridge between the producer and consumer because it can temporarily hold the requests till it is consumed. The Consumer `consumer()` receives the requests from the Pipeline and processes it.

## The App

**Producer :** The `producer()` pretends to listen for requests from the users. In this case, the users are asked how many student names they wish to enter into the database and then the users provides those names. The names are then passed on to the Pipeline so that the producer can listen and accept more requests. 

**Pipeline :** As the requests comes, the producer passes it to the `Pipeline` which holds the requests temporarily till the consumer can consume it. When the consumer consumes the request, the Pipeline is made free to accept and hold more requests.

**Consumer :** The `consumer()` pretends to store the requests from the users into the database. In this case, the database is presented in the form of a list. The consumer gets the requests from the Pipeline and stores it in the list.

The Producer-Consumer Scenario can be implemented in a number of ways. Two ways of implementing the Producer-Consumer Problem are show-cased in the `Threading_using_locks.py` and `Threading_using_queue_and_events.py`.

### Threading using locks

In this app, the `Pipeline` uses locks to manage the flow of data between the consumer and procuder. Since both the consumer and producer share the same data, in order to avoid the overlap between them, the procuder sends a signal `release()` to the consumer to consume the data and vice versa the consumer sends a signal to the producer to accept more request.

When the producer gets the lock via `acquire()`, the producer will pass the data in the Pipeline and when the consumer will get the lock via `acquire()` the consumer will get the data from the Pipeline and store it in the database. 

In this case, the drawback is that the Pipeline can only hold one data at a time.

### Threading using queue and events

In this app, the `Pipeline` inherits the `Queue` class, therefore allowing the Pipeline to hold more data. The passing of the data from the producer to the consumer is handled via the `put()` and `get()` methods, where the producer uses `put()` to put data into the queue and the consumer uses `get()` to get data from the queue.