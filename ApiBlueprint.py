import sublime
import sublime_plugin
import sys

from os import path
from subprocess import Popen, PIPE
from sublime_plugin import TextCommand, WindowCommand

settings = sublime.load_settings('ApiBlueprint.sublime-settings')

class Text():
        @staticmethod
        def all(view):
                return view.substr(sublime.Region(0, view.size()))
        @staticmethod
        def sel(view):
                text = []
                for region in view.sel():
                        if region.empty():
                                continue
                        text.append(view.substr(region))
                return "".join(text)

        @staticmethod
        def get(view):
                text = Text.sel(view)
                if len(text) > 0:
                        return text
                return Text.all(view)

def run_command(cmd, args = [], source="", cwd = None, env = None):
  if not type(args) is list:
    args = [args]
  
  if sys.platform == "win32":
    proc = Popen([cmd]+args, env=env, cwd=cwd, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
    stat = proc.communicate(input=source)
  
  else:
    if env is None:
      env = {"PATH": settings.get('binDir', '/usr/local/bin')}

    command = [cmd] + args
    
    proc = Popen(command, env=env, cwd=cwd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stat = proc.communicate(input=source)
  
  okay = proc.returncode == 0
  
  #remove leading empty line
  lines = stat[1].split('\n')
  if not lines[0]:
    lines.pop(0)
  sanitized_errout = '\n'.join(lines)

  return {"okay": okay, "out": stat[0], "err": sanitized_errout}

class ParseYamlAstCommand(TextCommand):
  def run(self, edit, **kwargs):
    opt = kwargs["opt"]
    args = opt
    
    source = Text.all(self.view)
    result = run_command ("snowcrash", args=args, source=source)

    body = result["err"] + '\n' + result["out"]

    output = self.view.window().new_file()
    output.set_scratch(True)
    output.set_syntax_file('Packages/YAML/YAML.tmLanguage')

    if result["okay"] is True:
      output.insert(edit, 0, body)
    else:
      output.insert(edit, 0, body)
      
class ParseJsonAstCommand(TextCommand):
  def run(self, edit, **kwargs):
    opt = kwargs["opt"]
    args = opt
    
    source = Text.all(self.view)
    result = run_command ("snowcrash", args=args, source=source)
    body = result["err"] + '\n' + result["out"]

    output = self.view.window().new_file()
    output.set_scratch(True)
    output.set_syntax_file('Packages/JSON/JSON.tmLanguage')

    if result["okay"] is True:
      output.insert(edit, 0, body)
    else:
      output.insert(edit, 0, body)
