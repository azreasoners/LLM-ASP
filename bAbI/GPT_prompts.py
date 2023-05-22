


# =============================================================================
# Task 1
# =============================================================================

parse_prompt_1 = '''Please parse the following statements into facts. The available keywords are: pickup, drop, and go.
Sentence: Max journeyed to the bathroom.
Semantic parse: go(Max, bathroom).

Sentence: Mary grabbed the football there.
Semantic parse: pickup(Mary, football).

Sentence: Bob picked up the apple.
Semantic parse: pickup(Bob, apple).

Sentence: Susan dropped the milk.
Semantic parse: drop(Susan, milk).

Sentence: Bob got the football there.
Semantic parse: pickup(Bob, football).

Sentence: Max left the cup.
Semantic parse: drop(Max, cup).

Sentence: Kevin put down the pie there.
Semantic parse: drop(Kevin, pie).

Sentence: John took the football there.
Semantic parse: pickup(John, football).

Sentence: '''

query_prompt_1 ='''Please parse the following questions into query facts. The available keywords are: whereAgent.
Sentence: Where is Mary?
Semantic parse: whereAgent(Mary).

Sentence: Where is Daniel?
Semantic parse: whereAgent(Daniel).

Sentence: Where is Sandra?
Semantic parse: whereAgent(Sandra).

Sentence: Where is John?
Semantic parse: whereAgent(John).

Sentence: '''




# =============================================================================
# Tasks 2 and 3
# =============================================================================

query_prompt_2='''Please parse the following questions into query facts. The available keywords are: loc.
Sentence: Where is the toothbrush?
Semantic parse: loc(toothbrush).

Sentence: Where is the milk?
Semantic parse: loc(milk).

Sentence: Where is the apple?
Semantic parse: loc(apple).

Sentence: Where is the football?
Semantic parse: loc(football).

Sentence: '''


query_prompt_3='''Please parse the following questions into query facts. The available keywords are: before.
Sentence: Where was the football before the bathroom?
Semantic parse: before(football,bathroom).

Sentence: Where was the apple before the garden?
Semantic parse: before(apple,garden).

Sentence: Where was the milk before the kitchen?
Semantic parse: before(milk,kitchen).

Sentence: Where was the apple before the bedroom?
Semantic parse: before(apple,bedroom).

Sentence: Where was the football before the hallway?
Semantic parse: before(football,hallway).

Sentence: '''



# =============================================================================
# Task 4
# =============================================================================

parse_prompt_4= '''Please parse the following statements into facts. The available keywords are: is, eastOf, westOf, northOf, and southOf.
Sentence: The office is east of the hallway.
Semantic parse: is(office, eastOf, hallway).

Sentence: The kitchen is north of the office.
Semantic parse: is(kitchen, northOf, office).

Sentence: The bedroom is west of the hallway.
Semantic parse: is(bedroom, westOf, hallway).

Sentence: The kitchen is west of the bedroom.
Semantic parse: is(kitchen, westOf, bedroom).

Sentence: The bedroom is west of the hallway.
Semantic parse: is(bedroom, westOf, hallway).

Sentence: The office is east of the garden.
Semantic parse: is(office, eastOf, garden).

Sentence: '''



query_prompt_4='''Please parse the following questions into query facts. The available keywords are: query, eastOf, westOf, northOf, and southOf, and what.
Sentence: What is south of the office?
Semantic parse: query(what, southOf, office).

Sentence: What is the hallway east of?
Semantic parse: query(hallway, eastOf, what).

Sentence: What is east of the bedroom?
Semantic parse: query(what, eastOf, bedroom).

Sentence: What is north of the garden?
Semantic parse: query(what, northOf, garden).

Sentence: What is the kitchen west of? 
Semantic parse: query(kitchen, westOf, what). 

Sentence: '''

# =============================================================================
# Task 5
# =============================================================================

parse_prompt_5 = '''Please parse the following statements into facts. The available keywords are: pickup, drop, and go, and give.
Sentence: Max journeyed to the bathroom.
Semantic parse: go(Max, bathroom)

Sentence: Mary grabbed the football there.
Semantic parse: pickup(Mary, football)

Sentence: Bob picked up the apple.
Semantic parse: pickup(Bob, apple)

Sentence: Susan dropped the milk.
Semantic parse: drop(Susan, milk)

Sentence: Mary handed the football to Sandra.
Semantic parse: give(Mary, football, Sandra)

Sentence: Max left the cup.
Semantic parse: drop(Max, cup)

Sentence: Kevin put down the pie there.
Semantic parse: drop(Kevin, pie)

Sentence: Daniel passed the football to Fred.
Semantic parse: give(Daniel, football, Fred)

Sentence: John took the football there.
Semantic parse: pickup(John, football)

Sentence: '''

