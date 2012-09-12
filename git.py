import sublime, sublime_plugin, subprocess, thread, os, functools, glob, fnmatch
class PromptGitCommitCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.active_view().run_command('save')
        self.window.show_input_panel("message:", "", self.on_done, None, None)
        pass

    def on_done(self, line):
        try:
            if self.window.active_view():
                self.window.active_view().run_command("git_commit", {"line": line} )
        except ValueError:
            pass

class GitCommand(sublime_plugin.TextCommand): 
    def run_command(self,edit,command): 
        os.chdir(self.folder())
        proc = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False, universal_newlines=True)
        self.output = proc.communicate()[0].split("\n")
        self.view.window().show_quick_panel(self.output[:-1],self.panel_done,sublime.MONOSPACE_FONT)

    def panel_done(self, index):
        pass
    def folder(self):
        return self.view.window().folders().pop()

class GitPullCommand(GitCommand):
    def run(self,edit):
        self.run_command(edit,["git","pull"])
class GitPushCommand(GitCommand):
    def run(self,edit):
        self.run_command(edit,["git","push","origin","master"])
class GitLogCommand(GitCommand):
    def run(self,edit):
        self.run_command(edit,["git","log",'--pretty=format:%s [%ce %h, %ar]',"--abbrev-commit"])

class GitCommitCommand(GitCommand):
    def run(self,edit,line):
        self.run_command(edit,["git","commit","-a","-m",line])
