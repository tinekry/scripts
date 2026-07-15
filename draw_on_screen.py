import tkinter as tk
from PIL import ImageTk, Image
import pyautogui
import keyboard
import time

class ScreenDrawer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.canvas_window = None
        self.is_active = False
        
        self.color = "red"
        self.brush_size = 4
        self.mode = "pen"  # "pen", "eraser", "arrow"
        
        # Переменные для временных объектов
        self.temp_arrow = None
        self.start_x, self.start_y = None, None
        
        print("--- Программа Рисования Запущена ---")
        print("ALT + SHIFT + D -> Начать рисовать")
        print("A -> Стрелка | E -> Перо | Q -> Ластик")
        
        keyboard.add_hotkey('alt+shift+d', self.safe_activate)

    def safe_activate(self):
        self.root.after(0, self.activate)

    def activate(self):
        if self.is_active: return
        self.is_active = True
        
        #time.sleep(0.1)
        
        self.canvas_window = tk.Toplevel(self.root)
        self.canvas_window.attributes("-fullscreen", True)
        self.canvas_window.attributes("-topmost", True)
        self.canvas_window.focus_force()
        
        screenshot = pyautogui.screenshot()
        self.bg_image = ImageTk.PhotoImage(screenshot)
        
        self.canvas = tk.Canvas(self.canvas_window, highlightthickness=0, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw", tags="background")
        
        self.last_x, self.last_y = None, None
        
        # События мыши
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<Button-1>", self.on_mouse_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)
        
        # Клавиши
        self.canvas_window.bind("<Key>", self.handle_keys)
        
        # Информационная панель с биндами
        self.status_bg = self.canvas.create_rectangle(10, 10, 600, 70, fill="#333333", outline="", stipple="gray50")
        self.status_text = self.canvas.create_text(
            20, 30, 
            text="РЕЖИМ: ПЕРО (Красный) | ESC: Скрыть | C: Очистить | E: Ластик | A: Стрелка", 
            anchor="nw", fill="white", font=("Arial", 12, "bold")
        )
        
        # Дополнительная панель биндов
        self.binds_text = self.canvas.create_text(
            20, 55,
            text="Q: Ластик | 1-4: Цвета | ↑↓←→: Стрелки | F: Режим фиксации",
            anchor="nw", fill="lightgray", font=("Arial", 10)
        )

    def handle_keys(self, event):
        key = event.keysym.lower()
        char = event.char.lower()
        
        if key == "escape":
            self.close_canvas()
        elif key == "c" or char == "с":
            self.clear_canvas()
        elif key == "e" or char == "у":
            self.set_mode("pen")
        elif key == "a" or char == "ф":
            self.set_mode("arrow")
        elif key == "q" or char == "й":
            self.set_mode("eraser")
        elif key in ["1", "2", "3", "4"]:
            colors = {"1": "red", "2": "blue", "3": "green", "4": "yellow"}
            self.set_mode(self.mode, colors[key])
        elif key in ["up", "down", "left", "right"]:
            # Обработка стрелок как особый случай
            self.handle_arrow_keys(key)

    def handle_arrow_keys(self, direction):
        # Здесь можно добавить логику для стрелок
        pass

    def set_mode(self, mode, color=None):
        self.mode = mode
        if color: self.color = color
        
        names = {"pen": "ПЕРО", "eraser": "ЛАСТИК", "arrow": "СТРЕЛКА"}
        mode_str = f"{names.get(self.mode, 'ПЕРО')} ({self.color})"
        self.canvas.itemconfig(self.status_text, text=f"РЕЖИМ: {mode_str} | ESC: Скрыть | C: Очистить | E: Ластик | A: Стрелка")
    def on_mouse_press(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.last_x, self.last_y = event.x, event.y
        
        if self.mode == "eraser":
            self.erase(event)
        elif self.mode == "arrow":
            # Создаем начальную невидимую стрелку
            self.temp_arrow = self.canvas.create_line(
                self.start_x, self.start_y, self.start_x, self.start_y,
                width=self.brush_size + 2, fill=self.color,
                arrow=tk.LAST, arrowshape=(16, 20, 8), tags="drawing"
            )

    def on_mouse_drag(self, event):
        if self.mode == "pen":
            if self.last_x and self.last_y:
                self.canvas.create_line(
                    self.last_x, self.last_y, event.x, event.y,
                    width=self.brush_size, fill=self.color,
                    capstyle=tk.ROUND, smooth=tk.TRUE, tags="drawing"
                )
            self.last_x, self.last_y = event.x, event.y
        elif self.mode == "arrow":
            # Обновляем координаты текущей стрелки
            if self.temp_arrow:
                self.canvas.coords(self.temp_arrow, self.start_x, self.start_y, event.x, event.y)
        elif self.mode == "eraser":
            self.erase(event)

    def on_mouse_release(self, event):
        self.temp_arrow = None # Фиксируем стрелку
        self.last_x, self.last_y = None, None

    def erase(self, event):
        r = 25
        items = self.canvas.find_overlapping(event.x-r, event.y-r, event.x+r, event.y+r)
        for item in items:
            if "drawing" in self.canvas.gettags(item):
                self.canvas.delete(item)

    def clear_canvas(self):
        self.canvas.delete("drawing")

    def close_canvas(self):
        if self.canvas_window:
            self.canvas_window.destroy()
            self.canvas_window = None
            self.is_active = False

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScreenDrawer()
    app.run()