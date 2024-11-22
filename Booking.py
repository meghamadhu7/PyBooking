import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk

class BookMyShowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Starlight Seats")
        self.root.geometry("900x700")
        self.root.configure(bg="#2b2b2b")  # Dark background color

        # Movie data with custom theater names and poster paths
        self.movies = {
            "Kanguva": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.58.58_dd9e39b3.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },
            "Amaran": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.59.00_7fa5eba8.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },
            "Lucky Baskha": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.58.58_7b53e681.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },
            "Meiyazhagan": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.58.59_3b8aed48.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },
            "Lubber Pandhu": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.58.57_ad256785.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },"Goat": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.58.58_3da34656.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },"Manjummel Boys": {
                "poster": "C:/Users/91860/Downloads/html/Photo/Manjumallanboy.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },"Brothers": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.58.57_9c0afee1.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },
            "Sita Ramam": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.59.00_0d0964c7.jpg",  # Replace with your actual poster path
                "theaters": {
                     "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },"Love Today": {
                "poster": "C:/Users/91860/Downloads/html/Photo/Love_Today_album_cover.jpg",  # Replace with your actual poster path
                "theaters": {
                     "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },"Kalki": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.58.57_11cb4b15.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },"Vaazhai": {
                "poster": "C:/Users/91860/Downloads/html/Photo/WhatsApp Image 2024-11-22 at 13.58.59_60772828.jpg",  # Replace with your actual poster path
                "theaters": {
                    "Rakki Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"],
                    "PVR Sathyam Cinemas": ["10:00 AM", "1:00 PM", "4:00 PM"],
                    "Green Cinemas": ["11:00 AM", "2:00 PM", "5:00 PM"],
                    "AGS Cinemas": ["9:00 AM", "12:00 PM", "3:00 PM"]
                }
            },
            # Add more movies here with custom names and poster paths
        }

        self.selected_movie = None
        self.selected_theater = None
        self.selected_showtime = None
        self.seats_selected = []
        self.booked_seats = ["2C", "3F", "4G"]  # Pre-booked seats
        self.page_history = []

        self.setup_ui()

    def setup_ui(self):
        self.page_history = []
        self.display_home()

    def add_back_button(self, command):
        back_btn = tk.Button(self.root, text="Back", font=("Arial", 12), command=command, bg="#e74c3c", fg="white")
        back_btn.place(x=10, y=10)

    def display_home(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.root, text="Welcome to Starlight Seats", font=("Arial", 20, "bold"), bg="#2b2b2b", fg="#ecf0f1")
        title_label.pack(pady=10)

        self.poster_frame = tk.Frame(self.root, bg="#2b2b2b")
        self.poster_frame.pack(pady=10)

        self.poster_images = {}
        for movie, data in self.movies.items():
            try:
                # Resize the image to a consistent size
                img = Image.open(data["poster"])
                img_resized = img.resize((100, 150), Image.LANCZOS)  # Resize while maintaining aspect ratio
                self.poster_images[movie] = ImageTk.PhotoImage(img_resized)
            except Exception as e:
                print(f"Error loading poster for {movie}: {e}")
                placeholder = Image.new("RGB", (100, 150), (255, 255, 255))  # Default placeholder if the image fails to load
                self.poster_images[movie] = ImageTk.PhotoImage(placeholder)

        self.display_posters()


    def display_posters(self):
        for widget in self.poster_frame.winfo_children():
            widget.destroy()

        movies = list(self.poster_images.items())
        for i in range(3):  # Three rows
            row_frame = tk.Frame(self.poster_frame, bg="#2b2b2b")
            row_frame.pack(pady=5)

            for j in range(4):  # Four posters in each row
                idx = i * 4 + j
                if idx < len(movies):
                    movie, img = movies[idx]
                    btn = tk.Button(row_frame, image=img, text=movie, compound="top",
                                    command=lambda m=movie: self.select_movie(m), bg="#e74c3c", fg="white")
                    btn.pack(side="left", padx=10)

    def navigate_back(self):
        if self.page_history:
            self.page_history.pop()()
        else:
            self.display_home()

    def select_movie(self, movie):
        self.selected_movie = movie
        self.page_history.append(self.display_home)
        self.show_theaters()

    def show_theaters(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.add_back_button(self.navigate_back)

        tk.Label(self.root, text=f"Selected Movie: {self.selected_movie}", font=("Arial", 16, "bold"), bg="#2b2b2b", fg="#ecf0f1").pack(pady=10)

        tk.Label(self.root, text="Select a Theater:", font=("Arial", 12), bg="#2b2b2b", fg="#ecf0f1").pack(pady=5)

        theater_frame = tk.Frame(self.root, bg="#2b2b2b")
        theater_frame.pack(pady=5)

        for theater in self.movies[self.selected_movie]["theaters"]:
            btn = tk.Button(theater_frame, text=theater, font=("Arial", 12), bg="#e74c3c", fg="white",
                            command=lambda t=theater: self.select_theater(t))
            btn.pack(side="left", padx=10)

    def select_theater(self, theater):
        self.selected_theater = theater
        self.page_history.append(self.show_theaters)
        self.show_showtimes()

    def show_showtimes(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.add_back_button(self.navigate_back)

        tk.Label(self.root, text=f"Selected Theater: {self.selected_theater}", font=("Arial", 16, "bold"), bg="#2b2b2b", fg="#ecf0f1").pack(pady=10)

        tk.Label(self.root, text="Select a Showtime:", font=("Arial", 12), bg="#2b2b2b", fg="#ecf0f1").pack(pady=5)

        showtime_frame = tk.Frame(self.root, bg="#2b2b2b")
        showtime_frame.pack(pady=5)

        showtimes = self.movies[self.selected_movie]["theaters"][self.selected_theater]
        for showtime in showtimes:
            btn = tk.Button(showtime_frame, text=showtime, font=("Arial", 12), bg="#e74c3c", fg="white",
                            command=lambda st=showtime: self.select_showtime(st))
            btn.pack(side="left", padx=10)

    def select_showtime(self, showtime):
        self.selected_showtime = showtime
        self.page_history.append(self.show_showtimes)
        self.show_seats()

    def show_seats(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.add_back_button(self.navigate_back)

        tk.Label(self.root, text=f"Selected Showtime: {self.selected_showtime}", font=("Arial", 16, "bold"), bg="#2b2b2b", fg="#ecf0f1").pack(pady=10)

        tk.Label(self.root, text="Available Seats (Click to Select):", font=("Arial", 12), bg="#2b2b2b", fg="#ecf0f1").pack(pady=5)

        legend_frame = tk.Frame(self.root, bg="#2b2b2b")
        legend_frame.pack(pady=5)
        tk.Label(legend_frame, text="Available: Gray", bg="gray", fg="white").pack(side="left", padx=5)
        tk.Label(legend_frame, text="Selected: Green", bg="green", fg="white").pack(side="left", padx=5)
        tk.Label(legend_frame, text="Booked: Red", bg="red", fg="white").pack(side="left", padx=5)

        seat_frame = tk.Frame(self.root, bg="#2b2b2b")
        seat_frame.pack(pady=5)

        self.seats_selected = []
        self.seat_buttons = []

        for row in range(5):
            for col in range(8):
                seat_id = f"{row+1}{chr(65+col)}"
                bg_color = "red" if seat_id in self.booked_seats else "gray"
                btn = tk.Button(seat_frame, text=seat_id, width=3, bg=bg_color,
                                state="disabled" if bg_color == "red" else "normal",
                                command=lambda r=row, c=col: self.toggle_seat(r, c))
                btn.grid(row=row, column=col, padx=2, pady=2)
                self.seat_buttons.append(btn)

        self.total_label = tk.Label(self.root, text="Total: ₹0", font=("Arial", 14, "bold"), bg="#2b2b2b", fg="#ecf0f1")
        self.total_label.pack(pady=10)

        tk.Label(self.root, text="Screen This Way", font=("Arial", 10, "bold"), bg="#2b2b2b", fg="#ecf0f1").pack(pady=5)
        tk.Label(self.root, text="[SCREEN]", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white").pack()

        proceed_btn = tk.Button(self.root, text="Proceed to Payment", font=("Arial", 12), bg="#e74c3c", fg="white", command=self.proceed_to_payment)
        proceed_btn.pack(pady=10)

    def toggle_seat(self, row, col):
        seat_id = f"{row+1}{chr(65+col)}"
        btn_index = row * 8 + col
        btn = self.seat_buttons[btn_index]

        if seat_id in self.seats_selected:
            self.seats_selected.remove(seat_id)
            btn.config(bg="gray")
        else:
            self.seats_selected.append(seat_id)
            btn.config(bg="green")

        total_cost = len(self.seats_selected) * 200
        self.total_label.config(text=f"Total: ₹{total_cost}")

    def proceed_to_payment(self):
        if not self.seats_selected:
            messagebox.showwarning("No Seats Selected", "Please select at least one seat.")
            return

        total_cost = len(self.seats_selected) * 200
        messagebox.showinfo("Booking Confirmed", f"Your booking for {self.selected_movie} at {self.selected_theater} "
                                                 f"({self.selected_showtime}) has been confirmed!\n"
                                                 f"Seats: {', '.join(self.seats_selected)}\nTotal: ₹{total_cost}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BookMyShowApp(root)
    root.mainloop()