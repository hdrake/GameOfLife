from GameOfLife import *

output_frames = False

fname1 = "BlockTest"
fname2 = "Henri-Drake-Skrrrrt"

import sys
ARGS = sys.argv[1:]

pvp = True
if len(ARGS) > 0:
    fname1 = ARGS[0]
    if len(ARGS) == 1:
        game = GameOfLife(10)
        pvp = False
    elif len(ARGS) == 2:
        fname2 = ARGS[1]
        game = GameOfLifePvP(100, 100, 1000)
    else:
        print("Requires either one or two entry filenames as arguments, or zero, in which case it defaults to hard-coded values.")
        sys.exit()
else:
    game = GameOfLifePvP(100, 100, 1000)

# Player vs. Player mode
if pvp:
    try:
        game.read_state_from_file(f"entries/{fname1}", red = True)
        game.read_state_from_file(f"entries/{fname2}", red = False)
    except:
        print(f"Input files {fname1} and/or {fname2} not found.")    
    game.update_display()
    input("Press enter to continue")

    while True:
        for _ in range(3):
            game.evolve()
            if game.red_has_won():
                game.update_display()
                game.display_result("red")
                input("Press enter to continue")
                exit()
            if game.black_has_won():
                game.update_display()
                game.display_result("black")
                input("Press enter to continue")
                exit()
            if game.tiebreaker_needed():
                game.update_display()
                game.display_result("tie")
                input("Press enter to continue")
                break
        game.update_display()
        if output_frames:
            game.save_display()


    game.t = game.T
    while True:
        game.seed_random_cells()
        game.evolve()
        game.update_display()
        if game.red_has_won():
            game.display_result("red")
            input("Press enter to continue")
            exit()
        if game.black_has_won():
            game.display_result("black")
            input("Press enter to continue")
            exit()

# Single-player mode
else:
    try:
        game.read_state_from_file(f"examples/{fname1}")
    except:
        print(f"Input file {fname1} not found.")    
    game.update_display()
    input("Press enter to continue")

    while True:
        game.evolve()
        input("Press enter to continue")
        game.update_display()
        if output_frames:
            game.save_display()