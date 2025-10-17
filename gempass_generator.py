
# gempass generator
import secrets
import string
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def generate_password(length=4, separator='-', chunked=True, exclude_chars=''):
    # Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    # remove excluded characters if any
    if exclude_chars:
        characters = ''.join(char for char in characters if char not in exclude_chars)
        if not characters:
            raise ValueError("You have excluded all possible characters for password generation.")
    # Generate password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    if chunked:
        return separator.join([password[i:i+4] for i in range(0, len(password), 4)])
        return separator.joing(chunks) # return chunked password
    else:
        return password
def calculate_entropy(password, char_pool_size):
    #calculate entropy in bits
    import math
    length = len(password)
    entropy = length * math.log2(char_pool_size)
    return entropy
@click.command()
@click.option('--length', default=16, help='Length of the password.')
@click.option('--hash', is_flag=True, help='Generate a hash of the password.')
@click.option('--separator', default='-', help='Separator for chunked passwords.')
@click.option('--exclude', default='', help='Characters to exclude from the password.')
@click.option('--exclude-ambiguous', is_flag=True, help='Exclude ambiguous characters (Il1O0).')
@click.option('--symbols-only', default=None, help='Use only symbols. Options: basic, moderate, all.')
@click.option('--count', default=1, help='Number of passwords to generate.')
@click.option('--copy', is_flag=True, help='Copy the generated password to clipboard.')
@click.option("--help", is_flag=True, help="Available options:\n" \
"--length: Length of the password (default: 16)\n" \
"--hash: Generate a hash of the password\n" \
"--separator: Separator for chunked passwords (default: '-')\n" \
"--exclude: Characters to exclude from the password\n" \
"--exclude-ambiguous: Exclude ambiguous characters (Il1O0)\n" \
"--symbols-only: Use only symbols. Options: basic, moderate, all\n" \
"--count: Number of passwords to generate (default: 1)\n" \
"--copy: Copy the generated password to clipboard" \
"--help: Show this help message and exit")

def main(length, hash, separator, exclude, exclude_ambiguous, symbols_only, count, copy):
    #generate gemmy cryptographically secure passwords
    
    exclude_chars = exclude #exclusion list
    if exclude_ambiguous:
        exclude_chars += 'Il1O0'
    if symbols_only:
        all_symbols = string.punctuation
        if symbols_only == 'basic':
            allowed_symbols = '!@#$%^&*'
            exclude_chars += ''.join(char for char in string.ascii_letters + string.digits if char not in allowed_symbols)
        elif symbols_only == 'moderate':
            allowed_symbols = '!@#$%^&*()[]{}+-_='
            exclude_chars += ''.join(char for char in string.ascii_letters + string.digits if char not in allowed_symbols)
        elif symbols_only == 'all':
            pass # use all symbols
        else:
            console.print(f"[red]Invalid symbols-only option: {symbols_only}[/red]")
            return
        #calculate char pool size
    char_pool_size = len(''.join(char for char in string.ascii_letters + string.digits + string.punctuation if char not in exclude_chars))
    
    table = Table(title="Generated Passwords") 
    table.add_column("Password", style="cyan")
    table.add_column("Entropy (bits)", style="magenta")
    for _ in range(count):
        password = generate_password(length, separator, chunked=True, exclude_chars=exclude_chars)
        entropy = calculate_entropy(password, char_pool_size)
        table.add_row(password, f"{entropy:.2f}")
        if copy:
            try:
                import pyperclip
                pyperclip.copy(password)
                console.print("[green]Password copied to clipboard![/green]")
            except ImportError:
                console.print("[red]pyperclip not installed. Cannot copy to clipboard.[/red]")
    console.print(table) 
if __name__ == "__main__":
    main()