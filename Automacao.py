import time
import pyautogui
from pyautogui import ImageNotFoundException

""""

textos = Tx
input = Inp
possibilidades = Infs
video = Vi


"""

class Automacao():
    def __init__(self) :

        self._caminhoQualificado = "E:\\autoAlura\\Imagens\\iconsPlataforms\\"
        self._memoria = []
        self._camadas = 0

        # observado que na regra de negocios
        # IconLinkTexto.png na plataforma sempre aparece verde

        self._iconsVideos = ['IconConjTexto.png', # garantido
                             'IconPeqTexto.png', # garantido
                             'IconSimpTexto.png',
                             'IconPlanilhaTexto.png']
    
    def mapeamento(self):
        print('Iniciando mapeamento!')
        element = None
        try:

            # verificacao de partes Texto

            for i in self._iconsVideos:

                element = pyautogui.locateCenterOnScreen(f'{self._caminhoQualificado}{i}',confidence=0.7)
                print(f'{self._caminhoQualificado}{i}')

                if ('Texto' in i):
                    
                    self.blocoTexto(element.x,element.y)

                # elif ('Video' in i):
                #     


        except ImageNotFoundException:
            time.sleep(1) 
            print('Nao encontrado')

    def blocoVideo(self,positonX,positonY):
        pyautogui.click(positonX,positonY)

    def blocoPossibilidade(self,positonX,positonY):
        pyautogui.click(positonX,positonY)

    def blocoInputLink(self,positonX,positonY):
        pyautogui.click(positonX,positonY)

    def blocoTexto(self,positonX,positonY):
        pyautogui.click(positonX,positonY)

