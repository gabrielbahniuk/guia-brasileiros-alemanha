## Contribuindo com o repositório

Toda contribuição é bem-vinda.

## Estrutura de conteúdo

- Conteúdo principal em `docs/topics/*.md`
- Conteúdo por cidade em `docs/cities/*.md`
- Texto dos arquivos em pt-BR
- Nomes de arquivos e pastas em inglês, `kebab-case`

## Mapeamento atual (PT -> EN)

- `advocacia` -> `legal.md`
- `automoveis` -> `vehicles.md`
- `comidas-brasileiras` -> `brazilian-food.md`
- `comparacao-de-precos` -> `price-comparison.md`
- `comunidade` -> `community.md`
- `imoveis` -> `housing.md`
- `produtos-e-servicos` -> `products-services.md`
- `saude` -> `health.md`
- `outros` -> `misc.md`
- `stuttgart` -> `cities/stuttgart.md`

## Verificar links

O repositório usa o [lychee](https://github.com/lycheeverse/lychee) no GitHub Actions (PR/push para `main` e verificação diária por cron). Rode localmente antes de enviar mudanças com muitos links:

```bash
./scripts/check-links.sh
```

Alguns links estão **excluídos** em `lychee.toml` por bloqueio a bots automáticos, mas o link continua válido no navegador. Evite URLs curtas que só redirecionam quando puder usar o link completo (ex.: `https://www.mobile.de/`).

Em horário agendado (e manualmente), o workflow **Propose removals for failing links** pode abrir **um PR normal por link** que o lychee marcou como falho (descrição do PR em inglês); você pode fechar sem merge se for falso positivo (ex.: 503 temporário).

O workflow **Close stale automated link PRs** (`close-stale-link-prs.yml`) fecha sozinho PRs desses ramos **`automated/remove-link-*`** após **`STALE_AUTOMATED_LINK_PR_MAX_DAYS`** (por padrão 14 dias; dá para mudar no `env` do YAML ou pelo *workflow_dispatch* com `max_age_days`).

## Como contribuir

### 1) Abrindo issue

Abra sua issue [aqui](https://github.com/gabrielbahniuk/guia-brasileiros-alemanha/issues/new) e envie sua sugestão de mudança ou melhoria.

### 2) Enviando PR

Forke o projeto e abra um [Pull Request](https://github.com/gabrielbahniuk/guia-brasileiros-alemanha/pulls) com sua alteração.

## Padrão recomendado para novos links

Quando possível, adicione contexto curto para deixar o conteúdo mais útil:

```md
**Quando usar:** ...
**Nível de confiança:** oficial | comercial | comunidade

- [Nome do recurso](https://example.com) - resumo rápido (o que resolve)

**Dica prática:** ...
```