# API Blueprint Sublime Text Plugin
This is the official [API Blueprint](http://apiblueprint.org/) plugin for [Sublime Text](http://www.sublimetext.com) with following features:

- Syntax highlighting for the `API Blueprint` format
- Compiling blueprint into its [AST media-type](https://github.com/apiaryio/snowcrash/wiki/API-Blueprint-AST-Media-Types)
- Live linting of blueprints as you type using `SublimeLinter3`

This plug-in works both with **Sublime Text 2 and 3**. However linting is supported on Sublime Text 3 only.

## Requirements
### Snow Crash
In order for this plugin to work properly you need to have the API Blueprint command line tool `snowcrash` installed. 

To install `Snow Crash` on OS X using run the following command: 
```sh
$ brew install --HEAD \
  https://raw.github.com/apiaryio/snowcrash/master/tools/homebrew/snowcrash.rb
```

Refer to [Snow Crash](https://github.com/apiaryio/snowcrash#install) installation notes for details on installing on [OS X & Linux](https://github.com/apiaryio/snowcrash#snow-crash-command-line-tool) or [Windows](https://github.com/apiaryio/snowcrash/wiki/Building-on-Windows).

### SublimeLinter3 (optional)
This plugin offers linting of your blueprints using the [SublimeLinter3](https://github.com/SublimeLinter/SublimeLinter3) plugin framework. In order for linting to work please [install](http://sublimelinter.readthedocs.org/en/latest/installation.html) `SublimeLinter3`.

### Markdown Highlighting (optional)
Note the API Blueprint Sublime Text syntax support relies on Markdown highlighing support in the color scheme used. For best results use a color scheme that supports Markdown-specific scopes (e.g. `markdown: heading`) such as [Monokai extended](https://github.com/jonschlinkert/sublime-monokai-extended) and [Sublime Markdown Extended](https://github.com/jonschlinkert/sublime-markdown-extended).

## Installation
### Using Package Control

With [Package Control](https://packagecontrol.io/installation):

1. Run “Package Control: Install Package” command, find and install `API Blueprint` plugin.
2. Restart SublimeText editor (if required)

### From the Source
With `Snow Crash` [installed](#requirements) run the following command in your Sublime Text 3 packages directory:

```sh
$ git clone https://github.com/apiaryio/api-blueprint-sublime-plugin.git  "API Blueprint"
```

Depending on your OS (and Sublime Text version) the packages directories are:
+ Linux: `~/.config/sublime-text-3/packages`
+ OS X: `~/Library/Application\ Support/Sublime\ Text\ 3/Packages`
+ Windows: `%APPDATA%\Sublime Text 3\Packages`

## Using the Plugin
### Commands
You can access the commands either using the command palette (`CTRL+SHIFT+P` or `CMD+SHIFT+P`) or via shortcuts.

### Shortcuts
- `ALT+SHIFT+B`: Parse the active file and open result [AST](https://github.com/apiaryio/snowcrash/wiki/API-Blueprint-AST-Media-Types) including any possible parser messages in a new tab.

## Acknowledgements
+ This plugin uses parts of [CoffeeScript Sublime Plugin](http://xavura.github.com/CoffeeScript-Sublime-Plugin). 
+ Thanks to [@WMeldon](https://github.com/WMeldon) for his contribution. 

## License
MIT License. See the [LICENSE](LICENSE) file.
