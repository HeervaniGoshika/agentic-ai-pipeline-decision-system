'''from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ExplanationAgent:

    def explain(self, input_data, risk, action):

        prompt = f"""
You are an expert Oil & Gas Maintenance Analyst.

Given the following pipeline data:
{input_data}

Predicted Failure Risk: {risk:.2f}
Recommended Action: {action}

Explain:
1. Why this risk level occurred
2. Why this action is appropriate
3. What could happen if ignored

Keep it simple, practical, and business-focused.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content'''
    
# OPENAI_API_KEY exceeded

'''from openai import OpenAI
import os

client = OpenAI()  # ✅ no need to pass api_key manually


class ExplanationAgent:

    def explain(self, input_data, risk, action):

        prompt = f"""
You are an expert Oil & Gas Maintenance Analyst.

Given the following pipeline data:
{input_data}

Predicted Failure Risk: {risk:.2f}
Recommended Action: {action}

Explain:
1. Why this risk level occurred
2. Why this action is appropriate
3. What could happen if ignored

Keep it simple and practical.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content'''

# 🔥 Add Offline Explanation Agent

from openai import OpenAI
import os

client = OpenAI() 
class ExplanationAgent:

    def explain(self, input_data, risk, action):

        try:
            from openai import OpenAI
            client = OpenAI()

            prompt = f"""
You are an expert Oil & Gas Maintenance Analyst.

Data: {input_data}
Risk: {risk:.2f}
Action: {action}

Explain briefly why this decision was made.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            return response.choices[0].message.content

        except Exception as e:
            print("LLM Error:", e)

            # 🔥 OFFLINE FALLBACK (IMPORTANT)
            return self.rule_based_explanation(input_data, risk, action)

    def rule_based_explanation(self, input_data, risk, action):

        explanation = f"Risk level is {risk:.2f}. "

        if risk > 0.7:
            explanation += "High corrosion or pressure likely detected. Immediate repair is required to avoid failure."
        elif risk > 0.4:
            explanation += "Moderate risk detected. Scheduling inspection helps prevent future damage."
        else:
            explanation += "Low risk. System can be monitored without immediate action."

        return explanation