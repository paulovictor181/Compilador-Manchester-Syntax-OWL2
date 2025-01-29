
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL AND CARDINALITY CLASS CLASS_IDENTIFIER CLOSE_BRACKET CLOSE_CURLY CLOSE_PAREN COMMA DISJOINTCLASSES DISJOINtWITH EQUAL EQUIVALENTTO EXACTLY GREATER_THAN INDIVIDUALS INDIVIDUAL_NAME LESS_THAN MAX MIN NAMESPACE NOT ONLY OPEN_BRACKET OPEN_CURLY OPEN_PAREN OR PROPERTY_IDENTIFIER PROPERTY_IDENTIFIER_SIMPLE SOME SUBCLASSOF THAT TYPE VALUEclasses : defined_class \n               | defined_class classes\n               | primitive_class \n               | primitive_class classes\n               primitive_class : CLASS CLASS_IDENTIFIER subclass_section disjoint_section individuals_sectionsubclass_section : SUBCLASSOF enum_class\n                        | SUBCLASSOF CLASS_IDENTIFIER def_descriptions_axioma ONLY OPEN_PAREN auxiliar_fechamento CLOSE_PAREN\n                        | SUBCLASSOF OR covered_class\n                        | SUBCLASSOF CLASS_IDENTIFIER \n                        | SUBCLASSOF quantifier_aux_axioma\n                        auxiliar_fechamento : CLASS_IDENTIFIER   \n                        | CLASS_IDENTIFIER OR auxiliar_fechamento\n    disjoint_section : DISJOINTCLASSES quantifier_aux\n                        | emptydisjoint_classes_list : CLASS_IDENTIFIER\n                             | CLASS_IDENTIFIER COMMA disjoint_classes_listdefined_class : CLASS CLASS_IDENTIFIER equivalentto_section subclass_section individuals_section\n                     | CLASS CLASS_IDENTIFIER equivalentto_sectionenum_class : OPEN_CURLY individuals CLOSE_CURLYcovered_class : CLASS_IDENTIFIER OR covered_class\n                     | CLASS_IDENTIFIER\n                equivalentto_section : EQUIVALENTTO enum_class\n                            | EQUIVALENTTO CLASS_IDENTIFIER OR covered_class\n                            | EQUIVALENTTO CLASS_IDENTIFIER aninhada \n                            | EQUIVALENTTO CLASS_IDENTIFIER only_defined\n    def_descriptions : quantifier_aux            \n    def_descriptions_axioma : quantifier_aux_axioma            \n    only_defined : comma_and quantifier_aux            \n    aninhada : comma_and OPEN_PAREN OPEN_PAREN quantifier_aux CLOSE_PAREN CLOSE_PAREN \n                | comma_and OPEN_PAREN PROPERTY_IDENTIFIER quantifier OPEN_PAREN quantifier_aux CLOSE_PAREN CLOSE_PAREN              \n    quantifier_aux : comma_and quantifier_aux\n                      | OPEN_PAREN quantifier_aux CLOSE_PAREN\n                      | PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER\n                      | PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER quantifier_aux\n                      | PROPERTY_IDENTIFIER quantifier namespace_type\n                      | PROPERTY_IDENTIFIER quantifier_number CARDINALITY namespace_type\n                      | PROPERTY_IDENTIFIER quantifier_number CARDINALITY CLASS_IDENTIFIER\n                      | quantifier_aux comma_and quantifier_aux\n                      | CLASS_IDENTIFIER quantifier quantifier_aux\n                      | CLASS_IDENTIFIER OR quantifier_aux\n                      | PROPERTY_IDENTIFIER quantifier quantifier_aux\n                      | CLASS_IDENTIFIER comma_and quantifier_aux\n                      | CLASS_IDENTIFIER\n                      | PROPERTY_IDENTIFIER\n    quantifier_aux_axioma : comma_and quantifier_aux_axioma\n                            | OPEN_PAREN quantifier_aux_axioma CLOSE_PAREN\n                            | PROPERTY_IDENTIFIER quantifier_geral CLASS_IDENTIFIER\n                            | PROPERTY_IDENTIFIER quantifier_geral namespace_type                 \n                            | quantifier_aux_axioma comma_and quantifier_aux_axioma\n                            | CLASS_IDENTIFIER quantifier_geral quantifier_aux_axioma\n                            | CLASS_IDENTIFIER OR quantifier_aux_axioma\n                            | PROPERTY_IDENTIFIER quantifier_geral quantifier_aux_axioma\n                            | CLASS_IDENTIFIER comma_and quantifier_aux_axioma\n                            | CLASS_IDENTIFIER\n                            | PROPERTY_IDENTIFIER\n    quantifier : SOME\n                  | ALL\n                  | VALUE\n                  | THAT\n                  quantifier_number : MAX\n                  | MIN\n                  | EXACTLY\n                  quantifier_geral : SOME\n                  | ALL\n                  | VALUE\n                  | MAX\n                  | MIN\n                  | EXACTLY\n                  | THAT\n                  sizecheck : EQUAL CARDINALITY\n                  | GREATER_THAN CARDINALITY\n                  | LESS_THAN CARDINALITY\n                  | GREATER_THAN EQUAL CARDINALITY\n                  | LESS_THAN EQUAL CARDINALITYnamespace_type : NAMESPACE TYPE\n                      | NAMESPACE TYPE OPEN_BRACKET sizecheck CLOSE_BRACKETindividuals_section : INDIVIDUALS individuals\n                           | emptyindividuals : INDIVIDUAL_NAME\n                   | INDIVIDUAL_NAME COMMA individualscomma_and : COMMA\n                     | ANDempty :'
    
