family = '''
% gender

male(B) :- grandson(A, B).
male(B) :- son(A, B).
male(B) :- nephew(A, B).
male(B) :- brother(A, B).
male(B) :- father(A, B).
male(B) :- uncle(A, B).
male(B) :- grandfather(A, B).

female(B) :- granddaughter(A, B).
female(B) :- daughter(A, B).
female(B) :- niece(A, B).
female(B) :- sister(A, B).
female(B) :- mother(A, B).
female(B) :- aunt(A, B).
female(B) :- grandmother(A, B).

% gender-irrelevant relationships

sibling(A, B) :- siblings(A, B).
sibling(A, B) :- brother(A, B).
sibling(A, B) :- sister(A, B).
sibling(A, B) :- parent(A, C), parent(B, C), A != B.
sibling(A, B) :- sibling(B, A).
sibling(A, B) :- sibling(A, C), sibling(C, B), A != B.
sibling(A, B); sibling_in_law(A, B) :- child(A, C), uncle(C, B).
sibling(A, B); sibling_in_law(A, B) :- child(A, C), aunt(C, B).
sibling(A, B); sibling_in_law(A, B) :- nephew(A, C), parent(C, B).
sibling(A, B); sibling_in_law(A, B) :- niece(A, C), parent(C, B).
sibling_in_law(A, B) :- sibling_in_law(B, A).
:- spouse(A, B), sibling(A, B).
:- spouse(A, B), sibling_in_law(A, B).
:- sibling(A, B), sibling_in_law(A, B).

spouse(A, B) :- wife(A, B).
spouse(A, B) :- husband(A, B).
spouse(A, B) :- spouse(B, A).

parent(A, B) :- father(A, B).
parent(A, B) :- mother(A, B).
parent(A, B) :- parent(A, C), spouse(C, B).
parent(A, B) :- sibling(A, C), parent(C, B).
parent(A, B) :- child(B, A).
parent(A, B) :- spouse(A, C), parent_in_law(C, B).
parent(A, B); parent_in_law(A, B) :- parent(C, A), grandparent(C, B).
parent_in_law(A, B) :- spouse(A, C), parent(C, B).
parent_in_law(A, B) :- parent_in_law(A, C), spouse(C, B).
parent_in_law(A, B) :- child_in_law(B, A).

child(A, B) :- children(A, B).
child(A, B) :- son(A, B).
child(A, B) :- daughter(A, B).
child(A, B) :- spouse(A, C), child(C, B).
child(A, B) :- child(A, C), sibling(C, B).
child(A, B) :- parent(B, A).
child_in_law(A, B) :- son_in_law(A, B).
child_in_law(A, B) :- daughter_in_law(A, B).
child_in_law(A, B) :- parent_in_law(B, A).

grandparent(A, B) :- grandfather(A, B).
grandparent(A, B) :- grandmother(A, B).
grandparent(A, B) :- parent(A, C), parent(C, B).
grandparent(A, B) :- grandchild(B, A).
grandparent(A, B) :- sibling(A, C), grandparent(C, B).
grandparent(A, B) :- grandparent(A, C), spouse(C, B).

grandchild(A, B) :- grandson(A, B).
grandchild(A, B) :- granddaughter(A, B).
grandchild(A, B) :- grandparent(B, A).

greatgrandparent(A, B) :- grandparent(A, C), parent(C, B).
greatgrandchild(A, B) :- greatgrandparent(B, A).

:- parent(A, B), parent(B, A).
:- parent(A, B), parent_in_law(A, B).


% gender-relevant relationships

greatgrandson(A, B) :- greatgrandchild(A, B), male(B).
greatgranddaughter(A, B) :- greatgrandchild(A, B), female(B).

grandson(A, B) :- grandchild(A, B), male(B).
granddaughter(A, B) :- grandchild(A, B), female(B).

son(A, B) :- child(A, B), male(B).
daughter(A, B) :- child(A, B), female(B).
nephew(A, B) :- sibling(A, C), son(C, B).
niece(A, B) :- sibling(A, C), daughter(C, B).

husband(A, B) :- spouse(A, B), male(B).
wife(A, B) :- spouse(A, B), female(B).
brother(A, B) :- sibling(A, B), male(B).
sister(A, B) :- sibling(A, B), female(B).

father(A, B) :- parent(A, B), male(B).
mother(A, B) :- parent(A, B), female(B).
uncle(A, B) :- parent(A, C), brother(C, B).
aunt(A, B) :- parent(A, C), sister(C, B).

grandfather(A, B) :- grandparent(A, B), male(B).
grandmother(A, B) :- grandparent(A, B), female(B).

greatgrandfather(A, B) :- greatgrandparent(A, B), male(B).
greatgrandmother(A, B) :- greatgrandparent(A, B), female(B).

son_in_law(A, B) :- child_in_law(A, B), male(B).
daughter_in_law(A, B) :- child_in_law(A, B), female(B).
father_in_law(A, B) :- parent_in_law(A, B), male(B).
mother_in_law(A, B) :- parent_in_law(A, B), female(B).








%%%% The following rules are only used for the ablation study on the order of arguments %%%%
father(A,B) :- father_of(B,A).
mother(A,B) :- mother_of(B,A).
parent(A,B) :- parent_of(B,A).
son(A,B) :- son_of(B,A).
daughter(A,B) :- daughter_of(B,A).
child(A,B) :- child_of(B,A).
grandfather(A,B) :- grandfather_of(B,A).
grandmother(A,B) :- grandmother_of(B,A).
grandson(A,B) :- grandson_of(B,A).
granddaughter(A,B) :- granddaughter_of(B,A).
wife(A,B) :- wife_of(B,A).
husband(A,B) :- husband_of(B,A).
spouse(A,B) :- spouse_of(B,A).
sibling(A,B) :- sibling_of(B,A).
nephew(A,B) :- nephew_of(B,A).
niece(A,B) :- niece_of(B,A).
uncle(A,B) :- uncle_of(B,A).
aunt(A,B) :- aunt_of(B,A).
child_in_law(A,B) :- child_in_law_of(B,A).
parent_in_law(A,B) :- parent_in_law_of(B,A).
sister(A,B) :- sister_of(B,A).
brother(A,B) :- brother_of(B,A).

father(A,B) :- fatherOf(B,A).
mother(A,B) :- motherOf(B,A).
parent(A,B) :- parentOf(B,A).
son(A,B) :- sonOf(B,A).
daughter(A,B) :- daughterOf(B,A).
child(A,B) :- childOf(B,A).
grandfather(A,B) :- grandfatherOf(B,A).
grandmother(A,B) :- grandmotherOf(B,A).
grandson(A,B) :- grandsonOf(B,A).
granddaughter(A,B) :- granddaughterOf(B,A).
wife(A,B) :- wifeOf(B,A).
husband(A,B) :- husbandOf(B,A).
spouse(A,B) :- spouseOf(B,A).
sibling(A,B) :- siblingOf(B,A).
nephew(A,B) :- nephewOf(B,A).
niece(A,B) :- nieceOf(B,A).
uncle(A,B) :- uncleOf(B,A).
aunt(A,B) :- auntOf(B,A).
child_in_law(A,B) :- childInLawOf(B,A).
parent_in_law(A,B) :- parentInLawOf(B,A).
sister(A,B) :- sisterOf(B,A).
brother(A,B) :- brotherOf(B,A).
'''