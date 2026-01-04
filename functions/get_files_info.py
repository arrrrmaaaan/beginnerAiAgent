import os

def get_files_info(working_directory, directory="."):
	if directory == ".":
		print("Result for current directory:")
	else:
		print(f'Result for "{directory}" directory')

	try:
		absPath = os.path.abspath(working_directory)
		fullPath = os.path.join(absPath, directory)
		target_dir = os.path.normpath(fullPath)

		if not os.path.isdir(target_dir):
			return (f'	Error: "{directory}" is not a directory')

		valid_target_dir = os.path.commonpath([absPath, target_dir]) == absPath
		if not valid_target_dir:
			return (f'	Error: Cannot list "{directory}" as it is outside the permitted working directory')
		
		files_info = []
		files = os.listdir(target_dir)
		if not files:
			return(f'	Error: No files found in directory: "{directory}"')

		for item in files:
			item_path = os.path.join(target_dir, item)
			size = os.path.getsize(item_path)
			is_dir = os.path.isdir(item_path)

			item_info = (f'	- {item}: file_size={size} bytes, is_dir={is_dir}')
			files_info.append(item_info)
			
		return "\n".join(files_info)
	except Exception as e:
		return f"	Error listing files: {e}"