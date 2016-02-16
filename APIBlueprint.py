import sublime
import sublime_plugin
import sys
import os

from os import path
from subprocess import Popen, PIPE
from sublime_plugin import TextCommand, WindowCommand


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


def run_command(cmd, args=[], source="", cwd=None, env=None):
    settings = sublime.load_settings('APIBlueprint.sublime-settings')

    if not type(args) is list:
        args = [args]

    if env is None:
        env = {"PATH": settings.get('binDir', '/usr/local/bin')}

    command = [cmd] + args

    proc = Popen(command, env=env, cwd=cwd,
                 stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stat = proc.communicate(input=source.encode('utf-8'))

    okay = proc.returncode == 0

    # remove leading empty line
    lines = stat[1].decode('UTF-8').split('\n')
    if not lines[0]:
        lines.pop(0)
    sanitized_errout = '\n'.join(lines)

    return {"okay": okay, "out": stat[0].decode('UTF-8'), "err": sanitized_errout}


def parse_buffer(view, args, edit):
    source = Text.all(view)
    result = run_command("drafter", args=args, source=source)
    body = result["err"] + '\n' + result["out"]

    output = view.window().new_file()
    output.set_scratch(True)

    if args[0] == '-f' and args[1] == 'yaml':
        output.set_syntax_file('Packages/YAML/YAML.tmLanguage')
    else:
        output.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')

    output.insert(edit, 0, body)


class ParseYamlAstCommand(TextCommand):

    def run(self, edit, **kwargs):
        parse_buffer(self.view, kwargs["opt"], edit)


class ParseJsonAstCommand(TextCommand):

    def run(self, edit, **kwargs):
        parse_buffer(self.view, kwargs["opt"], edit)
