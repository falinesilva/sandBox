"""Prototype"""
"""TODO: Improve ui and add types of assets an debt"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import io

class NetWorthApp:
    def __init__(self, root):
        """Initialize the app with UI setup."""
        font = "Arial"
        color_a = "#1A1A1A"

        self.root = root
        self.root.title("Net Worth Estimator")
        self.root.configure(bg=color_a)
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Set style for widgets
        style = ttk.Style()
        style.configure("TFrame", background=color_a)
        style.configure("TLabel", background=color_a, foreground="#FFFFFF", font=(font, 10))
        style.configure("TButton", background=color_a, foreground="black", font=(font, 10))
        style.map("TButton", background=[('active', '#454545')])

        # Create frame to hold widgets
        self.frame = ttk.Frame(self.root, padding="20 80 20 20", style="TFrame")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title label
        self.title_label = ttk.Label(self.frame, text="Net Worth Estimator", font=(font, 14), foreground="#FFFFFF", background=color_a)
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(40, 10))

        # Asset entry
        self.assets_label = ttk.Label(self.frame, text="Assets ($)", font=(font, 10), foreground="#FFFFFF", background=color_a)
        self.assets_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        self.assets_entry = ttk.Entry(self.frame, font=(font, 10), width=20)
        self.assets_entry.grid(row=1, column=1, pady=5)

        # Debt entry
        self.debt_label = ttk.Label(self.frame, text="Debt ($)", font=(font, 10), foreground="#FFFFFF", background=color_a)
        self.debt_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.debt_entry = ttk.Entry(self.frame, font=(font, 10), width=20)
        self.debt_entry.grid(row=2, column=1, pady=5)

        # Plot button
        self.plot_button = ttk.Button(self.frame, text="Plot Net Worth", command=self.plot_net_worth, width=20, style="TButton")
        self.plot_button.grid(row=3, column=0, columnspan=2, pady=15)

        # Canvas for graph
        self.canvas = tk.Canvas(self.frame, width=250, height=150, bg="white", bd=10, relief="flat")
        self.canvas.grid(row=4, column=0, columnspan=2, pady=(10))

    def plot_net_worth(self):
        """Handle button press, plot net worth."""
        try:
            # Get user input for assets and debt
            assets = float(self.assets_entry.get())
            debt = float(self.debt_entry.get())

            # Generate plot and show on canvas
            img_tk = self.generate_plot(assets, debt)

            # Account for canvas padding (10px on all sides)
            padding = 10
            canvas_width = self.canvas.winfo_width() - 2 * padding
            canvas_height = self.canvas.winfo_height() - 2 * padding
            img_width = img_tk.width()
            img_height = img_tk.height()

            # Calculate the position to center the image
            x = (canvas_width - img_width) // 2 + padding
            y = (canvas_height - img_height) // 2 + padding

            self.canvas.create_image(x, y, image=img_tk, anchor="nw")
            self.canvas.image = img_tk  # Keep reference
        except ValueError:
            # Handle invalid input
            print("Please enter valid numeric values for assets and debt.")
        
    def generate_plot(self, assets, debt):
        """Generate pie chart of assets vs debt."""
        labels = ['Assets', 'Debt']
        values = [assets, debt]

        # Create and save plot as PNG
        fig, ax = plt.subplots(figsize=(3, 2))  # Adjust the size here if necessary
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#595959', '#F44336'])
        ax.axis('equal')  # Ensure circle shape

        # Save plot to buffer
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight')  
        buf.seek(0)  # Rewind buffer

        # Convert to Tkinter-compatible image
        img = Image.open(buf)
        img_tk = ImageTk.PhotoImage(img)

        plt.close(fig)  # Close plot to free resources
        return img_tk

def main():
    """Run the app."""
    root = tk.Tk()
    app = NetWorthApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
