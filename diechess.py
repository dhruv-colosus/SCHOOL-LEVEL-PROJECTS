import random
pieces=["QUEEN","KING","PAWN","BISHOP","ROOK","KNIGHT"]
while True:
    a=input("<----------------Press Enter------------------------>")
    for a in range(0,3):
        print(random.choice(pieces))
        