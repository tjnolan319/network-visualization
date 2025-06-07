# GitHub Tag Network Visualization

This project visualizes the relationships between tags used across your GitHub repositories. It helps you see how topics, tools, and themes connect across different projects by rendering an interactive network diagram.

## 🔍 What It Does

- Fetches tag metadata from your GitHub repositories (via a script)
- Converts that metadata into a graph structure (`tag_network.json`)
- Displays the graph using a D3-based network diagram
- Live preview available in [Framer](https://timothynolan.framer.website/), embedded with a dynamic data source
- Automatically updates on a schedule using GitHub Actions (optional)

---

## ⚙️ How to Set It Up

### 1. Clone this Repository

```bash
git clone https://github.com/your-username/network-visualization.git
cd network-visualization
```

### 2. Install Requirements

Make sure you have Python 3 installed. Then install any needed packages:

```bash
pip install requests
```

> _Note: If you’re using only local files, you might not need `requests`. We’ll update this as needed._

### 3. Run the Script

To generate or update the `tag_network.json` file:

```bash
python github_tags_to_json.py
```

This script scans your GitHub repositories for tags and outputs a JSON file structured for visualization.

### 4. Open the Visualization

You can open `tag_network.html` in any browser directly:

```bash
start tag_network.html
```

Alternatively, you can serve it locally via Python:

```bash
python -m http.server
```

Then visit `http://localhost:8000` in your browser.

---

## 🔁 Automating Updates (Optional)

This repo supports automation using GitHub Actions.

### What it does:
- Runs daily (or on any schedule you choose)
- Executes the Python script
- Pushes the updated `tag_network.json` back to the repo

We’ll provide the `.github/workflows/update-network.yml` file shortly.

---

## 📦 Files

| File                      | Description                                         |
|---------------------------|-----------------------------------------------------|
| `github_tags_to_json.py`  | Python script that collects tags and builds the network |
| `tag_network.json`        | Auto-generated data file used by the visualizer    |
| `tag_network.html`        | The D3-based interactive visualization             |
| `README.md`               | This file                                          |

---

## ✅ Future Improvements

- Automatically detect all public repositories under your account
- Include tag frequency and connection strength as node and edge weights
- Add filters or search capability to the D3 visualization

---

## 🧠 Notes

- You only need to run the script manually if automation isn’t enabled.
- If you embed this in Framer, it will always load the **latest version** of `tag_network.json` from GitHub via the raw file URL.

---

## 👤 Author

Tim Nolan  
Bentley University — E-Hub

---
