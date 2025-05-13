# Data Science Cookiecutter

**A general template for any data science project**. The template available on the `master` branch utilizes the Poetry project management tool. Once the project is generated, it is highly recommended to thoroughly review the README file for detailed instructions and guidelines.

## Setup

To use this template, you need to have Python and Git installed and available in your PATH. Then, you need to install `cookiecutter`:

```sh
pip install cookiecutter
```

## Use this template

Copy following commands to create your project based on your need:

```sh
cookiecutter https://git.equancy.cloud/equancy/data-intelligence/cookiecutter-data-science-project/
```

This template comes with configured Git hooks. Once you run the command above, Pre-commit will automatically be installed if necessary. Any commit afterward will trigger multiple checks (e.g., ruff, interrogate, etc.) related to your code.

*Note that you can use the SSH protocol instead of HTTPS.*

## Template structure

```
repository_name/
    ├── data/                                       <---------- Directory to store data. It is gitignored!
    │    ├── processed/
    │    │
    │    └── raw/
    │
    ├── docs/                                       <---------- Directory of markdown files that will be used to build docs.
    │
    ├── models/
    │
    ├── notebooks/                                  <---------- Test notebooks, following a naming convention 
    │                                                           (e.g. `1.0-initial-data-exploration`).
    │
    ├── results/
    │
    ├── secrets/                                    <---------- Directory to store secrets. It is gitignored!
    │
    ├── src/                                        <---------- Directory of main source python files.
    │
    ├── tests/                                      <---------- Directory of unit test.
    │
    ├── .env                                        <---------- Environment variables, use `dotenv` to read them into python
    │                                                           files. It is gitignored!
    │
    ├── .gitignore
    │
    ├── .python-version                             <---------- The python version used (and created) by Pyenv.
    │
    ├── .gitlab-ci.yml                              <---------- The GitLab CI/CD definition.
    │
    ├── .pre-commit-config.yaml                     <---------- The Git hooks to use at the pre-commit stage.
    │
    ├── poetry.lock                                 <---------- The locked dependencies of the project.  
    │
    ├── poetry.toml                                 <---------- Configuration file for poetry backend.  
    │
    ├── pyproject.toml                              <---------- The project configuration, it contains the project 
    │                                                           information, dependencies, configuration and the pre-commit
    │                                                           configurations for ruff and interrogate.
    │
    └── README.md 
```

## Git Usage  

To learn more about how Equancy utilizes GitLab, refer to the `Git@Equancy.pdf` file located in the `docs/` folder of this project. For additional details, you can also consult the linked [article](https://medium.com/@adrien.riaux/mastering-git-documentation-and-usage-8057063608c7) for further insights.
