class Televisao:
    def __init__(self):
        self.canal = 1
        self.volume = 25
        self.volume_min = 0
        self.volume_max = 100
        self.canal_min = 1
        self.canal_max = 99
        self.ligada = False

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.desligada = False

    def mudar_canal_para_cima(self):

        if not self.ligada:
            return
        
        if self.canal < self.canal_max:
            self.canal += 1

    def mudar_canal_para_baixo(self):

        if not self.ligada:
            return
        
        if self.canal > self.canal_min:
            self.canal -= 1

    def reduzir_volume(self):

        if not self.ligada:
            return
        
        if self.volume > self.volume_min:
            self.volume -= 5

    def aumentar_volume(self):

        if not self.ligada:
            return
        
        if self.volume < self.volume_max:
            self.volume += 5

    def __str__(self) -> str:
        return f'Televisão - Está ligada: {self.ligada} - Canal: {self.canal} - Volume: {self.volume}'
    
minha_tv = Televisao()
print(minha_tv)
minha_tv.ligar()
print(minha_tv)

print()

minha_tv.mudar_canal_para_cima()
print(minha_tv)
minha_tv.mudar_canal_para_baixo()
print(minha_tv)

print()

minha_tv.aumentar_volume()
print(minha_tv)
minha_tv.reduzir_volume()
print(minha_tv)