query_prompt_5_main='''Please parse the following questions into query facts. The available keywords are: whatWasGiven, received, whoWasGiven, and whoGave.
Sentence: What did Bill give to Fred?
Semantic parse: whatWasGiven(Bill, Fred).

Sentence: Who received the football?
Semantic parse: received(football).

Sentence: Who did Jeff give the apple to?
Semantic parse: whoWasGiven(Jeff, apple).

Sentence: Who gave the apple?
Semantic parse: whoGave(apple).

Sentence: Who gave the football to Bill?
Semantic parse: whoGave(football, Bill).

Sentence: '''

query_prompt_5='''Please parse the following questions into query facts. The available keywords are: whatWasGiven, received, whoWasGiven, and whoGave.
Sentence: What did Bill give to Fred?
Semantic parse: whatWasGiven(Bill, Fred).

Sentence: Who received the football?
Semantic parse: received(football).

Sentence: Who did Jeff give the apple to?
Semantic parse: whoWasGiven(Jeff, apple).

Sentence: Who gave the apple?
Semantic parse: whoGave(apple).

Sentence: Who did Mary give the milk to?
Semantic parse: whoWasGiven(Mary, milk).

Sentence: Who gave the football to Bill?
Semantic parse: whoGave(football, Bill).

Sentence: '''


# =============================================================================
# Task 7
# =============================================================================

parse_prompt_7_real = '''Please parse the following statements into facts. The available keywords are: pickup, drop, go, and gave.
Sentence: Max journeyed to the bathroom.
Semantic parse: go(Max, bathroom).

Sentence: Mary grabbed the football there.
Semantic parse: pickup(Mary, football).

Sentence: Bob picked up the apple.
Semantic parse: pickup(Bob, apple).

Sentence: Susan dropped the milk.
Semantic parse: drop(Susan, milk).

Sentence: Mary gave the football to Sandra.
Semantic parse: gave(Mary, football, Sandra).

Sentence: Max left the cup.
Semantic parse: drop(Max, cup).

Sentence: Kevin put down the pie there.
Semantic parse: drop(Kevin, pie).

Sentence: John took the football there.
Semantic parse: pickup(John, football).

Sentence: Daniel passed the football to Sandra.
Semantic parse: gave(Daniel, football, Sandra).

Sentence: '''


parse_prompt_7_fixed_1 = '''Please parse the following statements into facts. The available keywords are: pickup, drop, go, and gave.
Sentence: Max journeyed to the bathroom.
Semantic parse: go(Max, bathroom).

Sentence: Mary grabbed the football there.
Semantic parse: pickup(Mary, football).

Sentence: Bob picked up the apple.
Semantic parse: pickup(Bob, apple).

Sentence: Susan dropped the milk.
Semantic parse: drop(Susan, milk).

Sentence: Mary gave the football to Sandra.
Semantic parse: gave(Mary, football, Sandra).

Sentence: Max left the cup.
Semantic parse: drop(Max, cup).

Sentence: Kevin put down the pie there.
Semantic parse: drop(Kevin, pie).

Sentence: John took the football there.
Semantic parse: pickup(John, football).

Sentence: Daniel passed the football to Sandra.
Semantic parse: gave(Daniel, football, Sandra).

Sentence: '''

parse_prompt_7 = '''Please parse the following statements into facts. The available keywords are: pickup, drop, go, and give.
Sentence: Max journeyed to the bathroom.
Semantic parse: go(Max, bathroom).

Sentence: Mary grabbed the football there.
Semantic parse: pickup(Mary, football).

Sentence: Bob picked up the apple.
Semantic parse: pickup(Bob, apple).

Sentence: Susan dropped the milk.
Semantic parse: drop(Susan, milk).

Sentence: Mary gave the football to Sandra.
Semantic parse: give(Mary, football, Sandra).

Sentence: Max left the cup.
Semantic parse: drop(Max, cup).

Sentence: Kevin put down the pie there.
Semantic parse: drop(Kevin, pie).

Sentence: John took the football there.
Semantic parse: pickup(John, football).

Sentence: '''

query_prompt_7='''Please parse the following questions into query facts. The available keywords are: howMany.
Sentence: How many objects is Mary carrying?
Semantic parse: howMany(Mary).

Sentence: How many objects is Sandra carrying?
Semantic parse: howMany(Sandra).

Sentence: How many objects is Daniel carrying?
Semantic parse: howMany(Daniel).

Sentence: How many objects is John carrying?
Semantic parse: howMany(John).

Sentence: '''


# =============================================================================
# Tasks 8
# =============================================================================

query_prompt_8='''Please parse the following questions into query facts. The available keywords are: carrying.
Sentence: What is Mary carrying?
Semantic parse: carrying(Mary).

Sentence: What is Sandra carrying?
Semantic parse: carrying(Sandra).

Sentence: What is Daniel carrying?
Semantic parse: carrying(Daniel).

Sentence: What is John carrying?
Semantic parse: carrying(John).

Sentence: '''



# =============================================================================
# Tasks 9 & 6
# =============================================================================

