import time
import sys

def move_cursor_up(n):
    """Move the cursor up by 'n' lines."""
    sys.stdout.write(f'\033[{n}A')
    sys.stdout.flush()

def clear_lines(n):
    """Clear 'n' lines."""
    for _ in range(n):
        sys.stdout.write('\033[K')  # Clear the line from cursor to end
        sys.stdout.write('\033[A')  # Move up one line
    sys.stdout.flush()

# Print the yellow square
sys.stdout.write('🟨\n')  # Print the yellow square and move to next line
sys.stdout.flush()

time.sleep(1)  # Wait for a second

# Move cursor up to the previous line
move_cursor_up(1)
sys.stdout.write('⚫')  # Print the black circle above the yellow square
sys.stdout.flush()

# Optional: Clear additional lines if needed (for multiple updates or clearing)
clear_lines(2)
