def on_button_pressed_a():
    basic.clear_screen()
    for index in range(5):
        for index2 in range(5):
            if index == index2:
                led.plot(index, index2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    for index3 in range(5):
        for index4 in range(5):
            if index3 + index4 == 4:
                led.plot(index3, index4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    for index5 in range(5):
            for index6 in range(5):
                if index5 + index6 == 4 or index5 == index6:
                    led.plot(index5, index6)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)