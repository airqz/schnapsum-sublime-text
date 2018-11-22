import sublime
import sublime_plugin
import random
import re
from random import choice

class SchnapsumCommand(sublime_plugin.TextCommand):

    def run(self, edit, qty=15):

        selections = self.view.sel()
        for selection in selections:

            # always start with schnapsum for first output lorem
            para = ""

            # start with schnapsum 20% of the time
            if random.randint(0, 5) == 0:
                para = "Schnapsum "

            # words from the original schnapsum text
            words = "Lorem Picon bière munster du ftomi! Ponchour bisame. Bibbeleskaas jetz rossbolla sech choucroute un schwanz geburtstàg, Chinette dû, ìch bier deppfele schiesser. Rossbolla de knèkes Sepala gal! a a hopla geburtstàg, alles fraü Chulia Roberts oder knäckes dûû blottkopf. Noch bredele geburtstàg schissabibala, hopla yeuh e schmutz. E picon bière Carola schneck fleishwurcht, schmutz a pfourtz! dûû guata eme choucroute Roger Roger of hopla, du Chinette de Scharrarbergheim. Kouglopf ech ìch wurscht rucksack mitt schneck jetz saucisse a du schiss mannele, knèkes saucisse de Niederhausbergen of fill mauls knèkes fleishwurcht kasnacka de eme gal nüdle rossbolla, de Chulien Roger hop pfourtz! bett mer ech scheni salami schmutz.".split()

            for x in list(range(random.randint(int(qty - qty/3)-2, int(qty + qty/3)-2))):
                para += choice(words) + " "

            para += choice(words)

            para = para.capitalize() + "."

            # erase region
            self.view.erase(edit, selection)

            last = self.view.substr(sublime.Region(selection.begin()-1, selection.end()))
            if last == ".":
                para = " " + para

            # insert para before current cursor position
            self.view.insert(edit, selection.begin(), para)

        self.view.end_edit(edit)
