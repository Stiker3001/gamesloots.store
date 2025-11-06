#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для замены старого логотипа на новый во всех HTML файлах проекта
"""
import os
import re
from pathlib import Path

# Старый и новый логотипы
OLD_LOGO = 'w1ym7ZP.png'
NEW_LOGO = 'ddededede.jpg'

def replace_logo_in_file(filepath):
    """Заменяет логотип в одном файле"""
    try:
        # Читаем файл с правильной кодировкой
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Проверяем, есть ли старый логотип
        if OLD_LOGO in content:
            # Заменяем все вхождения
            new_content = content.replace(OLD_LOGO, NEW_LOGO)
            
            # Записываем обратно
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        return False
    except Exception as e:
        print(f"Ошибка при обработке {filepath}: {e}")
        return False

def main():
    """Основная функция"""
    # Получаем список всех HTML файлов
    html_files = []
    for pattern in ['**/*.html', '**/*.htm']:
        html_files.extend(Path('.').glob(pattern))
    
    # Исключаем служебные файлы
    html_files = [f for f in html_files 
                  if 'replace_logo' not in str(f) 
                  and 'webcopy-origin' not in str(f)]
    
    processed = 0
    total = len(html_files)
    
    print(f"Найдено {total} HTML файлов для обработки...")
    print("-" * 50)
    
    # Обрабатываем каждый файл
    for filepath in html_files:
        if replace_logo_in_file(filepath):
            processed += 1
            print(f"✓ Обработан: {filepath}")
    
    print("-" * 50)
    print(f"Заменено логотипов в {processed} файлах из {total}")
    
    # Проверяем результат
    remaining = sum(1 for f in html_files if OLD_LOGO in f.read_text(encoding='utf-8'))
    if remaining == 0:
        print("✓ Все логотипы успешно заменены!")
    else:
        print(f"⚠ Осталось {remaining} файлов со старым логотипом")

if __name__ == '__main__':
    main()
