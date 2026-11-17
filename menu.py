

def menu():
    import ballgame
    
    print("""
        1. Show ballgame
        2.make painting turtle
        3. exit the game 
        """)

    user_choise = int(input())

    if user_choise == 1:
        ballgame.ball()
    elif user_choise == 2:
        pass
        # painting()
 
