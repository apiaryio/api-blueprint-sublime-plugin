#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by William Meldon
# Copyright (c) 2013 William Meldon
# https://github.com/WMeldon/SublimeLinter-apiblueprint
#
# Modified by Zdenek Nemec
#
# License: MIT

"""This module exports the Apiblueprint plugin class."""


def ApiBlueprintFactory():
    """ Define API Blueprint Linter Class"""

    class ApiBlueprint(Linter):
        """Provides an interface to apiblueprint."""

        syntax = 'apiblueprint'
        cmd = 'drafter --validate'
        executable = 'drafter'
        executable = None
        regex = (
            r'(?:(?P<warning>warning)|(?P<error>error)):\s*\((?P<code>\d+)\)'
            r'(?P<message>.+?)(?::|$)'
            r'(?P<line>\d+):(?P<col>\d+)(?:.*)'
        )
        multiline = False
        line_col_base = (0, 0)
        tempfile_suffix = None
        error_stream = util.STREAM_BOTH
        selectors = {}
        word_re = None
        defaults = {}
        inline_settings = None
        inline_overrides = None
        comment_re = None

        def split_match(self, match):
            """
            Run default match.  If match is found, convert line variable to line number
            and adjust col.
            """
            match, line, col, error, warning, message, near = super().split_match(match)

            if line is not None:
                line, col = self.view.rowcol((int(line)))
                line = int(line) - self.line_col_base[0]

            return match, line, col, error, warning, message, near

try:
    """Attempt to import SublimeLinter3"""
    from SublimeLinter.lint import Linter, util
    ApiBlueprintFactory()

except ImportError:
    print("No SublimeLinter3 installed - Install SublimeLinter3 to lint your API blueprints (ST3 Only)")