parse_prompt_9 = '''Please parse the following statements into facts. The available keywords are: pickup, drop, and go.
Sentence: Max journeyed to the bathroom.
Semantic parse: go(Max, bathroom).

Sentence: Mary grabbed the football there.
Semantic parse: pickup(Mary, football).

Sentence: Bob is in the hallway.
Semantic parse: go(Bob, hallway).

Sentence: Daniel is no longer in the garden.
Semantic parse: go(Daniel, unknown).

Sentence: Susan dropped the milk.
Semantic parse: drop(Susan, milk).

Sentence: Bob got the football there.
Semantic parse: pickup(Bob, football).

Sentence: Max left the cup.
Semantic parse: drop(Max, cup).

Sentence: Kevin is in the bathroom.
Semantic parse: go(Kevin, bathroom).

Sentence: John took the football there.
Semantic parse: pickup(John, football).

Sentence: Sandra is not in the bedroom.
Semantic parse: go(Sandra, unknown).

Sentence: '''

query_prompt_9='''Please parse the following questions into query facts. The available keywords are: isInQ.
Sentence: Is Mary in the bedroom? 
Semantic parse: isInQ(Mary, bedroom).

Sentence: Is Daniel in the bathroom?
Semantic parse: isInQ(Daniel, bathroom).

Sentence: Is Sandra in the office?
Semantic parse: isInQ(Sandra, office).

Sentence: Is Daniel in the hallway?
Semantic parse: isInQ(Daniel, hallway).

Sentence: '''


# =============================================================================
# Task 10
# =============================================================================

parse_prompt_10 = '''Please parse the following statements into facts. The available keywords are: go, isIn, and isEither.
Sentence: Fred is either in the school or the park.
Semantic parse: isEither(Fred, school, park).

Sentence: Mary went back to the office.
Semantic parse: go(Mary,office).

Sentence: Fred moved to the cinema.
Semantic parse: go(Fred,cinema).

Sentence: Fred is in the office.
Semantic parse: isIn(Fred,office).

Sentence: Fred travelled to the cinema.
Semantic parse: go(Fred,cinema).

Sentence: Mary moved to the park.
Semantic parse: go(Mary,park).

Sentence: Julie is either in the park or the office.
Semantic parse: isEither(Julie,park,office).

Sentence: Julie journeyed to the bedroom.
Semantic parse: go(Julie,bedroom).

Sentence: Bill is in the cinema.
Semantic parse: isIn(Bill,cinema).

Sentence: '''


query_prompt_10 = '''Please parse the following questions into query facts. The available keywords are: isInQ.
Sentence: Is Mary in the office?
Semantic parse: isInQ(Mary,office).

Sentence: Is Fred in the park?
Semantic parse: isInQ(Fred,park).

Sentence: Is Mary in the school?
Semantic parse: isInQ(Mary,school).

Sentence: Is Julie in the kitchen?
Semantic parse: isInQ(Julie,kitchen).

Sentence: Is Bill in the school?
Semantic parse: isInQ(Bill,school).

Sentence: Is Julie in the bedroom?
Semantic parse: isInQ(Julie,bedroom).

Sentence: '''




# =============================================================================
# Task 11
# =============================================================================

parse_prompt_11_previous ='''Please parse the following sentences into facts. The available keywords are: go.
Sentences:
Mary went back to the bathroom.
After that she went to the bedroom.
Daniel moved to the office.
Afterwards he moved to the hallway.
John travelled to the bathroom.
After that he journeyed to the hallway.

Semantic Parse:
go(Mary, bathroom).
go(Mary, bedroom).
go(Daniel, office).
go(Daniel, hallway).
go(John, bathroom).
go(John, hallway).

Sentences:
Sandra went back to the bathroom.
Afterwards she travelled to the office.

Semantic Parse:
go(Sandra, bathroom).
go(Sandra, office)

Sentences:
Mary travelled to the bedroom.
Then she went back to the bathroom.
Mary travelled to the hallway.
Following that she went to the garden.
Sandra went to the garden.
After that she went to the kitchen.
Mary journeyed to the kitchen.
After that she moved to the bedroom.

Semantic Parse:
go(Mary, bedroom).
go(Mary, bathroom).
go(Mary, hallway).
go(Mary, garden).
go(Sandra, garden).
go(Sandra, kitchen).
go(Mary, kitchen).
go(Mary, bedroom).

Sentences:
'''

