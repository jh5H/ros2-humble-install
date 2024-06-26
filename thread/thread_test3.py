import rclpy
from rclpy.node import Node
import time
from threading import Event, Thread
from std_msgs.msg import String
import sys
from rclpy.executors import MultiThreadedExecutor

class eventy:
    stop_event = Event()
    new_event = Event()


class Node1(Node):
    def __init__(self):
        super().__init__("node1")
        #self.sub1_ = self.create_subscription(String, '/rlrobot_msg', self.stop_callback, 10)
        # self.stop_event = Event()
        # self.new_event = Event()
        #self.callback_timer1()
        #self.create_timer(1.0, self.sibar_callback)
        self. callback_timer1()
    def callback_timer1(self):
        while not eventy.stop_event.is_set():
            print("failed..")
            if eventy.new_event.wait(0.1):
                eventy.new_event.clear()

                print('...')

            time.sleep(0.001)
        self.get_logger().info("multi_thread done")
        return


class Node2(Node):
    def __init__(self):
        super().__init__("node2")
        self.sub1_ = self.create_subscription(String, '/rlrobot_msg', self.stop_callback, 10)
        # self.stop_event = Event()
        # self.new_event = Event()
        #self.callback_timer1()
        #self.create_timer(1.0, self.sibar_callback)
        #self. callback_timer1()
        self.stop_callback()
    def stop_callback(self, msg):
        print("hi")
        if 'cancel' in msg.data:
            thread = Thread(target=Node1.callback_timer1, args=(eventy.stop_event, eventy.new_event))
            thread.start()
            eventy.stop_event.set()
            print("cancel data subscribed")
            #for i in range(5):
            eventy.new_event.set()
            time.sleep(1)
            thread.join()

        else:
            print("can't find cancel command")
    # def stop_callback(self, msg):
    #     lvmsg = msg.data.split()
    #     print('subs') 
    #     if "cancel" in lvmsg:
    #         if self.thread is None or not self.thread.is_alive():
    #             self.thread = Thread(target=self.callback_timer1)
    #             self.thread.start()
    #         self.get_logger().info("topic sub")
    #         self.stop_event.set()

def main(args=None):
    rclpy.init(args=args)
    stop1 = Node1()
    stop2 = Node2()
    executor = MultiThreadedExecutor()
    executor.add_node(stop2)
    executor.add_node(stop1)
    print('start')
    try:
        executor.spin()
    except KeyboardInterrupt:
        executor.get_logger().info('==== Server stopped cleanly ====')
    # except stop.stop_event.is_set():
    #     executor.get_logger().info('==== Server stopped cleanly ====')
    #     rclpy.shutdown()         
    except BaseException:
        executor.get_logger().info('!! Exception in server:', file=sys.stderr)
        raise
    finally:
        rclpy.shutdown()
    print('finish')

if __name__ == '__main__':
    main()

