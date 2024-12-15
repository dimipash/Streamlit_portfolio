import streamlit as st
from typing import List, Dict, Union
from data import PortfolioData

class Chatbot:
    """
    A simple chatbot that can answer questions about the portfolio content.
    """

    def __init__(self):
        """
        Initializes the chatbot with portfolio data.
        """
        self.skills_data = PortfolioData.get_skills_data()
        self.projects_data = PortfolioData.get_projects_data()
        self.soft_skills = PortfolioData.get_soft_skills()
        self.knowledge_base = self._build_knowledge_base()

    def _build_knowledge_base(self) -> Dict[str, str]:
        """
        Builds a knowledge base from the portfolio data.

        Returns:
            Dict[str, str]: A dictionary containing questions and their corresponding answers.
        """
        knowledge_base = {}

        # Skills
        for skill, data in self.skills_data.items():
            knowledge_base[f"What is your proficiency in {skill}?"] = f"My proficiency in {skill} is {data['proficiency']}%."
            knowledge_base[f"What category does {skill} belong to?"] = f"{skill} belongs to the {data['category']} category."
            knowledge_base[f"How many years of experience do you have in {skill}?"] = f"I have {data['experience_years']} years of experience in {skill}."

        # Soft Skills
        knowledge_base["What are your soft skills?"] = f"My soft skills are: {', '.join(self.soft_skills)}."

        # Projects
        for project in self.projects_data:
            knowledge_base[f"Tell me about the {project['name']} project."] = project['description']
            if "tech_stack" in project:
                knowledge_base[f"What technologies were used in the {project['name']} project?"] = f"The technologies used in the {project['name']} project are: {', '.join(project['tech_stack'])}."
            if "live_demo" in project:
                knowledge_base[f"Is there a live demo for the {project['name']} project?"] = f"Yes, you can view the live demo here: {project['live_demo']}"
            if "github_link" in project:
                knowledge_base[f"Is there a GitHub link for the {project['name']} project?"] = f"Yes, you can view the source code here: {project['github_link']}"

        return knowledge_base

    def _get_answer(self, question: str) -> str:
        """
        Retrieves an answer from the knowledge base based on the question.

        Args:
            question (str): The question asked by the user.

        Returns:
            str: The answer to the question, or a default message if not found.
        """
        question = question.strip()
        if question.lower() == "hello":
            return "Hello there! How can I help you today?"
        if question in self.knowledge_base:
            return self.knowledge_base[question]
        else:
            return "I'm sorry, I don't have an answer to that question."

    def display_chat(self) -> None:
        """
        Displays the chatbot interface in the Streamlit app.
        """
        st.markdown("<div id='chat'></div>", unsafe_allow_html=True)
        st.title("Chat with me! 💬")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_input = st.text_input("Your question:", key="user_input")

        if user_input:
            answer = self._get_answer(user_input)
            st.session_state.chat_history.append({"user": user_input, "bot": answer})

        for chat in st.session_state.chat_history:
            st.markdown(f"<p style='color: white;'>User: {chat['user']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: #00ff7f;'>Bot: {chat['bot']}</p>", unsafe_allow_html=True)