_lr_action_items = {'CLASS':([0,2,3,8,9,12,13,15,16,19,20,23,25,28,30,31,32,35,36,38,39,42,43,57,58,60,62,64,78,80,81,85,86,87,88,90,91,92,93,95,96,97,98,99,101,102,103,106,107,109,110,111,113,114,120,124,129,132,141,],[4,4,4,-18,-83,-83,-83,-14,-22,-6,-9,-10,-55,-17,-78,-5,-13,-44,-43,-24,-25,-79,-54,-8,-21,-45,-77,-31,-23,-28,-19,-50,-51,-53,-46,-49,-47,-48,-52,-38,-32,-33,-41,-35,-39,-40,-42,-80,-53,-20,-75,-34,-36,-37,-31,-7,-29,-76,-30,]),'$end':([1,2,3,5,6,8,9,12,13,15,16,19,20,23,25,28,30,31,32,35,36,38,39,42,43,57,58,60,62,64,78,80,81,85,86,87,88,90,91,92,93,95,96,97,98,99,101,102,103,106,107,109,110,111,113,114,120,124,129,132,141,],[0,-1,-3,-2,-4,-18,-83,-83,-83,-14,-22,-6,-9,-10,-55,-17,-78,-5,-13,-44,-43,-24,-25,-79,-54,-8,-21,-45,-77,-31,-23,-28,-19,-50,-51,-53,-46,-49,-47,-48,-52,-38,-32,-33,-41,-35,-39,-40,-42,-80,-53,-20,-75,-34,-36,-37,-31,-7,-29,-76,-30,]),'CLASS_IDENTIFIER':([4,10,11,14,20,21,22,24,26,27,33,34,37,40,45,47,48,49,50,51,52,53,54,55,59,61,63,66,68,69,70,71,75,76,77,79,83,89,97,100,104,108,112,116,122,123,],[7,17,20,36,43,43,58,43,-81,-82,36,36,58,36,43,43,43,-63,-64,-65,-66,-67,-68,-69,43,91,36,97,-56,-57,-58,-59,36,36,36,36,43,58,36,114,36,117,36,97,36,117,]),'EQUIVALENTTO':([7,],[10,]),'SUBCLASSOF':([7,8,16,35,36,38,39,58,64,78,80,81,95,96,97,98,99,101,102,103,109,110,111,113,114,120,129,132,141,],[11,11,-22,-44,-43,-24,-25,-21,-31,-23,-28,-19,-38,-32,-33,-41,-35,-39,-40,-42,-20,-75,-34,-36,-37,-31,-29,-76,-30,]),'DISJOINTCLASSES':([9,19,20,23,25,43,57,58,60,81,85,86,87,88,90,91,92,93,107,109,110,124,132,],[14,-6,-9,-10,-55,-54,-8,-21,-45,-19,-50,-51,-53,-46,-49,-47,-48,-52,-53,-20,-75,-7,-76,]),'INDIVIDUALS':([9,12,13,15,19,20,23,25,32,35,36,43,57,58,60,64,81,85,86,87,88,90,91,92,93,95,96,97,98,99,101,102,103,107,109,110,111,113,114,120,124,132,],[-83,29,29,-14,-6,-9,-10,-55,-13,-44,-43,-54,-8,-21,-45,-31,-19,-50,-51,-53,-46,-49,-47,-48,-52,-38,-32,-33,-41,-35,-39,-40,-42,-53,-20,-75,-34,-36,-37,-31,-7,-76,]),'OPEN_CURLY':([10,11,],[18,18,]),'OR':([11,17,20,36,43,58,91,97,117,],[22,37,47,76,47,89,47,76,123,]),'OPEN_PAREN':([11,14,20,21,24,26,27,33,34,40,45,47,48,49,50,51,52,53,54,55,59,61,63,66,68,69,70,71,75,76,77,79,83,84,97,104,112,116,122,],[21,34,21,21,21,-81,-82,34,34,79,21,21,21,-63,-64,-65,-66,-67,-68,-69,21,21,34,34,-56,-57,-58,-59,34,34,34,104,21,108,34,34,34,122,34,]),'PROPERTY_IDENTIFIER':([11,14,20,21,24,26,27,33,34,40,45,47,48,49,50,51,52,53,54,55,59,61,63,66,68,69,70,71,75,76,77,79,83,97,104,112,116,122,],[25,35,25,25,25,-81,-82,35,35,35,25,25,25,-63,-64,-65,-66,-67,-68,-69,25,25,35,35,-56,-57,-58,-59,35,35,35,105,25,35,35,35,35,35,]),'COMMA':([11,14,17,20,21,23,24,25,26,27,32,33,34,35,36,40,42,43,45,46,47,48,49,50,51,52,53,54,55,56,59,60,61,63,64,65,66,68,69,70,71,75,76,77,79,80,83,85,86,87,88,90,91,92,93,95,96,97,98,99,101,102,103,104,105,107,110,111,112,113,114,115,116,120,121,122,130,132,138,],[26,26,26,26,26,26,26,-55,-81,-82,26,26,26,-44,26,26,82,26,26,26,26,26,-63,-64,-65,-66,-67,-68,-69,26,26,26,26,26,26,26,26,-56,-57,-58,-59,26,26,26,26,26,26,26,26,26,-46,26,26,-48,26,26,-32,26,26,-35,26,26,26,26,-44,26,-75,26,26,-36,-37,26,26,26,-32,26,26,-76,-32,]),'AND':([11,14,17,20,21,23,24,25,26,27,32,33,34,35,36,40,43,45,46,47,48,49,50,51,52,53,54,55,56,59,60,61,63,64,65,66,68,69,70,71,75,76,77,79,80,83,85,86,87,88,90,91,92,93,95,96,97,98,99,101,102,103,104,105,107,110,111,112,113,114,115,116,120,121,122,130,132,138,],[27,27,27,27,27,27,27,-55,-81,-82,27,27,27,-44,27,27,27,27,27,27,27,-63,-64,-65,-66,-67,-68,-69,27,27,27,27,27,27,27,27,-56,-57,-58,-59,27,27,27,27,27,27,27,27,27,-46,27,27,-48,27,27,-32,27,27,-35,27,27,27,27,-44,27,-75,27,27,-36,-37,27,27,27,-32,27,27,-76,-32,]),'INDIVIDUAL_NAME':([18,29,82,],[42,42,42,]),'SOME':([20,25,35,36,43,91,97,105,],[49,49,68,68,49,49,68,68,]),'ALL':([20,25,35,36,43,91,97,105,],[50,50,69,69,50,50,69,69,]),'VALUE':([20,25,35,36,43,91,97,105,],[51,51,70,70,51,51,70,70,]),'MAX':([20,25,35,43,91,105,],[52,52,72,52,52,72,]),'MIN':([20,25,35,43,91,105,],[53,53,73,53,53,73,]),'EXACTLY':([20,25,35,43,91,105,],[54,54,74,54,54,74,]),'THAT':([20,25,35,36,43,91,97,105,],[55,55,71,71,55,55,71,71,]),'ONLY':([25,43,44,46,60,85,86,87,88,90,91,92,93,107,110,132,],[-55,-54,84,-27,-45,-50,-51,-45,-46,-49,-47,-48,-52,-53,-75,-76,]),'CLOSE_PAREN':([25,35,36,43,56,60,64,65,85,86,88,90,91,92,93,95,96,97,98,99,101,102,103,105,107,110,111,113,114,115,117,118,120,121,130,131,132,138,],[-55,-44,-43,-54,88,-45,-31,96,-50,-51,-46,-49,-47,-48,-52,-38,-32,-33,-41,-35,-39,-40,-42,-44,-53,-75,-34,-36,-37,121,-11,124,-31,129,138,-12,-76,141,]),'CLOSE_CURLY':([41,42,106,],[81,-79,-80,]),'NAMESPACE':([49,50,51,52,53,54,55,61,66,68,69,70,71,100,116,],[-63,-64,-65,-66,-67,-68,-69,94,94,-56,-57,-58,-59,94,94,]),'CARDINALITY':([67,72,73,74,126,127,128,135,137,],[100,-60,-61,-62,133,134,136,139,140,]),'TYPE':([94,],[110,]),'OPEN_BRACKET':([110,],[119,]),'EQUAL':([119,127,128,],[126,135,137,]),'GREATER_THAN':([119,],[127,]),'LESS_THAN':([119,],[128,]),'CLOSE_BRACKET':([125,133,134,136,139,140,],[132,-70,-71,-72,-73,-74,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'classes':([0,2,3,],[1,5,6,]),'defined_class':([0,2,3,],[2,2,2,]),'primitive_class':([0,2,3,],[3,3,3,]),'equivalentto_section':([7,],[8,]),'subclass_section':([7,8,],[9,12,]),'disjoint_section':([9,],[13,]),'empty':([9,12,13,],[15,30,30,]),'enum_class':([10,11,],[16,19,]),'quantifier_aux_axioma':([11,20,21,24,45,47,48,59,61,83,],[23,46,56,60,85,86,87,90,93,107,]),'comma_and':([11,14,17,20,21,23,24,32,33,34,36,40,43,45,46,47,48,56,59,60,61,63,64,65,66,75,76,77,79,80,83,85,86,87,90,91,93,95,97,98,101,102,103,104,107,111,112,115,116,120,122,130,],[24,33,40,48,24,59,24,63,33,33,77,33,83,24,59,24,24,59,24,59,24,33,63,63,33,33,33,33,33,63,24,59,59,59,59,83,59,63,112,63,63,63,63,33,59,63,33,63,33,63,33,63,]),'individuals_section':([12,13,],[28,31,]),'quantifier_aux':([14,33,34,40,63,66,75,76,77,79,97,104,112,116,122,],[32,64,65,80,95,98,101,102,103,65,111,115,120,98,130,]),'aninhada':([17,],[38,]),'only_defined':([17,],[39,]),'individuals':([18,29,82,],[41,62,106,]),'def_descriptions_axioma':([20,],[44,]),'quantifier_geral':([20,25,43,91,],[45,61,45,45,]),'covered_class':([22,37,89,],[57,78,109,]),'quantifier':([35,36,97,105,],[66,75,75,116,]),'quantifier_number':([35,105,],[67,67,]),'namespace_type':([61,66,100,116,],[92,99,113,99,]),'auxiliar_fechamento':([108,123,],[118,131,]),'sizecheck':([119,],[125,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> classes","S'",1,None,None,None),
  ('classes -> defined_class','classes',1,'p_classes','parser.py',11),
  ('classes -> defined_class classes','classes',2,'p_classes','parser.py',12),
  ('classes -> primitive_class','classes',1,'p_classes','parser.py',13),
  ('classes -> primitive_class classes','classes',2,'p_classes','parser.py',14),
  ('primitive_class -> CLASS CLASS_IDENTIFIER subclass_section disjoint_section individuals_section','primitive_class',5,'p_primitive_class','parser.py',22),
  ('subclass_section -> SUBCLASSOF enum_class','subclass_section',2,'p_subclass_section','parser.py',32),
  ('subclass_section -> SUBCLASSOF CLASS_IDENTIFIER def_descriptions_axioma ONLY OPEN_PAREN auxiliar_fechamento CLOSE_PAREN','subclass_section',7,'p_subclass_section','parser.py',33),
  ('subclass_section -> SUBCLASSOF OR covered_class','subclass_section',3,'p_subclass_section','parser.py',34),
  ('subclass_section -> SUBCLASSOF CLASS_IDENTIFIER','subclass_section',2,'p_subclass_section','parser.py',35),
  ('subclass_section -> SUBCLASSOF quantifier_aux_axioma','subclass_section',2,'p_subclass_section','parser.py',36),
  ('auxiliar_fechamento -> CLASS_IDENTIFIER','auxiliar_fechamento',1,'p_auxiliar_fechamento','parser.py',63),
  ('auxiliar_fechamento -> CLASS_IDENTIFIER OR auxiliar_fechamento','auxiliar_fechamento',3,'p_auxiliar_fechamento','parser.py',64),
  ('disjoint_section -> DISJOINTCLASSES quantifier_aux','disjoint_section',2,'p_disjoint_section','parser.py',72),
  ('disjoint_section -> empty','disjoint_section',1,'p_disjoint_section','parser.py',73),
  ('disjoint_classes_list -> CLASS_IDENTIFIER','disjoint_classes_list',1,'p_disjoint_classes_list','parser.py',80),
  ('disjoint_classes_list -> CLASS_IDENTIFIER COMMA disjoint_classes_list','disjoint_classes_list',3,'p_disjoint_classes_list','parser.py',81),
  ('defined_class -> CLASS CLASS_IDENTIFIER equivalentto_section subclass_section individuals_section','defined_class',5,'p_defined_class','parser.py',89),
  ('defined_class -> CLASS CLASS_IDENTIFIER equivalentto_section','defined_class',3,'p_defined_class','parser.py',90),
  ('enum_class -> OPEN_CURLY individuals CLOSE_CURLY','enum_class',3,'p_enum_class','parser.py',119),
  ('covered_class -> CLASS_IDENTIFIER OR covered_class','covered_class',3,'p_covered_class','parser.py',133),
  ('covered_class -> CLASS_IDENTIFIER','covered_class',1,'p_covered_class','parser.py',134),
  ('equivalentto_section -> EQUIVALENTTO enum_class','equivalentto_section',2,'p_equivalentto_section','parser.py',148),
  ('equivalentto_section -> EQUIVALENTTO CLASS_IDENTIFIER OR covered_class','equivalentto_section',4,'p_equivalentto_section','parser.py',149),
  ('equivalentto_section -> EQUIVALENTTO CLASS_IDENTIFIER aninhada','equivalentto_section',3,'p_equivalentto_section','parser.py',150),
  ('equivalentto_section -> EQUIVALENTTO CLASS_IDENTIFIER only_defined','equivalentto_section',3,'p_equivalentto_section','parser.py',151),
  ('def_descriptions -> quantifier_aux','def_descriptions',1,'p_def_descriptions','parser.py',163),
  ('def_descriptions_axioma -> quantifier_aux_axioma','def_descriptions_axioma',1,'p_def_descriptions_axioma','parser.py',168),
  ('only_defined -> comma_and quantifier_aux','only_defined',2,'p_only_defined','parser.py',173),
  ('aninhada -> comma_and OPEN_PAREN OPEN_PAREN quantifier_aux CLOSE_PAREN CLOSE_PAREN','aninhada',6,'p_aninhada','parser.py',177),
  ('aninhada -> comma_and OPEN_PAREN PROPERTY_IDENTIFIER quantifier OPEN_PAREN quantifier_aux CLOSE_PAREN CLOSE_PAREN','aninhada',8,'p_aninhada','parser.py',178),
  ('quantifier_aux -> comma_and quantifier_aux','quantifier_aux',2,'p_quantifier_aux','parser.py',184),
  ('quantifier_aux -> OPEN_PAREN quantifier_aux CLOSE_PAREN','quantifier_aux',3,'p_quantifier_aux','parser.py',185),
  ('quantifier_aux -> PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER','quantifier_aux',3,'p_quantifier_aux','parser.py',186),
  ('quantifier_aux -> PROPERTY_IDENTIFIER quantifier CLASS_IDENTIFIER quantifier_aux','quantifier_aux',4,'p_quantifier_aux','parser.py',187),
  ('quantifier_aux -> PROPERTY_IDENTIFIER quantifier namespace_type','quantifier_aux',3,'p_quantifier_aux','parser.py',188),
  ('quantifier_aux -> PROPERTY_IDENTIFIER quantifier_number CARDINALITY namespace_type','quantifier_aux',4,'p_quantifier_aux','parser.py',189),
  ('quantifier_aux -> PROPERTY_IDENTIFIER quantifier_number CARDINALITY CLASS_IDENTIFIER','quantifier_aux',4,'p_quantifier_aux','parser.py',190),
  ('quantifier_aux -> quantifier_aux comma_and quantifier_aux','quantifier_aux',3,'p_quantifier_aux','parser.py',191),
  ('quantifier_aux -> CLASS_IDENTIFIER quantifier quantifier_aux','quantifier_aux',3,'p_quantifier_aux','parser.py',192),
  ('quantifier_aux -> CLASS_IDENTIFIER OR quantifier_aux','quantifier_aux',3,'p_quantifier_aux','parser.py',193),
  ('quantifier_aux -> PROPERTY_IDENTIFIER quantifier quantifier_aux','quantifier_aux',3,'p_quantifier_aux','parser.py',194),
  ('quantifier_aux -> CLASS_IDENTIFIER comma_and quantifier_aux','quantifier_aux',3,'p_quantifier_aux','parser.py',195),
  ('quantifier_aux -> CLASS_IDENTIFIER','quantifier_aux',1,'p_quantifier_aux','parser.py',196),
  ('quantifier_aux -> PROPERTY_IDENTIFIER','quantifier_aux',1,'p_quantifier_aux','parser.py',197),
  ('quantifier_aux_axioma -> comma_and quantifier_aux_axioma','quantifier_aux_axioma',2,'p_quantifier_aux_axioma','parser.py',210),
  ('quantifier_aux_axioma -> OPEN_PAREN quantifier_aux_axioma CLOSE_PAREN','quantifier_aux_axioma',3,'p_quantifier_aux_axioma','parser.py',211),
  ('quantifier_aux_axioma -> PROPERTY_IDENTIFIER quantifier_geral CLASS_IDENTIFIER','quantifier_aux_axioma',3,'p_quantifier_aux_axioma','parser.py',212),
  ('quantifier_aux_axioma -> PROPERTY_IDENTIFIER quantifier_geral namespace_type','quantifier_aux_axioma',3,'p_quantifier_aux_axioma','parser.py',213),
  ('quantifier_aux_axioma -> quantifier_aux_axioma comma_and quantifier_aux_axioma','quantifier_aux_axioma',3,'p_quantifier_aux_axioma','parser.py',214),
  ('quantifier_aux_axioma -> CLASS_IDENTIFIER quantifier_geral quantifier_aux_axioma','quantifier_aux_axioma',3,'p_quantifier_aux_axioma','parser.py',215),
  ('quantifier_aux_axioma -> CLASS_IDENTIFIER OR quantifier_aux_axioma','quantifier_aux_axioma',3,'p_quantifier_aux_axioma','parser.py',216),
  ('quantifier_aux_axioma -> PROPERTY_IDENTIFIER quantifier_geral quantifier_aux_axioma','quantifier_aux_axioma',3,'p_quantifier_aux_axioma','parser.py',217),
  ('quantifier_aux_axioma -> CLASS_IDENTIFIER comma_and quantifier_aux_axioma','quantifier_aux_axioma',3,'p_quantifier_aux_axioma','parser.py',218),
  ('quantifier_aux_axioma -> CLASS_IDENTIFIER','quantifier_aux_axioma',1,'p_quantifier_aux_axioma','parser.py',219),
  ('quantifier_aux_axioma -> PROPERTY_IDENTIFIER','quantifier_aux_axioma',1,'p_quantifier_aux_axioma','parser.py',220),
  ('quantifier -> SOME','quantifier',1,'p_quantifier','parser.py',237),
  ('quantifier -> ALL','quantifier',1,'p_quantifier','parser.py',238),
  ('quantifier -> VALUE','quantifier',1,'p_quantifier','parser.py',239),
  ('quantifier -> THAT','quantifier',1,'p_quantifier','parser.py',240),
  ('quantifier_number -> MAX','quantifier_number',1,'p_quantifier_number','parser.py',245),
  ('quantifier_number -> MIN','quantifier_number',1,'p_quantifier_number','parser.py',246),
  ('quantifier_number -> EXACTLY','quantifier_number',1,'p_quantifier_number','parser.py',247),
  ('quantifier_geral -> SOME','quantifier_geral',1,'p_quantifier_geral','parser.py',252),
  ('quantifier_geral -> ALL','quantifier_geral',1,'p_quantifier_geral','parser.py',253),
  ('quantifier_geral -> VALUE','quantifier_geral',1,'p_quantifier_geral','parser.py',254),
  ('quantifier_geral -> MAX','quantifier_geral',1,'p_quantifier_geral','parser.py',255),
  ('quantifier_geral -> MIN','quantifier_geral',1,'p_quantifier_geral','parser.py',256),
  ('quantifier_geral -> EXACTLY','quantifier_geral',1,'p_quantifier_geral','parser.py',257),
  ('quantifier_geral -> THAT','quantifier_geral',1,'p_quantifier_geral','parser.py',258),
  ('sizecheck -> EQUAL CARDINALITY','sizecheck',2,'p_sizecheck','parser.py',264),
  ('sizecheck -> GREATER_THAN CARDINALITY','sizecheck',2,'p_sizecheck','parser.py',265),
  ('sizecheck -> LESS_THAN CARDINALITY','sizecheck',2,'p_sizecheck','parser.py',266),
  ('sizecheck -> GREATER_THAN EQUAL CARDINALITY','sizecheck',3,'p_sizecheck','parser.py',267),
  ('sizecheck -> LESS_THAN EQUAL CARDINALITY','sizecheck',3,'p_sizecheck','parser.py',268),
  ('namespace_type -> NAMESPACE TYPE','namespace_type',2,'p_namespace_type','parser.py',282),
  ('namespace_type -> NAMESPACE TYPE OPEN_BRACKET sizecheck CLOSE_BRACKET','namespace_type',5,'p_namespace_type','parser.py',283),
  ('individuals_section -> INDIVIDUALS individuals','individuals_section',2,'p_individuals_section','parser.py',290),
  ('individuals_section -> empty','individuals_section',1,'p_individuals_section','parser.py',291),
  ('individuals -> INDIVIDUAL_NAME','individuals',1,'p_individuals','parser.py',298),
  ('individuals -> INDIVIDUAL_NAME COMMA individuals','individuals',3,'p_individuals','parser.py',299),
  ('comma_and -> COMMA','comma_and',1,'p_comma_and','parser.py',306),
  ('comma_and -> AND','comma_and',1,'p_comma_and','parser.py',307),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',312),
]
