# Code Review Guide

This document outlines best practices for conducting and participating in code reviews, ensuring high quality, maintainability, and collaboration.

---

## 1. What Is a Code Review?
A **code review** is a systematic examination of source code by one or more developers (reviewers) other than the author. It aims to:
- Catch bugs early  
- Improve code clarity and maintainability  
- Share knowledge among team members  
- Enforce project standards  

---

## 2. When to Open a Pull Request (PR)
Open a PR when you have:
1. Completed a discrete unit of work (feature, bug fix, refactor)  
2. Written or updated tests covering your changes  
3. Formatted code according to style guidelines (e.g., PEP8)  
4. Updated documentation if the behavior or API changed  

---

## 3. Code Review Checklist
Use this checklist when reviewing someone else’s PR:

| Area             | What to Check                                                                 |
|------------------|-------------------------------------------------------------------------------|
| **Style & Format**  | ✅ Follows PEP8 / project style guide<br>✅ No trailing whitespace or long lines |
| **Correctness**     | ✅ Logic is sound and handles edge cases<br>✅ No silent failures or data loss    |
| **Tests**           | ✅ New/changed code is covered by unit/integration tests<br>✅ Tests pass reliably |
| **Documentation**   | ✅ Public functions/classes have docstrings<br>✅ README or docs updated as needed |
| **Naming**          | ✅ Variable, function, and class names are descriptive and consistent         |
| **Security**        | ✅ No secrets (API keys, passwords) in code<br>✅ Input is validated/sanitized  |
| **Performance**     | ✅ No obvious inefficiencies<br>✅ Large loops or I/O operations are optimized |

---

## 4. “LGTM” and Approvals
- **LGTM** (“Looks Good To Me”) is an informal sign‑off by a reviewer indicating comfort with merging.
- Aim for **at least 1–2 approvals** on non-trivial PRs.
- Reviewers can also leave **“Request Changes”** if issues are found.

---

## 5. Merge Strategies
Choose the right merge method based on project needs:

| Strategy           | Description                                                           | When to Use                                      |
|--------------------|-----------------------------------------------------------------------|--------------------------------------------------|
| **Merge Commit**     | Creates a merge commit, preserving full branch history               | When you want a record of feature branches       |
| **Squash & Merge**   | Combines all commits in the PR into a single commit                  | To keep `main` history linear and clean          |
| **Rebase & Merge**   | Reapplies each commit onto `main`, preserving individual commits     | When you want linear history but keep granular commits |

---

## 6. Branch Protection Rules
Enforce quality by requiring:
- Pull requests before merging  
- Minimum number of reviewer approvals (e.g., 1 or 2)  
- Passing status checks (linting, tests)  
- No force pushes to protected branches  

---

## 7. Tips for Effective Reviews
- **Be respectful & constructive**: focus on code, not the author.  
- **Keep comments clear**: reference lines or code snippets.  
- **Ask questions**: “Can you explain why…?”  
- **Praise good work**: highlight well‑written code or tests.  
- **Limit scope**: review ~200–400 lines at a time to stay focused.  

---

> **Remember:** A strong code review culture leads to better code quality, faster onboarding, and a more collaborative team. Happy reviewing!  
