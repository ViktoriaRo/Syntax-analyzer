import json

from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser

rule_names = None


def main(file_in, ind):
    """
    This method parses input python code to AST
    print json string into out.txt
    """
    global rule_names
    input = FileStream(file_in)
    lexer = Python3Lexer(input)
    rule_names = lexer.ruleNames

    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()

    tree_map = {}
    traverse(tree, map=tree_map)

    return json.dumps(tree_map, indent=ind)


def traverse(tree, map):
    """
    Implements BFS for AST, writes to map
    :param tree: ANTLR tree object
    :param map: dictionary
    :return: Nothing
    """
    global rule_names
    if not rule_names:
        raise Warning("Lexer is not set. Empty rule names.")

    if isinstance(tree, TerminalNodeImpl):
        map['type'] = rule_names.__getitem__(tree.symbol.type)  # get type name of lexema
        map['val'] = tree.getText()  # get lexema
    else:
        name = type(tree).__name__.replace('Context', '')
        map[name] = {}
        children = []
        for i in range(tree.getChildCount()):
            child = {}
            traverse(tree.getChild(i), child)
            children.append(child)
        map[name] = children


if __name__ == '__main__':
    f_out = open("out.txt", 'w')
    f_out.write(main("in.txt", 1))
