# E-Commerce Test Automation Framework

##  Overview
Enterprise-level test automation framework for e-commerce application testing using Python, Selenium WebDriver, and Pytest. Features Page Object Model design pattern, data-driven testing, and CI/CD integration with Jenkins.

##  Framework Architecture
```
EcommerceTestFramework/
├── config/          # Configuration and settings
├── pages/           # Page Object Models
├── tests/           # Test cases
├── utils/           # Helper utilities
├── testdata/        # Test data files
└── reports/         # Test execution reports
```

## 🔧 Technologies
- **Python 3.8+**
- **Selenium WebDriver 4.x**
- **Pytest** - Test framework
- **pytest-html** - HTML reporting
- **Page Object Model** - Design pattern
- **Jenkins** - CI/CD integration

## 📋 Features
-  Page Object Model architecture
-  Data-driven testing
-  Configurable environments
-  HTML test reports with screenshots
-  Automatic screenshot on failure
-  CI/CD ready
-  Cross-browser support

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Chrome browser
- Git

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ecommerce-test-automation.git
cd ecommerce-test-automation
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_login.py
```

Run with HTML report:
```bash
pytest --html=reports/test_report.html
```

##  Test Reports
After test execution, reports are available in:
- **HTML Report:** `reports/test_report.html`
- **Screenshots:** `reports/screenshots/`
- **Logs:** `reports/test_execution.log`

## CI/CD Integration
This framework is integrated with Jenkins for continuous testing:
- Automatic test execution on code push
- Email notifications with test results
- Test trend tracking

## 👤 Author
Dipti Gahdge
- LinkedIn: www.linkedin.com/in/dipti-g-16b43219
- Email: dipti_ghadge@yahoo.com


This project is for portfolio demonstration purposes.
