import random


class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ChapterScene:

    # Class Attribute
    # species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self):
        self.number_of_paragraphs = random.randint(1,101)


class RandomCharacter:

    # Class Attribute
    #species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self):

        #flip = random.randint(0,1)
        if random.randint(0,1) == 0: self.type = "major"
        else: self.type = "minor"

        if random.randint(0,1) == 0: self.depth = "flat"
        else: self.depth = "round"

        self.extroversion = random.randint(0,10)
        self.neuroticism = random.randint(0, 10)
        self.agreeableness = random.randint(0, 10)
        self.conscientiousness = random.randint(0, 10)
        self.openness = random.randint(0, 10)

        self.interaction_motive = random.randint(0, 10)
        self.achievement_motive = random.randint(0, 10)
        self.influence_motive = random.randint(0, 10)
        self.psychological_consistency_motive = random.randint(0, 10)
        self.self_esteem_motive = random.randint(0, 10)
        self.authenticity_motive = random.randint(0, 10)

        self.anger = random.randint(0, 10)
        self.sadness = random.randint(0, 10)
        self.guilt = random.randint(0, 10)
        self.joy = random.randint(0, 10)

        self.values = random.randint(0, 10)
        self.moral_foundations = random.randint(0, 10)
        self.virtues = random.randint(0, 10)
        self.character_strengths = random.randint(0, 10)

        self.curiousness = random.randint(0, 10)
        self.quick_decisions = random.randint(0, 10)
        self.critically_evaluate_own_beliefs = random.randint(0, 10)
        self.enjoy_thinking = random.randint(0, 10)