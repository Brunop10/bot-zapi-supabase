# Bot Z-API + Supabase

Aplicação em Python para buscar contatos no Supabase e enviar mensagens personalizadas via WhatsApp utilizando a Z-API.

## Tecnologias

- Python
- Supabase
- Z-API

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Status

- [x] Estrutura inicial do projeto
- [ ] Integração com Supabase
- [ ] Integração com Z-API
- [ ] Envio de mensagens personalizadas