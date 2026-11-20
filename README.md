# CamController

A simple Windows webcam configuration utility built for my personal use.

## Features

- Detect connected camera devices
- Optional live camera preview
- DirectShow properties window

## Requirements

- Windows 10 or Windows 11
- Python 3.12+

## From Executable 

Pre-built executable (.exe) is available in the [Releases](https://github.com/nordenxgt/CamController/releases) section.

1. Download `CamControl.exe`
2. Run `CamControl.exe`
3. Select a camera (Optionally choose the live camera feed)
4. Start configuring

## From source

1. Clone the Repository

```sh
git clone https://github.com/nordenxgt/CamController
cd CamController 
```

2. Install required packages

```sh
pipenv install
pip install pipenv
```

3. Run the app

```
pipenv shell
python app.py
```

4. Build Executable (Optional)

```sh
pipenv install --dev -e .
pyinstaller --onefile --windowed --name CamControl app.py
```

The executable will be available in the dist histrory.

## LICENSE

This project is licensed under the [MIT License](LICENSE).
