from pathlib import Path
import shutil
def run():
    dir_path = Path('./源文件')
    i = 1
    for item in dir_path.glob('*.m4a'):
        new_path = Path(f'./道德经浅解/{i}.m4a')
        shutil.copy(item, new_path)
        print(f'复制{item}成功')
        i+=1
        

if __name__ == '__main__':
    run()
