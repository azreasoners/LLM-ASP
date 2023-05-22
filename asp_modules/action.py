action = '''
%********************
* common interface
* check: if location(unknown) is needed
*********************%

% what happened in the given story
happens(action(A, pickup, I), T) :- pickup(A, I, T).
happens(action(A, drop, I), T) :- drop(A, I, T).
happens(action(A1, give, A2, I), T) :- give(A1, I, A2, T).
happens(action(A, goto, L), T) :- go(A, L, T).
happens(action(A, goto, L), T) :- isIn(A, L, T).

%********************
* basic atoms
*********************%

direction(east; west; north; south).

agent(A) :- happens(action(A, _, _), _).
agent(A) :- happens(action(A, _, _, _), _).
agent(A) :- happens(action(_, give, A, _), _).
item(I) :- happens(action(_, pickup, I), _).
item(I) :- happens(action(_, drop, I), _).
item(I) :- happens(action(_, give, _, I), _).
location(L) :- happens(action(_, goto, L), _), not direction(L).

%********************
* atoms in DEC_AXIOMS
*********************%

% event/1
event(action(A, pickup, I)) :- agent(A), item(I).
event(action(A, drop, I)) :- agent(A), item(I).
event(action(A1, give, A2, I)) :- agent(A1), agent(A2), item(I), A1 != A2.
event(action(A, goto, L)) :- agent(A), location(L).
event(action(A, goto, D)) :- agent(A), direction(D).
event(action(robot, pick_and_place, Src, Dst)) :- feature(Src, block), location(Dst), Src != Dst.

% timepoint/1
timepoint(T) :- happens(_, T). % the timepoint in story
timepoint(T) :- T=0..N, maxtime(N). % the timepoint for planning without story

% fluent/1
fluent(at(A, L)) :- agent(A), location(L).
fluent(at(I, L)) :- item(I), location(L).
fluent(carry(A, I)) :- agent(A), item(I).
fluent(on(B, L)) :- feature(B, block), location(L), B!=L.

% -released_at/2
%   1. -released_at(F, T) means commonsense law of inertia (CLI) can be applied to fluent F at T
%   2. CLI is also applied to this literal itself
-released_at(F, 0) :- fluent(F).

% holds_at/2
% initial states of fluents -- only location of items needs to be guessed
{holds_at(at(I, L), 0): location(L)} = 1 :- item(I).
holds_at(on(B, L), 0) :- on(B, L, 0).

% happens/2
% for each timepoint, at most 1 event happens; and it happens as fewer as possible
% {happens(E, T): event(E)}1 :- timepoint(T). % this rule would slow down many tasks
:~ happens(E, T). [1@0, E, T]

% every action should have some effect
%:- happens(E,T), not initiates(E,_,T).

% precondition on actions -- pickup
:- happens(action(A, pickup, I), T), holds_at(at(A, L1), T), holds_at(at(I, L2), T), L1 != L2.

% initiates/3 and terminates/3

% effect of actions -- pickup
initiates(action(A, pickup, I), carry(A, I), T) :- agent(A), item(I), timepoint(T).

% effect of actions -- drop
terminates(action(A, drop, I), carry(A, I), T) :- agent(A), item(I), timepoint(T).

% effect of actions -- give
initiates(action(A1, give, A2, I), carry(A2, I), T) :- agent(A1), agent(A2), item(I), timepoint(T), A1 != A2.
terminates(action(A1, give, A2, I), carry(A1, I), T) :- agent(A1), agent(A2), item(I), timepoint(T), A1 != A2.

% effect of actions -- goto
initiates(action(A, goto, L), at(A, L), T) :- agent(A), location(L), timepoint(T).
initiates(action(A, goto, L), at(I, L), T) :- holds_at(carry(A, I), T), location(L).
initiates(action(A, goto, D), at(A, L2), T) :- 
    agent(A), location(L1), location(L2), timepoint(T), 
    holds_at(at(A, L1), T), is(L2, D, L1).
terminates(action(A, goto, L1), at(A, L2), T) :- agent(A), location(L1), location(L2), timepoint(T), L1 != L2.
terminates(action(A, goto, L1), at(I, L2), T) :- holds_at(carry(A, I), T), location(L1), location(L2), L1 != L2.
terminates(action(A, goto, Direction), at(A, L), T) :-
    happens(action(A, goto, Direction), T),
    holds_at(at(A, L), T), Direction != L.

% effect of actions -- pick_and_place
initiates(action(robot, pick_and_place, Src, Dst), on(Src, Dst), T) :-
    feature(Src, block), location(Dst), Src != Dst, timepoint(T),
    not holds_at(on(_, Src), T), 
    not holds_at(on(_, Dst), T): Dst!="table".

terminates(action(robot, pick_and_place, Src, Dst), on(Src, L), T) :-
    holds_at(on(Src, L), T), location(Dst), Dst != L.

'''