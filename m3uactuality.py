import urllib.request
import sys

# URL da lista de origem fornecida
URL_ORIGEM = "https://gist.githubusercontent.com/divulgabr/351870c88e1ae8c7a9fcae17f21073b3/raw/ce710da9a329952e2d522b7cb1f7525b211ff99f/DIVULGABR%2520CANAIS.m3u"
ARQUIVO_SAIDA = "minha_lista.m3u"

def atualizar_lista():
    print("Baixando a lista de origem...")
    req = urllib.request.Request(
        URL_ORIGEM, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            conteudo = response.read().decode('utf-8')
        
        # Validação simples do formato M3U
        if "#EXTM3U" not in conteudo:
            print("Erro: O conteúdo baixado não é uma lista M3U válida.")
            sys.exit(1)
            
        with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
            f.write(conteudo)
            
        print(f"Lista atualizada com sucesso e salva em '{ARQUIVO_SAIDA}'!")
        
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar a lista: {e}")
        sys.exit(1)

if __name__ == "__main__":
    atualizar_lista()
