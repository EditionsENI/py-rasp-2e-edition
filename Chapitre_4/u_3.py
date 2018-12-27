import urwid
import time
import sys


class CountDown:
    def __init__(self, seconds):
        self.seconds = seconds
        self.palette = [
            ('start', 'yellow', ''),
            ('finish', 'dark red', '')
        ]
        self.alarm = None

    def main(self):
        self.setup_view()
        self.main_loop = urwid.MainLoop(
            self.view,
            palette=self.palette,
            unhandled_input=self.keypress
        )
        self.alarm = self.main_loop.set_alarm_in(1, self.start)
        self.main_loop.run()

    def keypress(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def setup_view(self):
        text = time.strftime('%H:%M:%S', time.gmtime(self.seconds))
        if self.seconds > 3:
            color = 'start'
            font = urwid.font.HalfBlock6x5Font()
        else:
            color = 'finish'
            font = urwid.font.HalfBlockHeavy6x5Font()
        self.count_text = urwid.BigText(text, font)
        self.view = urwid.Padding(self.count_text, 'center', width='clip')
        self.view = urwid.AttrMap(self.view, color)
        self.view = urwid.Filler(self.view, 'middle')

    def start(self, loop=None, data=None):
        self.seconds = self.seconds - 1
        self.setup_view()
        if self.seconds < 0:
            raise urwid.ExitMainLoop()
        loop.widget = self.view
        self.alarm = loop.set_alarm_in(1, self.start)


if __name__ == '__main__':
    try:
        seconds = int(sys.argv[1])
        c = CountDown(seconds)
        c.main()
    except Exception as KeyboardInterrupt:
        pass
