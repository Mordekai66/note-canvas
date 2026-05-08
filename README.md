<div align="center">

# 📒 Digital Notebook

### *Like a real paper notebook — but digital.*

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-GUI-green?logo=qt&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![License](https://img.shields.io/badge/license-MIT-yellow)

**A lightweight desktop notebook application built with PySide6 for creating editable digital notebook pages.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Use-Cases](#-use-cases) • [Project-Structure](#-project-structure)

</div>

---

# Overview

**Digital Notebook** is a desktop GUI application built with **PySide6** that recreates the feeling of using a real paper notebook — but in a digital form.

The project is designed for people who:
- do not want to write on physical paper
- have messy handwriting
- need fast digital note sharing
- want notebook-style pages that can be exported instantly

Instead of traditional handwriting, users can create structured notebook pages containing:
- editable text
- images
- movable elements
- resizable content

The application combines the familiarity of paper notebooks with the convenience of digital workflow.

---

# Features

| Feature | Description |
|---|---|
| 📝 Editable Text | Add and edit text blocks |
| 🖼️ Image Support | Insert local images |
| 📋 Clipboard Paste | Paste text/images directly |
| 🔄 Resizable Items | Resize text and images visually |
| 🖱️ Drag & Drop | Move items freely inside the page |
| 📤 PNG Export | Save notebook pages as images |
| 📄 PDF Export | Export notebook pages as PDF |
| ⚡ Keyboard Shortcuts | Fast workflow support |
| 🎨 Notebook Layout | Paper-like notebook appearance |

---

# Installation

## Clone Repository

**`Clone my repo`**

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run the application:

```bash
python main.py
```

---

# Use Cases

| Use Case                       | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| 📚 Study Notes                 | Create clean digital study notes instead of writing on paper |
| 🧾 Assignments                 | Prepare notebook-style assignments for online submission     |
| 📨 Digital Sharing             | Export notes quickly as PNG or PDF and send them online      |
| ✍️ Bad Handwriting Alternative | Useful for users with difficult-to-read handwriting          |
| 📄 Paper Replacement           | Replace physical notebooks with digital pages                |
| 🖥️ Documentation              | Create organized visual notes with text and images           |
| 🏫 Student Workflow            | Suitable for school and university note-taking               |
| 💼 Quick Drafting              | Create fast layouts, drafts, or visual notes                 |

---

# Shortcuts

| Shortcut           | Action               |
| ------------------ | -------------------- |
| `Ctrl + T`         | Add Text             |
| `Ctrl + I`         | Add Image            |
| `Ctrl + S`         | Save PNG             |
| `Ctrl + Shift + S` | Save PDF             |
| `Delete`           | Delete Selected Item |
| `Ctrl + V`         | Paste From Clipboard |

---

# Supported Clipboard Content

| Content Type | Supported |
| ------------ | --------- |
| Plain Text   | ✅         |
| Images       | ✅         |

---

# Project Structure

```text
digital-notebook/
│
├── .github/
│   └── workflows
│     └── release.yml
├── notebook/
│   ├── __init__.py
│   ├── items.py
│   ├── resize.py
│   ├── view.py
│   └── window.py
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

# Architecture

| File        | Responsibility                     |
| ----------- | ---------------------------------- |
| `main.py`   | Application entry point            |
| `window.py` | Main window & UI logic             |
| `view.py`   | Graphics view & clipboard behavior |
| `items.py`  | Custom graphics items              |
| `resize.py` | Reusable resize behavior           |

---

# Technologies Used

* Python
* PySide6
* Qt Graphics Framework

---

# Exporting

The notebook page can be exported as:

* PNG Image
* PDF Document

Exports preserve:

* text
* images
* positioning
* notebook layout

---

# Known Limitations

* Single-page export only
* No project save/load system yet
* Resize cursor directions are simplified

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

# License

This project is licensed under the MIT License.

---

# Author

**Abdelrahman Ali**

GitHub: `@Mordekai66`

---

<div align="center">

### Digital Notebook

Built with PySide6 & Qt Graphics Framework

</div>
```
