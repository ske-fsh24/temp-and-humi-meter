def on_button_pressed_a():
    I2C_LCD1602.lcd_init(0)
    I2C_LCD1602.backlight_on()
    I2C_LCD1602.show_string("welcome", 0, 0)
    I2C_LCD1602.show_string("access grounded", 0, 1)
    basic.pause(5000)
    I2C_LCD1602.clear()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    I2C_LCD1602.lcd_init(0)
    I2C_LCD1602.backlight_on()
    I2C_LCD1602.show_string("error 404", 0, 0)
    I2C_LCD1602.show_string("..........", 0, 1)
    basic.pause(5000)
    basic.pause(5000)
    I2C_LCD1602.clear()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    I2C_LCD1602.lcd_init(0)
    I2C_LCD1602.backlight_on()
    I2C_LCD1602.show_string("sorry", 0, 0)
    I2C_LCD1602.show_string("access denied", 0, 1)
    basic.pause(5000)
    I2C_LCD1602.clear()
input.on_button_pressed(Button.B, on_button_pressed_b)

I2C_LCD1602.lcd_init(0)
I2C_LCD1602.backlight_on()
I2C_LCD1602.show_string("loading...", 0, 0)
basic.pause(5000)
I2C_LCD1602.clear()