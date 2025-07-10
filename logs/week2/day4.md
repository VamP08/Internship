# 📅 Day 4 — July 11, 2025  
**Week:** 2 – Version Control & Git Workflows

---

## ✅ What I Did Today

- Enabled **branch protection** on `main`:
  - Required at least 1 review before merging  
  - Required status checks (e.g., `pre-commit`, CI)  
  - Disabled force pushes on protected branches

---

## 🧠 What I Learned

- **Branch protection rules** ensure no unreviewed or untested code gets merged into `main`.  
- **GPG-signed commits** add a cryptographic identity to each commit, preventing impersonation.  
- **PR templates** standardize contributions, making it easier for reviewers to understand and approve changes.  
- Enforcing signed commits is possible through GitHub settings, especially for high-security repositories.

---

## ❓ Questions / Blockers

- Is there any best practice around who should be allowed to bypass branch protection in emergency cases?
- Do all teams enforce signed commits in corporate environments?

---

## 🔧 Code/PR Links

- **Branch Protection:** Configured via GitHub UI → Settings → Branches → `main`
- No code or commits pushed today

---

## 🔜 Next Steps

- Try setting up **GPG key** and make a signed commit  
- Add a **PR template** to the `.github/` directory  
- Move to **Week 3**: Unit Testing & TDD
