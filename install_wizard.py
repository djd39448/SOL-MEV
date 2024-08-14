
import os

def check_python():
    try:
        import sys
        print('Python is installed')
    except ImportError:
        print('Python is not installed')

def install_packages():
    os.system('pip install -r requirements.txt')

if __name__ == '__main__':
    check_python()
    install_packages()
