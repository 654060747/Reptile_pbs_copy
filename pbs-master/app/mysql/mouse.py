# encoding: utf-8
import time

# 1、pip install pynput pymouse
# 2、修改pymouse的安装路径打开__init__.py文件；把92行的windows改为pymouse.windows
# 3、pip install pypiwin32
# 4、进入https://www.lfd.uci.edu/~gohlke/pythonlibs/这里下载pyHook，这里比较恶心，找python对应的32位或64位及对应版本
# 5、pip install C:\Users\dell\Desktop\pyHook-1.5.1-cp37-cp37m-win32.whl（pyHook下载的本地路径）

from pynput import mouse
from pymouse import PyMouse


class Orbit(object):

    def __init__(self, min_x=-10000, min_y=-10000, max_x=10000, max_y=10000, ):
        """可以设置滑动轨迹的范围，x轴和y轴移动的最小值和最大值。

        """

        # 默认的鼠标左键是松开的
        self.left_pressed = False

        self.mouse_x, mouse_y = 0, 0

        self.mouse_list = []

        self.min_x = min_x

        self.min_y = min_y

        self.max_x = max_x

        self.max_y = max_y
        self.jl = []

    def on_move(self, x, y):

        """移动鼠标时会触发这个函数。

        x，y为鼠标的绝对坐标。

        """

        # 当按下鼠标左键的时候开始打印轨迹，松开时结束。

        if self.left_pressed:
            # 打印和记录的是移动的相对距离。

            # print(f"({x - self.mouse_x}, {y - self.mouse_y})")
            x, y = PyMouse().position()
            print(x, y)

            self.mouse_list.append((x, y))

    def on_click(self, x, y, button, pressed):

        """点击鼠标时会触发这个函数。

        x，y为鼠标的绝对坐标。button为点击的左键还是右键。pressed为鼠标的按压状态，按下时为True。

        """

        print('pressed:', pressed, 'button: ', button)

        # 按下鼠标左键开始记录鼠标轨迹。

        if str(button) == "Button.left" and pressed:
            self.left_pressed = True

            self.mouse_x = x

            self.mouse_y = y

            self.mouse_list = []

            # 松开鼠标左键的饰扣开始打印轨迹。

        if str(button) == "Button.left" and not pressed:
            self.left_pressed = False

        if self.mouse_list and self.min_x < self.mouse_list[-1][0] < self.max_x and self.min_y < self.mouse_list[-1][
            1] < self.max_y:
            self.jl.append(self.mouse_list)
            print(self.mouse_list)

        # 按下鼠标右键的时候停止记录鼠标轨迹。

        if str(button) == "Button.right" and pressed:
            with open('move.txt', 'w', encoding='utf-8', errors="ignore") as fo:
                for i in self.mouse_list:
                    fo.write(str(i) + '\n')
                fo.flush()
            return False

    def start(self):
        with mouse.Listener(on_move=self.on_move, on_click=self.on_click) as listener:
            listener.join()
            # 需要监听的鼠标事件。
            listener = mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                suppress=False
            )
            # 开始监听
            listener.start()


if __name__ == '__main__':
    # 第一步解开注释记录鼠标状态
    # move_track = Orbit(min_x=1920, max_x=1920, min_y=1080, max_y=1080)
    # move_track.start()
    
    # 第二步即可运行第一步鼠标记录的状态
    m = PyMouse()
    with open('move.txt', 'r') as fo:
        for i in fo:
            m.move(eval(i)[0], eval(i)[1])
            time.sleep(0.01)
    m.position()  # 获取当前坐标的位置
    # 鼠标移动到xy位置
