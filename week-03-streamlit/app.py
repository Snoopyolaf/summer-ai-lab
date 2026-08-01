import streamlit as st
import anthropic
import os
import base64

# Page config
st.set_page_config(page_title="Allergen Scanner", page_icon="🥜")

# Title
st.title("🥜 Allergen Scanner")
st.write("Upload a photo of your food to check for allergens.")

# Allergen list
my_allergens = ["peanuts", "tree nuts", "shellfish", "dairy", "eggs", "wheat", "soy"]

# Call limit guardrail
if "call_count" not in st.session_state:
    st.session_state.call_count = 0

MAX_CALLS = 10

# Photo upload
photo = st.file_uploader("Upload a food photo", type=["jpg", "jpeg", "png"])

if photo is not None:
    st.image(photo, caption="Your food", width=300)

    if st.button("Scan for Allergens"):
        if st.session_state.call_count >= MAX_CALLS:
            st.error("Scan limit reached. Please restart the app.")
        else:
            with st.spinner("Scanning for allergens..."):
                photo.seek(0)
                image_data = base64.standard_b64encode(photo.read()).decode("utf-8")

                client = anthropic.Anthropic(
                    api_key=os.environ.get("ANTHROPIC_API_KEY")
                )

                message = client.messages.create(
                    model="claude-haiku-4-5",
                    max_tokens=1024,
                    messages=[{
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/jpeg",
                                    "data": image_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": f"Look at this food photo. Identify what food this is and list every ingredient or component you can see. Then check if any of these allergens are present, likely present, OR possibly present based on common recipes for this food type: {my_allergens}. When in doubt, flag it — this is a safety tool. Format your response with three sections: 1) What I see, 2) Allergens detected, 3) Recommendation."
                            }
                        ],
                    }]
                )

                st.session_state.call_count += 1
                result = message.content[0].text
                st.write(result)
                st.warning("⚠️ This AI analysis may not be 100% accurate. Always verify allergens with product packaging or a medical professional.")