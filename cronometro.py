import tkinter as tk


class Cronometro:
    def __init__(self, master):
        self.master = master

        # Variables del tiempo
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0

        self.corriendo = False

        # Variable del display
        self.display = tk.StringVar()
        self.actualizar_display("00:00:00.000")

        # Ventana
        self.master.title("Cronómetro")
        self.master.configure(bg="#220135")
        self.master.geometry("400x200")

        # Label del tiempo
        self.display_label = tk.Label(
            master,
            textvariable=self.display,
            font=("Arial", 30),
            bg="#220135",
            fg="#ffffff"
        )

        self.display_label.pack(pady=20)

        # Frame botones
        self.button_frame = tk.Frame(master, bg="#220135")
        self.button_frame.pack()

        # Botón iniciar
        self.start_button = tk.Button(
            self.button_frame,
            text="Iniciar",
            command=self.iniciar,
            bg="#2ecc71",
            fg="#ffffff",
            width=10
        )

        self.start_button.pack(side=tk.LEFT, padx=5)

        # Botón pausar
        self.stop_button = tk.Button(
            self.button_frame,
            text="Pausar",
            command=self.detener,
            bg="#e67e22",
            fg="#ffffff",
            width=10
        )

        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Botón reiniciar
        self.reset_button = tk.Button(
            self.button_frame,
            text="Reiniciar",
            command=self.reiniciar,
            bg="#e74c3c",
            fg="#ffffff",
            width=10
        )

        self.reset_button.pack(side=tk.LEFT, padx=5)

    # Actualizar display
    def actualizar_display(self, tiempo):
        self.display.set(tiempo)

    # Iniciar
    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True
            self.actualizar_cronometro()

    # Pausar
    def detener(self):
        self.corriendo = False

    # Reiniciar
    def reiniciar(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0

        self.corriendo = False

        self.actualizar_display("00:00:00.000")

    # Mecánica del cronómetro
    def actualizar_cronometro(self):
        if self.corriendo:

            self.milisegundos += 10

            if self.milisegundos >= 1000:
                self.milisegundos = 0
                self.segundos += 1

                if self.segundos >= 60:
                    self.segundos = 0
                    self.minutos += 1

                    if self.minutos >= 60:
                        self.minutos = 0
                        self.horas += 1

            tiempo_formateado = (
                f"{self.horas:02}:"
                f"{self.minutos:02}:"
                f"{self.segundos:02}."
                f"{self.milisegundos:03}"
            )

            self.actualizar_display(tiempo_formateado)

            self.master.after(10, self.actualizar_cronometro)


if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()