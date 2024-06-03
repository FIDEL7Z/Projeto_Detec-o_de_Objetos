# Projeto Acadêmico: Detecção de Objetos em Tempo Real com YOLOv4-Tiny e OpenCV

## Visão Geral

Este projeto acadêmico visa demonstrar a capacidade de detecção de objetos em tempo real utilizando o modelo YOLOv4-Tiny em conjunto com a biblioteca OpenCV. O modelo é treinado para identificar objetos e pessoas em um fluxo de vídeo, exibindo caixas delimitadoras em torno dos objetos detectados, juntamente com seus respectivos nomes de classe e pontuações de confiança.


![Projeto](https://github.com/FIDEL7Z/Projeto_Detec-o_de_Objetos/assets/103468557/f89ec0de-abf1-4cf7-a411-983324d20ac7)

## Pré-requisitos

- Python 3.x
- OpenCV
- Arquivos de Configuração e Pesos do YOLOv4-Tiny
- Arquivo de Nomes COCO (Common Objects in Context)

## Instalação e Configuração

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seuusuario/detecao-objetos-yolov4-tiny.git
   cd detecao-objetos-yolov4-tiny
   ```

2. **Instale as Dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Baixe os Arquivos Necessários:**

   - [YOLOv4-Tiny Configuration](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg)
   - [YOLOv4-Tiny Weights](https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights)
   - [COCO Names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

4. **Execute o Script:**

   ```bash
   python detect_objects.py
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request com melhorias ou correções.

