# Documentos (`docs/*.html`)

Toda vez que finalizar a edição de um doc, rode o script python para converter para PDF (`uv run pdf-convert`).

## Padrão de escrita

- Nunca use travessão (`—`) nem meia-risca (`–`). Use vírgula na prosa e hífen (`-`) em títulos, legendas e pares nome/RA.
- Texto em maiúscula e minúscula. Nada de caixa alta: sem `text-transform: uppercase` no CSS e sem títulos escritos em CAPS.
- Português do Brasil, primeira pessoa do plural ("separamos", "pretendemos"), tom direto, sem jargão.
- Parágrafos justificados com recuo de 1,25 cm na primeira linha (regra `p` do template). Não use parágrafo de uma frase só quando o conteúdo pedir desenvolvimento.
- Seções primárias numeradas (`<h1>1 Título da seção</h1>`), subseções em `<h2>2.1 Título</h2>`. Sem quebra de página forçada por seção.
- Quadros e tabelas: título acima (`Quadro N - Descrição`), fonte abaixo (`Fonte: elaboração do grupo.`), corpo em 10pt, filete superior e inferior, sem bordas verticais.
- Figuras e diagramas: legenda abaixo (`Figura N - Descrição. Fonte: elaboração do grupo.`), construídos em HTML/CSS, sem imagem externa.
- Só inclua a seção `REFERÊNCIAS` se o texto tiver citação real. Nunca deixe entrada de referência fictícia ou placeholder `[...]` no doc entregue.
- Capa na ordem: instituição, curso, disciplina; integrantes com RA; título e subtítulo; cidade e mês/ano.
