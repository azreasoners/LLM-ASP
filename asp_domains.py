task1 = '''
%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
query(at(A, where)) :- whereAgent(A).

% Find where last location of agent is
%answer(L) :- query(at(A, where)), holds_at(at(A, L), T), T>=Tx+1: timepoint(Tx).
answer(L) :- query(at(A, where)), holds_at(at(A, L), T), T>=Tx: holds_at(at(A, _), Tx).
'''

task2 = '''
%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
query(at(I, where)) :- loc(I).

% Find where last location of object is
%answer(L) :- query(at(A, where)), holds_at(at(A, L), T), T>=Tx+1: timepoint(Tx).
answer(L) :- query(at(A, where)), holds_at(at(A, L), T), T>=Tx: holds_at(at(A, _), Tx).
'''

task3 = '''
% the query before(O, L) is given, asking about the location of O before moving to L
% find all location changes of the queried object
location_change(L1, L2, T) :- before(O, _), holds_at(at(O, L1), T), holds_at(at(O, L2), T+1), L1 != L2.

% find the last location change to queried location
answer(L1) :- before(_, L2), location_change(L1, L2, T), T>=Tx: location_change(_, L2, Tx).
'''

task4 = '''
answer(A) :- query(what, R1, B), is(A, R1, B).
answer(B) :- query(A, R1, what), is(A, R1, B).
'''

task5 = '''
candidate(A1, T) :- query(action(who, give, A, I)), happens(action(A1, give, A2, I), T), 
    A2=A: A!=anyone.
candidate(A2, T) :- query(action(A, give, who, I)), happens(action(A1, give, A2, I), T), 
    A1=A: A!=anyone.
candidate(I, T) :- query(action(A1, give, A2, what)), happens(action(A1, give, A2, I), T).
location(unknown).

%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
give(A1, A2, I, T) :- gave(A1, I, A2, T).
query(action(A1, give, A2, what)) :- whatWasGiven(A1, A2).
query(action(anyone, give, who, I)) :- received(I).
query(action(A1, give, who, I)) :- whoWasGiven(A1, I).
query(action(who, give, anyone, I)) :- whoGave(I).
query(action(who, give, A2, I)) :- whoGave(I, A2).

answer(A) :- candidate(A, T), Tx<=T: candidate(_, Tx).
'''

task6 = '''
answer(yes) :- query(at(A, L)), holds_at(at(A, L), T), Tx<=T: holds_at(at(A, _), Tx).
answer(no) :- not answer(yes).

%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
query(at(A, L)) :- isInQ(A, L).
'''

task7 = '''
% find all items I that A is carrying at the last moment; then count I
carry(A, I) :- query(carry(A, count)), holds_at(carry(A,I),T), 
    T>Tx: happens(E,Tx).
location(unknown).

%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
query(carry(A, count)) :- howMany(A).
%give(A1, A2, I, T) :- gave(A1, I, A2, T).
answer(N) :- query(carry(A, count)), N=#count{I: carry(A, I)}.
'''

task8 = '''
%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
query(carry(A, what)) :- carrying(A).
location(unknown).

% find all items I that A is carrying at the last moment
answer(I) :- query(carry(A, what)), holds_at(carry(A,I),T), 
    T>Tx: happens(E,Tx).
'''

task9 = task6

task10 = '''
released(F,T) :- fluent(F), timepoint(T).

%answer(yes) :- query(at(A, L)), holds_at(at(A, L), T), Tx<=T: holds_at(at(A, _), Tx).
answer(yes) :- query(at(A, L)), holds_at(at(A, L), T), Tx<=T: holds_at(at(A, _), Tx); Ty+1<=T: isEither(A,_,_,Ty).
answer(maybe) :- query(at(A, L)), timepoint(T),
    1{isEither(A, L, _, T); isEither(A, _, L, T)},
    Tx<=T: holds_at(at(A, _), Tx);
    Tx<=T: isEither(A, _, _, Tx).

answer(no) :- not answer(yes), not answer(maybe).

%%%% Interface -- these rules may be removed if we let GPT3 return the heads directly
query(at(A, L)) :- isInQ(A, L).
%holds_at(at(A, L), T+1) :- isIn(A, L, T).
%holds_at(at(A, L), T) :- isIn(A, L, T).
go(A, L, T) :- move(A, L, T).
timepoint(T) :- isIn(_, _, T).
timepoint(T) :- isEither(_, _, _, T).
'''

