import os
# Renomeando a pasta \Broccoli_Headphones_Glasses  para \obj
caminho_antigo = r'.\OIDv4_ToolKit\OID\Dataset\train\Broccoli_Headphones_Glasses'
novo_nome = r'.\OIDv4_ToolKit\OID\Dataset\train\obj'

# Renomear a pasta
os.rename(caminho_antigo, novo_nome)