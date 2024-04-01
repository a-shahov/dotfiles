from contextlib import suppress

from libqtile import bar, layout, qtile, widget
from libqtile.config import Group, Match, Screen
from libqtile.config import EzKey as Key, EzClick as Click, EzDrag as Drag
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger


terminal = guess_terminal("kitty")
    
@lazy.function
def toggle_layout(qtile, layout_name, layouts, prev_layout_map={}):
    current_layout_map = {
        (qtile.current_screen.index, qtile.current_group.name): qtile.current_layout.name,
    }
    prev_layout_name = prev_layout_map.get(list(current_layout_map.keys()).pop(), None)

    if layout_name != qtile.current_layout.name:
        for layout in layouts:
            if layout_name == layout.name:
                if qtile.current_layout.name not in ("zoomy", "max"):
                    prev_layout_map.update(current_layout_map)
                qtile.to_layout_index(layouts.index(layout))
                return

    if prev_layout_name:
        for layout in layouts:
            if prev_layout_name == layout.name:
                qtile.to_layout_index(layouts.index(layout))
                return
 
layouts = [
    layout.Columns(grow_amount=15, border_width=2),
    layout.TreeTab(
        place_right=True, border_width=2,
        sections=["social", "youtube", "docs", "other"],
    ),
    layout.Stack(num_stacks=2, border_width=2),
    layout.Zoomy(border_width=2),
    layout.Max(),
]

keys = [
    # Columns layout
    Key("M-h", lazy.layout.left()),
    Key("M-l", lazy.layout.right()),
    Key("M-j", lazy.layout.down()),
    Key("M-k", lazy.layout.up()),
    Key("M-S-h", lazy.layout.shuffle_left()),
    Key("M-S-l", lazy.layout.shuffle_right()),
    Key("M-S-j", lazy.layout.shuffle_down()),
    Key("M-S-k", lazy.layout.shuffle_up()),
    Key("M-C-h", lazy.layout.grow_left(), lazy.layout.move_left().when(layout="treetab")),
    Key("M-C-l", lazy.layout.grow_right(), lazy.layout.move_right().when(layout="treetab")),
    Key("M-C-j", lazy.layout.grow_down(), lazy.layout.move_down()),
    Key("M-C-k", lazy.layout.grow_up(), lazy.layout.move_up()),
    Key("M-S-C-h", lazy.layout.swap_column_left()),
    Key("M-S-C-l", lazy.layout.swap_column_right()),
    Key("M-<backspace>", lazy.layout.normalize()),

    # Stack layout
    Key("M-<space>", lazy.layout.next()),
    Key("M-S-<space>", lazy.layout.previous()),
    Key("M-S-<return>", lazy.layout.toggle_split()),
    Key("M-r", lazy.layout.rotate()),

    # TreeTab layout
    Key("M-u", lazy.layout.section_down()),
    Key("M-i", lazy.layout.section_up()),

    # Shortcuts for layouts
    Key("M-z", toggle_layout("zoomy", layouts)),
    Key("M-x", toggle_layout("max", layouts)),
    
    # Common key bindings
    Key("M-<return>", lazy.spawn(terminal)),
    Key("M-<tab>", lazy.next_layout()),
    Key("M-S-<tab>", lazy.prev_layout()),
    Key("M-w", lazy.window.kill()),
    Key("M-f", lazy.window.toggle_fullscreen()),
    Key("M-t", lazy.window.toggle_floating()),
    Key("M-n", lazy.spawncmd()),
    Key("M-C-q", lazy.shutdown()),
    Key("M-C-r", lazy.reload_config()),
    Key("M-S-z", lazy.screen.prev_group()),
    Key("M-S-x", lazy.screen.next_group()),
]

groups = [
    Group("1", spawn=[], layout="columns", matches=[], label="home"),
    Group("2", spawn=[], layout="columns", matches=[], label="tty"),
    Group("3", spawn=[], layout="treetab", matches=[], label="www"),
    Group("4", spawn=[], layout="stack", matches=[], label="pdf"),
    Group("5", spawn=[], layout="columns", matches=[], label="dev"),
    Group("6", spawn=[], layout="columns", matches=[], label="vrt"),
    Group("7", spawn=[], layout="columns", matches=[], label="oth"),
]

for group in groups:
    keys.extend(
        [
            Key(f"M-{group.name}", lazy.group[group.name].toscreen()),
            Key(f"M-S-{group.name}", lazy.window.togroup(group.name, switch_group=True)),
        ]
    ),

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CapsNumLockIndicator(),
                widget.Battery(),
                widget.Backlight(),
                widget.Clock(),
                widget.Countdown(),
                widget.CurrentLayout(),
                widget.CurrentScreen(),
                widget.DF(),
                widget.GroupBox(),
                widget.KeyboardLayout(),
                widget.LaunchBar(),
                widget.Memory(),
                widget.Net(),
                widget.Notify(),
                widget.OpenWeather(),
                widget.Prompt(),
                widget.PulseVolume(),
                widget.Sep(),
                widget.StatusNotifier(),
                widget.Systray(),
            ],
            36,
        )
    ),
]

mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front()),
]

widget_defaults = dict(
    font="DaddyTimeMono Nerd Font",
    fontsize=14,
    padding=5,
)
extension_defaults = widget_defaults.copy()

auto_fullscreen = False
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []
floating_layout = layout.Floating(float_rules=[*layout.Floating.default_float_rules])
floats_kept_above = True
focus_on_window_activation = "focus"
follow_mouse_focus = False
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
