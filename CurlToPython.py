import tkinter as tk
from tkinter import ttk
import shlex

class CurlConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Curl to Python Converter")
        self.root.configure(bg="red")

        self.made_by_label = tk.Label(self.root, text="Made By MeMo", fg="white", bg="red", font=("Arial", 16, "bold"))
        self.made_by_label.pack()

        self.site_label = tk.Label(self.root, text="My Site: https://mehmetttw7.tk", fg="white", bg="red", font=("Arial", 16, "bold"))
        self.site_label.pack()

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.curl_entry = tk.Entry(self.frame, font=("Helvetica", 12), width=40)
        self.curl_entry.configure(bg="black", fg="white")
        self.curl_entry.pack()

        self.convert_button = tk.Button(self.frame, text="Convert", command=self.convert_and_display)
        self.convert_button.configure(bg="black", fg="white", highlightbackground="red")
        self.convert_button.pack()

        self.code_text = tk.Text(self.root, font=("Courier New", 12), wrap=tk.WORD, bg="red", fg="white")
        self.code_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def convert_curl(self, curl_command):
        parsed = shlex.split(curl_command)
        if not parsed:
            return "Invalid cURL command. Please enter a valid cURL command."

        method = parsed[0]
        url = parsed[-1]
        headers = {}
        data = None

        for i in range(1, len(parsed) - 1):
            if parsed[i] == "-H":
                header = parsed[i+1].replace("'", "").split(": ")
                headers[header[0]] = header[1]
            elif parsed[i] == "--data-binary":
                data = parsed[i+1].replace("'", "")

        if method == "curl":
            method = "post"

        if method.lower() == "get":
            converted_code = f"import requests\n\nheaders = {headers}\n\nresponse = requests.get('{url}', headers=headers)"
        elif method.lower() == "post":
            converted_code = f"import requests\n\nheaders = {headers}\n\ndata = {data}\n\nresponse = requests.post('{url}', headers=headers, json=data)"
        else:
            return f"{method} method is not supported."

        return converted_code

    def convert_and_display(self):
        curl_command = self.curl_entry.get()
        converted_code = self.convert_curl(curl_command)
        self.code_text.delete(1.0, tk.END)
        self.code_text.insert(tk.END, converted_code)

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurlConverter(root)
    root.mainloop()
