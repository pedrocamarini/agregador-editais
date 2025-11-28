# 📡 Radar de Editais & Fomento

Ferramenta de **Engenharia de Dados** que monitora automaticamente portais do governo em busca de oportunidades de fomento, bolsas e editais culturais/científicos.

O sistema realiza o ciclo completo de **ETL (Extract, Transform, Load)**: extrai dados de múltiplos sites, aplica filtros de limpeza e temporalidade, consolida em um banco histórico e exibe em um dashboard interativo.

## 🚀 Funcionalidades

- **Coleta Multi-Site:** Varredura automática no **CNPq**, **IPHAN** e **IBRAM**.
- **Filtro Inteligente:**
  - **Blacklist Institucional:** Remove links irrelevantes ("Quem somos", "Estatuto").
  - **Filtro Temporal:** Ignora editais antigos/encerrados, focando em 2025/2026.
  - **Deduplicação:** Garante que apenas novas oportunidades sejam adicionadas ao banco.
- **Persistência de Dados:** Histórico salvo incrementalmente em CSV.
- **Dashboard Interativo:** Interface visual em **Streamlit** para busca e filtragem.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Web Scraping:** `Requests`, `BeautifulSoup4`
- **Manipulação de Dados:** `Pandas`
- **Visualização:** `Streamlit`

## ⚙️ Como Rodar Localmente

1. **Clone o repositório:**

    git clone https://github.com/SEU_USUARIO/agregador-editais.git
    cd agregador-editais

2. **Instale as dependências:**

    pip install -r requirements.txt

3. **Execute o Robô de Coleta (ETL):**
   Este script vai varrer a internet e atualizar o arquivo CSV.

    python coletor.py

4. **Abra o Dashboard:**
   Para visualizar e filtrar os dados coletados.

    streamlit run dashboard.py

## 📂 Estrutura do Projeto

- `coletor.py`: O "cérebro" do robô. Contém a lógica de extração, limpeza (blacklist/whitelist) e salvamento incremental.
- `dashboard.py`: A interface gráfica. Lê o CSV gerado e cria a visualização web.
- `oportunidades_consolidada.csv`: Banco de dados local (gerado após a primeira execução).

## 📝 Licença

Desenvolvido para fins educacionais e de portfólio.