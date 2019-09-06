import sublime
import sublime_plugin

class XmlClean(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.assign_syntax('XML.sublime-syntax')
		regions = self.view.find_all( '><' )
		for region in reversed(regions):
			self.view.replace(edit, region, '>\n<' )
		self.view.run_command("reindent", {"single_line": False})