parse_prompt_11 ='''Please parse the following sentences into facts. The available keywords are: go.
Sentences:
Mary went back to the bathroom.
After that she went to the bedroom.
Daniel moved to the office.
Afterwards he moved to the hallway.
John travelled to the bathroom.
After that he journeyed to the hallway.

Semantic Parse:
go(Mary, bathroom).
go(Mary, bedroom).
go(Daniel, office).
go(Daniel, hallway).
go(John, bathroom).
go(John, hallway).

Sentences:
Sandra went back to the bathroom.
Afterwards she travelled to the office.

Semantic Parse:
go(Sandra, bathroom).
go(Sandra, office)

Sentences:
Mary travelled to the bedroom.
Then she went back to the bathroom.
Mary travelled to the hallway.
Following that she went to the garden.
Sandra went to the garden.
After that she went to the kitchen.
Mary journeyed to the kitchen.
After that she moved to the bedroom.

Semantic Parse:
go(Mary, bedroom).
go(Mary, bathroom).
go(Mary, hallway).
go(Mary, garden).
go(Sandra, garden).
go(Sandra, kitchen).
go(Mary, kitchen).
go(Mary, bedroom).

Sentences:
John journeyed to the bedroom.
Then he journeyed to the office.
John journeyed to the bedroom.
Afterwards he moved to the bathroom.
John went to the bedroom.
Then he went back to the hallway.
Sandra travelled to the hallway.
After that she moved to the bathroom.
John went to the bathroom.
Afterwards he went to the bedroom.

Semantic Parse:
go(John, bedroom)
go(John office).
go(John, bedroom).
go(John, bathroom).
go(John, bedroom).
go(John, hallway).
go(Sandra, hallway).
go(Sandra, bathroom).
go(John, bathroom).
go(John, bedroom).

Sentences:
    '''

query_prompt_11 = '''Please parse the following questions into query facts. The available keywords are: whereAgent. 
Sentence: Where is Daniel?
Semantic Parse: whereAgent(Daniel).

Sentence: Where is Sandra?
Semantic Parse: whereAgent(Sandra).

Sentence: Where is Mary?
Semantic Parse: whereAgent(Mary).

Sentence: Where is John?
Semantic Parse: whereAgent(John).

Sentence: '''

parse_prompt_11_no_newline ='''Please parse the following sentences into facts. The available keywords are: go.
Sentences: Mary went back to the bathroom. After that she went to the bedroom. Daniel moved to the office. Afterwards he moved to the hallway. John travelled to the bathroom. After that he journeyed to the hallway.
Semantic Parse: go(Mary, bathroom). go(Mary, bedroom). go(Daniel, office). go(Daniel, hallway). go(John, bathroom). go(John, hallway).

Sentences: Sandra went back to the bathroom. Afterwards she travelled to the office.
Semantic Parse: go(Sandra, bathroom). go(Sandra, office)

Sentences: Mary travelled to the bedroom. Then she went back to the bathroom. Mary travelled to the hallway. Following that she went to the garden. Sandra went to the garden. After that she went to the kitchen. Mary journeyed to the kitchen. After that she moved to the bedroom.
Semantic Parse: go(Mary, bedroom). go(Mary, bathroom). go(Mary, hallway). go(Mary, garden). go(Sandra, garden). go(Sandra, kitchen). go(Mary, kitchen). go(Mary, bedroom).

Sentences: '''

query_prompt_11_no_newline = '''Please parse the following questions into query facts. The available keywords are: whereAgent. 
Sentence: Where is Daniel?
Semantic Parse: whereAgent(Daniel).

Sentence: Where is Sandra?
Semantic Parse: whereAgent(Sandra).

Sentence: Where is Mary?
Semantic Parse: whereAgent(Mary).

Sentence: Where is John?
Semantic Parse: whereAgent(John).

Sentence: '''


# =============================================================================
# Task 12
# =============================================================================

parse_prompt_12 = '''Please parse the following statements into facts. The available keywords are: go.
Sentence: Mary and Daniel travelled to the bathroom.
Semantic parse: go(Mary, Daniel, bathroom).

Sentence: John and Daniel travelled to the office.
Semantic parse: go(John, Daniel, office).

Sentence: Sandra and John moved to the garden.
Semantic parse: go(Sandra, John, garden).

Sentence: Sandra and John journeyed to the garden.
Semantic parse: go(Sandra, John, garden).

Sentence: Mary and Daniel went back to the bedroom.
Semantic parse: go(Mary, Daniel, bedroom).

Sentence: '''

query_prompt_12 ='''Please parse the following questions into query facts. The available keywords are: whereAgent.
Sentence: Where is Mary?
Semantic parse: whereAgent(Mary).

Sentence: Where is Daniel?
Semantic parse: whereAgent(Daniel).

Sentence: Where is Sandra?
Semantic parse: whereAgent(Sandra).

Sentence: Where is John?
Semantic parse: whereAgent(John).

Sentence: '''

# =============================================================================
# Task 13
# =============================================================================

