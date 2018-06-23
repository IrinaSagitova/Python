import os
import subprocess
 
def all_list():
    source_dir = 'Source'    
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), source_dir))
    files_list = os.listdir(path=".")
    return files_list
 
def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
 
def main(files_list): 
    print('Идет обработка...')
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Source')
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Result')
    ensure_dir(result_dir)
    for i in files_list:
        input_path = os.path.join(source_dir, i)
        output_path = os.path.join(result_dir, i)
        command = 'convert ' + input_path + ' -resize 200 ' + output_path
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        subprocess.run(command)
    print('Готово')
 
main(all_list())