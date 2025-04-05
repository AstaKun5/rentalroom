import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


def open_main_page():
    # Create the application window
    main_root = tk.Tk()
    main_root.title("نظام إدارة العقارات والأملاك")
    main_root.geometry("1400x800")
    main_root.resizable(True, True)

    # Apply TTKBootstrap style with custom colors
    style = Style(theme="flatly")
    
    # Custom style configurations
    style.configure("TFrame", background="#f5f7fa")
    style.configure("Sidebar.TFrame", background="#2c3e50")
    style.configure("Content.TFrame", background="#ffffff")
    style.configure("Title.TLabel", 
                   background="#ffffff", 
                   foreground="#2c3e50", 
                   font=("Tahoma", 24, "bold"),
                   padding=20)
    style.configure("Sidebar.TButton", 
                   background="#2c3e50", 
                   foreground="#ecf0f1", 
                   font=("Tahoma", 12),
                   padding=10,
                   anchor="w")  # Align text to the left
    style.map("Sidebar.TButton",
             background=[("active", "#34495e")],
             foreground=[("active", "#ffffff")])
    style.configure("Card.TFrame", 
                   background="#ffffff", 
                   borderwidth=2, 
                   relief="groove",
                   padding=20)
    style.configure("Card.TLabel",
                   background="#ffffff",
                   foreground="#2c3e50",
                   font=("Tahoma", 14))
    style.configure("Header.TLabel",
                   background="#2c3e50",
                   foreground="#ffffff",
                   font=("Tahoma", 16, "bold"),
                   padding=10)

    # Main frame
    main_frame = ttk.Frame(main_root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # Sidebar frame with icons (aligned to left)
    sidebar_frame = ttk.Frame(main_frame, width=280, style="Sidebar.TFrame")
    sidebar_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(5, 0), pady=5)
    sidebar_frame.pack_propagate(False)

    # Add header to sidebar
    sidebar_header = ttk.Label(sidebar_frame, 
                            
                             style="Header.TLabel")
    sidebar_header.pack(fill=tk.X, pady=(0, 20))

    # Content frame for displaying information
    content_frame = ttk.Frame(main_frame, style="Content.TFrame")
    content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5), pady=5)

    # Function to change the content frame
    def show_frame(frame_content):
        # Clear current content
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        # Add padding frame for better spacing
        padding_frame = ttk.Frame(content_frame)
        padding_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Add the new content
        frame_content(padding_frame)

    # Home frame content
    def home_content(parent):
        frame = ttk.Frame(parent, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(frame, 
                              text="نظام إدارة العقارات والأملاك", 
                              style="Title.TLabel")
        title_label.pack(pady=20)
        
        # Add some dashboard cards
        cards_frame = ttk.Frame(frame)
        cards_frame.pack(fill=tk.BOTH, expand=True)
        
        # Card 1
        card1 = ttk.Frame(cards_frame, style="Card.TFrame")
        card1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ttk.Label(card1, text="إجمالي العقارات", style="Card.TLabel").pack()
        ttk.Label(card1, text="125", font=("Tahoma", 24, "bold")).pack()
        
        # Card 2
        card2 = ttk.Frame(cards_frame, style="Card.TFrame")
        card2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ttk.Label(card2, text="العقارات المؤجرة", style="Card.TLabel").pack()
        ttk.Label(card2, text="87", font=("Tahoma", 24, "bold")).pack()
        
        # Card 3
        card3 = ttk.Frame(cards_frame, style="Card.TFrame")
        card3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        ttk.Label(card3, text="إجمالي المستأجرين", style="Card.TLabel").pack()
        ttk.Label(card3, text="94", font=("Tahoma", 24, "bold")).pack()
        
        # Configure grid weights
        cards_frame.columnconfigure(0, weight=1)
        cards_frame.columnconfigure(1, weight=1)
        cards_frame.columnconfigure(2, weight=1)

    # Sidebar items with icons on the left (as shown in the image)
    sidebar_items = [
        ("🏠", "الرئيسية", lambda: show_frame(home_content)),
    ]

    # Add sidebar buttons with icons on the left
    for emoji, item, command in sidebar_items:
        btn_frame = ttk.Frame(sidebar_frame, style="Sidebar.TFrame")
        btn_frame.pack(fill=tk.X, padx=5, pady=2)
        
        # Icon label (left side)
        icon_label = ttk.Label(btn_frame, 
                             text=emoji, 
                             font=("Segoe UI Emoji", 14),
                             background="#2c3e50",
                             foreground="#ecf0f1")
        icon_label.pack(side=tk.LEFT, padx=(10, 5))
        
        # Button (text only)
        btn = ttk.Button(btn_frame, 
                        text=item, 
                        style="Sidebar.TButton",
                        command=command)
        btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # Show the home content on startup
    show_frame(home_content)

    main_root.mainloop()

if __name__ == "__main__":
    open_main_page()