# 🔐 Gem Pass Generator

A secure, beautiful CLI password generator with customizable options for developers and security professionals.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-alpha-yellow.svg)

## ✨ Features

- 🔒 **Cryptographically Secure** - Uses Python's `secrets` module for true randomness
- 🎨 **Beautiful CLI** - Rich formatting with colors, tables, and panels
- ⚙️ **Highly Customizable** - Control length, symbols, separators, and more
- 📊 **Entropy Display** - Shows password strength in bits
- 📋 **Clipboard Support** - Optional auto-copy to clipboard
- 🎯 **Multiple Generation** - Generate multiple passwords at once
- 🚫 **Character Exclusion** - Exclude problematic or ambiguous characters

## 📦 Installation

### From Source

```bash
git clone https://github.com/yourusername/gem-pass-gen.git
cd gem-pass-gen
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[clipboard]"
```

### Quick Install (Dev Mode)

```bash
pip install -e ".[dev,clipboard]"
```

## 🚀 Usage

### Basic Usage

```bash
# Generate a default 16-character password (chunked with hyphens)
gempass

# Output:
# 🔐 Gempass Generator
#
# Length:      16 characters
# Pool size:   94 characters
# Entropy:     104.8 bits
#
# ╭─ Generated Password ─╮
# │ aB3!-xY9@-mN2#-pQ7$  │
# ╰───────────────────────╯
#
# Strength: Strong 🔒🔒
```

### Advanced Options

```bash
# Generate a 32-character hash (no chunks)
gempass --length 32 --hash

# Generate 5 passwords at once
gempass --count 5

# Exclude specific symbols
gempass --exclude "!@#$%^&*()"

# Exclude ambiguous characters (0/O, 1/l/I)
gempass --exclude-ambiguous

# Use only basic symbols
gempass --symbols-only basic

# Custom separator
gempass --separator "_"

# Copy to clipboard
gempass --copy

# Combine options
gempass -l 24 --hash --exclude-ambiguous --copy
```

## 📋 Command Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--length` | `-l` | Password length | `16` |
| `--hash` | | Generate single hash (no chunks) | `False` |
| `--separator` | `-s` | Chunk separator | `"-"` |
| `--exclude` | `-x` | Characters to exclude | `""` |
| `--exclude-ambiguous` | | Exclude 0/O, 1/l/I, etc. | `False` |
| `--symbols-only` | | Symbol level: basic/moderate/all | `None` |
| `--count` | `-n` | Number of passwords | `1` |
| `--copy` | | Copy to clipboard | `False` |
| `--help` | | Show help message | |

## 🎯 Symbol Levels

When using `--symbols-only`:

- **basic**: `!@#$%^&*` (8 symbols)
- **moderate**: `!@#$%^&*()[]{}+-_=` (16 symbols)
- **all**: All punctuation characters (32 symbols)

## 🔐 Security Features

- Uses `secrets` module for cryptographically secure random generation
- Displays entropy calculation (bits of randomness)
- Configurable character pool (52 letters + 10 digits + 32 symbols = 94 total)
- Strength indicators based on entropy:
  - **Excellent** 🔒🔒🔒: ≥128 bits
  - **Strong** 🔒🔒: ≥80 bits
  - **Moderate** 🔒: ≥60 bits
  - **Weak** ⚠️: <60 bits

## 📊 Examples

### API Keys & Tokens
```bash
gempass -l 32 --hash --copy
# Output: aB3xY9mN2pQ7kL4wR8tF6vC1zD5hG0jM
```

### User-Friendly Passwords
```bash
gempass --symbols-only basic --exclude-ambiguous
# Output: kL4w-R8tF-6vC2-zD5h
```

### Database Passwords
```bash
gempass -l 24 --exclude "'\"\`"
# Output: aB3x-Y9mN-2pQ7-kL4w-R8tF-6vC1
```

### Multiple Passwords
```bash
gempass -n 5 -l 12
```

## 🛠️ Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/gem-pass-gen.git
cd gem-pass-gen

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev,clipboard]"
```

### Run Tests

```bash
pytest
pytest --cov=gem_pass_gen  # With coverage
```

### Code Formatting

```bash
black gempass_generator.py
ruff check gempass_generator.py
mypy gempass_generator.py
```

## 📝 Requirements

- Python 3.8+
- click >= 8.0.0
- rich >= 13.0.0
- pyperclip >= 1.8.0 (optional, for clipboard support)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI framework
- Styled with [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- Inspired by the need for secure, customizable password generation

## 📧 Contact

Joshua - pq@extantra.net

Project Link: [https://github.com/yourusername/gem-pass-gen](https://github.com/yourusername/gem-pass-gen)

---

**Made with ❤️ for security-conscious developers**
# gem-pass-gen
# gem-pass-gen
