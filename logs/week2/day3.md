# 📅 Day 3 — July 10, 2025  
**Week:** 2 – Version Control & Git Workflows

---

## ✅ What I Did Today

- Learned how to manually trigger and resolve a **Git rebase conflict**.
- Created a new demo file `conflict_demo.py` on both `main` and a `feature` branch with conflicting content.
- Rebased `feature/change-line` onto `main` to simulate a conflict.
- Encountered a Python syntax error due to a null byte caused by improper file creation (`echo`).
- Resolved the issue by editing the file manually and cleaning up its contents.
- Continued the rebase after resolving the conflict.
- Also practiced **cherry-picking** a specific commit from the feature branch into a clean new branch.

---

## 🧠 What I Learned

- **Git rebase conflicts** occur when two branches edit the same line differently — Git inserts conflict markers in the file (`<<<<<<<`, `=======`, `>>>>>>>`).
- You must **manually edit the file** to resolve the conflict and use `git add` + `git rebase --continue` to proceed.
- **Cherry-picking** is useful for grabbing a specific commit from another branch, e.g. hotfixes or isolated features.
- **Null byte errors** in Python are caused by control characters (`\x00`) — best avoided by editing code files directly in a proper editor.

---

## ❓ Questions / Blockers

- Is there a preferred way to organize conflict resolution when multiple files are involved?
- When should I use `rebase` vs `merge` in team workflows?

---

## 🔧 Code/PR Links

- **Branch:** `week2-day3-rebase-conflict`  
  - Rebase conflict creation and resolution
- **Branch:** `week2-day3-cherry-pick`  
  - Cherry-picked specific commit from feature branch
- **PR:** _To be added once raised_

---

## 🔜 Next Steps

- Final Day 4 of Week 2: Learn **branch protection**, **signed commits**, and team collaboration etiquette with PRs
- Prepare for Week 3: Unit testing foundations using `pytest`, fixtures, mocks, and coverage
