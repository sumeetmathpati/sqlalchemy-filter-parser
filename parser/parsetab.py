
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COMMA IDENTIFIER OPexpressions : expression\n    | expression AND expressionsexpression : IDENTIFIER OP identifiersidentifiers : IDENTIFIER\n    | IDENTIFIER COMMA identifiers'
    
_lr_action_items = {'IDENTIFIER':([0,4,5,9,],[3,3,7,7,]),'$end':([1,2,6,7,8,10,],[0,-1,-2,-4,-3,-5,]),'AND':([2,7,8,10,],[4,-4,-3,-5,]),'OP':([3,],[5,]),'COMMA':([7,],[9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,4,],[1,6,]),'expression':([0,4,],[2,2,]),'identifiers':([5,9,],[8,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> expression','expressions',1,'p_expressions','parser.py',13),
  ('expressions -> expression AND expressions','expressions',3,'p_expressions','parser.py',14),
  ('expression -> IDENTIFIER OP identifiers','expression',3,'p_expression','parser.py',30),
  ('identifiers -> IDENTIFIER','identifiers',1,'p_identifiers','parser.py',43),
  ('identifiers -> IDENTIFIER COMMA identifiers','identifiers',3,'p_identifiers','parser.py',44),
]