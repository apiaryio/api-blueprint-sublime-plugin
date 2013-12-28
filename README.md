# API Blueprint Sublime Text Plug-in
This plugin will help you with writing [API blueprints](http://apiblueprint.org/) in Sublime Text. This plug-in works both with Sublime Text 2 and 3. 

## Requirements
- [Install](http://apiblueprint.org/#get-started) API Blueprint command-line parser `snowcrash` first.

## Installation
Sublime Text 2 stores packages in the following locations:


	Nix: ~/.config/sublime-text-2/packages
	Mac: ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
	Win: %APPDATA%\Sublime Text 2\Packages

Open a terminal and run the following commands, replacing `PACKAGE_PATH` with the path corresponding to your OS above.


	cd PACKAGE_PATH
	git clone https://github.com/apiaryio/api-blueprint-sublime-plugin.git "API Blueprint"

## Commands
You can access the commands either using the command palette (`CTRL+SHIFT+P` or `CMD+SHIFT+P`) or via shortcuts.

## Shortcuts
`ALT+SHIFT+B` - Parse the active file and open result [AST](https://github.com/apiaryio/snowcrash/wiki/API-Blueprint-AST-Media-Types) including any possible parser messages in a new tab.

## Possible Future Features
- Syntax highlighting for blueprint
- Show a preview at [Apiary](http://apiary.io/) in a browser
- Generate and show static HTML documentation from [Iglo](https://github.com/subosito/iglo) and/or [Aglio](https://github.com/danielgtaylor/aglio)

# Acknowledgements
+ Thanks for inspiration to [CoffeeScript Sublime Plugin](http://xavura.github.com/CoffeeScript-Sublime-Plugin).
+ Thanks to [@WMeldon](https://github.com/WMeldon) for his contribution.
