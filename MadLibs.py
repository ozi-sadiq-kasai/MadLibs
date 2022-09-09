adj = input("Type an adjective: ")
bird = input("Type a bird: ")
room_in_house = input("Type a room in house: ")
verb_past_tense = input("Type a verb past tense: ")
verb = input("Type a verb: ")
relative_name = input("Type a relative's name: ")
noun = input("Type a noun: ")
liquid = input("Type a liquid: ")
part_of_body_plural = input("Type a part of body(plural): ")


MadLibs = f"Woke up to the {adj} smell of {bird} roasting in the {room_in_house} downstairs."\
          f"I {verb_past_tense} downstairs to see if i could help {verb} dinner.\n"\
          f"My mom said,'See if {relative_name} needs a fresh {noun}'.\n"\
          f"So i carried a tray of glasses full of {liquid} into the living room,\n"\
          f"when i got there, i couldn't believe my {part_of_body_plural}."

print(MadLibs)

