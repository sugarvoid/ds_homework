from pyray import (
    init_window,
    window_should_close,
    begin_drawing,
    clear_background,
    RAYWHITE,
    gui_button,
    gui_text_box,
    end_drawing,
    ffi,
)

SCREEN_HEIGHT = 450
SCREEN_WIDTH = 800

txt1_buffer = ffi.new("char [100]")
txt1_enable = True

init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "final project")
while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)

    if gui_button((10, 50, 100, 50), "Add"):
        print("add poke guy (push)")
        txt1_enable = True

    gui_text_box(
        (0, SCREEN_HEIGHT - 50 - 50 - 5, SCREEN_WIDTH, 50),
        txt1_buffer,
        100,
        txt1_enable,
    )

    if gui_button((0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50), "remove"):
        print("remove poke guy (pop)")

    end_drawing()
