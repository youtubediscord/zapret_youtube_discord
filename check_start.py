import os
import sys
from PyQt5.QtWidgets import QMessageBox, QApplication
import ctypes, sys

# Импортируем константы из конфига
from config import BIN_FOLDER, LISTS_FOLDER

def _native_message(title: str, text: str, style=0x00000010):  # MB_ICONERROR
    """
    Показывает нативное окно MessageBox (не требует QApplication)
    style: 0x10 = MB_ICONERROR,  0x30 = MB_ICONWARNING | MB_YESNO
    """
    ctypes.windll.user32.MessageBoxW(0, text, title, style)

def check_if_in_archive():
    """
    Проверяет, находится ли EXE-файл в временной директории,
    что обычно характерно для распаковки из архива.
    """
    try:
        exe_path = os.path.abspath(sys.executable)
        try:
            from log import log
            log(f"Executable path: {exe_path}", level="CHECK_START")
        except ImportError:
            log(f"DEBUG: Executable path: {exe_path}")

        # Получаем пути к системным временным директориям
        system32_path = os.path.abspath(os.path.join(os.environ.get("WINDIR", ""), "System32"))
        temp_env = os.environ.get("TEMP", "")
        tmp_env = os.environ.get("TMP", "")
        temp_dirs = [temp_env, tmp_env, system32_path]
        
        for temp_dir in temp_dirs:
            if temp_dir and exe_path.lower().startswith(os.path.abspath(temp_dir).lower()):
                try:
                    from log import log
                    log(f"EXE запущен из временной директории: {temp_dir}", level="WARNING")
                except ImportError:
                    log(f"WARNING: EXE запущен из временной директории: {temp_dir}")
                return True
        return False
    except Exception as e:
        log(f"DEBUG: Ошибка при проверке расположения EXE: {str(e)}")
        return False

import re
def contains_special_chars(path: str) -> bool:
    """
    True, если путь содержит:
      • пробел
      • (опционально) цифру
      • символ НЕ из списка  A-Z a-z 0-9 _ . : \ /
    """
    if " " in path:
        return True            # пробел — сразу ошибка

    # если хотите запретить цифры — раскомментируйте строку ниже
    # if re.search(r"\d", path):
    #     return True

    # проверяем оставшиеся символы
    #  ^ – отрицание; разрешаем  A-Z a-z 0-9 _ . : \ /
    return bool(re.search(r"[^A-Za-z0-9_\.:\\/]", path))

def check_path_for_special_chars():
    """Проверяет пути программы на наличие специальных символов"""
    current_path = os.path.abspath(os.getcwd())
    exe_path = os.path.abspath(sys.executable)
    
    paths_to_check = [current_path, exe_path, BIN_FOLDER, LISTS_FOLDER]
    
    for path in paths_to_check:
        if contains_special_chars(path):
            error_message = (
                f"Путь содержит специальные символы: {path}\n\n"
                "Программа не может корректно работать в папке со специальными символами (РФ символы (недопустимы символы от А до Я!), пробелы, цифры, точки, скобки, запятые и т.д.).\n"
                "Пожалуйста, переместите программу в папку (или корень диска) без специальных символов в пути (например, по пути C:\\zapret или D:\\zapret) и запустите её снова."
            )
            try:
                from log import log
                log(f"ERROR: Путь содержит специальные символы: {path}", level="ERROR")
            except ImportError:
                log(f"ERROR: Путь содержит специальных символов: {path}")
            return True, error_message
    return False, ""

def check_startup_conditions():
    """
    Выполняет все проверки условий запуска программы
    
    Возвращает:
    - tuple: (success, error_message)
        - success (bool): True если все проверки успешны, False в противном случае
        - error_message (str): текст сообщения об ошибке, если проверка не пройдена
    """
    try:
        # Проверка на запуск из архива
        if check_if_in_archive():
            error_message = (
                "Программа запущена из временной директории.\n\n"
                "Для корректной работы необходимо распаковать архив в постоянную директорию "
                "(например, C:\\zapretgui) и запустить программу оттуда.\n\n"
                "Продолжение работы возможно, но некоторые функции могут работать некорректно."
            )
            return False, error_message
        
        # Проверка на специальные символы в пути
        has_special_chars, error_message = check_path_for_special_chars()
        if has_special_chars:
            return False, error_message
        
        # Все проверки успешны
        return True, ""
    except Exception as e:
        error_message = f"Ошибка при выполнении проверок запуска: {str(e)}"
        try:
            from log import log
            log(error_message, level="ERROR")
        except ImportError:
            log(f"ERROR: {error_message}")
        return False, error_message

# Изменяем функцию для работы с уже созданным QApplication
def display_startup_warnings():
    """
    Выполняет проверки запуска и отображает предупреждения если необходимо
    
    Возвращает:
    - bool: True если запуск можно продолжать, False если запуск следует прервать
    """
    success, message = check_startup_conditions()
    
    if not success:
        # Определяем, является ли ошибка критической
        is_critical = "специальные символы" in message

        app_exists = QApplication.instance() is not None

        if is_critical:
            if app_exists:
                QMessageBox.critical(None, "Критическая ошибка", message)
            else:
                _native_message("Критическая ошибка", message, 0x10)
            return False
        else:
            if app_exists:
                result = QMessageBox.warning(
                    None, "Предупреждение",
                    message + "\n\nПродолжить запуск программы?",
                    QMessageBox.No
                )
                return result == QMessageBox.Yes
            else:
                btn = _native_message("Предупреждение",
                                    message + "\n\nНажмите «Да» для продолжения.",
                                    0x30)  # MB_ICONWARNING | MB_YESNO
                return btn == 6  # IDYES
    return True
