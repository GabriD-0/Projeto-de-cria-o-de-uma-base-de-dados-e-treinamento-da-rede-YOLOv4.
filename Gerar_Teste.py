import os

# o que o codigo abaixo faz: adiciona o nome e caminho de todos as fotos (.jpg) em um txt
imagens = []
os.chdir(os.path.join(r".\OIDv4_ToolKit\OID\Dataset\valid"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        imagens.append("data/valid/" + filename)
os.chdir("..")

with open("test.txt", "w") as outfile:
    for img in imagens:
        outfile.write(img)
        outfile.write("\n")
    outfile.close()
os.chdir("..")