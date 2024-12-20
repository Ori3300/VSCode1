import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import requests
import os

# VirusTotal API key and headers
api_key = '791ab4286de615872a538a5a7c3f7f80201d712002b726afd21f86fa9afa0aac'
headers = {
    "x-apikey": api_key
}
url = "https://www.virustotal.com/api/v3/files"

# Function to upload a file to VirusTotal
def upload_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url=url, headers=headers, files=files)
            response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Function to scan a directory (called in a thread)
def scan_directory(directory):
    # Clear previous results before starting the scan
    append_to_display("Starting scan...\n")
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Update GUI with the file being scanned
            append_to_display(f"Scanning file: {file_path}\n")
            result = upload_file(file_path)
            # Update GUI with the scan result
            if "error" in result:
                append_to_display(f"Error: {result['error']}\n\n")
            else:
                scan_id = result.get('data', {}).get('id', 'Unknown')
                append_to_display(f"Scan ID: {scan_id}\n\n")
    
    append_to_display("Scan completed.\n")

# Helper function to safely update the Text widget
def append_to_display(text):
    result_display.after(0, lambda: result_display.insert(tk.END, text))
    result_display.after(0, result_display.yview_moveto, 1)  # Auto-scroll to the bottom

# Function to start scanning in a thread
def start_scan(directory):
    if directory:
        # Start a background thread to scan files
        threading.Thread(target=scan_directory, args=(directory,), daemon=True).start()
    else:
        messagebox.showwarning("Warning", "Please select a directory to scan.")

# Browse directory and initiate scan
def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Selected Directory: {directory}")
        result_display.delete(1.0, tk.END)  # Clear previous results
        start_scan(directory)

# Tkinter GUI setup
root = tk.Tk()
root.title("VirusTotal Scanner")
root.geometry("700x500")

# Frame and widgets
frame = tk.Frame(root)
frame.pack(pady=10)

browse_button = tk.Button(frame, text="Select Directory", command=browse_directory, font=("Arial", 12))
browse_button.pack()

dir_label = tk.Label(root, text="No directory selected", font=("Arial", 10))
dir_label.pack(pady=5)

# Scrollable text widget for results
result_display = tk.Text(root, wrap="word", height=25, width=80)
result_display.pack(pady=10)

scrollbar = tk.Scrollbar(result_display, command=result_display.yview)
result_display.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start Tkinter main loop
root.mainloop()
