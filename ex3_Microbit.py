valchoisie = 0
compteur = 0
while True:
    if input.button_is_pressed(Button.B) and compteur < 9:
        compteur += 1
        valchoisie = compteur
        basic.show_number(compteur)
    if input.button_is_pressed(Button.A) and compteur >= 1:
        compteur += -1
        valchoisie = compteur
        basic.show_number(compteur)
    if input.logo_is_pressed():
        print(valchoisie)