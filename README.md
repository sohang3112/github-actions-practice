# github-actions-practice
Practising Github CI/CD Actions

## Steps Followed
- Created test repo on Github, and cloned it: `git clone https://github.com/sohang3112/github-actions-practice.git`
- Added *.gitignore* by copying from [Python gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore).
  Gitignore just tells git to ignore certain files that are not useful (for example, Python creates a folder called *__pycache__* when you install any library. We don't need to commit it, so added it to *.gitignore*)
- Created *lib.py* (module which will be tested).
- **Unit Testing**: Unit Testing means a list of tests (as Python code only!). Whenever any change is made, we can test using `pytest` command. Tests are in *test_lib.py*. Libraries used for testing are `pytest` and `hypothesis`.
- Added required libraries to *requirements.txt*.
- Created Github Action workflow YAML in *.github/workflows/test.yml*

## Resources Used
- [Github Actions Guide](https://github.com/readme/guides/sothebys-github-actions)

