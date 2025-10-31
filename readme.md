# 🩺 CareBridge AI

**Your bridge between clinical insight and patient clarity.**  
CareBridge AI is a role-based healthcare interface designed to empower both doctors and patients with intuitive, secure, and emotionally resonant tools. Built with Streamlit, it transforms clinical workflows into human-centered experiences.

---

## 🌟 Features

- **Role-Based Access**: Separate portals for doctors and patients with tailored functionality.
- **Clean, Hospital-Grade UI**: Custom typography, color palette, and layout for professional clarity.
- **Interactive Navigation**: Sidebar with icon-enhanced links and smooth transitions.
- **Modular Design**: Easily extendable architecture for adding new features or roles.
- **Responsive Layout**: Designed to feel intuitive across devices and screen sizes.

---

## 🧑‍⚕️ Doctor Portal

- Session tracking and summaries  
- Voice-to-EHR integration (coming soon)  
- Clinical dashboard components

## 👤 Patient Portal

- Appointment overview  
- Summary access  
- Educational insights (coming soon)

---

## 🚀 Getting Started

### 1. Clone the repo
bash
git clone https://github.com/your-username/carebridge-ai.git
cd carebridge-ai

### 2. Install dependencies
pip install -r requirements.txt


### 3. Run the app
streamlit run main.py

---

## Project Structure

```
├── main.py                  # Entry point with welcome and role selection
│
├── pages/                   # Contains doctor and patient portal pages
│   ├── doctor_portal.py     # Doctor-facing interface
│   └── patient_portal.py    # Patient-facing interface
│
├── styles/                  # Styling and design assets
│   └── theme.css            # Custom color palette & typography
│
├── utils.py                 # Helper functions for data and logic
│
├── data/
│   └── carebridge_mock_data.json   # Mock dataset for testing
│
└── .streamlit/              # Streamlit app configuration
    └── config.toml          # Theme and UI settings

```

## Design Philosophy

CareBridge AI is built to feel trustworthy, professional, and emotionally intelligent. Every design choice — from typography to layout — is made to reduce cognitive load and foster clarity in clinical communication.

---

## Contributing
We welcome thoughtful contributions! Whether you're improving UI, adding features, or refining logic, feel free to fork the repo and submit a pull request.

---

## License
MIT License. See LICENSE for details.

---

Let me know if you want to add badges, screenshots, or a contribution guide. This README already feels like a product someone would trust in a hospital setting.





