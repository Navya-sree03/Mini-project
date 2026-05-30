# 🎬 OTT Login System — Python

A console-based OTT (Over-The-Top) platform simulation built with pure Python.
Inspired by how apps like Netflix and Hotstar handle login and content menus.

---

## 📌 Features

- Login system with **3 attempts** before account lockout
- Subscription-based access control
- Watch **Movies** and **Series**
- **Search** content by name
- Clean logout

---

## 🚀 How to Run

1. Make sure Python is installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ott-login-python.git
   ```
3. Navigate to the folder:
   ```bash
   cd ott-login-python
   ```
4. Run the program:
   ```bash
   python ott_login.py
   ```

---

## 💻 Demo

```
------- LOGIN -------
Enter the Username: john
Enter the Password: ••••••
Invalid Credentials
Attempts Left: 2

Enter the Username: john
Enter the Password: ••••••••
Login Successful!

------ OTT PLATFORM ------
1. View Subscription
2. Watch Movies
3. Watch Series
4. Search Content
5. Logout
```

---

## 🧠 Concepts Used

| Concept | Usage |
|---|---|
| `while` loop | Login attempts, main menu |
| `if/elif/else` | Menu choices, content selection |
| `break` | Logout, successful login |
| Boolean flag | Subscription check |
| `.strip()` / `.lower()` | Cleaning user input |
| `input()` | All user interactions |

---

## 📁 Project Structure

```
ott-login-python/
│
└── ott_login.py      # Main program file
└── README.md         # Project documentation
```

---

## 🔮 Future Improvements

- [ ] Store multiple users in a JSON file
- [ ] Hash passwords using `hashlib`
- [ ] Add more movies and series
- [ ] Build a GUI with `tkinter`

---

## 👨‍💻 Author

Made with ❤️ as a beginner Python project.

Feel free to fork and improve it!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
