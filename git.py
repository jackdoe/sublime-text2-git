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
    def run_thread(self,edit,command):
        os.chdir(self.folder())
        thread.start_new_thread(self.run_command,(edit,command))
    def run_command(self,edit,command): 
        proc = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False, universal_newlines=True)
        self.output = proc.communicate()[0].split("\n")
        sublime.set_timeout(self.draw, 20)
    def win(self):
        return self.view.window() or sublime.active_window()
    def draw(self):
        self.win().show_quick_panel(self.output,self.panel_done,sublime.MONOSPACE_FONT)
    def panel_done(self, index):
        pass
    def folder(self):
        return self.win().folders().pop()

class GitPullCommand(GitCommand):
    def run(self,edit):
        self.run_thread(edit,["git","pull"])

class GitPushCommand(GitCommand):
    def run(self,edit):
        self.run_thread(edit,["git","push","-u","origin","master"])

class GitLogCommand(GitCommand):
    def run(self,edit):
        self.run_thread(edit,["git","log",'--pretty=format:%s [%ce %h, %ar]',"--abbrev-commit"])

class GitCommitCommand(GitCommand):
    def run(self,edit,line):
        self.run_thread(edit,["git","commit","-a","-m",line])

