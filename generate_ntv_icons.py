import cv2
import numpy as np
import os

# Configuration
input_image_path = 'нтв-рус.png' 
output_folder = 'icons' # Название папки, как вы и указали
shift_range = range(-1, 10)
qual_labels = ['sd', 'hd']

# 1. Получаем путь к директории, где лежит исходный файл
base_dir = os.path.dirname(os.path.abspath(input_image_path))
# 2. Соединяем путь исходника с вашей переменной output_folder
full_output_path = os.path.join(base_dir, output_folder)

# Создаем папку, если её нет
if not os.path.exists(full_output_path):
    os.makedirs(full_output_path)

# Читаем изображение
original_image = cv2.imread(input_image_path)

if original_image is not None:
    for quality in qual_labels:
        for shift in shift_range:
            image_copy = original_image.copy()
            text_label = f'{quality}_{shift}'

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image_copy, text_label, (10, 50), font, 1, (255, 255, 255), 2)

            # Сохраняем в full_output_path
            output_filename = f'ntv_{quality}_{shift}.png'
            final_path = os.path.join(full_output_path, output_filename)
            
            cv2.imwrite(final_path, image_copy)
    print(f"Готово! Файлы сохранены в: {full_output_path}")
else:
    print("Ошибка: Исходный файл не найден.")
