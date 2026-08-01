import anthropic
import os
import base64

def scan_food_for_allergens(image_path, my_allergens):
    with open(image_path, "rb") as image_file:
        image_data = base64.standard_b64encode(image_file.read()).decode("utf-8")

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {
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
                        "text": f"Look at this food photo. List every ingredient or component you can identify. Then check if any of these allergens are present or likely present: {my_allergens}. Be clear about what you see and flag any allergen risks."
                    }
                ],
            }
        ],
    )
    return message.content[0].text

my_allergens = ["peanuts", "tree nuts", "shellfish", "dairy", "eggs"]

result = scan_food_for_allergens("test_food.jpg", my_allergens)
print(result)