parse_prompt_13 = '''Please parse the following statements into facts. The available keywords are: go. 
Sentences:
Mary and Daniel went to the bathroom.
Then they journeyed to the hallway.
Sandra and John moved to the kitchen.
Then they moved to the hallway.

Semantic parse:
go(Mary, Daniel, bathroom).
go(Mary, Daniel, hallway).
go(Sandra, John, kitchen).
go(Sandra, John, hallway).

Sentences:
Daniel and Sandra travelled to the kitchen.
After that they journeyed to the hallway.

Semantic parse:
go(Daniel, Sandra, kitchen).
go(Daniel, Sandra, hallway).

Sentences:
John and Mary moved to the bathroom.
Then they travelled to the office.
John and Mary went to the kitchen.
Afterwards they went to the bedroom.
John and Sandra moved to the bathroom.
Following that they went back to the kitchen.

Semantic parse:
go(John, Mary, bathroom).
go(John, Mary, bathroom).
go(John, Mary, kitchen).
go(John, Mary, bedroom).
go(John, Sandra, bathroom).
go(John, Sandra, kitchen).

Sentences:
John and Mary travelled to the bathroom.
Afterwards they went to the hallway.
Mary and Daniel journeyed to the bathroom.
Then they travelled to the office.
John and Sandra went to the garden.
After that they went back to the bedroom.
John and Sandra moved to the bathroom.
Afterwards they went to the bedroom.

Semantic parse:
go(John, Mary, bathroom).
go(John, Mary, hallway).
go(Mary, Daniel, bathroom).
go(Mary, Daniel, office).
go(John, Sandra, garden).
go(John, Sandra, bedroom).
go(John, Sandra, bathroom).
go(John, Sandra, bedroom).

Sentences:
'''
parse_prompt_13_previous = '''Please parse the following statements into facts. The available keywords are: go. 
Sentences:
Mary and Daniel went to the bathroom.
Then they journeyed to the hallway.
Sandra and John moved to the kitchen.
Then they moved to the hallway.

Semantic parse:
go(Mary, Daniel, bathroom).
go(Mary, Daniel, hallway).
go(Sandra, John, kitchen).
go(Sandra, John, hallway).

Sentences:
Daniel and Sandra travelled to the kitchen.
After that they journeyed to the hallway.

Semantic parse:
go(Daniel, Sandra, kitchen).
go(Daniel, Sandra, hallway).

Sentences:
John and Mary moved to the bathroom.
Then they travelled to the office.
John and Mary went to the kitchen.
Afterwards they went to the bedroom.
John and Sandra moved to the bathroom.
Following that they went back to the kitchen.

Semantic parse:
go(John, Mary, bathroom).
go(John, Mary, bathroom).
go(John, Mary, kitchen).
go(John, Mary, bedroom).
go(John, Sandra, bathroom).
go(John, Sandra, kitchen).

Sentences:
'''
query_prompt_13 = '''Please parse the following questions into query facts. The available keywords are: whereAgent.
Sentence: Where is John?
Semantic parse: whereAgent(John).

Sentence: Where is Sandra?
Semantic parse: whereAgent(Sandra).

Sentence: Where is Mary?
Semantic parse: whereAgent(Mary).

Sentence: '''

# =============================================================================
# Tasks 14
# =============================================================================

parse_prompt_14 = '''Please parse the following statements into facts. The available keywords are: go. Time stamps are as follows: yesterday - 0 , morning - 1, afternoon - 2, evening - 3.  
Sentence: Bill went back to the cinema yesterday.
Semantic parse: go(Bill, cinema, 0).

Sentence: Julie went to the school this morning.
Semantic parse: go(Julie, school, 1).

Sentence: This evening Fred went back to the office.
Semantic parse: go(Fred, office, 3).

Sentence: Yesterday Julie went to the office.
Semantic parse: go(Julie, office, 0).

Sentence: Mary travelled to the bedroom this morning.
Semantic parse: go(Mary, bedroom, 1).

Sentence: This afternoon Fred travelled to the cinema.
Semantic parse: go(Fred, cinema, 2).

Sentence: This evening Julie went to the school.
Semantic parse: go(Julie, school, 3).

Sentence: Bill moved to the kitchen this afternoon.
Semantic parse: go(Bill, kitchen, 2).

Sentence: '''

query_prompt_task_14='''Please parse the following questions into query facts. The available keywords are: before:
Sentence: Where was Julie before the school?
Semantic parse: before(Julie,school).

Sentence: Where was Bill before the school? 
Semantic parse: before(Bill,school).

Sentence: Where was Fred before the kitchen?
Semantic parse: before(Fred,kitchen).

Sentence: Where was Mary before the office?
Semantic parse: before(Mary,office).

Sentence: '''

# =============================================================================
# Task 15
# =============================================================================

