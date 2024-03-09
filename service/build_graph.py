import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из первого файла
file1 = 'service/results/jarvis_test.txt'  
data1 = np.loadtxt(file1, delimiter=' ', dtype=float)

# Загрузка данных из второго файла
file2 = 'service/results/graham_test.txt' 
data2 = np.loadtxt(file2, delimiter=' ', dtype=float)

# Загрузка данных из первого файла
file3 = 'service/results/quick_test.txt'  
data3 = np.loadtxt(file3, delimiter=' ', dtype=float)

# Загрузка данных из первого файла
file4 = 'service/results/chans_test.txt'  
data4 = np.loadtxt(file4, delimiter=' ', dtype=float)

# Извлечение значений X и Y из данных
x1, y1 = data1[:, 0], data1[:, 1]
x2, y2 = data2[:, 0], data2[:, 1]
x3, y3 = data3[:, 0], data3[:, 1]
x4, y4 = data4[:, 0], data4[:, 1]

# переменные чтобы удобно менять цвет было
main_color = "#343434" # задний фон
second_color = "#EEEEEE" # акцент - текст, риски
plot_font = "Consolas" # шрифт 

# Создаем объект Figure
fig, ax = plt.subplots()

# Отлюкчаем тулбар
# ???

# Меняем цвета фона
ax.set_facecolor(main_color)
fig.set_facecolor(main_color)

# Меняем цвет и толщину осей
ax.spines['bottom'].set_color(second_color) # Цвет нижней границы
ax.spines['bottom'].set_linewidth(1) # выбор тощины границы
ax.spines['left'].set_color(second_color)   
ax.spines['left'].set_linewidth(1)
ax.spines['top'].set_color(main_color)   
ax.spines['top'].set_linewidth(1)
ax.spines['right'].set_color(main_color)
ax.spines['right'].set_linewidth(1)

# меняем цветь обозначения на грфике
ax.tick_params(axis='x', color=second_color, width=1)  # Изменяет цвет рисок и их подписей на оси X
ax.tick_params(axis='y', color=second_color, width=1)

# Изменение цифр у рисок
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_color(second_color) # цвет
    label.set_weight('regular') # вес - толщина шрифта
    label.set_fontsize(9) # размер
    label.set_fontname(plot_font) # шрифт

# Обозначения
ax.set_xlabel('количетсво точек', color=second_color, fontsize=12, fontweight='regular', fontname=plot_font)
ax.set_ylabel('время работы', color=second_color, fontsize=12, fontweight='regular', fontname=plot_font)
ax.set_title('время работы алгоритмов', color=second_color, fontsize=14, fontweight='regular', fontname=plot_font)

# Строим графики и красим под ними

line_colors = [
    '#d125e1', # 0 фиолетовый
    '#28beff', # 1 голубой
    '#23fa6c', # 2 зеленый
    '#f78735', # 3 оранжевый
    '#fa0000', # 4 красный
    '#fff840', # 5 желтый
    '#f525d4', # 6 розовый
    '#1df8c4', # 7 бирюзовый
]

lines = []
lines.append(ax.plot(x1, y1, color=line_colors[1], linewidth=1, label='Джарвис')[0]) # ставим нужный цвет линии
ax.fill_between(x1, y1, color=line_colors[1], alpha=0.1) # закрашиваем под ноими
lines.append(ax.plot(x2, y2, color=line_colors[2], linewidth=1, label='Грэхэм')[0])
ax.fill_between(x2, y2, color=line_colors[2], alpha=0.1)
lines.append(ax.plot(x3, y3, color=line_colors[3], linewidth=1, label='Быстаря оболочка')[0])
ax.fill_between(x3, y3, color=line_colors[3], alpha=0.1)
lines.append(ax.plot(x4, y4, color=line_colors[4], linewidth=1, label='Чан')[0])
ax.fill_between(x4, y4, color=line_colors[4], alpha=0.1)

# Добавляем легенду с настройкой стиля
legend = ax.legend(
        loc='upper left', # Расположение
          
        frameon=True, # Включить рамку
        edgecolor=second_color, # Цвет рамки
        facecolor=main_color, # Цвет фона
        framealpha=1, # Прозрачность фона
          
        shadow=False, # Тень
          
        title='легенда', # Заголовок легенды
        prop={'family': plot_font, 'size': 10}, # Настройки шрифта
        
        borderpad=0.5, # Внутренний отступ рамки
        labelspacing=0.5, # Расстояние между метками
        handlelength=1, # Длина маркеров в легенде
        borderaxespad=1, # Отступ рамки от осей
        handletextpad=0.5) # Расстояние между маркером и текстом

# меняем цвет текста легенды
plt.setp(legend.get_title(), color=second_color) # заголовок
plt.setp(legend.get_texts(), color=second_color) # текст

### обработчик мышки

# Инициализируем аннотацию
annot = ax.annotate("", xy=(0,0), xytext=(-55, 10), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc=main_color, ec=second_color, lw=1),
                    fontname=plot_font, fontsize=9, color=second_color)
annot.set_visible(False)

# Функция для обновления аннотации
def update_annot(ind, line):
    x,y = line.get_data()
    annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    text = f"{line.get_label()}:\nточек: {x[ind['ind'][0]]:.2f}\nвермя: {y[ind['ind'][0]]:.4f} сек."
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)

# Обработчик событий перемещения мыши
def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        for line in lines:
            cont, ind = line.contains(event)
            if cont:
                update_annot(ind, line)
                annot.set_visible(True)
                fig.canvas.draw_idle()
                return
    if vis:
        annot.set_visible(False)
        fig.canvas.draw_idle()

# Подключаем обработчик события
fig.canvas.mpl_connect("motion_notify_event", hover)

# покзать график
plt.show();
