import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        entries = []
        with os.scandir(target_dir) as it:
            for entry in it:
                try:
                    size = entry.stat().st_size
                    is_dir = entry.is_dir()
                    entries.append(f"- {entry.name}: file_size={size} bytes, is_dir={is_dir}")
                except OSError:
                    continue

        return "\n".join(entries)
    
    except Exception as e:
        return f"Error: {e}"