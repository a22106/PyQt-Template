# PyQt Template

## 사전 준비

0. Python Interpreter 설치 및 vscode Interpreter 설정

    ```bash
    conda create -n ENCLoader python=3.11
    conda activate ENCLoader
    ```

1. 필수 패키지 설치

    ```bash
    pip install -r requirements.txt
    ```

2. 필수 확장 패키지 설치

- Qt for Python

## UI 업데이트

1. UI 수정

- `UI`폴더 안의 `ENCLoader.ui` 파일을 vscode에서 우클릭하면 Edit Qt UI File 메뉴가 나옴
- 해당 메뉴를 선택하면 Qt Designer가 실행됨
- Qt Designer에서 UI를 수정하고 저장하면 자동으로 `ENCLoader_ui.py` 파일이 업데이트 됨
