class Head:
    def __init__(self, eye, ear, nose, mouth):
        self.eye = eye
        self.ear = ear
        self.nose = nose
        self.mouth = mouth

class Hand:
    def __init__(self, finger, thumb):
        self.finger = finger
        self.thumb = thumb

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Feet:
    def __init__(self, toes, heel):
        self.toes = toes
        self.heel = heel

class Leg:
    def __init__(self, knee, foot):
        self.knee = knee
        self.foot = foot

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self, name, age, torso):
        self.name = name
        self.age = age
        self.torso = torso

right_feet = Feet(5, 1)
left_feet = Feet(5, 1)
right_leg = Leg(1, right_feet)
left_leg = Leg(1, left_feet)
right_hand = Hand(4, 1)
left_hand = Hand(4, 1)
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
head = Head(2, 2, 1, 1)
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
person = Human('Kenny', 25, torso)