# Ecco Web Playwright Test Framework

This repository contains an automated testing framework for the [Ecco](https://ecco.app) content discovery app using **Playwright** and **Pytest**.

## 🔧 Tech Stack

- Python
- Playwright
- Pytest
- Allure (for reporting)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- Playwright & browser binaries

### Setup Instructions

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

Run Tests

pytest --alluredir=reports/
allure serve reports/

🌐 Cross-Browser Support

Tests can run on Chromium, Firefox, and WebKit. Configuration is handled via Pytest parameters.
🧪 Test Structure

    `tests/`: Test cases

    `pages/`: Page Object Models

    `config/`: Credentials and environment configs

    `utils/`: Helper functions and utilities

📄 License

This project is licensed under the MIT License. See LICENSE for details.
