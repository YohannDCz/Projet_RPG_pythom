level1 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "o2", "o2", "o2", "o2", "o2", "o2", "o2", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "  ", "e1", "e1", "e1", "e1", "e1", "  ", "l "],
          ["  ", "l ", "  ", "o1", "o1", "o1", "  ", "l ", "  "],
          ["  ", "  ", "l ", "  ", "  ", "  ", "l ", "  ", "  "],
          ["  ", "  ", "  ", "l ", "J ", "l ", "  ", "  ", "  "],
          ["  ", "  ", "  ", "  ", "l ", "  ", "  ", "  ", "  "]]
 
level2 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "e4", "e4", "e4", "e4", "e4", "e4", "e4", "l "],
          ["l ", "  ", "  ", "p2", "p2", "p2", "  ", "  ", "l "],
          ["l ", "  ", "  ", "e3", "e3", "e3", "  ", "  ", "l "],
          ["l ", "o4", "  ", "o4", "  ", "o4", "  ", "o4", "l "],
          ["l ", "  ", "p1", "p1", "p1", "p1", "p1", "  ", "l "],
          ["l ", "  ", "e2", "  ", "e2", "  ", "e2", "  ", "l "],
          ["l ", "  ", "o3", "  ", "o3", "  ", "o3", "  ", "l "]]

level3 = [["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "  ", "P ", "  ", "P ", "  ", "P ", "  ", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "e5", "e5", "e5", "e5", "e5", "e5", "e5", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "],
          ["l ", "p3", "p3", "p3", "p3", "p3", "p3", "p3", "l "],
          ["l ", "  ", "o5", "  ", "o5", "  ", "o5", "  ", "l "],
          ["l ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "l "]]

### J = Joueur
### P = Princesse
### l = limite de jeu
### o = objet
### e = ennemi
### p = potion

def display_grid(grid):
    column_header= [" ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]
    grid.insert(0, column_header)
    for i in range(1,9):
        grid[i].insert(0, chr(64 + i))
    for y in range(len(grid)):
        b = "-----------------------------------------------"
        print(b)
        a = " | ".join(grid[y])
        print(a)

display_grid(level3)
display_grid(level2)
display_grid(level1)