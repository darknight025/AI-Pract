class ExpertSystem:
    def __init__(self):
        self.rules = {
            'critical_condition': {
                'symptoms': ['difficulty_breathing', 'unconsciousness', 'severe_bleeding'],
                'response': "I'm sorry to hear that. This sounds like a critical condition. Please call emergency services immediately."
            },
            'fever': {
                'symptoms': ['fever'],
                'response': 'It seems like the patient has a fever. It is advisable to consult with the general medicine department.'
            },
            'chest_pain': {
                'symptoms': ['chest_pain'],
                'response': 'Chest pain can be a serious symptom. Please consult with the cardiology department.'
            },
            # Add more rules for different conditions and departments
        }

    def infer_department(self, symptoms):
        for condition, data in self.rules.items():
            if any(symptom in data['symptoms'] for symptom in symptoms):
                return condition
        return None

class HospitalChatbot:
    def __init__(self, expert_system):
        self.expert_system = expert_system

    def chat(self):
        print("Hospital Management System Chatbot: Hello! How can I assist you today?")
        while True:
            user_input = input("You: ").lower()
            if user_input == 'exit':
                print("Hospital Management System Chatbot: Goodbye! Take care.")
                break

            symptoms = user_input.split(',')
            department = self.expert_system.infer_department(symptoms)

            if department:
                print(f"Hospital Management System Chatbot: {self.expert_system.rules[department]['response']}")
            else:
                print("Hospital Management System Chatbot: I'm sorry, I didn't understand. Can you please provide more information?")

if __name__ == "__main__":
    expert_system = ExpertSystem()
    hospital_chatbot = HospitalChatbot(expert_system)
    hospital_chatbot.chat()
