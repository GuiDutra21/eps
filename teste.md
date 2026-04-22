| ID | Requisito | Descrição | Priorização |
|----|------------|-----------|-------------|
| RF01| Ingestão Documental | Suporte à leitura e extração de texto de arquivos PDF (incluindo PDFs de imagem via OCR) e DOCX. | Must Have |
| RF02 | Extração de Entidades (NER) | Identificação automática e listagem de Nomes, CPFs, Locais, Organizações e Datas citadas. | Must Have |
| RF03 | Análise de Contradições | Comparação entre documentos (Ex: Depoimento 1 vs. Depoimento 2) para destacar divergências em datas, horários ou locais. | Should Have |
| RF04 | Cronologia Automática | Geração de uma linha do tempo dos fatos baseada na narrativa dos documentos processados. | Should Have |
| RF05 | Resumo Executivo | Produção de sínteses curtas e objetivas, mantendo o contexto jurídico e técnico | Must Have |
| RF06 | Citação de Fonte | Cada afirmação gerada pela IA deve vir acompanhada de um link ou referência à página/parágrafo do documento original.| Should Have |
| RNF01 | Baixa Alucinação | Implementação de técnicas de RAG (Retrieval-Augmented Generation) para garantir que a IA responda apenas com base nos documentos fornecidos |  Must Have |
| RNF02 | Privacidade Total | O processamento não deve utilizar APIs públicas (como OpenAI) que usem dados para treinamento. Preferência por modelos Local-LLM ou instâncias privadas. | Must Have |
| RNF03 | Rastreabilidade | Logs de auditoria indicando qual usuário processou quais documentos, em conformidade com a LGPD. | Should Have |
| RNF04 | Performance | Capacidade de processar um documento de 50 páginas e gerar o resumo em até 30 segundos. | Should Have |
| RNF05 | Interoperabilidade |Exportação dos resultados em formatos compatíveis com os relatórios oficiais da PCDF (PDF e Markdown). | Should Have |
