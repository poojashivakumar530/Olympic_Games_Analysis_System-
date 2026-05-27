# 🏅 Olympics Games Analysis System

A menu-driven Python application for analysing and visualising historical Olympics data across countries, using Pandas, NumPy, and Matplotlib.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Requirements](#requirements)
- [Setup & Installation](#setup--installation)
- [How to Run](#how-to-run)
- [Menu Overview](#menu-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)

---

## About the Project

The **Olympics Games Analysis System** is a console-based Python project that allows users to explore Olympic medal data interactively. It supports data visualisation, analysis, file reading, and data manipulation — all through a simple numbered menu system.

---

## Features

### 📊 Data Visualisation (Top 10 Countries)
- Line chart — Countries vs Total Medals
- Line chart — Countries vs Total Times Participated (Summer & Winter)
- Bar chart — Gold, Silver, and Bronze medals
- Pie chart — Distribution of Gold, Silver & Bronze medals
- Grouped bar chart — Summer vs Winter medals

### 🔍 Data Analysis
- View top/bottom N records sorted by total, gold, silver, or bronze medals
- Display DataFrame info and descriptive statistics
- Print specific column data
- Show maximum value per column

### 📁 File Reading
- Read and display the CSV dataset
- Read and display any Excel file by providing its path

### ✏️ Data Manipulation
- Insert or delete rows
- Insert or delete columns
- Rename columns

---

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib

Install dependencies with:

```bash
pip install pandas numpy matplotlib openpyxl
```

---

## Setup & Installation

1. Clone or download this repository.
2. Place your dataset CSV file at the path specified in the code:
   ```
   <paste csv/excel file path here>
   ```
   Or update the file path in the script to match your local setup.
3. Ensure all required libraries are installed (see Requirements above).

---

## How to Run

```bash
python olympics_analysis.py
```

The main menu will appear in the terminal, and you can navigate by entering the corresponding number for each option.

---

## Menu Overview

```
OLYMPICS GAMES ANALYSIS SYSTEM
:::::::::::::::::::::::::::::::
  1 - Data Visualisation
  2 - Data Analysis
  3 - Read CSV/EXCEL file
  4 - Data Manipulation
  5 - Exit
:::::::::::::::::::::::::::::::
```

---

## Dataset

The project uses a CSV file (`<file_name>.csv`) with the following expected columns:

| Column | Description |
|---|---|
| `Country` | Name of the country |
| `TotalMedal` | Total medals won (all-time) |
| `Tgoldmedal` | Total gold medals |
| `Tsilvermedal` | Total silver medals |
| `Tbronzemedal` | Total bronze medals |
| `SummerMedal` | Medals won in Summer Olympics |
| `WinterMedal` | Medals won in Winter Olympics |
| `SummerTimesPart` | Number of times participated in Summer Olympics |
| `WinterTimesPart` | Number of times participated in Winter Olympics |
| `TotalTimesPart` | Total participations (Summer + Winter) |

---

## Project Structure

```
ip_project/
│
├── olympics_analysis.py      # Main Python script
├── <file_name>.csv          # Dataset (not included — add your own)
└── README.md                 # Project documentation
```

---

## Author

Developed as part of an Informatics Practices (IP) project.
