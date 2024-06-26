import rclpy
from rclpy.node import Node
import time
import threading
from std_msgs.msg import String
import sys



class Node1(Node):
    def __init__(self):
        super().__init__("node1")
        self.timer1_ = self.create_timer(1.0, self.callback_timer1)
        self.sub1_ = self.create_subscription(String, '/rlrobot_msg', self.stop_callback, 10)
        self.stop_event = threading.Event()
        self.callback_timer1()
    def callback_timer1(self):
        
        while not self.stop_event.is_set():
            print("failed...")
            time.sleep(2.0)
            pass    
        self.get_logger().info("multi_thread done")



    def stop_callback(self, msg):
         
        if "cancel" in msg.data:
            self.stop_event.set()
            self.get_logger().info("topic sub") 
        

# class Node2(Node):
#     def __init__(self):
#         super().__init__("node2")
#         self.timer1_ = self.create_timer(1.0, self.callback_timer1)


#     def callback_timer1(self):
#          time.sleep(2.0)
#          self.get_logger().info("cb 2") 

def main(args=None):
    rclpy.init(args=args)
    stop = Node1()
    print('start')
    
    try:
        rclpy.spin(stop)
        #rclpy.spin(posehandle_node)
    except KeyboardInterrupt:
        stop.get_logger().info('==== Server stopped cleanly ====')
    except BaseException:
        stop.get_logger().info('!! Exception in server:', file=sys.stderr)
        raise
    finally:
        # (optional - Done automatically when node is garbage collected)
        rclpy.shutdown()

    print('finish')

if __name__ == '__main__':
    main()