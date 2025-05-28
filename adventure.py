# Title and intro
title = input("***** ERUDITE *****\n")
name = input("TELL ME YOUR NAME:\n")
start = input(f"{name}, ARE YOU READY FOR THE ADVENTURE!!! (yes/no)\n")

if start.lower().strip() == "yes":
    print("LET'S GET STARTED!\n")
else:
    print("YOU ARE NOT AT ALL BRAVE |*.*|")
    exit()

# Common exit function
def game_over():
    print("YOU HAVE BEEN LOCKED IN THIS WORLD PERMANENTLY")
    exit()

# ------ ADVENTURE BEGINS ------
print("\n*********************************  INTRODUCTION  *********************************")
input("""You wake up in a circular white room. No windows. No doors.
Only a voice echoes:

"You are trapped inside your own mind. To escape, solve the puzzles within. 
Fail... and remain lost in thought forever.”

You take a deep breath.

Suddenly, three doors appear...\n""")

# STAGE 1
print("\n*************** FIRST STAGE: THE DOOR OF LIES ***************")
stage_one_level = input("""Each door has a sign:
Door A: This door leads to freedom.
Door B: This door leads to death.
Door C: Door A is lying.

The voice whispers:
Only one sign is telling the truth.

🧠 Which door do you choose? (A/B/C):\n""")

if stage_one_level.lower().strip() == "c":
    print("YOU HAVE CHOSEN THE PERFECT ANSWER!!!")
else:
    game_over()

# STAGE 2
print("\n*************** SECOND STAGE: THE WALL OF TRUTH ***************")
stage_two_level = input("""You pass the door and find a mirror with your reflection—but something is off.
Three reflections step out. Each says:

Reflection A: I am the real you.
Reflection B: A is lying.
Reflection C: B is not the real you.

🧠 Which reflection is telling the truth? (A/B/C):\n""")

if stage_two_level.lower().strip() == "b":
    print("YOU ARE REALLY GOOD, KEEP IT UP!!!")
else:
    game_over()

# STAGE 3
print("\n*************** THIRD STAGE: THE TIME LOOP ROOM ***************")
stage_three_level = input("""You walk into a digital room. A screen shows:
The passcode is a 3-digit number. You have one try.

Clue:
426 — One digit correct and well-placed.
183 — One digit correct, wrong place.
325 — Two digits correct, wrong places.
789 — All digits wrong.

🧠 What is the 3-digit code?\n""")

if stage_three_level.strip() == "362":
    print("YOU ARE BRILLIANT!!!")
else:
    game_over()

# STAGE 4
print("\n*************** FOURTH STAGE: THE MAZE OF MEMORY ***************")
stage_four_level = input("""You now enter a room filled with floating photos of your life: childhood, school, friends, mistakes, victories.

A sign says:
“To move forward, you must forget one memory forever.”

Photos glow:
🧸 Your childhood toy.
📝 Your first exam failure.
❤️ A broken relationship.
🎓 Your graduation day.

🧠 Which memory do you give up to continue? (type the exact phrase)\n""")

if stage_four_level.lower().strip() == "your first exam failure":
    print("YOU ARE SHARP!!!")
else:
    game_over()

# STAGE 5
print("\n*************** FINAL STAGE: THE CHOICE OF RETURN ***************")
stage_five_level = input("""A silver figure greets you.

“You’ve solved every puzzle. You may now return to reality…
But if you go back, all of this will fade like a dream.
Stay here, and gain complete control over your inner world.

Choose: Escape or Evolve?

🧠 Do you return home… or rule your own mind forever?\n""")

if stage_five_level.lower().strip() == "escape":
    print("WELCOME HOME!")
else:
    print("GET READY FOR PART-2")
    exit()
