from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqitle.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"  # super key
terminal = guess_terminal("kitty")

keys = [
    #  Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus to down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus to up")
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),  # Is it really necessary?

    #  Moving windows between left/right columns or move up/down in current stack
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window to the down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window to the up"),

    #  Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window to the down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window to the up"),
    Key([mod], "backspace", lazy.layout.normalize(), desc="Reset all window sizes"),
