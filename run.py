from pathlib import Path
import shutil
def run():
    dir_path = Path('./源文件')
    orgin_path = Path('./道德经浅解')
    count = len(list(orgin_path.glob('*.m4a')))+1
    for item in dir_path.glob('*.m4a'):
        new_path = Path(f'./道德经浅解/{count}.m4a')
        shutil.copy(item, new_path)
        print(f'复制{item}成功')
        count+=1
        

if __name__ == '__main__':
    run()
