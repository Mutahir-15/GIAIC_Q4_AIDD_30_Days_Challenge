**Project 01 — PDF Summarizer & Quiz Generator (Gemini + Streamlit + OpenAgents SDK)**
======================================================================================

🧠 **Overview**
---------------

This project implements an **AI Agent** using:

*   **OpenAgents SDK (Python)**
    
*   **Gemini API (google-generativeai)**
    
*   **PyPDF** for text extraction
    
*   **Streamlit** for the UI
    
*   **Context7 MCP** (already integrated)

*   **Storage** (lpain text files no database)
    

The agent processes a PDF, produces a high-quality summary, and generates MCQs or mixed-style quizzes from the original PDF content.

🎯 **Primary Goals**
====================

1.  Allow the user to **upload a PDF**.
    
2.  Extract text using **PyPDF**.
    
3.  Summarize the extracted text using **Gemini**.
    
4.  Display the summary in a clean UI component (card, container, block, etc.).
    
5.  Allow the user to generate quizzes directly from the PDF.
    
6.  Support:
    
    *   **MCQs**
        
    *   **Mixed-style quizzes**
        
7.  Maintain clean agent architecture following AIDD principles.
    

🗂 **High-Level Architecture**
==============================

`   project-1/  │  ├── app.py                     # Streamlit UI  ├── agent/  │   ├── __init__.py  │   ├── agent.py               # Agent orchestration logic  │   ├── extractor.py           # PDF text extraction  │   ├── summarizer.py          # Gemini summarization  │   ├── quiz_generator.py      # Gemini quiz generation  │  ├── specs/  │   └── gemini.md              # This specification  │  ├── utils/  │   └── helpers.py (optional)  │  ├── .env                       # GEMINI_API_KEY  └── requirements.txt   `

⚙️ **Technologies Required**
============================

ComponentPurpose**OpenAgents SDK**Agent orchestration**Gemini (google-generativeai)**Summaries + quizzes**PyPDF**Extract text from PDF**Streamlit**Simple web UI**Context7 MCP**Context management

🚀 **Features**
===============

**A) PDF Summarizer**
---------------------

### **User Workflow**

1.  User uploads a PDF.
    
2.  Agent extracts text using PyPDF (pages → text).
    
3.  Summarizer module sends content to Gemini.
    
4.  Gemini returns:
    
    *   Structured summary
        
    *   Short paragraphs
        
    *   Clean formatting
        
5.  UI displays the summary inside a styled component.
    

### **Functional Requirements**

IDRequirementSUM-01Extract PDF text using PyPDFSUM-02Send extracted text to Gemini modelSUM-03Generate concise paragraphsSUM-04Avoid hallucinationsSUM-05Support large PDFs (multi-page)SUM-06Show summary in Streamlit card/container

**B) Quiz Generator**
---------------------

### **User Workflow**

1.  After generating summary → user clicks **Create Quiz**.
    
2.  Agent reads **original PDF text** (not summary).
    
3.  Quiz module sends text to Gemini.
    
4.  Gemini generates:
    
    *   MCQs
        
    *   Or mixed quizzes
        
5.  Display in UI.
    

### **Functional Requirements**

IDRequirementQUIZ-01Use original extracted textQUIZ-02Generate at least 10 MCQsQUIZ-03Each MCQ must contain 4 optionsQUIZ-04Correct answer must be labeledQUIZ-05Support mixed question types (optional)QUIZ-06Show quizzes in readable format

🧩 **Modules Breakdown**
========================

**1\. extractor.py**
--------------------

*   Use PyPDF to read pages.
    
*   Extract text with fallback for missing content.
    

**Responsibilities**

*   Read PDF → return string.
    
*   Gracefully handle empty pages.
    
*   Normalize spacing.
    

**2\. summarizer.py (Gemini)**
------------------------------

Prompts must enforce:

*   Short meaningful summary
    
*   Avoid unnecessary sections
    
*   No markdown unless asked
    

**Responsibilities**

*   Initialize Gemini (gemini-1.5-flash)
    
*   Send structured prompt
    
*   Return clean summary
    

**3\. quiz\_generator.py (Gemini)**
-----------------------------------

Prompts must enforce:

*   10 MCQs
    
*   4 options
    
*   Identify correct answer
    
*   Clean formatting
    

**4\. agent.py**
----------------

Controls:

*   PDF extraction
    
*   Summary generation
    
*   Quiz generation
    
*   Routing functions for Streamlit UI
    

**5\. app.py (UI)**
-------------------

User-facing:

*   Upload PDF
    
*   Generate summary
    
*   Generate quiz
    
*   Local state stored in st.session\_state
    

🎨 **UI Requirements**
======================

*   Title: **PDF Summarizer + Quiz Generator**
    
*   PDF Upload (Streamlit uploader)
    
*   Button 1: "Generate Summary"
    
*   Output container:
    
    *   summary text
        
*   Button 2: "Create Quiz"
    
*   Output container:
    
    *   MCQs / mixed quiz
        
*   Must handle:
    
    *   Loading states
        
    *   Errors (missing PDF, Gemini key, empty PDF)
        

🧪 **Test Scenarios**
=====================

TestActionExpected OutputT-01Upload a normal PDFText extracted correctlyT-02SummarizeGood summary (2–5 paragraphs)T-03Generate quiz10 MCQs with answersT-04Large PDF (20+ pages)Works without crashingT-05No PDF uploadedShow Streamlit warning

🔐 **Environment Variables**
============================

In .env:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   GEMINI_API_KEY=your_api_key_here   `