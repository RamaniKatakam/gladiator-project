# Gladiator Project 🏟️

A comprehensive machine learning project for team data analysis and player management system. This project establishes the foundational architecture for collecting, storing, and analyzing team player data with future ML capabilities.

## 📋 Overview

The Gladiator Project is designed to:
- Manage team player data (name, height, weight, games played)
- Provide a structured MVC architecture for data operations
- Serve as a foundation for machine learning analysis on player performance
- Demonstrate best practices in Python project organization

## 🚀 Features

- **Player Data Management**: Add, store, and retrieve player information
- **Database Integration**: PostgreSQL with secure connection handling
- **MVC Architecture**: Clean separation of concerns
- **Environment Configuration**: Secure credential management with .env
- **Error Handling**: Robust exception handling for database operations
- **Future ML Ready**: Structure prepared for data analysis and ML models

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Database**: PostgreSQL
- **ORM**: psycopg2
- **Environment**: python-dotenv
- **Architecture**: MVC (Model-View-Controller)

## 📁 Project Structure

```
Gladiator_Project/
├── controller/
│   └── TeamDCController.py    # Handles user interactions and business logic
├── model/
│   └── TeamDC.py             # Data models and player entity
├── repository/
│   └── TeamDCRepository.py   # Database operations and queries
├── view/
│   └── TeamDCView.py         # User interface and display logic
├── main.py                   # Application entry point
├── .env                      # Environment variables (not in git)
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL database
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/RamaniKatakam/gladiator-project.git
cd gladiator-project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install psycopg2-binary python-dotenv
```

### 4. Database Setup
1. Create a PostgreSQL database
2. Update `.env` file with your database credentials:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
```

### 5. Run the Application
```bash
python main.py
```

## 💻 Usage

The application will prompt you to enter player information for 5 players:

1. **Player Name**: Enter the player's full name
2. **Height**: Enter height in centimeters (e.g., 180.5)
3. **Weight**: Enter weight in kilograms (e.g., 75.2)
4. **Games Played**: Enter number of games played (integer)

Example interaction:
```
Enter Player Name: John Doe
Enter Player Height(cm): 185.5
Enter Player Weight(kg): 82.3
Enter Games Played: 45
Player saved with ID: 1
```

## 🗄️ Database Schema

```sql
CREATE TABLE team_dc_players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    height DECIMAL(6,2) NOT NULL,
    weight DECIMAL(6,2) NOT NULL,
    games_played INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔮 Future Machine Learning Features

This project is structured to support future ML implementations:

- **Data Analysis**: Player performance metrics and statistics
- **Predictive Modeling**: Game outcome predictions based on player data
- **Clustering**: Player categorization and team optimization
- **Recommendation Systems**: Player development suggestions
- **Data Visualization**: Performance dashboards and insights

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Development Guidelines

- Follow PEP 8 style guidelines
- Use meaningful commit messages
- Add docstrings to functions and classes
- Test database operations thoroughly
- Keep environment variables secure

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Author

**Ramani Katakam**
- GitHub: [@RamaniKatakam](https://github.com/RamaniKatakam)

## 🙏 Acknowledgments

- PostgreSQL for robust database management
- Python community for excellent libraries
- Open source contributors

---

*This project is part of an AI/ML learning journey. Future updates will include machine learning models and advanced analytics.*