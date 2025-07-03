# 📅 Day 1 — July 2, 2025  
**Week:** 1 – Clean Python & Code Quality

---

## ✅ What I Did Today
- Installed and configured `black`, `isort`, and `pre-commit` hooks in the repo  
- Added `.pre-commit-config.yaml` with Black and isort hooks  
- Refactored `src/week1/csv_parser.py` to:
  - Use **type hints** on all functions  
  - Define a `@dataclass Row(name: str, age: int, city: str)`  
  - Replace dictionary rows with `Row` instances  
- Ran `pre-commit run --all-files` to auto‑format the code

---

## 🧠 What I Learned
- **PEP8**: the Python style guide—Black enforces it automatically  
- **black**: an “opinionated” formatter that rewrites code to a uniform style  
- **isort**: organizes imports into standard groups and sorts them alphabetically  
- **Pre‑commit hook**: a Git hook that runs checks/formatters before each commit  
- **Type hints**: improve code readability and help static analysis tools  
- **@dataclass**: auto‑generates init/repr methods for simple data containers

---

## ❓ Questions / Blockers
- When should I prefer `NamedTuple` over `@dataclass`?  
- Is it worth adding `mypy` for static type checking now, or later?  

---

## 🔧 Code/PR Links
- Refactored script: `src/week1/csv_parser.py`  
- Pre‑commit config: `.pre-commit-config.yaml`  
- PR #1: https://github.com/VamP08/Internship/pull/1

---

## 🔜 Next Steps
- Write unit tests for `read_csv()` using `pytest`  
- Create `tests/test_csv_parser.py` and `data/sample.csv`  
- Begin Day 2 assignment  
