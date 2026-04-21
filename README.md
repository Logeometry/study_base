# 🎮 게임 개발자를 위한 알고리즘 & 디버깅 학습 로드맵

> 취업/면접 대비 + 실전 게임 개발 역량 강화를 목표로 한다.

---

## 📌 사이트 개요

### 알고리즘 풀이
| 사이트 | 성격 | 링크 |
|---|---|---|
| [Codewars](https://www.codewars.com) | 커뮤니티 기반 Kata 풀이, 감각 훈련 | 입문 추천 |
| [HackerRank](https://www.hackerrank.com) | 기업 채용 테스트 플랫폼, 주제별 정리 | 기초~중급 |
| [LeetCode](https://leetcode.com) | 코딩 인터뷰 특화, FAANG 면접 기반 | 중급~실전 |
| [Codeforces](https://codeforces.com) | 경쟁 프로그래밍(CP), 실시간 대회 | 심화 |

### 디버깅 & 케이스 분석
| 사이트 | 성격 | 링크 |
|---|---|---|
| [Exercism](https://exercism.org) | Fix the Bug 트랙, 멘토 피드백 포함 | GitHub 연동 가능 |
| [CodeAbbey](https://www.codeabbey.com) | 히스토리컬 문제 + 풀이 비교 분석 | GitHub 연동 가능 |
| [Code Review Stack Exchange](https://codereview.stackexchange.com) | 실제 코드 집단 분석, 틈날 때 열람 | 수시 탐방 |
| [GDC Vault](https://gdcvault.com) | 게임 팀 Postmortem, 실제 버그 사례 보고서 | 필독 추천 |

---

## 🗺️ 학습 로드맵

```
Phase 1 — 감각 익히기 (1~2개월)
└ Codewars: 8kyu → 6kyu
  · 문제가 짧고 즉각적인 피드백
  · 부담 없이 언어 감각 훈련

Phase 2 — 자료구조 + 알고리즘 기초 (2~3개월)
└ HackerRank: Problem Solving 트랙 (Easy → Medium)
  · 주제별(배열, 정렬, 해시, 스택 등) 체계적 학습
  └ Exercism: Fix the Bug 트랙 병행
    · 버그 수정 감각 + 멘토 피드백

Phase 3 — 인터뷰형 문제 적응 (3개월~)
└ LeetCode: Easy → Medium (NeetCode 150 커리큘럼 추천)
  · 실전 면접 감각, 커뮤니티 풀이 분석
  └ CodeAbbey 병행
    · 다른 사람 풀이와 비교 분석

Phase 4 — 경쟁 프로그래밍 도전 (심화, 선택)
└ Codeforces: Div.4 → Div.3
  · 시간 압박 + 수학적 사고력 훈련
```

---

## 🎮 게임 개발자 마지노선

### ✅ 필수 (반드시 잡기)
- 자료구조: 배열, 연결리스트, 스택, 큐, 해시맵, 트리
- 정렬 / 이진 탐색
- 재귀 / DFS / BFS ← 맵 탐색, 길찾기 직결
- 동적 프로그래밍 기초 ← 스킬 쿨타임, 상태 관리
- 그리디 기초

### 🎯 게임 특화 추가 권장
- **A\* 알고리즘** ← 게임 AI 길찾기 핵심
- **공간 분할 (쿼드트리 등)** ← 충돌 감지 최적화
- **비트마스킹** ← 상태 플래그, 인벤토리 관리

### ❌ 게임 개발자에겐 과잉
- Codeforces Div.1~2 수준의 수학적 증명형 문제
- 정수론, 고급 그래프 이론 (네트워크 플로우 등)

> 💡 **LeetCode 기준 목표:** Easy 완벽 + Medium 60~70%

---

## 🐛 디버깅 케이스 공부법

의사의 케이스 레포트처럼, 버그도 구조적으로 분석한다.

```
🏥 의사 케이스 레포트        💻 코드 케이스 분석
─────────────────────────────────────────────
환자 증상 제시          →   버그 증상 (어떤 에러인가)
진단 과정              →   원인 추적 (어디서 터졌나)
감별 진단              →   유사 버그 패턴 비교
치료 방법              →   수정 방법
재발 방지              →   테스트 케이스 추가
```

### 실천 방법
- **Exercism / CodeAbbey 풀이** → GitHub에 커밋하며 기록 관리
- **Code Review Stack Exchange** → 틈날 때마다 열람, 흥미로운 케이스 북마크
- **GDC Vault Postmortem** → 게임 팀이 직접 쓴 버그 사례 보고서 정독

---

```

init_study_base.py
README.md
1_codewars/
	easy/
	medium/
2_hackerrank/
	basic/
	data_structures/
3_leetcode/
	easy/
	hard/
	medium/
4_codeforces/
	div2/
	div3/
DebugExrecism/
	BuggyCode/
	codeabbey/
	Debugging.io/
	Fix the Bug/
	references/
logs/
	bug_cases.md
	patterns.md
```

---

## 🔗 참고 링크

- [NeetCode 150](https://neetcode.io) — LeetCode 커리큘럼 추천
- [GDC Vault](https://gdcvault.com/free) — 무료 Postmortem 모음
- [Code Review Stack Exchange](https://codereview.stackexchange.com)
