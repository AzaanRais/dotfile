# ---------------------------------------------------------------------
# Qtile Configuration for Azaan  https://github.com/AzaanRais
# ---------------------------------------------------------------------


# --- IMPORTS ---

import os, subprocess
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.command import lazy
# from libqtile.dgroups import simple_key_binder				# (see groups section for more info on this)


# --- VARIABLES ---

mod = 'mod4' # sets mod key to Super/Windows key
editor = 'code' # text editor of choice
terminal = 'kitty' # terminal of choice
browser = 'librewolf' # browser of choice


## theme name: Catppuccin
colors = [['#161320', '#161320'], # black
		  ['#D9E0EE', '#D9E0EE'], # white
		  ['#F28FAD', '#F28FAD'], # red
		  ['#ABE9B3', '#ABE9B3'], # green
		  ['#FAE3B0', '#FAE3B0'], # yellow
		  ['#96CDFB', '#96CDFB'], # blue
		  ['#DDB6F2', '#DDB6F2'], # magenta
		  ['#B5E8E0', '#B5E8E0']] # cyan


# --- HOOKS ---

@hook.subscribe.startup_once
def start_once():
	home = os.path.expanduser('~/.config/qtile/launch.sh')
	subprocess.run([home])


# --- KEYBINDS ---

keys = [
	# essential keybinds
	Key([mod], 'q', 
		lazy.spawn(f'rofi -show drun'),
		desc = 'Run rofi'
	),
	Key([mod], 'Return',
		lazy.spawn(terminal),
		desc = 'Open terminal'
	),
	Key([mod], 'b',
		lazy.spawn(browser),
		desc = 'Open browser'
	),
	Key([mod], 'c',
		lazy.spawn(editor),
		desc = 'Open text editor'
	),
	Key([mod, 'shift'], 'p',
		lazy.spawn('flameshot gui'),
		desc = 'Open flameshot (screenshots)'
	),
	Key([mod, 'shift'], 'r',
		lazy.restart(),
		desc = 'Restart Qtile'
	),
	Key([mod, 'shift'], 'q',
		lazy.shutdown(),
		desc = 'Shutdown Qtile'
	),
	Key([mod, 'shift'], 'KP_Add',
		lazy.spawn('xbacklight -inc 5'),
		desc = 'Increase brightness by 5'
	),
	Key([mod, 'shift'], 'KP_Subtract',
		lazy.spawn('xbacklight -dec 5'),
		desc = 'Decrease brightness by 5'
	),
	Key([mod, 'control'], 'KP_Add',
		lazy.spawn('amixer sset Master 2%+'),
		desc = 'Increase volume by 2'
	),
	Key([mod, 'control'], 'KP_Subtract',
		lazy.spawn('amixer sset Master 2%-'),
		desc = 'Decrease volume by 2'
	),
	Key([mod, 'shift'], 'b',
		lazy.spawn('bluetoothctl connect E8:07:BF:D8:FA:95'),
		desc = 'Connect headphones'
	),
	Key([mod, 'control'], 'b',
		lazy.spawn('bluetoothctl disconnect E8:07:BF:D8:FA:95'),
		desc = 'Connect headphones'
	),

	# window keybinds
	Key([mod], 'Tab',
		lazy.next_layout(),
		desc = 'Switch between window layouts'
	),
	Key([mod, 'shift'], 'c',
		lazy.window.kill(),
		desc = 'Kill active window'
	),
	Key([mod], 'h',
		lazy.layout.left(),
		desc = 'Move focus to left'
	),
	Key([mod], 'j',
		lazy.layout.up(),
		desc = 'Move focus up'
	),
	Key([mod], 'k',
		lazy.layout.down(),
		desc = 'Move focus down'
	),
	Key([mod], 'l',
		lazy.layout.right(),
		desc = 'Move focus to right'
	),
	Key([mod, 'shift'], 'h',
		lazy.layout.shuffle_left(),
		desc = 'Move window to left'
	),
	Key([mod, 'shift'], 'l',
		lazy.layout.shuffle_right(),
		desc = 'Move window to right'
	),
	Key([mod], 'n',
		lazy.layout.normalize(),
		desc = 'Normalize window size ratios'
	),
	Key([mod], 'm',
		lazy.layout.maximize(),
		desc = 'Toggle window between minimum and maximum sizes'
	),
	Key([mod, 'shift'], 'f',
		lazy.window.toggle_floating(),
		desc = 'Toggle floating'
	),
	Key([mod], 'f',
		lazy.window.toggle_fullscreen(),
		desc = 'Toggle fullscreen'
	),
	Key([mod], 'space',
		lazy.layout.next(),
		desc = 'Move focus to next window'
	),
	Key([mod, 'control'], 'h',
		lazy.layout.grow_left(), 
		desc = 'Grow window to the left'
	),
	Key([mod, 'control'], 'l', 
		lazy.layout.grow_right(), 
		desc = 'Grow window to the right'
	),
	Key([mod, 'control'], 'j', 
		lazy.layout.grow_down(),
		desc = 'Grow window down'
	),
	Key([mod, 'control'], 'k', 
		lazy.layout.grow_up(), 
		desc = 'Grow window up'
	),
	Key([mod, 'shift'], 'Return',
		lazy.layout.toggle_split(),
		desc = 'Toggle between split and unsplit sides of stack',
	)
]


# --- GROUPS ---

groups = [Group(i) for i in '12345']

for i in groups:
	keys.extend(
		[
			Key([mod], i.name,
				lazy.group[i.name].toscreen(),
				desc='Switch to group {}'.format(i.name),
			),
			Key([mod, 'shift'],i.name,
				lazy.window.togroup(i.name),
				desc='Move focused window to group {}'.format(i.name),
			),
		]
	)

