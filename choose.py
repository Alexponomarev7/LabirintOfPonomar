def choose(sq_u, sq_d, sq_l, sq_r):
    if not sq_u and not sq_d and not sq_l and not sq_r:
        return 1
    
    if sq_u and sq_d and sq_l and sq_r:
        return 0
        
    if sq_u and sq_d and not sq_l and sq_r:
        return 3
    
    if not sq_u and sq_d and sq_l and sq_r:
        return 2
    
    if sq_u and not sq_d and sq_l and sq_r:
        return 4
    
    if sq_u and sq_d and sq_l and not sq_r:
        return 5
    
    if not sq_u and not sq_d and sq_l and sq_r:
        return 6
    
    if  sq_u and sq_d and not sq_l and not sq_r:
        return 7
    
    if  not sq_u and sq_d and sq_l and not sq_r:
        return 10
    
    if  not sq_u and sq_d and not sq_l and sq_r:
        return 11
    
    if  sq_u and not sq_d and not sq_l and sq_r:
        return 12
    
    if  sq_u and not sq_d and sq_l and not sq_r:
        return 13
    
    if  not sq_u and not sq_d and sq_l and not sq_r:
        return 14
    
    if  not sq_u and sq_d and not sq_l and not sq_r:
        return 15
    
    if  not sq_u and not sq_d and not sq_l and sq_r:
        return 16
    
    if  sq_u and not sq_d and not sq_l and not sq_r:
        return 17
    
    return 0