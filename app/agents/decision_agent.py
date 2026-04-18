'''class DecisionAgent:

    def decide(self, risk):
        if risk > 0.7:
            return "Immediate Repair"
        elif risk > 0.4:
            return "Schedule Inspection"
        else:
            return "Monitor"'''

class DecisionAgent:

    def decide(self, risk, repair_cost=None, downtime=None):

        if risk > 0.7:
            if repair_cost and downtime:
                if repair_cost < downtime * 1000:
                    return "Immediate Repair"
            return "Immediate Repair"

        elif risk > 0.4:
            return "Schedule Inspection"

        else:
            return "Monitor"