import nltk

from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

grammar = nltk.data.load(r'./dvandva.fcfg')

hpi = "history of coronary artery disease".split()
parser = nltk.parse.FeatureEarleyChartParser(grammar)
trees = [tree for tree in parser.parse(hpi)]

if len(trees) == 1:
	phrase_tree = trees[0]
	phrase_tree.draw()
	lam_fxn = phrase_tree.label()['SEM']
else:
	print '%d trees. Have to choose'%len(trees)
	print 'No choice function defined'
