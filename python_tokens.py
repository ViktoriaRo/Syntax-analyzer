"""
This file contains all python language tokens:
1. Operators (arithmetic, comparison, assignment, bitwise, logical, identity, membership)
2. Symbols
3. Keywords
4. Literals (datatypes)
"""
# t_IDENTIFIER = r'^[^\d\W]\w*\Z'
# t_IDENTIFIER = r'[a-z]\w*'

digit            = r'([0-9])'
nondigit         = r'([_A-Za-z])'
identifier       = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

# newline = r'\n+'
# Operators

operators = ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION', 'MOD', 'EXPONENT', 'FLOOR_DIVISION', 'EQUALS',
             'NOT_EQUALS', 'GREATER', 'LESS', 'GREATER_EQ', 'LESS_EQ', ' ASSIGNMENT', 'ADD_ASS', 'SUB_ASS', 'MULTIPLY_ASS',
             'DIVIDE_ASS', 'MOD_ASS', 'EXP_ASS', 'FLOOR_DIV_ASS', 'BI_AND', 'BI_OR', 'BI_XOR', 'BI_ONES_COMP',
             'BI_LEFT_SHIFT', 'BI_RIGHT_SHIFT', 'LOG_AND', 'LOG_OR', 'LOG_NOT']



# TODO

# ARITHMETIC OPERATORS

t_ADDITION = r'\+'
t_DIVISION = r'\\'
t_SUBTRACTION = r'-'
t_MULTIPLICATION = r'\*'



t_NOT_EQUALS = r'' # != same as <>


# SYMBOLS TODO

symbols = ['LEFT_PAREN', 'RIGHT_PAREN', 'COLON', 'LEFT_BRACE', 'RIGHT_BRACE', 'SEMICOLON', 'LEFT_SQ_BRACKET',
           'RIGHT_SQ_BRACKET']


# KEYWORDS

keywords = ['FALSE', 'TRUE', 'CLASS', 'FINALLY', 'IS', 'IN', 'RETURN', 'NONE', 'CONTINUE', 'FOR', 'LAMBDA', 'TRY',
            'DEF', 'FROM', 'NONLOCAL', 'WHILE', 'AND', 'DEL', 'GLOBAL', 'NOT', 'WITH', 'AS', 'ELIF', 'IF', 'OR', 'YIELD',
            'ASSERT', 'ELSE', 'IMPORT', 'PASS', 'BREAK', 'EXCEPT', 'RAISE']

