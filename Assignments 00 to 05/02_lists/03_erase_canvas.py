import tkinter as tk
import time

# Canvas dimensions
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# Cell and eraser sizes
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    mouse_x = canvas.winfo_pointerx()
    mouse_y = canvas.winfo_pointery()
    
    # Calculate where the eraser is
    left_x = mouse_x - canvas.winfo_rootx() - ERASER_SIZE // 2
    top_y = mouse_y - canvas.winfo_rooty() - ERASER_SIZE // 2
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find items that overlap with the eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For each overlapping object, change its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.itemconfig(overlapping_object, fill='white')

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Erase Canvas")
    
    # Create the canvas widget
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Calculate number of rows and columns for the grid
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    # Draw the grid cells
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')

    # Wait for a click to create the eraser
    canvas.bind("<Button-1>", lambda event: create_eraser(event, canvas))  # Wait for click event
    
    root.mainloop()

def create_eraser(event, canvas):
    last_click_x, last_click_y = event.x, event.y
    
    # Create the eraser
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        fill='pink'
    )
    
    # Continuously move the eraser and erase cells in contact with it
    while True:
        mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
        mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()

        # Move the eraser with the mouse
        canvas.coords(eraser, mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2,
                      mouse_x + ERASER_SIZE // 2, mouse_y + ERASER_SIZE // 2)

        # Erase objects in contact with the eraser
        erase_objects(canvas, eraser)

        # Sleep to control the movement speed of the eraser
        time.sleep(0.05)

if __name__ == '__main__':
    main()
