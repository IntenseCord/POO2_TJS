import tkinter as tk
from tkinter import ttk, messagebox
from core.fetcher import DataFetcher
from core.sorter import Sorter
import threading, itertools  # 🔹 necesarios para el spinner

class GUIApp:
    """Interfaz gráfica que maneja la interacción del usuario."""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Evaluación 2 - Ordenamiento")
        self.root.geometry("1000x600")

        self.data = []
        self.api_url = tk.StringVar(value="https://api.example.com/data")

        # 🔹 control del spinner
        self._spinner_running = False
        self.spinner_label = None

        self.algorithms = {
            "Burbuja": Sorter.bubble_sort,
            "Selección": Sorter.selection_sort,
            "Inserción": Sorter.insertion_sort,
            "Merge": Sorter.merge_sort,
            "Quick": Sorter.quick_sort,
            "Counting": Sorter.counting_sort,
            "Radix": Sorter.radix_sort,
            "Heap": Sorter.heap_sort,
            "Bucket": Sorter.bucket_sort
        }

        self._build_ui()

    def _build_ui(self):
        # Panel superior: URL + botón
        top = ttk.Frame(self.root, padding=8)
        top.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(top, text="API URL:").pack(side=tk.LEFT)
        ttk.Entry(top, textvariable=self.api_url, width=60).pack(side=tk.LEFT, padx=6)
        ttk.Button(top, text="Cargar datos", command=self.load_data).pack(side=tk.LEFT, padx=6)

        # Opciones
        opts = ttk.Frame(self.root, padding=8)
        opts.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(opts, text="Algoritmo:").grid(row=0, column=0, sticky=tk.W)
        self.alg_combo = ttk.Combobox(opts, values=list(self.algorithms.keys()), state="readonly", width=18)
        self.alg_combo.current(0)
        self.alg_combo.grid(row=0, column=1, padx=6)

        ttk.Label(opts, text="Variable numérica:").grid(row=0, column=2, sticky=tk.W)
        self.var_combo = ttk.Combobox(opts, values=[], state="readonly", width=18)
        self.var_combo.grid(row=0, column=3, padx=6)

        ttk.Label(opts, text="Dirección:").grid(row=0, column=4, sticky=tk.W)
        self.dir_combo = ttk.Combobox(opts, values=["Ascendente", "Descendente"], state="readonly", width=12)
        self.dir_combo.current(0)
        self.dir_combo.grid(row=0, column=5, padx=6)

        ttk.Button(opts, text="Ordenar", command=self.run_sort).grid(row=0, column=6, padx=8)

        # Panel tablas
        center = ttk.Panedwindow(self.root, orient=tk.HORIZONTAL)
        center.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        left_frame = ttk.Labelframe(center, text="Datos originales", width=480)
        right_frame = ttk.Labelframe(center, text="Datos ordenados", width=480)
        center.add(left_frame); center.add(right_frame)

        self.left_tree = ttk.Treeview(left_frame, columns=(), show="headings")
        self.left_tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.left_scroll = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.left_tree.yview)
        self.left_tree.configure(yscrollcommand=self.left_scroll.set)
        self.left_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.right_tree = ttk.Treeview(right_frame, columns=(), show="headings")
        self.right_tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.right_scroll = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.right_tree.yview)
        self.right_tree.configure(yscrollcommand=self.right_scroll.set)
        self.right_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        bottom = ttk.Frame(self.root, padding=6)
        bottom.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_label = ttk.Label(bottom, text="Esperando acción...")
        self.status_label.pack(side=tk.LEFT)

    # ===================== SPINNER ======================
    def _animate_spinner(self):
        if not hasattr(self, "_spinner_cycle"):
            self._spinner_cycle = itertools.cycle(["◐", "◓", "◑", "◒"])
        if self._spinner_running:
            self.spinner_label.config(text=next(self._spinner_cycle))
            self.root.after(200, self._animate_spinner)

    def _start_spinner(self):
        if not self.spinner_label:
            self.spinner_label = ttk.Label(self.root, text="◐", font=("Arial", 32))
            self.spinner_label.place(relx=0.5, rely=0.3, anchor="center")
        self._spinner_running = True
        self._animate_spinner()

    def _stop_spinner(self):
        self._spinner_running = False
        if self.spinner_label:
            self.spinner_label.destroy()
            self.spinner_label = None
    # ====================================================

    def load_data(self):
        self._start_spinner()

        def task():
            fetcher = DataFetcher(self.api_url.get())
            try:
                data = fetcher.fetch()
                self.root.after(0, lambda: self._on_data_loaded(data))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error al cargar", str(e)))
            finally:
                self.root.after(0, self._stop_spinner)

        threading.Thread(target=task, daemon=True).start()

    def _on_data_loaded(self, data):
        self.data = data
        if not self.data:
            messagebox.showinfo("Sin datos", "La API devolvió una lista vacía.")
            return
        self._populate_tables()
        # detectar campos numéricos
        first = self.data[0]
        numeric_fields = []
        for k, v in first.items():
            try:
                float(v); numeric_fields.append(k)
            except: pass
        self.var_combo['values'] = numeric_fields
        if numeric_fields:
            self.var_combo.current(0)
        self.status_label.config(text=f"Cargados {len(self.data)} registros.")

    def _populate_tables(self):
        for tree in (self.left_tree, self.right_tree):
            tree.delete(*tree.get_children())
            tree['columns'] = []
        if not self.data: return
        cols = list(self.data[0].keys())
        for tree in (self.left_tree, self.right_tree):
            tree['columns'] = cols
            for c in cols:
                tree.heading(c, text=c)
                tree.column(c, width=120, anchor=tk.W)
        for item in self.data:
            self.left_tree.insert("", tk.END, values=[item.get(c, "") for c in cols])

    def run_sort(self):
        if not self.data:
            messagebox.showwarning("Sin datos", "Primero carga datos.")
            return
        alg = self.alg_combo.get()
        var = self.var_combo.get()
        rev = (self.dir_combo.get() == "Descendente")
        try:
            sorter_func = self.algorithms[alg]
            sorted_data = sorter_func(self.data, var, rev)
            self._show_sorted(sorted_data)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _show_sorted(self, sorted_data):
        self.right_tree.delete(*self.right_tree.get_children())
        if not sorted_data: return
        cols = list(sorted_data[0].keys())
        self.right_tree['columns'] = cols
        for c in cols:
            self.right_tree.heading(c, text=c)
            self.right_tree.column(c, width=120, anchor=tk.W)
        for item in sorted_data:
            self.right_tree.insert("", tk.END, values=[item.get(c, "") for c in cols])
