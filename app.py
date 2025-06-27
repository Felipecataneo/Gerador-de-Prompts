import streamlit as st
import google.generativeai as genai
from pathlib import Path
import os
from typing import Optional

# Configuração da página
st.set_page_config(
    page_title="AI Prompt Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para deixar o app mais moderno
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .stTextArea textarea {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 8px;
    }
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
    .generated-prompt {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin-top: 1rem;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def load_guide() -> str:
    """Carrega o guia de boas práticas do arquivo guide.md"""
    try:
        guide_path = Path("guide.md")
        if guide_path.exists():
            return guide_path.read_text(encoding='utf-8')
        else:
            return """
# Guia de Boas Práticas para Prompts

## Princípios Fundamentais
- Seja específico e claro
- Forneça contexto suficiente
- Use exemplos quando apropriado
- Defina o formato de saída desejado

## Estrutura Recomendada
1. Contexto e objetivo
2. Instruções específicas
3. Exemplos (se necessário)
4. Formato de saída
5. Restrições ou considerações especiais
"""
    except Exception as e:
        st.error(f"Erro ao carregar o guia: {e}")
        return ""

def process_uploaded_files(uploaded_files):
    """Processa múltiplos arquivos enviados e retorna conteúdo estruturado"""
    if not uploaded_files:
        return "", []
    
    processed_files = []
    total_content = ""
    
    for file in uploaded_files:
        try:
            file_content = file.read().decode('utf-8')
            file_info = {
                'name': file.name,
                'size': len(file_content),
                'type': file.name.split('.')[-1].lower() if '.' in file.name else 'txt',
                'content': file_content
            }
            processed_files.append(file_info)
            total_content += f"\n\n--- ARQUIVO: {file.name} ---\n{file_content}"
            file.seek(0)
        except Exception as e:
            st.error(f"❌ Erro ao processar {file.name}: {e}")
    
    return total_content, processed_files

# <<<<<<<<<<<<<<<< FIX #1: A FUNÇÃO configure_gemini ESTAVA NO LUGAR ERRADO >>>>>>>>>>>>>>>>
def configure_gemini(api_key: str) -> bool:
    """Configura a API do Gemini"""
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        st.error(f"Erro ao configurar Gemini: {e}")
        return False

def generate_prompt(project_idea: str, code_snippets: str, guide_content: str, api_key: str, file_count: int = 0) -> Optional[str]:
    """Gera o prompt otimizado usando Gemini"""
    try:
        # A chamada para configure_gemini agora funciona
        if not configure_gemini(api_key):
            return None
            
        model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-06-17') # Usando um modelo estável
        
        file_context = ""
        if file_count > 0:
            file_context = f"\n\nO usuário forneceu {file_count} arquivo(s) de código como contexto adicional. Use essas informações para criar um prompt mais específico e contextualizado."
        
        system_prompt = f"""
Você é um especialista em engenharia de prompts com vasta experiência em desenvolvimento de software e IA. Sua tarefa é criar prompts otimizados, profissionais e extremamente eficazes.

GUIA DE BOAS PRÁTICAS:
{guide_content}

CONTEXTO DO PROJETO:
Ideia/Objetivo: {project_idea}

CÓDIGO E ARQUIVOS FORNECIDOS:
{code_snippets if code_snippets else "Nenhum código fornecido"}{file_context}

INSTRUÇÕES PARA CRIAÇÃO DO PROMPT:

1. **ANÁLISE PRIMEIRO**: Analise cuidadosamente a ideia do projeto e os arquivos fornecidos para entender:
   - O contexto técnico e domínio
   - As tecnologias sendo utilizadas
   - A complexidade e escopo do projeto
   - Possíveis desafios e necessidades específicas

2. **ESTRUTURE O PROMPT** seguindo as melhores práticas:
   - Contexto claro e específico
   - Papel/persona adequado para a tarefa
   - Instruções detalhadas e organizadas
   - Formato de saída bem definido
   - Exemplos quando apropriado
   - Restrições e considerações importantes

3. **OTIMIZE PARA RESULTADOS**: O prompt deve ser:
   - Específico o suficiente para evitar ambiguidades
   - Completo para cobrir todos os aspectos necessários
   - Estruturado para facilitar a compreensão
   - Prático e acionável

4. **CONSIDERE O CONTEXTO TÉCNICO**: Se arquivos de código foram fornecidos:
   - Referencie tecnologias específicas encontradas
   - Considere padrões de código e arquitetura
   - Inclua detalhes técnicos relevantes
   - Mantenha consistência com o stack tecnológico

Crie um prompt profissional, detalhado e otimizado que maximize as chances de obter resultados excepcionais para este projeto específico, somente responda com o prompt otimizado, sem explicações adicionais.
"""

        response = model.generate_content(system_prompt)
        return response.text
        
    except Exception as e:
        st.error(f"Erro ao gerar prompt: {e}")
        return None

def main():
    st.markdown("""
    <div class="main-header">
        <h1>🚀 AI Prompt Generator</h1>
        <p>Transforme suas ideias em prompts otimizados e eficazes</p>
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.header("⚙️ Configurações")
        api_key = st.text_input(
            "🔑 Google Gemini API Key",
            type="password",
            help="Insira sua chave de API do Google Gemini"
        )
        if api_key:
            st.markdown('<div class="success-message">✅ API Key configurada!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error-message">⚠️ API Key necessária para funcionar</div>', unsafe_allow_html=True)
        st.divider()
        st.header("📋 Como usar")
        st.markdown("""
        1. **Insira sua API Key** do Google Gemini
        2. **Descreva seu projeto** na área principal
        3. **Adicione código** (opcional) para contexto
        4. **Clique em Gerar** para criar seu prompt otimizado
        """)
        st.divider()
        st.markdown("""
        ### 🔗 Links Úteis
        - [Obter API Key Gemini](https://makersuite.google.com/app/apikey)
        - [Documentação Gemini](https://ai.google.dev/docs)
        """)

    # <<<<<<<<<<<<<<<< FIX #2: RENOMEEI AS COLUNAS PRINCIPAIS PARA EVITAR CONFLITO >>>>>>>>>>>>>>>>
    main_col1, main_col2 = st.columns([1.2, 0.8])
    
    with main_col1:
        st.header("💡 Descreva seu Projeto")
        
        project_idea = st.text_area(
            "Ideia do Projeto",
            placeholder="Descreva seu projeto, objetivo, funcionalidades desejadas, público-alvo, etc...",
            height=200,
            help="Seja o mais específico possível sobre o que você quer criar"
        )
        
        st.header("💻 Código (Opcional)")
        
        code_snippets = st.text_area(
            "Trechos de Código ou Arquivos",
            placeholder="Cole aqui trechos do seu código, estruturas, APIs que você está usando, etc...",
            height=150,
            help="Adicione código existente para dar mais contexto ao prompt"
        )
        
        st.subheader("📁 Upload de Arquivos")
        
        if 'clear_files' not in st.session_state:
            st.session_state.clear_files = False
            
        # <<<<<<<<<<<<<<<< FIX #2: USEI NOMES DE VARIÁVEIS ÚNICOS PARA AS COLUNAS ANINHADAS >>>>>>>>>>>>>>>>
        uploader_col, button_col = st.columns([3, 1])
        with uploader_col:
            uploaded_files = st.file_uploader(
                "Faça upload de arquivos de código",
                type=['py', 'js', 'html', 'css', 'json', 'md', 'txt', 'jsx', 'ts', 'tsx', 'php', 'java', 'cpp', 'c', 'sql', 'yaml', 'yml', 'xml', 'sh', 'bat'],
                accept_multiple_files=True,
                help="Formatos suportados: Python, JavaScript, HTML, CSS, JSON, Markdown, TypeScript, PHP, Java, C++, SQL, YAML, XML, Shell e outros",
                key="file_uploader"
            )
        
        with button_col:
            if uploaded_files:
                if st.button("🗑️ Limpar", help="Remover todos os arquivos", use_container_width=True):
                    st.session_state.clear_files = True
                    st.rerun()
        
        uploaded_content = ""
        if uploaded_files:
            uploaded_content, processed_files = process_uploaded_files(uploaded_files)
            
            st.markdown("---")
            st.subheader(f"📊 Resumo: {len(processed_files)} arquivo(s) carregado(s)")
            
            stat_col1, stat_col2, stat_col3 = st.columns(3)
            with stat_col1:
                st.metric("Arquivos", len(processed_files))
            with stat_col2:
                total_chars = sum(f['size'] for f in processed_files)
                st.metric("Caracteres", f"{total_chars:,}")
            with stat_col3:
                types = set(f['type'] for f in processed_files)
                st.metric("Tipos", len(types))
            
            if len(processed_files) <= 10:
                with st.expander("📁 Detalhes dos arquivos", expanded=True):
                    for i, file_info in enumerate(processed_files):
                        file_name_col, file_type_col, file_size_col = st.columns([3, 1, 1])
                        with file_name_col:
                            st.write(f"📄 **{file_info['name']}**")
                        with file_type_col:
                            st.write(f"`{file_info['type']}`")
                        with file_size_col:
                            st.write(f"{file_info['size']:,} chars")
                        
                        if file_info['size'] > 0:
                            preview = file_info['content'][:200] + ("..." if len(file_info['content']) > 200 else "")
                            st.code(preview, language=file_info['type'])
                        
                        if i < len(processed_files) - 1:
                            st.divider()
            else:
                with st.expander(f"📋 Lista de {len(processed_files)} arquivos"):
                    files_by_type = {}
                    for file_info in processed_files:
                        file_type = file_info['type']
                        if file_type not in files_by_type:
                            files_by_type[file_type] = []
                        files_by_type[file_type].append(file_info)
                    
                    for file_type, files in files_by_type.items():
                        st.write(f"**📁 {file_type.upper()} ({len(files)} arquivos)**")
                        for file_info in files:
                            st.write(f"  • {file_info['name']} ({file_info['size']:,} chars)")
                        st.write("")
        
        if uploaded_content:
            code_snippets = code_snippets + uploaded_content

    with main_col2:
        st.header("✨ Prompt Gerado")
        
        # Movi a área de resultado para fora do botão para manter o layout
        result_area = st.container()

        if st.button("🚀 Gerar Prompt Otimizado", type="primary", use_container_width=True):
            if not api_key:
                st.error("⚠️ Por favor, insira sua API Key do Gemini na sidebar")
            elif not project_idea.strip():
                st.error("⚠️ Por favor, descreva sua ideia de projeto")
            else:
                with st.spinner("🔄 Gerando prompt otimizado..."):
                    guide_content = load_guide()
                    file_count = len(uploaded_files) if uploaded_files else 0
                    generated_prompt = generate_prompt(project_idea, code_snippets, guide_content, api_key, file_count)
                    
                    if generated_prompt:
                        with result_area:
                            st.markdown('<div class="generated-prompt">', unsafe_allow_html=True)
                            st.markdown("### 📝 Seu Prompt Otimizado:")
                            st.markdown(generated_prompt)
                            st.markdown('</div>', unsafe_allow_html=True)
                            st.code(generated_prompt, language=None)
                            st.download_button(
                                label="💾 Download do Prompt",
                                data=generated_prompt,
                                file_name="prompt_otimizado.txt",
                                mime="text/plain"
                            )
                    else:
                        st.error("❌ Erro ao gerar o prompt. Verifique sua API Key e tente novamente.")

    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 2rem;">
        <p>🤖 Powered by Google Gemini | 🛠️ Built with Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()