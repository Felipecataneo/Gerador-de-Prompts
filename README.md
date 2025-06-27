# 🚀 AI Prompt Generator

Um aplicativo Streamlit moderno para gerar prompts otimizados usando Google Gemini AI. Transforme suas ideias em prompts profissionais e eficazes com base em melhores práticas de engenharia de prompts.

## ✨ Funcionalidades

- 🤖 **Geração inteligente de prompts** usando Google Gemini
- 📚 **Guia integrado de boas práticas** para prompts eficazes
- 💻 **Upload de arquivos de código** para contexto adicional
- 🎨 **Interface moderna e intuitiva** com Streamlit
- 📋 **Templates prontos** para diferentes tipos de projeto
- 💾 **Download dos prompts gerados** em formato texto
- 🔒 **Configuração segura** de API key via sidebar

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Conta Google para obter API key do Gemini

### Passos de instalação

1. **Clone o repositório**
```bash
git clone https://github.com/Felipecataneo/Gerador-de-Prompts.git
cd promptgenerator-main
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Obtenha sua API Key do Google Gemini**
   - Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Faça login com sua conta Google
   - Crie uma nova API key
   - Copie a chave gerada

## 🚀 Como usar

1. **Execute o aplicativo**
```bash
streamlit run app.py
```

2. **Configure sua API Key**
   - Na sidebar, insira sua API Key do Google Gemini
   - A chave é armazenada apenas durante a sessão (não é salva)

3. **Descreva seu projeto**
   - Insira uma descrição detalhada do seu projeto
   - Seja específico sobre objetivos, funcionalidades e público-alvo

4. **Adicione contexto (opcional)**
   - Cole trechos de código relevantes
   - Ou faça upload de arquivos de código
   - Formatos suportados: `.py`, `.js`, `.html`, `.css`, `.json`, `.md`, `.txt`

5. **Gere o prompt**
   - Clique em "Gerar Prompt Otimizado"
   - Aguarde o processamento
   - Copie ou baixe o prompt gerado

## 📁 Estrutura do projeto

```
ai-prompt-generator/
├── app.py              # Aplicação principal Streamlit
├── guide.md            # Guia de boas práticas para prompts
├── requirements.txt    # Dependências Python
└── README.md          # Documentação
```

## 🎯 Casos de uso

### Desenvolvimento de Software
- Geração de código
- Revisão e otimização
- Documentação técnica
- Resolução de bugs

### Análise de Dados
- Exploração de datasets
- Criação de visualizações
- Relatórios automatizados
- Insights de negócio

### Criação de Conteúdo
- Artigos e blogs
- Materiais educacionais
- Descrições de produtos
- Campanhas de marketing

### Automação
- Scripts de automação
- Workflows
- Integração de sistemas
- Processamento de dados

## 🔧 Configuração avançada

### Variáveis de ambiente (opcional)
Você pode definir a API key como variável de ambiente:

```bash
export GOOGLE_API_KEY="sua-api-key-aqui"
```

### Customização do guia
Edite o arquivo `guide.md` para adicionar suas próprias melhores práticas e templates específicos do seu domínio.

## 📋 Exemplos de uso

### Exemplo 1: Desenvolvimento Web
**Entrada:**
```
Projeto: Sistema de e-commerce com carrinho de compras
Tecnologias: React, Node.js, MongoDB
Funcionalidades: Catálogo de produtos, carrinho, checkout, pagamentos
```

**Saída:** Prompt otimizado para gerar código completo do sistema

### Exemplo 2: Análise de Dados
**Entrada:**
```
Projeto: Dashboard de vendas com métricas KPI
Dados: CSV com vendas dos últimos 2 anos
Visualizações: Gráficos de tendência, mapas de calor, métricas principais
```

**Saída:** Prompt para criar dashboard interativo com análises

## ⚠️ Limitações

- Requer conexão com internet para usar a API do Gemini
- API key necessária (pode ter custos associados)
- Limitações de rate limiting da API do Google
- Tamanho máximo de upload de arquivos: 200MB

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se você encontrar problemas ou tiver dúvidas:

1. Verifique se sua API key está correta
2. Confirme que todas as dependências foram instaladas
3. Consulte a [documentação do Gemini](https://ai.google.dev/docs)
4. Abra uma issue no repositório

## 🙏 Agradecimentos

- [Streamlit](https://streamlit.io/) pela framework de interface
- [Google Gemini](https://ai.google.dev/) pela API de IA
- Comunidade open source pelas inspirações e melhores práticas

---

**Desenvolvido com ❤️ para a comunidade de desenvolvedores**