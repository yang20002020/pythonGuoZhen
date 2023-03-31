import time

class DigitClock:
    """
    数字时钟  定义类
    """

    def __init__(self):
        """
        初始化方法
        """
        cur_time = time.localtime()
        self._hour = cur_time.tm_hour
        self._minute = cur_time.tm_hour
        self._second = cur_time.tm_sec

    def run(self):
        """
        时钟行走方法

        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1

        if self._minute == 60:
            self._minute = 0
            self._hour += 1
        if self._hour == 24:
            self._hour = 0

    def show(self):
        """
        显示时间

        """
        return f"{self._hour}:{self._minute}:{self._second}"


def main():
    myclock = DigitClock()
    # 走10步 自动停止
    steps = 10
    for _ in range(steps):
        print(myclock.show())
        time.sleep(1)
        myclock.run()


main()
