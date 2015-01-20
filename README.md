# Redacted

A plugin for Sublime Text to hide text inside a selection.

![Redact Demo](/redact.gif?raw=true "Redact Demo")

The idea came from wanting to be able to write up some kind of form letter and leave a placeholder for a code/key/etc. Rather than leave it blank, I thought it would be nice to put in a real key and then have it blank out. But I wanted to keep punctuation in there so it was clear what the space was for.

## Installation

Easily install with [Package Control](https://packagecontrol.io) under the name "Redacted". Or install manually:

1. Clone or download the repo into a directory named "Redacted".
2. Put that directory into Sublime's Packages directory. On OS X that'd be `~/Library/Application Support/Sublime Text 3/Packages/Redacted`.

## Usage

1. Select some text.
2. Press `ctrl+shift+delete` or use the menu item `Edit->Text->Redact` to redact characters in the selection.

## Keybinding

Redacted defaults to binding to `ctrl+shift+delete`, but you can easily rebind that in your user key binding file.

## Settings

Redacted has two simple settings to completely control its behavior. Here are the defaults:

    // Regular expression used to match characters to be redacted.
    // By default it's any non-whitespace, non-punctuation character.
    "redacted_search": "[\\P{P}\\w]"

    // Character used to replace redacted characters.
    // Should be a single character, but technically it doesn't need to be.
    "redacted_replacement": "?"