## if you want to change your workspace name to words, comment the code above and uncomment the code below and the import statement

'''
groups = [Group('DEV', layout='monadtall'),
		  Group('WWW', layout='monadtall'),
		  Group('SYS', layout='monadtall'),
		  Group('DOC', layout='monadtall'),
		  Group('STD', layout='monadtall'),
		  Group('CHAT', layout='monadtall'),
		  Group('MUS', layout='monadtall'),
		  Group('VID', layout='monadtall'),
		  Group('GFX', layout='floating')]

dgroups_key_binder = simple_key_binder('mod4')
'''


# --- GROUP LAYOUTS ---

layout_theme = {'border_width': 2,
				'margin': 8,
				'border_focus': 'DDB6F2',
				'border_normal': '1b1918'
				}


layouts = [
	# layout.Columns(border_focus_stack=['#9bf2bf', '#5a8f70'], border_width=2),
	# layout.Bsp()
	# layout.Matrix(),
	# layout.MonadWide(),
	# layout.TreeTab(),
	# layout.VerticalTile(),
	# layout.Zoomy(),   
	# layout.Stack(num_stacks=2),
	layout.Max(**layout_theme),
	layout.MonadTall(**layout_theme),
	layout.RatioTile(**layout_theme),
	layout.Tile(**layout_theme),
]


# --- WIDGETS ---

# prompt = '{0}@{1}: '.format(os.environ['USER'], socket.gethostname())


widget_defaults = dict(
	font='JetBrainsMono Nerd Font Mono',
	fontsize= 15,
	padding = 5,
	background=colors[0],
	foreground=colors[1]
)
extension_defaults = widget_defaults.copy()

screens = [
	# Screen(
	# 	top=bar.Bar(
	# 		[
	# 			widget.Sep(
	# 				linewidth = 0,
	# 				padding = 20,
	# 			),
	# 			widget.Clock(
	# 				format = '%a, %b %d - %H:%M',
	# 			),
	# 			widget.Sep(
	# 				linewidth = 0,
	# 				padding = 685,
	# 			),
	# 			widget.GroupBox(
	# 				active = colors[1],
	# 				disable_drag = True,
	# 				inactive = colors[1],
	# 				highlight_method = 'line',
	# 				urgent_alert_method = 'line',
	# 				urgent_text = colors[2],
	# 				urgent_border = colors[2],
	# 			),
	# 			widget.Sep(
	# 				linewidth = 0,
	# 				padding = 550,
	# 			),
	# 			widget.TextBox(
	# 				text = '',
	# 				padding = 0,
	# 				fontsize = 30,
	# 				foreground = colors[5]
	# 			),
	# 			widget.Memory(
	# 				measure_mem = 'G',
	# 				format = '{MemUsed: 0.1f} GiB',
	# 				padding = 0,
	# 				mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(f'{terminal} -e htop')}
	# 			),
	# 			widget.Sep(
	# 				linewidth = 0,
	# 				padding = 20,
	# 			),
	# 			widget.TextBox(
	# 				text = '',
	# 				padding = 0,
	# 				fontsize = 30,
	# 				foreground = colors[4]
	# 			),
	# 			widget.CPU(
	# 				format = '{load_percent: 0.1f}%',
	# 				padding = 0,
	# 				mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(f'{terminal} -e htop')}
	# 			),
	# 			widget.Sep(
	# 				linewidth = 0,
	# 				padding = 20,
	# 			),
	# 			widget.Battery(
	# 				charge_char = '',
	# 				discharge_char = '',
	# 				empty_char = '',
	# 				full_char = '', 
	# 				low_percentage = 15,
	# 				low_foreground = colors[1],
	# 				background = colors[0],
	# 				foreground = colors[1],
	# 				padding = 0,
	# 				format = '{char} {percent:2.0%}'	
	# 			),
	# 			widget.Sep(
	# 				linewidth = 0,
	# 				padding = 20,
	# 			),
	# 			widget.TextBox(
	# 				text = '',
	# 				padding = 0,
	# 				fontsize = 30,
	# 				foreground = colors[3]
	# 			),
	# 			widget.Volume(
	# 				padding = 7,
	# 				volume_app = 'pavucontrol'
	# 			),
	# 			widget.Sep(
	# 				linewidth = 0,
	# 				padding = 50,
	# 			),
	# 		],
	# 		24,
	# 		border_width=[4, 0, 4, 0],  # Draw top and bottom borders
	# 		border_color=['1d1f21', '000000', '1d1f21', '000000']  # Borders are magenta
	# 	),
	# ),
]


# --- FLOATING LAYOUT CONFIG

mouse = [
	Drag(
		[mod],
		'Button1',
		lazy.window.set_position_floating(),
		start=lazy.window.get_position(),
	),
	Drag(
		[mod], 'Button3', lazy.window.set_size_floating(), start=lazy.window.get_size()
	),
	Click([mod], 'Button2', lazy.window.bring_to_front()),
]

groups_app_rules = []
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	**layout_theme,
	float_rules=[
		# Run the utility of `xprop` to see the wm class and name of an X client.
		*layout.Floating.default_float_rules,
		Match(wm_class='confirmreset'),  # gitk
		Match(wm_class='makebranch'),  # gitk
		Match(wm_class='maketag'),  # gitk
		Match(wm_class='ssh-askpass'),  # ssh-askpass
		Match(title='branchdialog'),  # gitk
		Match(title='pinentry'),  # GPG key password entry
		Match(title='MEGAsync') # megasync
	]
)
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True
auto_minimize = True

# --- MISCELLANEOUS ---
wmname = 'LG3D'
