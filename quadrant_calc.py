import math

def get_custom_nether_quadrants(center_x, center_z, radius_blocks):
    """
    Рассчитывает углы активных квадрантов и их пустых зон (margins).
    Размер сектора: 432x432 блоков.
    Ширина маржи: 64 блока.
    Активная зона: 368x368 блоков.
    """
    GRID_SIZE = 432
    MARGIN = 64
    ACTIVE_SIZE = GRID_SIZE - MARGIN  # 368 blocks
    
    # Определение границ области поиска
    min_x = center_x - radius_blocks
    max_x = center_x + radius_blocks
    min_z = center_z - radius_blocks
    max_z = center_z + radius_blocks
    
    # Нахождение индексов секторов сетки
    start_q_x = math.floor(min_x / GRID_SIZE)
    end_q_x = math.floor(max_x / GRID_SIZE)
    start_q_z = math.floor(min_z / GRID_SIZE)
    end_q_z = math.floor(max_z / GRID_SIZE)
    
    print(f"=== Квадранты сетки (Размер: {GRID_SIZE}, Маржа: {MARGIN}) ===")
    print(f"Поиск в радиусе {radius_blocks} блоков от ({center_x}, {center_z})\n")
    
    count = 0
    for q_x in range(start_q_x, end_q_x + 1):
        for q_z in range(start_q_z, end_q_z + 1):
            # Начало текущего сектора сетки
            grid_start_x = q_x * GRID_SIZE
            grid_start_z = q_z * GRID_SIZE
            
            # Границы Активной Зоны (368x368), где спавнятся структуры
            active_x1 = grid_start_x
            active_z1 = grid_start_z
            active_x2 = grid_start_x + ACTIVE_SIZE - 1
            active_z2 = grid_start_z + ACTIVE_SIZE - 1
            # Границы Маржи (последние 64 блока сектора), где спавн невозможен
            # Пример для сектора [0,0]: от 368 до 431 по осям X и Z
            print(f"[{q_x}, {q_z}]".ljust(8), end=" ")
            print(f"({active_x1}, {active_z1})".ljust(14), end =" ")
            print(f"({active_x2}, {active_z2})")
            count += 1
            
    print(f"Всего выведено квадрантов: {count}")

# --- НАСТРОЙКА ПАРАМЕТРОВ ---
current_x = 0        # Ваша координата X
current_z = 0        # Ваша координата Z
search_radius = 1000  # Радиус отображения вокруг вас

# Запуск расчета
get_custom_nether_quadrants(current_x, current_z, search_radius)
