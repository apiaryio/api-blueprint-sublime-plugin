# API Blueprint Sublime Text plugin

This plugin will help you write [API Blueprints](http://apiblueprint.org/) in your [favorite text editor](http://apiblueprint.org/) easier. 

## Requirements

- [Install](http://apiblueprint.org/#get-started) API Blueprint command-line parser `snowcrash` first, please!

## Installation

Sublime stores packages in the following locations:
```
Nix: ~/.config/sublime-text-2/packages
Mac: ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
Win: %APPDATA%\Sublime Text 2\Packages
```
Open a Terminal/Console and run the following commands, replacing `PACKAGE_PATH` with the path corresponding to your OS above.

```
cd PACKAGE_PATH
git clone https://github.com/apiaryio/api-blueprint-sublime-plugin.git ApiBlueprint
```

## Commands/Shortcuts

You can access the commands either using the command palette (`ctrl+shift+P` or `cmd+shift+P`) or via shortcuts.

```
alt+shift+b - Parse active file and open result in new tab 
```

# Notes

**Ideas to do**

- Syntax highlighting for blueprint
- Syntax highliting for AST (yaml, json)
- Show in browser preview of [Apiary](http://apiary.io/)interacitive Documentation
- Generate and show static HTML documentation from [Iglo](https://github.com/subosito/iglo)
- Show AST in JSON

[Many thanks for inspiration](http://xavura.github.com/CoffeeScript-Sublime-Plugin)
