import sys
import subprocess
import argparse
import requests
import pip
import platform

def show_gui_libraries():
    """Fetch and display GUI libraries for Python."""
    gui_libraries = [
        "tkinter", "PyQt5", "wxPython", "Kivy", "PySide2", "Flask", "Django"
    ]
    print("List of GUI Libraries available for Python:")
    for lib in gui_libraries:
        print(f"- {lib}")

def show_pypi_info(library):
    """Fetch information about a specific library from PyPI."""
    url = f"https://pypi.org/pypi/{library}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Information for {library}:")
        print(f"Version: {data['info']['version']}")
        print(f"Summary: {data['info']['summary']}")
        print(f"Home Page: {data['info']['home_page']}")
        print(f"Author: {data['info']['author']}")
        print(f"License: {data['info']['license']}")
    else:
        print(f"Library {library} not found on PyPI.")

def install_library(library):
    """Install a library using pip."""
    print(f"Installing {library}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", library])

def uninstall_library(library):
    """Uninstall a library using pip."""
    print(f"Uninstalling {library}...")
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", library])

def show_python_version():
    """Display the Python version."""
    print(f"Python version: {platform.python_version()}")

def list_installed_packages():
    """List all installed Python packages."""
    installed_packages = pip.get_installed_distributions()
    print("Installed Python Packages:")
    for package in installed_packages:
        print(f"- {package.project_name} ({package.version})")

def show_python_path():
    """Display the Python executable path."""
    print(f"Python executable path: {sys.executable}")

def list_available_versions(library):
    """List available versions of a package from PyPI."""
    url = f"https://pypi.org/pypi/{library}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        versions = data['releases'].keys()
        print(f"Available versions for {library}:")
        for version in versions:
            print(f"- {version}")
    else:
        print(f"Library {library} not found on PyPI.")

def check_pip_version():
    """Check the installed pip version."""
    pip_version = subprocess.check_output([sys.executable, "-m", "pip", "--version"])
    print(f"Pip version: {pip_version.decode().strip()}")

def upgrade_library(library):
    """Upgrade a library to the latest version."""
    print(f"Upgrading {library} to the latest version...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", library])

def show_usage():
    """Display the header and usage instructions."""
    print("-------------------------------DEVCRACKS VERSION 1.0-------------------------------")
    print("Devcracks is licensed under GNU GENERAL PUBLIC LICENSE V3 and is open source")
    print("\n--------------------------------------USAGE---------------------------------------------")
    print("Commands:")
    print("-devcracks --gui-libraries      : Show a list of popular GUI libraries for Python")
    print("-devcracks --pypi-info <library> : Show information about a specific library on PyPI")
    print("-devcracks --install <library>   : Install a Python library using pip")
    print("-devcracks --uninstall <library> : Uninstall a Python library using pip")
    print("-devcracks --python-version      : Show the Python version")
    print("-devcracks --list-packages       : List installed Python packages")
    print("-devcracks --python-path         : Show Python executable path")
    print("-devcracks --list-versions <library> : List available versions for a package from PyPI")
    print("-devcracks --pip-version         : Check the installed pip version")
    print("-devcracks --upgrade <library>   : Upgrade a Python library to the latest version")

def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="Devcracks: Advanced Python Developer Tools")
    
    # Define the available arguments
    parser.add_argument('--gui-libraries', action='store_true', help='Show list of GUI libraries for Python')
    parser.add_argument('--pypi-info', type=str, help='Show information about a specific library on PyPI')
    parser.add_argument('--install', type=str, help='Install a Python library using pip')
    parser.add_argument('--uninstall', type=str, help='Uninstall a Python library using pip')
    parser.add_argument('--python-version', action='store_true', help='Show Python version')
    parser.add_argument('--list-packages', action='store_true', help='List installed Python packages')
    parser.add_argument('--python-path', action='store_true', help='Show Python executable path')
    parser.add_argument('--list-versions', type=str, help='List available versions of a package from PyPI')
    parser.add_argument('--pip-version', action='store_true', help='Check the installed pip version')
    parser.add_argument('--upgrade', type=str, help='Upgrade a Python library to the latest version')
    
    # Parse the arguments
    args = parser.parse_args()
    
    if args.gui_libraries:
        show_gui_libraries()
    elif args.pypi_info:
        show_pypi_info(args.pypi_info)
    elif args.install:
        install_library(args.install)
    elif args.uninstall:
        uninstall_library(args.uninstall)
    elif args.python_version:
        show_python_version()
    elif args.list_packages:
        list_installed_packages()
    elif args.python_path:
        show_python_path()
    elif args.list_versions:
        list_available_versions(args.list_versions)
    elif args.pip_version:
        check_pip_version()
    elif args.upgrade:
        upgrade_library(args.upgrade)
    else:
        show_usage()

if __name__ == "__main__":
    main()