parse_prompt_15_old = '''Please parse the following statements into facts. The available keywords are: species_afraid and is.
Sentences:
Mice are afraid of wolves.
Gertrude is a mouse.
Cats are afraid of sheep.
Winona is a mouse.
Sheep are afraid of wolves.
Wolves are afraid of cats.
Emily is a mouse.
Jessica is a wolf.

Semantic parse:
species_afraid(mice,wolves).
is(Gertrude,mouse).
species_afraid(cats,sheep).
is(Winona,mouse).
species_afraid(sheep,wolves).
species_afraid(wolves,cats).
is(Emily,mouse).
is(Jessica,wolf).

Sentences:
Sheep are afraid of mice.
Emily is a sheep.
Mice are afraid of sheep.
Cats are afraid of sheep.
Winona is a sheep.
Jessica is a mouse.
Gertrude is a sheep.
Wolves are afraid of sheep.

Semantic parse:
species_afraid(sheep,mice).
is(Emily,sheep).
species_afraid(mice,sheep).
species_afraid(cats,sheep).
is(Winona,sheep).
is(Jessica,mouse).
is(Gertrude,sheep).
species_afraid(wolves,sheep).

Sentences:
'''
parse_prompt_15 = '''Please parse the following statements into facts. The available keywords are: species_afraid and is.
Sentence: Mice are afraid of wolves.
Semantic parse: species_afraid(mice,wolves).

Sentence: Winona is a mouse.
Semantic parse: is(Winona,mouse).

Sentence: Jessica is a wolf.
Semantic parse: is(Jessica,wolf).

Sentence: Wolves are afraid of cats.
Semantic parse: species_afraid(wolves,cats).

Sentence: Sheep are afraid of wolves.
Semantic parse: species_afraid(sheep,wolves).

Sentence: Emily is a sheep.
Semantic parse: is(Emily,sheep).

Sentence: Wolves are afraid of sheep.
Semantic parse: species_afraid(wolves,sheep).

Sentence: '''

query_prompt_15 = '''Please parse the following questions into query facts. The available keywords are: agent_afraid.
Sentence: What is gertrude afraid of?
Semantic parse: agent_afraid(gertrude).

Sentence: What is jessica afraid of?
Semantic parse: agent_afraid(jessica).

Sentence: What is emily afraid of?
Semantic parse: agent_afraid(emily).

Sentence: What is winona afraid of?
Semantic parse: agent_afraid(winona).

Sentence: '''


# =============================================================================
# Task 16
# =============================================================================

parse_prompt_16 = '''Please parse the following statements into facts. The available keywords are: isAnimal and isColor.
Sentence: Lily is a frog.
Semantic parse: isAnimal(Lily,frog).

Sentence: Bernhard is green.
Semantic parse: isColor(Bernhard,green).

Sentence: Greg is a swan.
Semantic parse: isAnimal(Greg,swan).

Sentence: Julius is a lion.
Semantic parse: isAnimal(Julius,lion).

Sentence: Brian is white.
Semantic parse: isColor(Brian,white).

Sentence: Greg is gray.
Semantic parse: isColor(Greg,gray).

Sentence: '''

query_prompt_16 = '''Please parse the following questions into query facts. The available keywords are: isColor.
Sentence: What color is Greg?
Semantic parse: isColor(Greg).

Sentence: What color is Brian?
Semantic parse: isColor(Brian).

Sentence: What color is Lily?
Semantic parse: isColor(Lily).

Sentence: What color is Julius?
Semantic parse: isColor(Julius).

Sentence: What color is Bernhard?
Semantic parse: isColor(Bernhard).

Sentence: '''



# =============================================================================
# Task 17
# =============================================================================



parse_prompt_17 = '''Please parse the following statements into facts. The available facts are leftOf, rightOf, above, below, and feature.
Sentence: The triangle is above the pink rectangle.
Semantic parse: above(1,2). feature(1,triangle). feature(2,pink). feature(2, rectangle).

Sentence: The blue square is to the left of the triangle.
Semantic parse: leftOf(1,2). feature(1,blue). feature(1,square). feature(2, triangle).

Sentence: The red sphere is to the left of the yellow square.
Semantic parse: leftOf(1,2). feature(1,red). feature(1,sphere). feature(2,yellow). feature(2,square).

Sentence: The red sphere is below the pink rectangle.
Semantic parse: below(1,2). feature(1,red). feature(1,sphere). feature(2,pink). feature(2,rectangle).

Sentence: The blue square is to the right of the triangle.
Semantic parse: rightOf(1,2). feature(1,blue). feature(1,square). feature(2,triangle).

Sentence: The blue square is to the left of the red square.
Semantic parse: leftOf(1,2). feature(1,blue). feature(1,square). feature(2,red). feature(2,square).

Sentence: The yellow square is to the right of the red square.
Semantic parse: rightOf(1,2). feature(1,yellow). feature(1,square). feature(2, red). feature(2, square).

Sentence: The yellow square is above the pink rectangle.
Semantic parse: above(1,2). feature(1,yellow). feature(1,square). feature(2, pink). feature(2, rectangle).

Sentence: '''


query_prompt_17='''Please parse the following questions into facts. The available facts are leftOf, rightOf, above, below, and feature.
Question: Is the pink rectangle to the right of the blue square?
Semantic parse: rightOf(1,2) feature(1,pink). feature(1,rectangle). feature(2,blue). feature(2, square).

Question: Is the blue square below the pink rectangle?
Semantic parse: below(1,2). feature(1, blue). feature(1, square). feature(2, pink). feature(2, rectangle).

Question: Is the red square above the triangle?
Semantic parse: above(1,2). feature(1,red). feature(1,square). feature(2, triangle).

Question: Is the yellow square to the left of the triangle?
Semantic parse: leftOf(1,2). feature(1,yellow). feature(1,square). feature(2,triangle).

Question: '''