task11 = task1

task12 = '''
%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
query(at(A, where)) :- whereAgent(A).
go(A1, L, T) :- go(A1, A2, L, T).
go(A2, L, T) :- go(A1, A2, L, T).

% Find where last location of agent is
%answer(L) :- query(at(A, where)), holds_at(at(A, L), T), T>=Tx+1: timepoint(Tx).
answer(L) :- query(at(A, where)), holds_at(at(A, L), T), T>=Tx: holds_at(at(A, _), Tx).
'''

task13 = task12

task14 = task3

task15 = '''
% if N belongs to species S1, and S1 is afraid of S2, then N is afraid of S2
% PS: the last literal singular_plural(S2,_) is not needed once we remove the interface part below
answer(S2) :- query(afraid(N, what)), is(N, S1), species_afraid(S1,S2), singular_plural(S2,_).

%%%% Interface -- these rules can be removed if we let GPT3 return the singular directly
singular_plural(wolf,wolves; mouse,mice; cat,cats; sheep,sheep).
species_afraid(Singular1, Singular2) :- species_afraid(Plural1, Plural2), 
    singular_plural(Singular1, Plural1),
    singular_plural(Singular2, Plural2).

query(afraid(N, what)) :- agent_afraid(N).
'''

task16 = '''
animal(frog;lion;swan;rhino).
color(green;white;yellow;gray).
isColor(Agent2,Color):- isAnimal(Agent,Animal),isColor(Agent,Color),isAnimal(Agent2,Animal).
answer(Color) :- isColor(Name), isColor(Name,Color).
#show answer/1.
'''

task17 = '''
% assume the 2nd queried object is at location (0,0)
location(B, 0, 0) :- query(_, _, B).

% the queried relation R is correct if its offset agrees with the location of A
answer(yes) :- query(A, R, B), offset(R, Dx, Dy), location(A, X, Y),
    X>0: Dx=1; X<0: Dx=-1;
    Y>0: Dy=1; Y<0: Dy=-1.

answer(no) :- not answer(yes).

%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
is(A, left, B) :- leftOf(A, B).
is(A, right, B) :- rightOf(A, B).
is(A, top, B) :- above(A, B).
is(A, down, B) :- below(A, B).
query(A, left, B) :- leftOf_nondirect(A, B).
query(A, right, B) :- rightOf_nondirect(A, B).
query(A, top, B) :- above_nondirect(A, B).
query(A, down, B) :- below_nondirect(A, B).
'''

task18 = '''
smaller(A, B) :- bigger(B, A).
smaller(A, C) :- smaller(A, B), smaller(B, C).
answer(yes) :- query(smaller(A, B)), smaller(A, B).
answer(no) :- not answer(yes).

%%%% Interface -- these rules can be removed if we let GPT3 return the heads directly
query(smaller(A, B)) :- doesFit(A, B).
query(smaller(A, B)) :- isBigger(B, A).
'''

task19 = '''
agent(agent).
maxtime(10).
% location
location(L) :- is(L,_,_).
location(L) :- is(_,_,L).

% for each timestep, we take at most 1 action
{happens(action(agent, goto, D), T): direction(D)}1 :- timepoint(T).

% initial location
holds_at(at(agent, L), 0) :- initial_loc(L).

% goal
:- goal(L), not holds_at(at(agent, L), _).

% we aim to achieve the goal as early as possible
:~ goal(L), holds_at(at(agent, L), T). [-T@1, goal]
'''

