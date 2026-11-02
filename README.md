# neural-network-lab

NumPy로 여러 신경망을 직접 구현하는 Python 학습 프로젝트입니다. 각 신경망은 독립된 폴더에서 개발하고 공용 학습 데이터는 프로젝트 루트에서 관리합니다.

현재는 개발 환경과 MLP 작업 폴더를 준비한 상태입니다. 순전파·역전파·학습 코드는 다음 단계에서 작성합니다.

## 폴더 구성

```text
networks/
  mlp/                첫 번째 신경망 작업 폴더
  transformer_origin/ Transformer 작업 폴더
  _template/          새 신경망 폴더를 만들 때 복사할 기본 틀
common/
  paths.py            공용 데이터 경로
학습 데이터/
  raw/                원본 데이터
  processed/          전처리 결과
pyproject.toml        Python 버전 범위와 의존성
uv.lock               설치 버전을 고정한 잠금 파일
.vscode/              실행·디버깅 설정
```

## 환경 구성

Python 3.13과 [uv](https://docs.astral.sh/uv/)를 사용합니다. 외부 라이브러리는 NumPy와 Matplotlib입니다.

```powershell
git clone https://github.com/ParkIsPark/neural-network-lab.git
cd neural-network-lab
uv sync --locked
uv run python -m networks.mlp
```

`uv sync --locked`는 프로젝트의 `.venv`에 잠금 파일에 지정한 패키지를 설치합니다. 전역 Python 환경에 패키지를 추가하지 않습니다. `uv run`을 사용하면 가상환경을 수동으로 활성화할 필요가 없습니다.

환경 확인 예제는 NumPy 행렬 곱과 데이터 폴더 경로를 검사합니다. 결과 행렬은 `[[19, 22], [43, 50]]`입니다.

## 새 신경망 추가

프로젝트 루트에서 기본 틀을 복사합니다. 폴더 이름은 Python 모듈로 사용할 수 있도록 영문 소문자와 밑줄로 작성합니다.

```powershell
Copy-Item -LiteralPath networks/_template -Destination networks/cnn -Recurse
uv run python -m networks.cnn
```

이후 `networks/cnn/` 안에 `model.py`, `train.py` 등을 추가합니다. 실행 진입점인 `__main__.py`를 수정하면 같은 명령으로 실행할 수 있습니다. 신경망별 모델 코드와 학습 코드는 해당 폴더에 두고, 다른 신경망 폴더에 의존하지 않도록 구성합니다.

새 라이브러리가 필요하면 프로젝트 루트에서 `uv add 패키지이름`으로 추가합니다. 변경된 `pyproject.toml`과 `uv.lock`을 함께 커밋합니다.

## 데이터 관리

원본 데이터는 `학습 데이터/raw/`, 전처리 결과는 `학습 데이터/processed/`에 보관합니다. 데이터셋별 하위 폴더를 추가할 수 있습니다.

```python
from common.paths import RAW_DATA_DIR, PROCESSED_DATA_DIR

source = RAW_DATA_DIR / "dataset_name"
destination = PROCESSED_DATA_DIR / "dataset_name"
```

공용 경로는 소스 파일 위치를 기준으로 계산하므로 데이터 폴더의 한글 이름을 각 구현에서 반복해서 입력할 필요가 없습니다.

실제 데이터 파일, 가상환경, Python 캐시, `outputs/`의 실행 결과는 Git에 포함하지 않습니다. 데이터 폴더 구조와 설명용 README는 Git에 보관합니다.

## VS Code

이 저장소 폴더를 열고 권장 확장을 설치합니다. `Ctrl+Shift+B`로 MLP 환경 확인 예제를 실행하고, `F5`로 디버깅할 수 있습니다. 인터프리터는 `.venv/Scripts/python.exe`를 사용합니다.

다른 신경망을 디버깅하려면 `.vscode/launch.json`의 설정을 복사하고 `module`을 `networks.cnn`처럼 변경합니다.
