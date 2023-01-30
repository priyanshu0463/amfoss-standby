def isValidChessBoard(cb):
    pcs={'pawn':8,'knight':2,'bishop':2,'rook':2,'queen':1,'king':1}
    
    if list(cb.values()).count("wking")!=1 or list(cb.values()).count("bking")!=1:
        return False  #this part i checked from net
    for i in cb.values():
        if list(cb.values()).count(i) > pcs[i[1:]]:
            return False
        
    
   

cb={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
if isValidChessBoard(cb):
    print("valid")
else:
    print("invalid")

