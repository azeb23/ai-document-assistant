
import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Document Assistant")
st.write("Analyze architecture project documents using local AI.")

uploaded_file = st.file_uploader(
    "Upload a project document",
    type=["txt"]

)

if uploaded_file is not None:
    document_text = uploaded_file.getvalue().decode("utf-8")

    st.success("Document uploaded successfully!")

    with st.expander("View Document"):
        st.text_area(
            "Document Content",
            document_text,
            height=200
        )

    if st.button("Summarize Document"):
        with st.spinner("AI is analyzing your document..."):
            try:
                response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an assistant for architecture "
                                "project managers. Summarize only facts "
                                "found in the provided document. "
                                "Do not invent information."
                            )
                        },
                        {
                            "role": "user",
                            "content": (
                                "Summarize this project document:\n\n"
                                + document_text
                            )
                        }
                    ]
                )

                st.subheader("AI Summary")
                st.write(response["message"]["content"])

            except Exception as error:
                st.error(f"AI connection error: {error}")

    st.subheader("Ask Questions About the Document")

    question = st.text_input(
        "Enter your question",
        placeholder="What is the project budget?"
    )

    if st.button("Ask AI"):
        if question.strip():
            with st.spinner("AI is finding an answer..."):
                try:
                    response = ollama.chat(
                        model="llama3.2:1b",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "Answer questions using only the "
                                    "provided project document. "
                                    "If the answer is not in the document, "
                                    "say that the information is unavailable."
                                )
                            },
                            {
                                "role": "user",
                                "content": (
                                    "Document:\n"
                                    + document_text
                                    + "\n\nQuestion: "
                                    + question
                                )
                            }
                        ]
                    )

                    st.subheader("AI Answer")
                    st.write(response["message"]["content"])

                except Exception as error:
                    st.error(f"AI connection error: {error}")
                    
        else:
            st.warning("Please enter a question.")
