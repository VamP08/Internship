# 📅 Day 2 — July 3, 2025  
**Week:** 1 – Clean Python & Code Quality

---

## ✅ What I Did Today
- Installed `pytest` and added it to `requirements.txt`  
- Created `tests/test_csv_parser.py` with three test cases:
  1. Valid CSV parsing returns correct number of `DeliveryRecord` instances  
  2. Empty CSV returns an empty list  
  3. CSV with missing or invalid fields raises a `TypeError`  
- Added `data/sample.csv` and `data/empty.csv` for test fixtures  
- Utilized `tmp_path` fixture in tests for dynamic file creation  
- Ran `pytest tests/` and saw all tests pass

---

## 🧠 What I Learned
- **pytest**: a powerful, simple testing framework that auto-discovers tests  
- **Fixtures** (`tmp_path`): provide temporary directories/files for isolated, self‑contained tests  
- **Assertion style**: plain `assert` statements are preferred over `unittest` methods  
- Importance of testing both **success** and **failure** scenarios  

---

## ❓ Questions / Blockers
- Should I add more edge‑case tests (e.g., non-numeric strings in numeric fields)?  
- Best practices for organizing test fixtures beyond using `data/` and `tmp_path`?

---

## 🔧 Code/PR Links
- Test suite: `tests/test_csv_parser.py`  
- Sample data files: `data/sample.csv`, `data/empty.csv`  
- PR #3: https://github.com/VamP08/Internship/pull/3

---

## 🔜 Next Steps
- Merge current PR and delete feature branch  
- Add `__init__.py` to `src/week1/` and `tests/` for clean imports  
- Draft `docs/CodeReview.md` for Day 3 assignment  
