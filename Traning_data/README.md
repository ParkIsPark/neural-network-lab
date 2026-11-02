# 공용 데이터 보관

모든 신경망 구현에서 사용하는 학습 데이터를 이 폴더에 보관합니다.

- `raw/`: 내려받은 원본 데이터
- `processed/`: 전처리한 데이터

데이터셋별로 하위 폴더를 만들어 보관할 수 있습니다. 실제 데이터 파일은 Git 추적에서 제외하며, 데이터 설명을 적은 `README.md`는 추적합니다. 사용한 데이터의 출처, 이용 조건, 다운로드 방법을 해당 README에 기록합니다.

Python 코드에서는 다음 경로를 사용합니다.

```python
from common.paths import RAW_DATA_DIR, PROCESSED_DATA_DIR

dataset_path = RAW_DATA_DIR / "dataset_name"
```
