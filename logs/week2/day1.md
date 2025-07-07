# 📅 Day 1 — July 8, 2025  
**Week:** 2 – Version Control & Git Workflows

---

## ✅ What I Did Today

- Learned about **Git internals**: HEAD, index (staging), and object database (commits, blobs, trees)
- Created a new branch `week2-day1-git-internals` from `main`
- Updated `README.md` with Git explanation and commands
- Created a second feature branch `feature/day1-demo`, added a dummy script `demo.py`, and merged it back
- Visualized commit tree using `git log --oneline --graph`
- Submitted and merged PR with all Git history and branching demonstration

---

## 🧠 What I Learned

- **HEAD** is a pointer to the current branch or commit
- The **index** (staging area) is where you collect changes before making a commit
- Git stores files as compressed **blobs**, organizes them in **trees**, and links them with **commits**
- How to create, switch between, and merge branches properly
- How to write clear, atomic commits and create clean history

---

## ❓ Questions / Blockers

- Are merge commits always preferred over rebasing when working on collaborative branches?
- What’s the best way to keep long feature branches in sync with `main` over time?

---

## 🔧 Code/PR Links

- **Branch:** `week2-day1-git-internals`  
- **PR:** [#5 – Git internals & branching demo](https://github.com/VamP08/Internship/pull/5)  
- **Files changed:**
  - `README.md` → Git demo section
  - `demo.py` → Minimal script from feature branch

---

## 🔜 Next Steps

- Move to Day 2: Learn and apply **rebase**, **squash**, and **interactive commit rewriting**
- Prepare for a cleaner collaborative Git workflow

