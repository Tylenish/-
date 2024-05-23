import tkinter as tk

# Створення головного вікна
root = tk.Tk()
root.title("Калькулятор")

# Створення рядка введення
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
entry.grid(row=0, column=0, columnspan=4)

# Функція для обробки натискання кнопок
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Функція для обчислення результату
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Функція для очищення рядка введення
def clear():
    entry.delete(0, tk.END)

# Створення кнопок
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    action = lambda x=button: button_click(x) if x != '=' else calculate()
    if button == '=':
        action = calculate
    elif button == 'C':
        action = clear
    tk.Button(root, text=button, width=5, height=2, command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Кнопка очищення
tk.Button(root, text='C', width=5, height=2, command=clear).grid(row=row, column=col)

# Запуск головного циклу програми
root.mainloop()
