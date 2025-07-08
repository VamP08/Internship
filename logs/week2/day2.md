# 📅 Day 2 — July 9, 2025  
**Week:** 2 – Version Control & Git Workflows

---

## ✅ What I Did Today

- Practiced **interactive rebase** and **commit squashing** to keep Git history clean and linear.
- Created a branch `week2-day2-rebase` and made 3 granular commits to `demo.py`:
  - Added "Line A"
  - Added "Line B"
  - Added "Line C"
- Ran:
  `git rebase -i HEAD~3` to squash all 3 commits into a single commit with a unified message: 
  `feat: extend demo.py with Lines A, B & C`
- While pushing, encountered a GitHub sync warning: branch was behind origin/main.
- Resolved by rebasing my feature branch onto the latest origin/main:
    `git fetch origin`
    `git rebase origin/main`
- Force-pushed the rewritten history using:
    `git push origin week2-day2-rebase`

---

## 🧠 What I Learned
- Rebasing rewrites commit history by moving your branch’s commits to a new base, producing a linear history.
- Squashing is useful for combining multiple smaller or “work-in-progress” commits into one clear, meaningful commit.
- Force pushing is required after rebasing because it rewrites commit hashes, making the local and remote history diverge.
- Rebasing onto `origin/main` before opening a PR ensures your work is built on top of the latest code and helps prevent future merge conflicts.

---

## ❓Questions / Blockers
- Should I always rebase onto `origin/main` before raising a PR?
- When collaborating with others, how can I safely use git rebase without disrupting shared history?

---

## 🔧 Code/PR Links
- **Branch:** `week2-day2-rebase`  
- **PR:** [#9 – Rebase & Squash Demo](https://github.com/VamP08/Internship/pull/9)  
- **Files changed:**
  - `demo.py` → All three changes (Line A, B, C) combined into a single clean commit

---

## 🔜 Next Steps

- Move to **Day 3**: Practice resolving rebase conflicts and using `git cherry-pick` to move commits across branches
- Learn how to extract partial contributions and apply hotfixes with precision