task20 = '''
motivation(hungry, kitchen).
motivation(tired, bedroom).
motivation(thirsty, kitchen).
motivation(bored, garden).

motivation(thirsty, milk).
motivation(tired, pajamas).
motivation(bored, football).
motivation(hungry, apple).

loc(kitchen). loc(bedroom). loc(kitchen). loc(garden).
obj(pajamas). obj(football). obj(milk). obj(apple).

answer(Location) :- query(where, Agent, go), is(Agent, Quality), motivation(Quality,Location), loc(Location).
answer(Quality) :- query(why, Agent, go, Location), is(Agent, Quality), motivation(Quality, Location), loc(Location).
answer(Quality) :- query(why,Agent, get, Obj),is(Agent, Quality), motivation(Quality, Obj), obj(Obj).
answer(Location) :- query(where, Agent, go), is(Agent, Quality), motivation(Quality, Location), loc(Location).
'''



babi_tasks={1: task1,
             2: task2,
             3: task3,
             4: task4,
             5: task5,
             6: task6,
             7: task7,
             8: task8,
             9:  task9,
             10: task10,
             11: task11,
             12: task12,
             13: task13,
             14: task14,
             15: task15,
             16: task16,
             17: task17,
             18: task18,
             19: task19,
             20: task20}


stepgame = '''
% assume the 2nd queried object is at location (0,0)
location(Q2, 0, 0) :- query(_, Q2).

% extract answer relation R such that the offset (Ox,Oy) of R is in the same direction of (X,Y)
answer(R) :- query(Q1, _), location(Q1, X, Y), offset(R, Ox, Oy),
    Ox=-1: X<0; Ox=0: X=0; Ox=1: X>0;
    Oy=-1: Y<0; Oy=0: Y=0; Oy=1: Y>0.
'''

