# IcanDoIt

노인분들을 위한 **아이폰 초간단 사용법 웹 가이드** 예제입니다.

## 빠른 실행 방법 (PyCharm/터미널 공통)

1. 가상환경 생성 및 활성화

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

2. 패키지 설치

```bash
pip install -r requirements.txt
```

3. 서버 실행

```bash
uvicorn app.main:app --reload
```

4. 브라우저에서 확인

- http://127.0.0.1:8000

## 현재 포함된 메뉴

- 문자 메시지 보내기 (아이폰 기준)

왼쪽 메뉴(기능 목록) + 오른쪽 가이드(단계별 설명) 형태의 2단 레이아웃으로 구성되어 있습니다.
