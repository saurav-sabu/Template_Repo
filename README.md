# 🧱 Template Repo

A boilerplate Python project repository designed to kickstart new projects with a standardized structure for components, pipelines, utilities, logging, exception handling, and testing. Ideal for scalable and maintainable development.

## 📁 Project Structure

```
Template Repo/
├── .github/workflows/              # GitHub workflows (CI/CD)
├── src/
│   ├── components/                 # Core modules: data ingestion, transformation, training, evaluation
│   ├── pipeline/                   # Training and prediction pipeline scripts
│   ├── utils/                      # Utility functions
│   ├── logger/                     # Logging logic
│   └── exception/                  # Custom exception handling
├── tests/
│   ├── unit/                       # Unit tests
│   └── integration/               # Integration tests
├── experiments/                   # Jupyter notebooks for experimentation
├── init_setup.sh                  # Shell script to initialize project setup
├── requirements.txt               # Project dependencies
├── requirements_dev.txt           # Development dependencies
├── setup.cfg                      # Configuration for setup.py
├── setup.py                       # Install script
├── pyproject.toml                 # PEP 517/518 build config
├── tox.ini                        # Tox testing config
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/template-repo.git](https://github.com/saurav-sabu/Template_Repo.git)
cd Template_Repo
```

### 2. Initialize the setup

```bash
bash init_setup.sh
```

### 3. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install in editable mode

```bash
pip install -e .
```

## 🧪 Running Tests

```bash
pytest tests/
```

## 📦 Build and Publish (optional)

```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

## 🛠️ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

[APACHE](LICENSE)

---
