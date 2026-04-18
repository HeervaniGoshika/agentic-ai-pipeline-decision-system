class SelfCorrectionAgent:

    def evaluate(self, risk, confidence):
        
        # 🔥 If confidence low → trigger correction
        if confidence < 0.6:
            return True
        
        return False

    def correct(self, risk):
        # Simple correction logic (can be improved later)
        
        if risk > 0.8:
            return risk * 0.95
        elif risk < 0.2:
            return risk * 1.05
        
        return risk