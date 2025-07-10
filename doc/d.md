## 1. Branch Protection Rules on GitHub

### What It Is

Branch protection rules are policies you set in a repository’s settings to enforce quality and safety checks on critical branches (e.g., `main`). Once enabled, certain actions (merges, force pushes) are blocked or gated until conditions are met.

### Key Settings & Their Meanings

- **Require pull request reviews before merging**: Ensures at least one reviewer approval before merging.  
- **Require status checks to pass before merging**: Blocks merges until automated tests or linters (GitHub Actions) succeed.  
- **Require signed commits**: Optional; enforces that all commits are GPG-signed.  
- **Include administrators**: Applies rules even to admin users to avoid bypass.  
- **Disable force pushes**: Prevents rewriting history on protected branches.

### Example Configuration

1. Go to **Settings → Branches → Add rule → `main`**  
2. Enable:  
   - Require pull request reviews → Minimum approvals: 1  
   - Require status checks → e.g., `pre-commit`, `pytest` pipelines  
   - Require signed commits → toggled on  
   - Restrict who can push → leave blank or specify a team  
   - Disable force pushes → checked  

### Real‑World Application

In companies like Google and Microsoft, `main` often represents production‑ready code. Branch protection ensures no broken or unreviewed code reaches production. Status checks integrate with CI systems (e.g., Jenkins, GitHub Actions) to run tests, security scans, and deployment previews.

---

## 2. GPG‑Signed Commits

### What It Is

GPG (GNU Privacy Guard) signing attaches a cryptographic signature to each commit, verifying the author’s identity.

### Setup Steps
# 1. Generate a new key (valid for 1 year)
gpg --quick-generate-key "Your Name <you@example.com>" default default 1y

# 2. List your key to get the ID
gpg --list-secret-keys --keyid-format LONG

# 3. Configure Git to use that key
git config --global user.signingkey <YOUR_KEY_ID>
git config --global commit.gpgSign true

# 4. Make a signed commit
git add <file>
git commit -m "feat: add GPG test file" --gpg-sign

### Why It Matters

- Ensures commits come from a **verified source**, which is critical in both open-source and enterprise repositories.
- Helps **prevent impersonation** and unauthorized commits from untrusted contributors.
- Enables **auditability** — every commit can be cryptographically traced to a known developer.
- In some teams, **CI/CD systems reject unsigned commits** to enforce higher trust and security.
- Public profiles like GitHub show a **“Verified” badge** on signed commits, building credibility.

---

## 3. Pull Request (PR) Etiquette & Templates

### Why Use a PR Template

- Standardizes information across all PRs (purpose, steps to test, related issues).
- Encourages good documentation and makes reviewing faster and more consistent.
- Ensures that no key step is missed during development or submission.

### Example `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
# Pull Request Title

## Description
<!-- What does this change do? Why? -->

## Related Issue
<!-- Reference issue number or URL -->

## How to Test
1. Steps to reproduce
2. Commands to run
3. Expected outputs

## Checklist
- [ ] Code follows project style
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All checks pass

### Application in Teams

- Every PR opens with a uniform template, guiding reviewers through required sections.
- Labels (e.g., `bug`, `feature`, `refactor`) can be applied automatically via GitHub Actions or manually.
- The checklist ensures that code is tested, documented, and adheres to the team's standards before merging.
- Helps new contributors follow consistent workflows and reduces onboarding effort.
- Reviewers can focus on logic and design instead of chasing missing information or context.

---