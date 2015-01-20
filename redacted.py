import sublime, sublime_plugin, re

settings = None

class RedactedCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    find = settings.get("redacted_search", "[\\P{P}\\w]")
    replace = settings.get("redacted_replacement", "?")

    for region in self.view.sel():
      str = self.view.substr(region)
      str = re.sub(find, replace, str)
      self.view.replace(edit, region, str)

def plugin_loaded():
  global settings
  settings = sublime.load_settings("Redacted.sublime-settings")

if int(sublime.version()) < 3000: plugin_loaded()
