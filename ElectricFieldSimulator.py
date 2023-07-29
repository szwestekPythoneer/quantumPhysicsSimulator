from tkinter import Tk, Canvas
from time import sleep
root = Tk()
window = Canvas(height=700, width=1300, bg='black')
window.pack()


class Quant:
    def __init__(self, position=None, paint=None, speed=None, quantumSpeed=None):
        self.position = position
        self.classicSpeed = speed
        self.sigma = 0
        self.quantumSpeed = quantumSpeed
        self.color = paint
        self.graphic = window.create_oval(self.position[0], self.position[1], self.position[0] + self.sigma,
                                          self.position[1] + self.sigma, outline=self.color)

    def spreadParticle(self):
        self.sigma += self.quantumSpeed

    def moveParticle(self):
        for i in range(3):
            self.position[i] += self.classicSpeed[i]

    def updateParticleGraphics(self):
        window.coords(self.graphic, self.position[0] - self.sigma, self.position[1] - self.sigma,
                      self.position[0] + self.sigma, self.position[1] + self.sigma)


fermions = [Quant(position=[650, 350, 650], speed=[0, 0, 0], quantumSpeed=0, paint='yellow'),
            Quant(position=[597, 350, 650], speed=[0.01, 0, 0], quantumSpeed=0.01, paint='blue')]
bosons = [Quant(position=[650, 350, 650], speed=[0, 0, 0], quantumSpeed=1, paint='white')]
for i in range(1000):
    for f in fermions:
        f.spreadParticle()
        f.moveParticle()
        f.updateParticleGraphics()
    for b in bosons:
        b.spreadParticle()
        b.updateParticleGraphics()
    window.update()
    sleep(0.001)
window.mainloop()
