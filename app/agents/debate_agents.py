class SafetyAgent:

    def argue(self, risk):
        if risk > 0.6:
            return "Risk is high. Immediate repair is safest to avoid failure."
        elif risk > 0.4:
            return "Moderate risk. Inspection is needed soon."
        else:
            return "Risk is low. Monitoring is acceptable."


class CostAgent:

    def argue(self, risk, repair_cost=None, downtime=None):
        if repair_cost and repair_cost > 15000:
            return "Repair cost is high. Avoid immediate repair unless critical."
        
        if risk < 0.5:
            return "Risk is manageable. Monitoring or inspection saves cost."
        
        return "Balanced approach needed to minimize cost and risk."


class ModeratorAgent:

    def decide(self, risk, safety_opinion, cost_opinion):

        if risk > 0.7:
            decision = "Immediate Repair"
        elif risk > 0.4:
            decision = "Schedule Inspection"
        else:
            decision = "Monitor"

        '''explanation = f"""
Safety Perspective: {safety_opinion}

Cost Perspective: {cost_opinion}

Final Decision: {decision} based on balanced risk and cost.
"""'''
        explanation = (
            f"Safety Perspective: {safety_opinion}\n"
            f"Cost Perspective: {cost_opinion}\n"
            f"Final Decision: {decision} based on balanced risk and cost."
        )

        return decision, explanation