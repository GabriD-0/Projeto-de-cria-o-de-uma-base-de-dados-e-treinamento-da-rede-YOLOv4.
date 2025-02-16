# Projeto: Criação de uma Base de Dados e Treinamento da Rede YOLOv4

Este projeto demonstra como criar uma base de dados utilizando o *Open Images Dataset* e treinar uma rede YOLOv4 para detecção de objetos.

---

## Sumário

1. [Preparação do Ambiente](#preparação-do-ambiente)  
2. [Download das Imagens](#download-das-imagens)  
3. [Organização do Dataset](#organização-do-dataset)  
4. [Conversão das Anotações](#conversão-das-anotações)  
5. [Geração dos Arquivos `train.txt` e `test.txt`](#geração-dos-arquivos-traintxt-e-testtxt)  
6. [Clonando e Configurando o Darknet](#clonando-e-configurando-o-darknet)  
7. [Instalação do CMake](#instalação-do-cmake)  
8. [Compilando o Darknet](#compilando-o-darknet)  
9. [Download dos Pesos Pré-Treinados](#download-dos-pesos-pré-treinados)  
10. [Teste Rápido de Detecção](#teste-rápido-de-detecção)  
11. [Referências](#referências)

---

## 1. Preparação do Ambiente

1. **Clonar o repositório OIDv4_ToolKit**:  
   ```bash
   git clone https://github.com/EscVM/OIDv4_ToolKit.git
   ```

2. **Entrar na pasta e instalar dependências**:
   ```bash
   cd OIDv4_ToolKit
   pip install -r requirements.txt
   ```

3. **Criar ambiente virtual (opcional)**:  
   Caso deseje isolar dependências, crie e ative um `venv` (Python 3.10.11 neste exemplo):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

---

## 2. Download das Imagens

Utilizaremos o [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html), que disponibiliza imagens para diversas classes. Neste exemplo, selecionamos **Broccoli**, **Headphones** e **Glasses**.

### 2.1. Conjunto de Treinamento
```bash
python main.py downloader \
  --classes Broccoli Headphones Glasses \
  --type_csv train \
  --limit 200 \
  --multiclasses 1
```
- `--limit 200` baixa até 200 imagens por classe.

### 2.2. Conjunto de Validação
```bash
python main.py downloader \
  --classes Broccoli Headphones Glasses \
  --type_csv test \
  --limit 50 \
  --multiclasses 1
```
- `--limit 50` baixa até 50 imagens por classe para validação.

---

## 3. Organização do Dataset

Após o download, as imagens ficarão em **OIDv4_ToolKit/OID/Dataset**:

- `train/`  
  - `Broccoli/`  
  - `Headphones/`  
  - `Glasses/`  
- `test/`  
  - `Broccoli/`  
  - `Headphones/`  
  - `Glasses/`

Verifique também se o arquivo `classes.txt` contém apenas as classes desejadas:
```
Broccoli
Headphones
Glasses
```

---

## 4. Conversão das Anotações

- **Converter_Anotacoes.py**: Script que converte as anotações do Open Images Dataset para o formato YOLO.  
  Execute:
  ```bash
  python Converter_Anotacoes.py
  ```
- Opcionalmente, utilize outro script (por exemplo, `Compactador_de_Treinamento.py`) para compactar o dataset final, caso necessário.

---

## 5. Geração dos Arquivos `train.txt` e `test.txt`

Para gerar as listas de imagens que serão utilizadas no treinamento (`train.txt`) e no teste/validação (`test.txt`), você pode usar os scripts **Gerar_Treinamento.py** e **Gerar_Teste.py**:

- **Gerar_Treinamento.py**: varre a pasta de treinamento e gera o arquivo `train.txt` com o caminho de cada imagem.
- **Gerar_Teste.py**: varre a pasta de teste/validação e gera o arquivo `test.txt`.

Exemplo de execução:
```bash
python Gerar_Treinamento.py
python Gerar_Teste.py
```
Certifique-se de ajustar os caminhos dentro desses scripts conforme a estrutura de pastas do seu projeto.

---

## 6. Clonando e Configurando o Darknet

1. **Clonar o repositório Darknet** (fork do AlexeyAB):
   ```bash
   git clone https://github.com/AlexeyAB/darknet.git
   ```

2. **Entrar na pasta**:
   ```bash
   cd darknet
   ```

3. **Ajustar Makefile** (ou `CMakeLists.txt`) para ativar/desativar opções:
   ```makefile
   GPU=1
   CUDNN=1
   CUDNN_HALF=0
   OPENCV=1
   AVX=0
   OPENMP=0
   LIBSO=0
   ZED_CAMERA=0
   ZED_CAMERA_v2_8=0
   ```
   - `GPU=1`: habilita CUDA
   - `CUDNN=1`: habilita cuDNN
   - `OPENCV=1`: habilita OpenCV

---

## 7. Instalação do CMake

No Windows, baixe o instalador em [https://cmake.org/download/](https://cmake.org/download/).  
Durante a instalação, **marque a opção** para adicionar o CMake ao `PATH` do sistema.

No PowerShell, execute:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
para permitir a execução de scripts, caso necessário.

---

## 8. Compilando o Darknet

No Windows, execute o script `build.ps1` dentro da pasta `darknet`:
```powershell
.\build.ps1
```
- Pode ser necessário responder **no** para algumas integrações (ex.: vcpkg) caso não deseje instalá-las.

No Linux, basta ajustar as flags no `Makefile` e rodar:
```bash
make
```

---

## 9. Download dos Pesos Pré-Treinados

Baixe os pesos pré-treinados do YOLOv4:
```bash
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
```
Coloque o arquivo `yolov4.weights` na pasta do Darknet (geralmente `darknet/`).

---

## 10. Teste Rápido de Detecção

Para testar se tudo está funcionando, execute:
```bash
./darknet detect cfg/yolov4.cfg yolov4.weights data/person.jpg
```
- Este comando usa o modelo pré-treinado YOLOv4 para detectar objetos na imagem `person.jpg` (classe “person” faz parte do conjunto COCO).

Se o Darknet estiver configurado corretamente, um arquivo `predictions.jpg` será gerado, exibindo as detecções.

---

## 11. Referências

- [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)  
- [Repositório OIDv4_ToolKit](https://github.com/EscVM/OIDv4_ToolKit)  
- [Repositório Darknet (AlexeyAB)](https://github.com/AlexeyAB/darknet)  
- [Documentação do CMake](https://cmake.org/)  
