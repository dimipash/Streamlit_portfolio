# Professional Portfolio Website with Streamlit

[![CI](https://github.com/dimipash/Streamlit_portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/dimipash/Streamlit_portfolio/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/dimipash/Streamlit_portfolio/branch/main/graph/badge.svg)](https://codecov.io/gh/dimipash/Streamlit_portfolio)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

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
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run main.py
```

## Docker Deployment

### Quick Start with Docker

The easiest way to run the portfolio is using Docker:

```bash
# Build and run with Docker Compose (Development)
docker-compose up

# Or build and run with Docker Compose (Production)
docker-compose -f docker-compose.prod.yml up -d
```

Access the application at `http://localhost:8501`

### Docker Options

#### Option 1: Docker Compose (Recommended)

**Development Mode** (with live code reload):
```bash
# Start development server
docker-compose up

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

**Production Mode** (optimized):
```bash
# Start production server
docker-compose -f docker-compose.prod.yml up -d

# View logs
docker-compose -f docker-compose.prod.yml logs -f

# Stop containers
docker-compose -f docker-compose.prod.yml down
```

#### Option 2: Plain Docker

```bash
# Build the image
docker build -t streamlit-portfolio .

# Run the container
docker run -p 8501:8501 --env-file .env streamlit-portfolio

# Run in background
docker run -d -p 8501:8501 --env-file .env streamlit-portfolio

# With custom environment variables
docker run -p 8501:8501 \
  -e EMAIL_HOST=smtp.gmail.com \
  -e EMAIL_PORT=587 \
  -e EMAIL_USERNAME=your@email.com \
  -e EMAIL_PASSWORD=yourpassword \
  streamlit-portfolio
```

### Docker Features

- ✅ **Multi-stage build** - Small image size (~150MB)
- ✅ **Non-root user** - Security best practices
- ✅ **Health checks** - Container monitoring
- ✅ **Volume mounts** - Development hot-reload
- ✅ **Environment variables** - Easy configuration
- ✅ **Production-ready** - Resource limits and logging

### Docker Environment Setup

1. **Copy environment template**:
   ```bash
   cp .env.template .env
   ```

2. **Edit .env file** with your credentials:
   ```bash
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USERNAME=your.email@gmail.com
   EMAIL_PASSWORD=your_app_specific_password
   GITHUB_TOKEN=your_github_token_here  # Optional
   ```

3. **Run with Docker**:
   ```bash
   docker-compose up
   ```

### Deployment Platforms

Deploy the Docker container to:
- **AWS ECS/Fargate** - Fully managed containers
- **Google Cloud Run** - Serverless containers
- **Azure Container Instances** - Quick container deployment
- **DigitalOcean App Platform** - Simple container hosting
- **Railway** - One-click container deployment
- **Fly.io** - Global container deployment

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

### Running Tests
```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Run specific test file
uv run pytest tests/test_data.py

# Run tests in watch mode (requires pytest-watch)
uv run ptw
```

### Code Quality
```bash
# Run linter
uv run ruff check .

# Auto-fix linting issues
uv run ruff check --fix .

# Format code
uv run ruff format .

# Check formatting without changes
uv run ruff format --check .
```

### Running Commands
```bash
# Run any command in the project environment
uv run python script.py
uv run streamlit run main.py

# Or activate the environment
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

## Continuous Integration

This project uses GitHub Actions for CI/CD:

- **Automated Testing**: All tests run on every push and pull request
- **Code Quality**: Linting and formatting checks with Ruff
- **Coverage Reports**: Test coverage tracked with Codecov
- **Python 3.13**: Tests run on latest Python version

See [.github/workflows/ci.yml](.github/workflows/ci.yml) for the full CI configuration.

## Customization

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
