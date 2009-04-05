from __future__ import division
import sys, time
sys.path.append('pytc-0.7/build/lib.linux-x86_64-2.5')
sys.path.insert(0, 'rdflib/build/lib.linux-x86_64-2.5')

from rdflib.Graph import ConjunctiveGraph
from rdflib import Namespace, Literal

EX = Namespace("http://example.com/")
graph = ConjunctiveGraph('TokyoCabinet')
graph.open("tcgraph", create=True)
graph.add((EX['hello'], EX['world'], Literal("lit")))
print list(graph.triples((None, None, None)))
graph.close()

