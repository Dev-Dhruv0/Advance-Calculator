# Advance-Calculator 🧮 *(In Development)*

A feature-rich, modern Python calculator app with a sleek GUI powered by `customtkinter`. Supports both basic and advanced mathematical operations using Python's powerful built-in libraries like `ast` and `operator`.

## 🚧 Status

> **Note:** This project is currently under active development. Features are being added and refined. Contributions and feedback are welcome!

## ✨ Features

* ➕ Basic Arithmetic (Add, Subtract, Multiply, Divide)
* 🧠 Advanced Math (Exponentiation, Roots, Trigonometry)
* 🎛️ CustomTkinter GUI Interface
* 🧮 Expression Parsing using `ast`
* ⚙️ Evaluation via `operator` module
* 🔁 Expression History *(Coming Soon)*
* 📐 Unit Conversion *(Planned)*
* 🧩 Modular & Extendable Design

## 🛠️ Built With

* Python 3.10+
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – modern GUI framework for Python
* `math` – for trigonometry, logs, roots, etc.
* `ast` – for safe expression parsing
* `operator` – for dynamic and clean operation handling
* `decimal` – for high-precision calculations *(optional)*

## 🚀 Getting Started

1. Clone the repository

```bash
git clone https://github.com/YourUsername/Advance-Calculator.git
```

2. Navigate to the project folder

```bash
cd Advance-Calculator
```

3. Install dependencies

```bash
pip install customtkinter
```

4. Run the calculator

```bash
python calculator.py
```

## 💡 Key Features

### Expression Evaluation

* Supports full math expressions (e.g., `2 + 3 * (4 - 1)`)
* Safe parsing using `ast` (Abstract Syntax Tree)
* Clean evaluation using `operator` functions

### GUI Experience

* Built with `customtkinter` for a modern feel
* Dark mode by default
* Responsive layout for different screen sizes
* Button-driven interface with visual feedback

### Math Features

* Basic: `+`, `-`, `*`, `/`
* Advanced: `**`, `sqrt()`, `log()`, `sin()`, `cos()`, etc.
* Support for parentheses, decimal points, and more

### In Development

* 📝 Calculation History Panel
* 🧮 Unit Conversion Tool
* 💾 Save/Load expressions
* 🎨 Theme Customization Options

## 📱 GUI Preview *(Coming Soon)*

> Screenshots and design previews will be added once core features are stable.

## 🔧 Code Structure (Planned)

```bash
Advance-Calculator/
│
├── calculator.py          # Main app entry point
├── gui.py                 # CustomTkinter GUI logic
├── core/
│   ├── parser.py          # AST parsing and validation
│   ├── operations.py      # Operator-based calculations
│   └── utils.py           # Helper functions
└── README.md
```

## 📌 Future Enhancements

* Scientific calculator mode toggle
* Keyboard input support
* Theme switcher (Light/Dark)
* Portable `.exe` version using PyInstaller

## 📝 License

This project is licensed under the MIT License.

---

Made with 🐍 + 💻 by \ Dhruv
Stay tuned for updates and enhancements! 🚀

---
