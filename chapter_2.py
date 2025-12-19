## Attribute shadowing 
class Ghusuri:
    colour = "black"
    food = "poop"
    no_of_leg = 4
    no_of_hand = 0

anita = Ghusuri()
kodi = Ghusuri()
kodi.colour = "black & white"
anita.fav = "gandhia"
anita.no_of_leg = 2 
anita.no_of_hand = 2 

print(f"colour of kodi before deleting: {kodi.colour}")
del kodi.colour
print(f"colour of kodi after deleting: {kodi.colour}")

print(f"fav place of anita before deleting: {anita.fav}")
del anita.fav
print(f"fav place of anita after deleting: {anita.fav}")