import customtkinter as ctk
from tkinter import messagebox

# Configuración de apariencia
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class OutdoorPlannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Outdoor Planner Pro - V1.0")
        self.geometry("800x600")

        # Diccionario de Datos
        self.equipo_data = {
            "Trekking por el día": ["Zapatos trekking", "Mochila 20L", "Agua", "Botiquín"],
            "Trail Running": ["Zapatillas trail", "Chaleco hidratación", "Manta térmica", "Botiquín"],
            "Montañismo Invernal": ["Botas rígidas", "Crampones", "Piolet", "Casco", "Arnés", "Cuerda (30m aprox.)", "Mochila 55+ ltrs.", "Comida colórica", "Agua", "Botiquín"],
            "Snowboard / Splitboard": ["DVA", "Pala", "Sonda", "Tabla/s", "Pieles", "Ración de marcha", "Equipo de reparación", "Casco", "Antiparras", "Mochila 25/35 ltrs.", "Agua", "Botiquín"]
        }

        # --- LAYOUT: Sidebar ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(
            self.sidebar, text="OUTDOOR\nPLANNER", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=20)

        # --- LAYOUT: Main Frame ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.pack(side="right", fill="both",
                             expand=True, padx=20, pady=20)

        # Elementos de Entrada
        self.label_titulo = ctk.CTkLabel(
            self.main_frame, text="Planificación de Ruta", font=ctk.CTkFont(size=24))
        self.label_titulo.pack(pady=10)

        self.entry_nombre = ctk.CTkEntry(
            self.main_frame, placeholder_text="Nombre de la ruta (ej: Volcán Villarrica)", width=400)
        self.entry_nombre.pack(pady=10)

        self.option_actividad = ctk.CTkOptionMenu(
            self.main_frame, values=list(self.equipo_data.keys()), width=400)
        self.option_actividad.pack(pady=10)

        self.entry_dist = ctk.CTkEntry(
            self.main_frame, placeholder_text="Distancia (km)", width=400)
        self.entry_dist.pack(pady=10)

        self.entry_asc = ctk.CTkEntry(
            self.main_frame, placeholder_text="Ascenso total (m)", width=400)
        self.entry_asc.pack(pady=10)

        # Botón Calcular
        self.btn_calc = ctk.CTkButton(self.main_frame, text="Calcular y Generar Plan",
                                      command=self.calcular_plan, fg_color="#38bdf8", hover_color="#0ea5e9", text_color="black")
        self.btn_calc.pack(pady=20)

        # Area de Resultados
        self.text_result = ctk.CTkTextbox(
            self.main_frame, width=500, height=200)
        self.text_result.pack(pady=10)

    def calcular_plan(self):
        try:
            nombre = self.entry_nombre.get()
            dist = float(self.entry_dist.get())
            asc = float(self.entry_asc.get())
            actividad = self.option_actividad.get()

            # Lógica de Naismith
            tiempo = (dist / 4) + (asc / 400)
            checklist = self.equipo_data[actividad]

            # Generar Reporte
            resumen = f"RUTA: {nombre}\nACTIVIDAD: {actividad}\n"
            resumen += f"TIEMPO ESTIMADO: {tiempo:.2f} horas\n"
            resumen += "-"*30 + "\nEQUIPO NECESARIO:\n"
            for item in checklist:
                resumen += f"• {item}\n"

            # Mostrar en el cuadro de texto
            self.text_result.delete("1.0", "end")
            self.text_result.insert("0.0", resumen)

            # Guardar archivo automáticamente
            with open(f"plan_{nombre}.txt", "w", encoding="utf-8") as f:
                f.write(resumen)

            messagebox.showinfo(
                "Éxito", f"Plan guardado como plan_{nombre}.txt")

        except ValueError:
            messagebox.showerror(
                "Error", "Por favor ingresa números válidos en distancia y ascenso.")


if __name__ == "__main__":
    app = OutdoorPlannerApp()
    app.mainloop()
