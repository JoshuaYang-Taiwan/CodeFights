def bishopAndPawn(bishop, pawn):
    bishop = position(bishop)
    pawn = position(pawn)
    return bishop,pawn
    return bishop[1]-bishop[0]==pawn[1]-pawn[0] or sum(bishop)==sum(pawn)
def position(l):
    return [ord(l[0]),int(l[1])]