gscan = '''
%********************
* find the goal
*********************%

% features of objects
feature(O, shape, V) :- shape(O, V).
feature(O, color, V) :- color(O, V).
feature(O, size, V) :- size(O, V).

% feature of destination
feature(destination, V) :- query(walk), queryDesc(V).
feature(destination, V) :- query(push), queryDesc(V).
feature(destination, V) :- query(pull), queryDesc(V).

% find the destination object and location
pos_same(destination, O) :- feature(O,_,_),
    feature(O,_,V): feature(destination, V), feature(_,_,V).

same(destination, O) :- pos_same(destination, O), feature(O, size, V),
    Vx<=V: feature(destination, big), pos_same(destination, Ox), feature(Ox, size, Vx);
    Vx>=V: feature(destination, small), pos_same(destination, Ox), feature(Ox, size, Vx).

goal(at(agent,L)) :- same(destination, O), pos(O,L).


%********************
* basic atoms
*********************%
agent(agent).
item(I) :-  pos(I, L), I!=agent.
location((X,Y)) :- X=0..N-1, Y=0..N-1, gridSize(N).

is((X1,Y1), east, (X2,Y2)) :- location((X1,Y1)), location((X2,Y2)), X1=X2, Y1=Y2+1.
is((X1,Y1), west, (X2,Y2)) :- location((X1,Y1)), location((X2,Y2)), X1=X2, Y1=Y2-1.
is((X1,Y1), north, (X2,Y2)) :- location((X1,Y1)), location((X2,Y2)), X1=X2-1, Y1=Y2.
is((X1,Y1), south, (X2,Y2)) :- location((X1,Y1)), location((X2,Y2)), X1=X2+1, Y1=Y2.

pos_actions(walk; turn_left; turn_right; stay; push; pull).
left_dir(east, north; north, west; west, south; south, east).

%********************
* atoms in DEC_AXIOMS
*********************%

% fluent/1
fluent(dir(A, L)) :- agent(A), direction(L).
fluent(ready(A)) :- agent(A).

% event/1
event(action(Agent, A)) :- agent(Agent), pos_actions(A).

% initial fluent values
holds_at(at(O,L),0) :- pos(O, L).
holds_at(dir(A,D),0) :- dir(A, D).

% for each timestep, we take at most 1 action
{happens(action(agent, A), T): pos_actions(A)}1 :- timepoint(T).

% initial location
holds_at(at(agent, L), 0) :- initial_loc(L).

%%%%%%%%%%%%%%%
% action -- walk (to check simplification)
%%%%%%%%%%%%%%%

% initiates/3
initiates(action(A, walk), at(A, L2), T) :- agent(A), location(L), timepoint(T),
    holds_at(dir(A, D), T),
    holds_at(at(A, L1), T),
    is(L2, D, L1).

% terminates/3
terminates(action(A, walk), at(A, L1), T) :- agent(A), location(L), timepoint(T),
    holds_at(dir(A, D), T),
    holds_at(at(A, L1), T),
    is(L2, D, L1).

% precondition
% we don't walk in a deadend (i.e., the walk will result in no location change)
:- happens(action(agent, walk), T), not initiates(action(agent, walk), _, T).

%%%%%%%%%%%%%%%
% action -- turn_left (to check simplification)
%%%%%%%%%%%%%%%

% initiates/3
initiates(action(A, turn_left), dir(A, D2), T) :- agent(A), timepoint(T),
    holds_at(dir(A, D1), T),
    left_dir(D1, D2).

% terminates/3
terminates(action(A, turn_left), dir(A, D1), T) :- agent(A), timepoint(T),
    holds_at(dir(A, D1), T).

%%%%%%%%%%%%%%%
% action -- turn_right (to check simplification)
%%%%%%%%%%%%%%%

% initiates/3
initiates(action(A, turn_right), dir(A, D2), T) :- agent(A), timepoint(T),
    holds_at(dir(A, D1), T),
    left_dir(D2, D1).

% terminates/3
terminates(action(A, turn_right), dir(A, D), T) :- agent(A), timepoint(T),
    holds_at(dir(A, D), T).

%%%%%%%%%%%%%%%
% action -- push/pull
%%%%%%%%%%%%%%%

% initiates/3 for objects with size <= 2
initiates(action(A, push), at(A, L2), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    is(L2, D, L1), feature(Target, size, V), V <= 2.

initiates(action(A, push), at(Target, L2), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    is(L2, D, L1), feature(Target, size, V), V <= 2.

initiates(action(A, pull), at(A, L2), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    is(L1, D, L2), feature(Target, size, V), V <= 2.

initiates(action(A, pull), at(Target, L2), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    is(L1, D, L2), feature(Target, size, V), V <= 2.

% terminates/3 for objects with size <= 2
terminates(action(A, push), at(A, L1), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    is(L2, D, L1), feature(Target, size, V), V <= 2.

terminates(action(A, push), at(Target, L1), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    is(L2, D, L1), feature(Target, size, V), V <= 2.

terminates(action(A, pull), at(A, L1), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    is(L1, D, L2), feature(Target, size, V), V <= 2.

terminates(action(A, pull), at(Target, L1), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    is(L1, D, L2), feature(Target, size, V), V <= 2.

% initiates/3 for objects with size >= 3

initiates(action(A, push), ready(A), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T), not holds_at(ready(A), T),
    same(destination, Target), holds_at(at(Target, L1), T), feature(Target, size, V), V >= 3.

initiates(action(A, push), at(A, L2), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T), holds_at(ready(A), T),
    same(destination, Target), holds_at(at(Target, L1), T), feature(Target, size, V), V >= 3,
    is(L2, D, L1).

initiates(action(A, push), at(Target, L2), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T), holds_at(ready(A), T),
    same(destination, Target), holds_at(at(Target, L1), T), feature(Target, size, V), V >= 3,
    is(L2, D, L1).

initiates(action(A, pull), ready(A), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T), not holds_at(ready(A), T),
    same(destination, Target), holds_at(at(Target, L1), T), feature(Target, size, V), V >= 3.

initiates(action(A, pull), at(A, L2), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T), holds_at(ready(A), T),
    same(destination, Target), holds_at(at(Target, L1), T), feature(Target, size, V), V >= 3,
    is(L1, D, L2).

initiates(action(A, pull), at(Target, L2), T) :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T), holds_at(ready(A), T),
    same(destination, Target), holds_at(at(Target, L1), T), feature(Target, size, V), V >= 3,
    is(L1, D, L2).

% terminates/3 for objects with size >= 3

{ terminates(action(A, push), ready(A), T);
  terminates(action(A, push), at(A, L1), T);
  terminates(action(A, push), at(Target, L1), T) 
}=3 :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T), holds_at(ready(A), T),
    same(destination, Target), holds_at(at(Target, L1), T), feature(Target, size, V), V >= 3,
    is(L2, D, L1).

{ terminates(action(A, pull), ready(A), T);
  terminates(action(A, pull), at(A, L1), T);
  terminates(action(A, pull), at(Target, L1), T) 
}=3 :-
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T), holds_at(ready(A), T),
    same(destination, Target), holds_at(at(Target, L1), T), feature(Target, size, V), V >= 3,
    is(L1, D, L2).

% precondition

% 1. we don't push/pull in a deadend (i.e., the action will result in no location change)
:- happens(action(agent, push), T), not initiates(action(agent, push), _, T).
:- happens(action(agent, pull), T), not initiates(action(agent, pull), _, T).

% 2. the agent can push/pull only if it's queried
:- happens(action(agent, push), _), not query(push).
:- happens(action(agent, pull), _), not query(pull).

% 2. it's not allowed to have 3 objects (agent + 2 items) in the same cell
% (I use holds_at(_, T) instead of timepoint(T) since the latter doesn't cover the last T+1 timestamp)
%:- holds_at(_, T), location(L), N = #count{O: holds_at(at(O, L), T)}, N>2.

% 3. after push/pull, the agent cannot do a different action in {walk, push, pull}
:- happens(action(agent, A1), T1), happens(action(agent, A2), T2), A1!=A2, T1<T2,
    1{A1=push; A1=pull},
    1{A2=push; A2=pull; A2=walk}.

% 4. the agent cannot change its direction to push/pull after reaching destination
reach_destination(T) :- goal(at(agent,L)), holds_at(at(agent, L), T),
    not reach_destination(Tx): timepoint(Tx), Tx<T.
:- reach_destination(T1), holds_at(dir(agent, D1), T1), 
    holds_at(dir(agent, D2), T2), happens(action(agent, push), T2), T1<T2, D1!=D2.
:- reach_destination(T1), holds_at(dir(agent, D1), T1), 
    holds_at(dir(agent, D2), T2), happens(action(agent, pull), T2), T1<T2, D1!=D2.

%%%%%%%%%%%%%%%
% goal
%%%%%%%%%%%%%%%

% 1. (optional to speed up) we need to reach the destination and as early as possible
:- goal(at(agent,L)), not reach_destination(_).
:~ goal(at(agent, L)), reach_destination(T). [T@10, goal]

% 2. we need to reach the goal and as early as possible
%   a. the direction when reaching goal must align with the direction when reaching destination
%   b. if it's not deadend, there must be something blocking the next push/pull
reach_goal(T) :- 
    agent(A), holds_at(at(A, L1), T), holds_at(dir(A, D), T),
    same(destination, Target), holds_at(at(Target, L1), T),
    reach_destination(Tr), holds_at(dir(A, D), Tr),
    holds_at(at(_, L2), T): query(push), is(L2, D, L1);
    holds_at(at(_, L2), T): query(pull), is(L1, D, L2);
    not reach_goal(Tx): timepoint(Tx), Tx<T.
:- not reach_goal(_).
:~ reach_goal(T). [T@9, goal]




% 3. if the goal is push/pull, we want to push/pull as many times as possible
%:~ query(push), happens(action(agent, push), T). [-1@9, push, T]
%:~ query(pull), happens(action(agent, pull), T). [-1@9, pull, T]

% 4. we want to complete the plan as early as possible (this is not necessary)
%:~ happens(action(agent, _), T). [T@8, plan]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% additional requirements to achieve the goal
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% the agent cannot move further before reaching destination
:- reach_destination(T), goal(at(agent, (Xg,Yg))),
    holds_at(at(agent, (X1,Y1)), Tx), holds_at(at(agent, (X2,Y2)), Tx+1), Tx<T,
    |X1-Xg| + |Y1-Yg| < |X2-Xg| + |Y2-Yg|.

% by default, walking all the way horizontally first and then vertically
move(horizontally, T) :- happens(action(agent, walk), T), holds_at(dir(agent, D), T), 1{D=east; D=west}.
move(vertically, T) :- happens(action(agent, walk), T), holds_at(dir(agent, D), T), 1{D=south; D=north}.
:- not while(zigzagging), move(horizontally, T1), move(vertically, T2), T1>T2.

% hesitantly: the agent must stay after every action in {walk, push, pull}
while(hesitantly) :- queryDesc(hesitantly).
:- while(hesitantly), happens(action(agent, A), T),
    1{A=walk; A=push; A=pull},
    not happens(action(agent, stay), T+1).

% cautiously
cautious(T) :- happens(action(agent, turn_left), T), 
    happens(action(agent, turn_right), T+1),
    happens(action(agent, turn_right), T+2),
    happens(action(agent, turn_left), T+3).

% the agent must be cautious before every action in {walk, push, pull}
:- while(cautiously), happens(action(agent, A), T),
    1{A=walk; A=push; A=pull},
    not cautious(T-4).

% spinning
spin(T) :- happens(action(agent, turn_left), T), 
    happens(action(agent, turn_left), T+1),
    happens(action(agent, turn_left), T+2),
    happens(action(agent, turn_left), T+3).

% we always spin at the beginning if there is any action
:- while(spinning), happens(_,_), not spin(0).

% we always spin after every action in {walk, push, pull} except for the last one
:- while(spinning), happens(action(agent, A1), T1), happens(action(agent, A2), T2), T1<T2,
    1{A1=walk; A1=push; A1=pull},
    1{A2=walk; A2=push; A2=pull},
    not spin(T1+1).

% zigzagging
% if horizontal move is needed, the first move must be horizontal
:- while(zigzagging), move(horizontally, _), move(D, Tmin), D!=horizontally,
    Tmin<=Tx: move(_,Tx).
% if a different kind of move D2 is after D1, D2 must be followed directly
:- while(zigzagging), move(D1, T1), move(D2, T2), D1!=D2, T1<T2,
    not move(D2, T1+2).
'''

