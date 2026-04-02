import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to add timezone shift and quality information to icons
def add_info_to_icons(icon_file):
    try:
        # Create a new window
        window = tk.Tk()
        window.withdraw()  # Hide the root window
        while True:
            # Input for timezone shift
            shift = simpledialog.askstring('Input', 'Enter timezone shift (e.g., +2, -3):')
            if shift is None:
                break  # User canceled
            # Input for quality
            quality = simpledialog.askstring('Input', 'Enter quality (SD or HD):')
            if quality is None:
                break  # User canceled
            # Validate input
            if quality not in ['SD', 'HD']:
                messagebox.showerror('Error', 'Quality must be either SD or HD.')
                continue
            # Perform any graphic operations to add the information to the icon here
            # Placeholder for actual implementation.
            # Geometry information for text (in a real case)
            shift_text_color = 'red' if shift else 'black'
            quality_text_color = 'salad green' if quality == 'SD' else 'dark lemon green'
            # Example message to be displayed
            messagebox.showinfo('Information Added', f'Timezone shift: {shift}, Quality: {quality}')
    except Exception as e:
        messagebox.showerror('Error', str(e))

# Main execution flow
if __name__ == '__main__':
    icon_file_name = 'path/to/icon/file.png'  # Update this path according to your setup
    add_info_to_icons(icon_file_name)
