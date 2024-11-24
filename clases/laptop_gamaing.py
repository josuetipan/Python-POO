from laptop import Laptop
class Laptop_Gaming(Laptop):

    def __init__(self,marca,procesador,memoria,tarje_graf,consto=500,impuesto=10):
        super().__init__(marca, procesador, memoria, consto, impuesto)
        self.tarje_graf = tarje_graf
    def __str__(self):
        return f"marca: {self.marca} \n PROcesador: {self.procesador} \n Memoria: {self.memoria} \n tarje_graf: {self.tarje_graf} \n consto: {self.costo} \n impuesto: {self.impuestos} \n"
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos  = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resulatdos juegsos"] = resultado_juegos
        return resultado_diagnostico
    
    def realizar_diagnostico_juegos(self):
        juegos = ["Forminte","COD","GTA"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarje_graf:
                fps = fps_base * 3
            elif "GTX" in self.tarje_graf:
                fps = fps_base *2
            else:
                fps = fps_base
            
            resultados[juego] = f"{fps} FPS"
        return resultados
    
    def realizar_informe_uso(self):
        informe = super().realizar_informe_uso()
        informe.update({
            "tipo":"Gaming",
            "Uso Recomendado": "juego de video",
            "Horas de uso": 10,
            "Recomendaciones de sofware": ["antivirus", "VPN"]
        })
        return informe
    
    pass