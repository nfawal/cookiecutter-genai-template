# {{cookiecutter.project_name}}

**{{cookiecutter.description}}**

## Overview

Provide a high-level overview of the project, its objectives, and its significance.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Setup](#setup)
3. [Data](#data)
4. [Modeling](#modeling)
5. [Results](#results)
6. [Code](#code)
7. [Contributing](#contributing)
8. [License](#license)

## Project Structure

Explain the structure of your project. Highlight important directories and their purposes.

```
{{cookiecutter.repository_name}}/
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

## Setup

This section provides guidance on setting up your project and enabling GitLab CI/CD functionality.

### Project setup

If you use Cookiecutter, Poetry has been installed during the project building, the virtual environment is available, and the development dependencies are installed. You can use [Poetry](https://python-poetry.org/) as usual.

If you clone the project to contribute, you first need to install Poetry using pip:

```sh
pip install poetry
```

Then you can create the virtual environment and install the development dependencies using:

```sh
poetry install
```

Finally, we strongly recommend setting up Pre-commit to ensure linted and formatted code. You can run:

```sh
poetry run pre-commit install
```

### CI/CD setup

This repository includes a CI/CD pipeline designed to push the documentation (in markdown format) to the project's wiki. The wiki is a separate repository and must be activated along with the CI/CD pipeline to function correctly. Follow these steps to enable and configure it:

1. **Enable Wiki and CI/CD Features:**
   - Navigate to your project in GitLab.
   - Go to **Settings** > **General**.
   - Expand the **Visibility, project features, permissions** section.
   - Enable the toggles for both **CI/CD** and **Wiki**.

2. **Create a Project Access Token (PAT):**
   - Go to **Settings** > **Access Tokens**.
   - Click **Add new token**.
   - Provide a name for the token, such as `CI_WIKI_TOKEN`.
   - Optionally, remove the expiration date to extend it beyond the default 12 months.
   - Select the **Developer** role.
   - Enable the **write_repository** scope to grant read and write access (pull and push) to the repository.
   - Copy the PAT value, as you will need it in the next step.

3. **Configure CI/CD Variables:**
   - Navigate to **Settings** > **CI/CD**.
   - Expand the **Variables** section.
   - Click **Add variable**.
   - Change the **Visibility** to **Masked** for security.
   - Set the **Key** to `CI_WIKI_TOKEN` (this specific name is required by the CI/CD pipeline and cannot be changed).
   - Paste the PAT value into the **Value** field.
   - Optionally, provide a description for the variable.
   - Click **Add variable**.

Your CI/CD pipeline is now fully configured and ready to push documentation to the project's wiki!

## Data

Describe the dataset used in the project. Include information about the source, format, and any data preprocessing steps.

## Modeling

Explain the machine learning models used in the project. Include information about hyperparameters, training process, and any model tuning.

## Results

Present the key findings and results of the project. Include visualizations and any important conclusions drawn.

## Code

This section lists the best practices for coding. We strongly advise you to follow them.

### Coding style

Typing must be used in all modules, classes, methods and functions. Significant improvements to type hinting have been introduced in the latest Python versions. If you are using a Python version earlier than 3.10, consider utilizing the `typing` module to define complex types effectively, as it provides robust support for type annotations in older versions.
- Docstrings must follow the [Google standard](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).
- Use type hints to explicitly specify the argument and return types for your methods and functions, ensuring better readability, maintainability, and tooling support.
- Use a formatter and a linter, such as [Ruff](https://docs.astral.sh/ruff/), to ensure your code is clean and readable.
- Always use absolute imports, and avoid importing any packages in **\_\_init\_\_.py**.
- Always use configuration files, like config.py, YAML configs, or environment variables.
- Use [Poetry](https://python-poetry.org/docs/) to manage dependencies and avoid conflicts you may encounter using pip.
- Use [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) to create SQL templates that can be used within your Python methods.

### Unit tests

- Write simple unit tests with good coverage. Instead of testing every single function, focus on creating relevant tests for the main modules.
- Use the [Pytest](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html) framework to write your tests, and take advantage of fixtures by using a **conftest.py** file at the root of your tests.

### Python versioning

[Pyenv](https://github.com/pyenv/pyenv) offers a straightforward method to manage Python versions, whether at the system or project level.

We suggest following a general rule of using an n-2 or n-1 major version from the most recent release. For instance, if Python 3.13 is the latest release, consider using 3.11 or 3.12. This approach helps mitigate dependency issues, as many Python packages may face compatibility challenges.

To install Pyenv, please refer to the [installation guidelines](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation). For further information, you can also consult this [article](https://realpython.com/intro-to-pyenv/).

### Project management

This repository leverages [Poetry](https://python-poetry.org/) for dependency management and project configuration. Additionally, it integrates [Pre-commit](https://pre-commit.com/) to enforce code quality and consistency through hooks. These hooks utilize tools such as [Ruff](https://docs.astral.sh/ruff/) for linting and [Interrogate](https://interrogate.readthedocs.io/en/latest/#) for ensuring comprehensive docstring coverage.

## Contributing

This section provides guidelines and best practices for contributing to the project, including how to collaborate effectively on GitLab, use continuous integration and development tools.

### Collaborating on GitLab

Working with GitLab involves using Git, making clear commits, managing branches correctly, and using tags effectively. Here are some guidelines:

**Commits:**

Avoid long commits and aim for smaller, easier-to-understand commit messages. Write one commit per changed file, following this template:
```
<type>: <description>
```
Where `<type>` can be one of the following:
- `add`: Adding new files or components
- `feat`: Feature creation
- `fix`: Bug fixing
- `perf`: Performance improvements
- `ci`: Continuous Integration updates
- `refacto`: Code refactoring with no new features or bug fixes
- `docs`: Documentation updates
- `test`: Adding new tests and/or correcting previous ones
- `revert`: Reverting to a previous commit
- `conf`: Configuration updates

For example:
```
docs: adding some best practices elements to README.md
```

**Branches:**

Use `<type>/<name>` for your branches, where `<type>` can be one of the following:
- `feat` or `feature`: New feature
- `fix`: Bug fix
- `docs`: Changes to the documentation
- `style`: Formatting, linting; no production code change
- `refacto`: Refactoring production code

**Tags:**

Use an vX.Y.Z pattern, where X is for major releases, Y is for new features, and Z is for bug fixes. When pushing a new tag, remember to always provide a release with it!

**Merge Requests:**

Ensure you have the right code reviewers when creating your merge request. Use pre-commits and CI to create better PRs.

**Issues:**

Utilize GitLab issues to request changes or share bug reports with the packaging team responsible for modifying the main branch.

### Continuous integration / Continous development

**Pre-commit:**

Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. It helps to ensure that your code meets the required standards before committing. It provides several guardrails such as:
- Preventing the commit of private keys
- Preventing commits on the main branch
- Preventing the commit of large files (more than 50000KB)
- Providing a code formatter and linter through Ruff
- Providing a docstring coverage checker through Interrogate

*Ruff is a fast code linting and formatting tool, written in Rust, set to replace tools like Black, Flake8, and Isort.*
*Interrogate is a checker for missing docstrings in the codebase.*

**GitLab CI/CD:**

GitLab CI/CD is a robust tool for Continuous Integration and Continuous Deployment (CI/CD). For detailed information, refer to the [official documentation](https://docs.gitlab.com/ee/topics/build_your_application.html).

In this project, we leverage CI/CD to automate the deployment of documentation. The pipeline is configured to take the content from the `docs/` folder and push it to the project's wiki repository whenever changes are pushed to the `main` branch. This ensures that the documentation remains up-to-date with minimal manual effort.

## License

{{cookiecutter.license}}