all_prompt_17 = '''Please parse the following statements into facts. The available facts corresponding to sentences are leftOf, rightOf, above, below. The available facts corresponding to question facts are leftOf_nondirect, rightOf_nondirect, above_nondirect, below_nondirect.
Sentence 1: The triangle is above the pink rectangle.
Sentence 2: The blue square is to the left of the triangle.
Question: Is the pink rectangle to the right of the blue square?

Sentence 1: above(1,2).
Sentence 2: leftOf(3,1).
Question: rightOf_nondirect(2,3).


Sentence 1: The red sphere is to the left of the yellow square.
Sentence 2: The red sphere is below the pink rectangle.
Question: Is the pink rectangle to the right of the yellow square?

Sentence 1: leftOf(1,2).
Sentence 2: below(1,3).
Question: rightOf_nondirect(3,2).


Sentence 1: The blue square is to the right of the triangle.
Sentence 2: The blue square is to the left of the red square.
Question: Is the red square above the triangle?

Sentence 1: rightOf(1,2).
Sentence 2: leftOf(1,3).
Question: above_nondirect(3,2).


Sentence 1: The red sphere is below the yellow square.
Sentence 2: The red sphere is above the blue square.
Question: Is the blue square below the yellow square?

Sentence 1: below(1,2).
Sentence 2: above(1,3).
Question: below_nondirect(3,2).


Sentence 1: The red square is below the blue square.
Sentence 2: The blue square is below the pink rectangle.
Question: Is the red square to the left of the pink rectangle?

Sentence 1: below(1,2).
Sentence 2: below(2,3).
Question: leftOf_nondirect(1,3).

'''


all_prompt_17_context = '''Please parse the following statements into facts. The available keywords are: obj, leftOf, rightOf, above and below.
Sentence 1: The triangle is above the pink rectangle.
Sentence 2: The blue square is to the left of the triangle.
Objects: obj(1, (triangle)). obj(2, (pink, rectangle)). obj(3, (blue, square)).
Direction Facts: above(1,2). leftOf(3,1).


Sentence 1: The red sphere is to the left of the yellow square.
Sentence 2: The red sphere is below the pink rectangle.
Objects: obj(1, (red, sphere)). obj(2, (yellow, square)). obj(3, (pink, rectangle)).
Direction Facts: leftOf(1,2). below(1,3).


Sentence 1: The blue square is to the right of the triangle.
Sentence 2: The blue square is to the left of the red square.
Objects: obj(1, (blue, square)). obj(2, (triangle)). obj(3, (red, square)).
Direction Facts: rightOf(1,2). leftOf(1,3).


Sentence 1: The red sphere is below the yellow square.
Sentence 2: The red sphere is above the blue square.
Objects: obj(1, (red, sphere)). obj(2, (yellow, square)). obj(3, (blue, square)).
Direction Facts: below(1,2). above(1,3).


Sentence 1: The red square is below the blue square.
Sentence 2: The blue square is below the pink rectangle.
Objects: obj(1, (red, square)). obj(2, (blue, square)). obj(3, (pink, rectangle)).
Direction Facts: below(1,2). below(2,3).


'''


all_prompt_17_query = '''Please parse the following questions into query facts. The available keywords are: leftOf_nondirect, rightOf_nondirect, above_nondirect, below_nondirect.
Objects: obj(1, (triangle)). obj(2, (pink, rectangle)). obj(3, (blue, square)).
Sentence: Is the pink rectangle to the right of the blue square?
Query Fact: rightOf_nondirect(2,3).


Objects: obj(1, (red, sphere)). obj(2, (yellow, square)). obj(3, (pink, rectangle)).
Sentence: Is the pink rectangle to the right of the yellow square?
Query Fact: rightOf_nondirect(3,2).


Objects: obj(1, (blue, square)). obj(2, (triangle)). obj(3, (red, square)).
Sentence: Is the red square above the triangle?
Query Fact: above_nondirect(3,2).


Objects: obj(1, (red, sphere)). obj(2, (yellow, square)). obj(3, (blue, square)).
Sentence: Is the blue square below the yellow square?
Query Fact: below_nondirect(3,2).


Objects: obj(1, (red, square)). obj(2, (blue, square)). obj(3, (pink, rectangle)).
Sentence: Is the red square to the left of the pink rectangle?
Query Fact: leftOf_nondirect(1,3).

'''

# =============================================================================
# Task 18
# =============================================================================

parse_prompt_18 = '''Please parse the following statements into commands. The available keywords are: smaller and bigger.
Sentence: The box of chocolates fits inside the chest.
Semantic parse: smaller(box_of_chocolates,chest).

Sentence: The box is bigger than the chest.
Semantic parse: bigger(box,chest).

Sentence: The chocolate fits inside the chest.
Semantic parse: smaller(chocolate,chest).

Sentence: The chocolate fits inside the container.
Semantic parse: smaller(chocolate,container).

Sentence: '''

