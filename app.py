import streamlit as st
import google.generativeai as genai
from pathlib import Path
import os
from typing import Optional

# Configuração da página
st.set_page_config(
    page_title="🚀 AI Prompt Generator",
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

def configure_gemini(api_key: str) -> bool:
    """Configura a API do Gemini"""
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        st.error(f"Erro ao configurar Gemini: {e}")
        return False

def generate_prompt(project_idea: str, code_snippets: str, guide_content: str, api_key: str) -> Optional[str]:
    """Gera o prompt otimizado usando Gemini"""
    try:
        if not configure_gemini(api_key):
            return None
            
        model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-06-17')
        
        system_prompt = f"""
Você é um especialista em engenharia de prompts. Sua tarefa é criar prompts otimizados e eficazes.

GUIA DE BOAS PRÁTICAS:
{guide_content}

Com base no guia acima e nas informações fornecidas pelo usuário, crie um prompt otimizado que:

1. Seja claro e específico
2. Forneça contexto adequado
3. Inclua instruções detalhadas
4. Defina o formato de saída esperado
5. Considere possíveis edge cases
6. Somente responda com o prompt otimizado, sem explicações adicionais

INFORMAÇÕES DO PROJETO:
Ideia do Projeto: {project_idea}

CÓDIGO/TRECHOS FORNECIDOS:
{code_snippets if code_snippets else "Nenhum código fornecido"}

Gere um prompt profissional e otimizado que ajudará o usuário a alcançar seus objetivos de forma eficaz.
"""

        response = model.generate_content(system_prompt)
        return response.text
        
    except Exception as e:
        st.error(f"Erro ao gerar prompt: {e}")
        return None

def main():
    # Header principal
    st.markdown("""
    <div class="main-header">
        <h1>🚀 AI Prompt Generator</h1>
        <p>Transforme suas ideias em prompts otimizados e eficazes</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar para configurações
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        # Campo para API Key
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
        
        # Informações sobre o app
        st.header("📋 Como usar")
        st.markdown("""
        1. **Insira sua API Key** do Google Gemini
        2. **Descreva seu projeto** na área principal
        3. **Adicione código** (opcional) para contexto
        4. **Clique em Gerar** para criar seu prompt otimizado
        """)
        
        st.divider()
        
        # Link para obter API Key
        st.markdown("""
        ### 🔗 Links Úteis
        - [Obter API Key Gemini](https://makersuite.google.com/app/apikey)
        - [Documentação Gemini](https://ai.google.dev/docs)
        """)

    # Conteúdo principal
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("💡 Describe seu Projeto")
        
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
        
        # Opção de upload de arquivo
        uploaded_file = st.file_uploader(
            "Ou faça upload de um arquivo de código",
            type=['py', 'js', 'html', 'css', 'json', 'md', 'txt'],
            help="Formatos suportados: Python, JavaScript, HTML, CSS, JSON, Markdown, TXT"
        )
        
        if uploaded_file is not None:
            try:
                file_content = uploaded_file.read().decode('utf-8')
                st.text_area(
                    f"Conteúdo do arquivo: {uploaded_file.name}",
                    value=file_content,
                    height=100,
                    disabled=True
                )
                code_snippets += f"\n\n--- Arquivo: {uploaded_file.name} ---\n{file_content}"
            except Exception as e:
                st.error(f"Erro ao ler arquivo: {e}")

    with col2:
        st.header("✨ Prompt Gerado")
        
        if st.button("🚀 Gerar Prompt Otimizado", type="primary", use_container_width=True):
            if not api_key:
                st.error("⚠️ Por favor, insira sua API Key do Gemini na sidebar")
            elif not project_idea.strip():
                st.error("⚠️ Por favor, descreva sua ideia de projeto")
            else:
                with st.spinner("🔄 Gerando prompt otimizado..."):
                    guide_content = load_guide()
                    generated_prompt = generate_prompt(project_idea, code_snippets, guide_content, api_key)
                    
                    if generated_prompt:
                        st.markdown('<div class="generated-prompt">', unsafe_allow_html=True)
                        st.markdown("### 📝 Seu Prompt Otimizado:")
                        st.markdown(generated_prompt)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Botão para copiar
                        st.code(generated_prompt, language=None)
                        
                        # Opção de download
                        st.download_button(
                            label="💾 Download do Prompt",
                            data=generated_prompt,
                            file_name="prompt_otimizado.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error("❌ Erro ao gerar o prompt. Verifique sua API Key e tente novamente.")

    # Footer
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 2rem;">
        <p>🤖 Powered by Google Gemini | 🛠️ Built with Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()