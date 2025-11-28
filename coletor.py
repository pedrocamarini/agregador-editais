import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL alvo
URL_ALVO = "https://www.gov.br/cnpq/pt-br/assuntos/noticias"

def buscar_editais():
    print(f"📡 Conectando ao site: {URL_ALVO}")
    
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    
    try:
        response = requests.get(URL_ALVO, headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(f"❌ Erro ao acessar: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # --- MUDANÇA AQUI: ESTRATÉGIA ARRASTÃO ---
        # Em vez de procurar uma classe específica, pegamos TODOS os links da página
        todos_links = soup.find_all('a')
        
        print(f"🔍 Total de links brutos encontrados: {len(todos_links)}")
        
        dados_coletados = []
        # Palavras-chave expandidas
        palavras_chave = ['edital', 'chamada', 'bolsa', 'fomento', 'inscrição', 'seleção', 'resultado', 'cnpq']

        for link_tag in todos_links:
            titulo = link_tag.get_text().strip()
            link = link_tag.get('href')
            
            # Filtro de qualidade: O título tem que ter texto e ser maior que 10 letras
            if titulo and len(titulo) > 10 and link:
                # Verifica se alguma palavra chave está no título (tudo minúsculo)
                if any(palavra in titulo.lower() for palavra in palavras_chave):
                    
                    # Evita duplicatas (links repetidos)
                    if not any(d['Link'] == link for d in dados_coletados):
                        print(f"✅ ACHOU: {titulo[:60]}...") # Mostra só o começo do título
                        
                        dados_coletados.append({
                            'Titulo': titulo,
                            'Link': link,
                            'Data_Coleta': datetime.now().strftime("%d/%m/%Y")
                        })

        # Salvar
        if dados_coletados:
            df = pd.DataFrame(dados_coletados)
            nome_arquivo = "oportunidades_cnpq.csv"
            df.to_csv(nome_arquivo, index=False, sep=';', encoding='utf-8-sig') 
            print(f"\n💾 SUCESSO! {len(dados_coletados)} itens salvos em '{nome_arquivo}'")
        else:
            print("\n🤷 Nenhum edital encontrado, mas a conexão funcionou.")

    except Exception as e:
        print(f"⚠️ Erro crítico: {e}")

if __name__ == "__main__":
    buscar_editais()