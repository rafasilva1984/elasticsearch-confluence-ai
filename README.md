# Elasticsearch + Confluence Cloud + IA (PoC)

Este projeto integra Confluence Cloud e Elastic Cloud com busca semântica via IA.

## Pré-requisitos

- Conta no [Elastic Cloud](https://cloud.elastic.co)
- Conta no [Confluence Cloud](https://www.atlassian.com/software/confluence/try)
- Python 3.8+
- Modelo `paraphrase-MiniLM-L6-v2` baixado localmente

## Como usar

1️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

2️⃣ Copie `.env.example` e edite como `.env`:
```bash
cp .env.example .env
```
Preencha com seus dados do Elastic e Confluence.

3️⃣ Crie o índice no Elastic Cloud (via Kibana Dev Tools):
```
PUT confluence_docs
{ <conteúdo do config/index_mapping.json> }
```

4️⃣ Rode os scripts:
```bash
python scripts/1_extract_confluence.py
python scripts/2_clean_transform.py
python scripts/3_index_elasticsearch.py
python scripts/4_vectorize_ia.py
python frontend/app.py
```

## Configuração obrigatória

Edite o `.env`:
- `CONFLUENCE_BASE_URL`
- `CONFLUENCE_USER`
- `CONFLUENCE_API_TOKEN`
- `ELASTIC_URL`
- `ELASTIC_USER`
- `ELASTIC_PASSWORD`

## Observação
O client do Elasticsearch foi configurado com `verify_certs=False` para facilitar testes em redes com proxy SSL.
