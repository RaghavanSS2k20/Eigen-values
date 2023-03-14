import threading

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

class MyThread(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n

    def run(self):
        print("Factorial of {} is {}".format(self.n, factorial(self.n)))

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    t = MyThread(n)
    t.start()