block_world = '''
%%%%%
% Set up the environment
%%%%%

% Define the number of grippers for the robot
#const grippers=1.

% Define the maximum number of steps to consider
{maxtime(M): M=0..10} = 1.
:~ maxtime(M). [M]

%%%%%
% Extract the features for all items in the intial and goal states
% we assume these items form the complete set of items in this example
%%%%%

feature(I, F) :- on(I,_), F=@gen_feature(I).
feature(I, F) :- on(I,_,0), F=@gen_feature(I).
feature(I, F) :- on(_,I), I!="table", F=@gen_feature(I).
feature(I, F) :- on(_,I,0), I!="table", F=@gen_feature(I).

% Define all locations
location("table").
location(L) :- feature(L, block).
location(L) :- feature(L, bowl).

%********************
* atoms in DEC_AXIOMS
*********************%

% happens/2
{happens(E,T): event(E)}grippers :- timepoint(T).

% **** constraints ****
% every action should have some effect		
:- happens(E,T), not initiates(E,_,T).
% the goal must be achieved in the end
:- maxtime(M), on(A, B), not holds_at(on(A,B), M+1).

% At any time T, for each block/bowl, there cannot be 2 items directly on it
:- timepoint(T), feature(L, _), 2{holds_at(on(I, L), T): feature(I,_)}.

% if there are bowls on the table, a block can only be on a block or a bowl;
:- feature(_,bowl), feature(I,block), holds_at(on(I,L),_), {feature(L, block); feature(L, bowl)} = 0.

% there cannot be more than max_height-1 blocks stacked on a block
up(A,B,T) :- holds_at(on(A, B), T).
up(A,C,T) :- up(A,B,T), up(B,C,T).
:- timepoint(T), feature(L, block), #count{I: up(I,L,T)} >= max_height.
'''