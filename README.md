# Guia rápido para brasileiros na Alemanha :de: :book:

## Sobre

Este repositório é um guia rápido com links selecionados e roteiros por fase (antes de vir, primeira semana, primeiros 90 dias) para quem está planejando a mudança ou já mora na Alemanha.

## Site

- GitHub Pages: [gabrielbahniuk.github.io/guia-brasileiros-alemanha](https://gabrielbahniuk.github.io/guia-brasileiros-alemanha/)

## Comece aqui

- [Antes de vir](./docs/guides/before-arrival.md)
- [Primeira semana](./docs/guides/first-week.md)
- [Primeiros 90 dias](./docs/guides/first-90-days.md)

## Lista (por tema)

- [Advocacia](./docs/topics/legal.md)
- [Automóveis](./docs/topics/vehicles.md)
- [Comidas brasileiras](./docs/topics/brazilian-food.md)
- [Comparação de preços](./docs/topics/price-comparison.md)
- [Comunidade brasileira na Alemanha](./docs/topics/community.md)
- [Imóveis](./docs/topics/housing.md)
- [Produtos e serviços](./docs/topics/products-services.md)
- [Saúde](./docs/topics/health.md)
- [Outros](./docs/topics/misc.md)

## Lista (por cidade)

- [Stuttgart e região](./docs/cities/stuttgart.md)

## FAQ

- [Perguntas frequentes](./docs/faq.md)

## Listas semelhantes

- [Awesome Berlin](https://github.com/marlonbernardes/awesome-berlin)
- [Equivalentes Brasil/Alemanha](https://github.com/diessica/equivalentes-brasil-alemanha)

## Contribua

Para contribuir, veja o [guia](./CONTRIBUTING.md).

### Site em localhost (venv + MkDocs)

No macOS/Linux, na pasta do clone do repositório:

1. **Criar o ambiente virtual** (só na primeira vez):

   ```bash
   python3 -m venv .venv
   ```

2. **Ativar o `.venv`** (em cada terminal novo antes de rodar `mkdocs` ou `pip`):

   ```bash
   source .venv/bin/activate
   ```

   O prompt costuma mostrar `(.venv)`. Para sair depois: `deactivate`.

3. **Instalar dependências** (Python 3.10+ recomendado):

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Ver o site no browser** (recarrega ao salvar os `.md`):

   ```bash
   mkdocs serve
   ```

   Abra a URL que aparecer (em geral `http://127.0.0.1:8000`).

5. **Só gerar HTML estático** (pasta `site/`):

   ```bash
   mkdocs build
   ```

### Verificar links (local)

Antes de abrir um PR, rode o mesmo check que o GitHub Actions usa:

```bash
./scripts/check-links.sh
```

Precisa do [lychee](https://github.com/lycheeverse/lychee) no PATH.

No GitHub Actions, o workflow **Check links** roda em cada PR/push na `main`, para evitar que links quebrados entrem por engano, e também uma vez por dia (cron job).

Outro workflow diário abre (possivelmente) **um PR normal por link** com falha (corpo do PR em inglês; você pode fechar o PR se não fizer sentido): `.github/workflows/broken-links-prs.yml`.

Pull Requests abertos por mais de **`STALE_AUTOMATED_LINK_PR_MAX_DAYS`** dias fecham automaticamente usando `.github/workflows/close-stale-link-prs.yml`.