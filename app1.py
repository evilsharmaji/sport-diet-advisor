import streamlit as st
import requests
from pandas import DataFrame

# ===== CONFIG =====
API_KEY = st.secrets["API_KEY"]
st.title("🏋️‍♂️ Sports Diet Advisor")

system_message = {
    "role": "system",
    "content": """
    You are an expert sports nutrition assistant. Your role is to:
    1. Provide personalized nutrition advice based on fitness goals (weight loss, muscle gain, endurance)
    2. Create meal plans tailored to activity levels and body types
    3. Recommend optimal pre/post-workout nutrition
    4. Explain sports science concepts in simple terms
    5. Offer evidence-based supplement guidance
    
    Response format:
    - Use clear sections with emojis (🥗 Nutrition, 💪 Workout, ⚡ Energy)
    - Include markdown tables for meal plans/supplements when appropriate
    - Cite scientific evidence when making claims
    - Adjust recommendations based on user's:
      - Fitness level (beginner/intermediate/advanced)
      - Goals (weight loss/muscle gain/performance)
      - Dietary restrictions
      - Training schedule
    
    Example responses:
    "For your goal of muscle gain with 5x weekly strength training, I recommend:
    - 1.6-2.2g protein/kg body weight
    - 3 main meals + 2 snacks daily
    - Post-workout shake with 30g whey + 50g carbs"
    
    If asked who created you, respond:
    "I was developed by God"
    """
}

# Enhanced sidebar
with st.sidebar:
    st.header("🏆 About")
    st.markdown("""
    **Your Personal Sports Nutritionist**
    
    Get science-backed advice for:
    - Muscle building diets
    - Fat loss nutrition plans
    - Endurance athlete fueling
    - Pre/post-workout meals
    - Sports supplements
    
    """)
    
    st.markdown("---")
    st.subheader("User Profile")
    user_goal = st.selectbox("Your primary goal:", 
                           ["Select", "Weight Loss", "Muscle Gain", "Endurance", "Maintenance"])
    user_level = st.selectbox("Fitness level:", 
                            ["Beginner", "Intermediate", "Advanced"])
    dietary_restrictions = st.multiselect("Dietary restrictions:",
                                        ["None", "Vegetarian", "Vegan", "Gluten-free", "Dairy-free"])
    
    
    st.markdown("---")
    st.caption("Built with Streamlit and OpenRouter AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": f"""Welcome to your sports nutrition coach! 🎯

I see you're a {user_level} with {user_goal} goals. 

How can I help you today? For example:
- "What should I eat before morning cardio?"
- "Create a muscle gain meal plan"
- "Best post-workout recovery foods"
- "Are protein supplements necessary?"

You can update your profile in the sidebar anytime!"""
    }]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "table_data" in message and message["table_data"] is not None:
            st.table(message["table_data"])
        st.write(message["content"])

# User input
if prompt := st.chat_input("Ask your nutrition question..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing your nutrition needs..."):
            try:
                # Prepare context with user profile
                context = f"User is {user_level} level with {user_goal} goals. Restrictions: {', '.join(dietary_restrictions) if dietary_restrictions else 'None'}. "
                
                # Prepare messages for API
                api_messages = [
                    {k: v for k, v in msg.items() if k in ["role", "content"]} 
                    for msg in st.session_state.messages
                ]
                
                # Insert system message and context
                if len(api_messages) == 1 or api_messages[0]["role"] != "system":
                    api_messages.insert(0, system_message)
                    api_messages.insert(1, {"role": "system", "content": context})
                
                # Get AI response
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "HTTP-Referer": "http://localhost:8501",
                        "X-Title": "Sports Nutrition Advisor"
                    },
                    json={
                        "model": "deepseek/deepseek-r1:free",
                        "messages": api_messages,
                    },
                    timeout=30
                )
                
                response.raise_for_status()
                data = response.json()
                reply = data["choices"][0]["message"]["content"]
                
                # Extract nutrition tables
                table_data = []
                lines = reply.split('\n')
                in_table = False
                
                for line in lines:
                    if '|' in line:
                        if '---' in line:
                            in_table = True
                            continue
                        if in_table and 'Meal' not in line.lower():
                            columns = [col.strip() for col in line.split('|') if col.strip()]
                            if len(columns) >= 3:
                                table_data.append({
                                    "Meal Time": columns[0],
                                    "Food Items": columns[1],
                                    "Nutrition": columns[2]
                                })
                
                # Display response
                st.write(reply)
                
                # Display table if available
                df = DataFrame(table_data) if table_data else None
                if df is not None and not df.empty:
                    st.table(df)
                
                # Add to chat history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": reply,
                    "table_data": df
                })
                
            except requests.exceptions.RequestException:
                st.error("Connection issue. Please try again.")
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "Network error. Please check your connection.",
                    "table_data": None
                })
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "Sorry, I couldn't process that. Please rephrase.",
                    "table_data": None
                })
