installation:
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
$ git clone git://github.com/kemayo/sublime-text-2-git.git Git

simple key bindings:
[
	{ "keys": ["alt+c"], "command": "prompt_git_commit" },
	{ "keys": ["alt+p"], "command": "git_pull" },
	{ "keys": ["alt+l"], "command": "git_log" },
	{ "keys": ["alt+s"], "command": "git_push" }
]
