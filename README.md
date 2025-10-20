# Professional Portfolio Website with Streamlit

A modern, interactive portfolio showcasing professional skills, experience, and projects through an elegant web interface.

## Key Features

- **Professional Presentation**: Clean, responsive design with professional profile and resume
- **Comprehensive Overview**: Detailed sections for skills, experience, education, and projects
- **Interactive Experience**: Dynamic content presentation with GitHub integration
- **Easy Maintenance**: Simple content updates through Python code
- **Portable Deployment**: Ready for deployment on any Streamlit-supported platform

## Technology Stack

### Core Framework
- **Streamlit**: Web application framework for Python

### Data Handling
- **Pandas**: Data manipulation and organization
- **Requests**: API integration for GitHub data

### Media Processing
- **Pillow (PIL)**: Image processing for profile pictures

## Getting Started

### Prerequisites
- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) - Ultra-fast Python package installer and resolver

### Installation

1. **Install uv** (if you haven't already):
   ```bash
   # macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Or via pip
   pip install uv
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/dimipash/Streamlit_portfolio.git
   cd Streamlit_portfolio
   ```

3. **Install dependencies** (fast with uv!):
   ```bash
   uv sync
   ```

4. **Run the application**:
   ```bash
   uv run streamlit run main.py
   ```

5. **Access your portfolio** at `http://localhost:8501`

### Why uv?

- **⚡ Ultra-fast**: 10-100x faster than pip for dependency resolution and installation
- **🔒 Reliable**: Consistent dependency resolution with lock files
- **🎯 Simple**: Drop-in replacement for pip with better defaults
- **📦 Modern**: Built-in virtual environment management

### Alternative Setup (Traditional)

If you prefer using pip:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

## Development

### Adding Dependencies
```bash
# Add a new dependency
uv add package-name

# Add development dependencies
uv add --dev package-name

# Update all dependencies
uv sync --upgrade
```

### Running Commands
```bash
# Run any command in the project environment
uv run python script.py
uv run streamlit run main.py

# Or activate the environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Customization

Replace the following files with your personal content:
- `photo.jpeg`: Profile picture
- `resume.pdf`: Professional resume
- Update content in `main.py` to reflect your personal information

## Deployment

### Streamlit Community Cloud
1. Push your repository to GitHub
2. Connect to [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Deploy directly from your repository

### Other Platforms
The project is compatible with:
- Heroku
- Railway
- Render
- Any platform supporting Python web applications

## Project Structure

```
Streamlit_portfolio/
├── main.py              # Main application entry point
├── components.py        # Reusable UI components
├── config.py           # Configuration settings
├── data.py             # Data management
├── styles.py           # Custom CSS styling
├── analytics.py        # Analytics and tracking
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock            # Locked dependency versions
├── requirements.txt    # Pip compatibility (auto-generated)
├── photo.jpeg         # Profile picture
└── resume.pdf         # Professional resume
```

## License

This project is open-source and available under the MIT License.

---

*Built with ❤️ using Streamlit and uv for blazingly fast setup*
