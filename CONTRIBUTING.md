# Contributing

Thanks for your interest in contributing to **api-task-tracker**! This is a small learning/portfolio project, but contributions, bug reports and suggestions are welcome.

## Getting started

1. Fork the repository and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/api-task-tracker.git
   cd api-task-tracker
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1   # Windows
   source .venv/bin/activate    # macOS / Linux
   pip install -r requirements.txt
   ```
3. Run the app locally to verify everything works:
   ```bash
   python src/main.py
   ```

## Making changes

- Create a new branch for your change:
  ```bash
  git checkout -b feature/your-feature-name
  ```
- Keep changes focused — one feature or fix per branch/PR.
- Follow the existing code style (PEP 8, type hints on function signatures).
- Manually verify your change against the running API (e.g. via `/docs` or `curl`) before opening a PR.

## Submitting a pull request

1. Push your branch to your fork.
2. Open a pull request describing:
   - What the change does and why
   - How you tested it
3. Be ready to discuss feedback — this project is a learning exercise, so reviews are meant to be constructive.

## Reporting issues

If you find a bug or have a suggestion, please open an issue including:

- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Environment details (OS, Python version)

## Code of conduct

Be respectful and constructive. This project is maintained on a best-effort basis.