query_prompt_18='''Please parse the following questions into query facts. The available keywords are: doesFit and isBigger.
Sentence: Does the suitcase fit in the chocolate?
Semantic parse: doesFit(suitcase,chocolate).

Sentence: Does the chocolate fit in the container?
Semantic parse: doesFit(football).

Sentence: Does the box fit in the chocolate?
Semantic parse: doesFit(box, chocolate).

Sentence: Is the chest bigger than the chocolate?
Semantic parse: isBigger(apple).

Sentence: Is the box of chocolates bigger than the container?
Semantic parse: isBigger(box_of_chocolates, container).

Sentence: '''



# =============================================================================
# Task 19
# =============================================================================
parse_prompt_19 = '''Please parse the following statements into facts. The available keywords are: east, west, north, south.

Sentence: The office is east of the hallway.
Semantic parse: east(office,hallway).

Sentence: The kitchen is north of the office.
Semantic parse: north(kitchen,office).

Sentence: The garden is west of the bedroom.
Semantic parse: west(garden,bedroom).

Sentence: The office is west of the garden.
Semantic parse: west(office,garden).

Sentence: The bathroom is north of the garden.
Semantic parse: north(bathroom,garden).

Sentence: The bedroom is west of the hallway.
Semantic parse: west(bedroom,hallway).

Sentence: The bedroom is west of the hallway.
Semantic parse: east(office,garden).

Sentence: The garden is north of the kitchen.
Semantic parse: north(garden,kitchen).

Sentence: The kitchen is north of the bathroom.
Semantic parse: north(kitchen,bathroom).

Sentence: '''



parse_19_query = '''Please parse the following questions into query facts. The available keywords are: intitial_loc and goal.

Sentence: How do you go from the kitchen to the garden?
Semantic parse: initial_loc(kitchen). goal(garden).

Sentence: How do you go from the hallway to the office?
Semantic parse: initial_loc(hallway). goal(office).

Sentence: How do you go from the bathroom to the hallway?
Semantic parse: initial_loc(bathroom). goal(hallway).

Sentence: How do you go from the garden to the bedroom?
Semantic parse: initial_loc(garden). goal(bedroom).

Sentence: '''

# =============================================================================
# Task 20
# =============================================================================
parse_prompt_20='''Please parse the following statements into facts. The available keywords are: is, pickup, and go.
Sentence: Sumit is tired.
Semantic parse: is(Sumit, tired).

Sentence: Yann picked up the pajamas there.
Semantic parse: pickup(Yann, pajamas).

Sentence: Antoine is thirsty.
Semantic parse: is(Antoine, thirsty).

Sentence: Jason went back to the kitchen.
Semantic parse: go(Jason, kitchen).

Sentence: Yann is hungry.
Semantic parse: is(Yann, hungry).

Sentence: Antoine took the apple there.
Semantic parse: pickup(Antoine, apple).

Sentence: '''

query_prompt_20='''Please parse the following questions into query facts. The available keywords are: query, where, why, go, and get. 
Sentence: Where will Sumit go?
Semantic parse: query(where, Sumit, go)

Sentence: Why did Yann go to the kitchen?
Semantic parse: query(why, Yann, go, kitchen).

Sentence: Why did Yann get the pajamas?
Semantic parse: query(why,Yann, get, pajamas).

Sentence: Why did Sumit get the apple?
Semantic parse: query(why,Sumit, get, apple).

Sentence: '''

# prompts dictionary
prompts = {1: [parse_prompt_1, query_prompt_1], 
           2: [parse_prompt_1,query_prompt_2],
           3: [parse_prompt_1,query_prompt_3],
           4: [parse_prompt_4, query_prompt_4], 
           5: [parse_prompt_5,query_prompt_5], 
           6: [parse_prompt_9,query_prompt_10],
           7: [parse_prompt_7,query_prompt_7],
           8: [parse_prompt_1,query_prompt_8],
           9: [parse_prompt_9,query_prompt_10],
           10: [parse_prompt_10,query_prompt_10],
           11: [parse_prompt_11, query_prompt_11],
           12: [parse_prompt_12,query_prompt_12],
           13: [parse_prompt_13, query_prompt_13],
           14: [parse_prompt_14,query_prompt_task_14],
           15: [parse_prompt_15,query_prompt_15],
           16: [parse_prompt_16,query_prompt_16],
           17: [all_prompt_17_context, all_prompt_17_query],
           18: [parse_prompt_18,query_prompt_18],
           19: [parse_prompt_19, parse_19_query ],
           20: [parse_prompt_20, query_prompt_20]}



if __name__=='__main__':
    from task_config import tasks_dict
    breakpoint()
    for key,pr in prompts.items():
        parse_words = tasks_dict[key]['parse_word']
        for idx,pp in enumerate(pr):
            print('PROMPT ' + str(key))
            print(pp + '[INPUT]'+parse_words[idx])
            breakpoint()

# =============================================================================
# for key,item in prompts.items():
#     if key in [11,13,17]:
#         continue
#     context,query = item
#     assert 'Sentence:' in context
#     print(key,context.count('Sentence'))
#     
# =============================================================================


