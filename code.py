class Node:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def _init_(self):
        self.head = None
        self.tail = None

    def add_content_item(self, content_item):
        new_node = Node(content_item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search_content_item(self, name):
        current = self.head
        while current is not None:
            if current.data.name == name:
                return current.data
            current = current.next
        return None

    def display_content_items(self):
        current = self.head
        while current is not None:
            print(current.data.name)
            current = current.next

class Node_N:
    def _init_(self, data):
        self.data = data
        self.children = []

class NaryTree:
    def _init_(self):
        self.root = None

    def add_node(self, parent_data, child_data):
        if self.root is None:
            self.root = Node_N(parent_data)
            self.root.children.append(Node_N(child_data))
        else:
            self._add_node(self.root, parent_data, child_data)

    def _add_node(self, node, parent_data, child_data):
        if node.data == parent_data:
            node.children.append(Node_N(child_data))
        else:
            for child in node.children:
                self._add_node(child, parent_data, child_data)

class ContentItem:
    def _init_(self, name, textbooks, links):
        self.name = name
        self.textbooks = textbooks
        self.links = links

class RecommendationSystem:
    def _init_(self):
        self.category_tree = NaryTree()
        self.content_list = DoublyLinkedList()

    def add_category(self, parent_category, child_category):
        self.category_tree.add_node(parent_category, child_category)

    def add_content_item(self, name, textbooks, links):
        content_item = ContentItem(name, textbooks, links)
        self.content_list.add_content_item(content_item)

    def recommend_content(self, user_input, grade_input, subject_input):
    # Traverse the category tree to find the relevant content items
        self._traverse_category_tree(user_input, grade_input, subject_input)

    def _traverse_category_tree(self, user_input, grade_input, subject_input):
        if user_input == "High School":
            if grade_input == "10th" and subject_input == "Mathematics":
                self._recommend_content_items(["Algebra Textbook", "Calculus Textbook", "Linear Algebra Textbook"])
            elif grade_input == "10th" and subject_input == "Physics":
                self._recommend_content_items(["Physics Textbook", "Differential Equations Textbook"])
        elif user_input == "Intermediate":
            if grade_input == "Plus 1" and subject_input == "Mathematics":
                self._recommend_content_items(["Calculus Textbook", "Linear Algebra Textbook"])
            elif grade_input == "Plus 2" and subject_input == "Mathematics":
                self._recommend_content_items(["Differential Equations Textbook"])
        elif user_input == "UG":
            if grade_input == "1":
                if subject_input == "CSE":
                    self._recommend_content_items(["CAD", "System Essentials"])
                elif subject_input == "Mechanical":
                    self._recommend_content_items(["Single Variable Calculus", "Electrical & Electronic Circuits"])
                elif subject_input == "ECE":
                    self._recommend_content_items(["Basic Electrical and Electronics Engineering", "Electronic Devices and Circuits"])
            elif grade_input == "2" and subject_input == "CSE":
                self._recommend_content_items(["Advanced programming", "DATA STRUCTURES AND ALGORITHMS"])

    def _recommend_content_items(self, content_names):
        for name in content_names:
            content_item = self.search_content_by_name(name)
            if content_item:
                print(f"Name: {content_item.name}")
                print(f"Textbooks: {', '.join(content_item.textbooks)}")
                print(f"Links: {', '.join(content_item.links)}")
            else:
                print(f"No content found for '{name}'.")


    def display_all_content(self):
        self.content_list.display_content_items()

    def search_content_by_name(self, name):
        return self.content_list.search_content_item(name)


# Example usage
recommendation_system = RecommendationSystem()

# Add categories
recommendation_system.add_category("High School", "8th Grade")
recommendation_system.add_category("High School", "9th Grade")
recommendation_system.add_category("High School", "10th Grade")
recommendation_system.add_category("8th Grade", "Mathematics")
recommendation_system.add_category("8th Grade", "Physics")
recommendation_system.add_category("8th Grade", "Chemistry")
recommendation_system.add_category("8th Grade", "Biology")
recommendation_system.add_category("8th Grade", "Social Studies")
recommendation_system.add_category("8th Grade", "English")
recommendation_system.add_category("9th Grade", "Mathematics")
recommendation_system.add_category("9th Grade", "Physics")
recommendation_system.add_category("9th Grade", "Chemistry")
recommendation_system.add_category("9th Grade", "Biology")
recommendation_system.add_category("9th Grade", "Social Studies")
recommendation_system.add_category("9th Grade", "English")
recommendation_system.add_category("10th Grade", "Mathematics")
recommendation_system.add_category("10th Grade", "Physics")
recommendation_system.add_category("10th Grade", "Chemistry")
recommendation_system.add_category("10th Grade", "Biology")
recommendation_system.add_category("10th Grade", "Social Studies")
recommendation_system.add_category("10th Grade", "English")
recommendation_system.add_category("Intermediate", "Plus 1")
recommendation_system.add_category("Intermediate", "Plus 2")
recommendation_system.add_category("Plus 1", "Mathematics")
recommendation_system.add_category("Plus 1", "Physics")
recommendation_system.add_category("Plus 1", "Chemistry")
recommendation_system.add_category("Plus 2", "Mathematics")
recommendation_system.add_category("Plus 2", "Physics")
recommendation_system.add_category("Plus 2", "Chemistry")
recommendation_system.add_category("UG", "CSE")
recommendation_system.add_category("UG", "Mechanical")
recommendation_system.add_category("UG", "ECE")
recommendation_system.add_category("CSE", "Year 1")
recommendation_system.add_category("CSE", "Year 2")
recommendation_system.add_category("CSE", "Year 3")
recommendation_system.add_category("CSE", "Year 4")
recommendation_system.add_category("Year 1", "CAD")
recommendation_system.add_category("Year 1", "Manufacturing Lab")
recommendation_system.add_category("Year 1", "System Essentials")
recommendation_system.add_category("Year 1", "PSAT")
recommendation_system.add_category("Year 1", "Physics")
recommendation_system.add_category("Year 1", "UID")
recommendation_system.add_category("Year 2", "Advanced programming")
recommendation_system.add_category("Year 2", "PROGRAM REASONING")
recommendation_system.add_category("Year 2", "DATABASE MANAGEMENT SYSTEMS")
recommendation_system.add_category("Year 2", "OBJECT ORIENTED PARADIGM")
recommendation_system.add_category("Year 2", "DATA STRUCTURES AND ALGORITHMS")
recommendation_system.add_category("Year 2", "THEORY OF COMPUTATION")
recommendation_system.add_category("Year 2", "COMPUTER ORGANIZATION AND ARCHITECTURE")
recommendation_system.add_category("Year 2", "OPERATING SYSTEMS")
recommendation_system.add_category("Year 3", "MACHINE LEARNING")
recommendation_system.add_category("Year 3", "DESIGN AND ANALYSIS OF ALGORITHMS")
recommendation_system.add_category("Year 3", "COMPUTER NETWORKS")
recommendation_system.add_category("Year 3", "FOUNDATIONS OF DATA SCIENCE")
recommendation_system.add_category("Year 3", "EMBEDDED SYSTEMS")
recommendation_system.add_category("Year 3", "SOFTWARE ENGINEERING")
recommendation_system.add_category("Year 3", "PRINCIPLES OF PROGRAMMING LANGUAGES")
recommendation_system.add_category("Year 3", "DISTRIBUTED SYSTEMS")
recommendation_system.add_category("Year 4", "COMPILER DESIGN")
recommendation_system.add_category("Mechanical", "Year 1")
recommendation_system.add_category("Mechanical", "Year 2")
recommendation_system.add_category("Mechanical", "Year 3")
recommendation_system.add_category("Mechanical", "Year 4")
recommendation_system.add_category("Year 1", "Single Variable Calculus")
recommendation_system.add_category("Year 1", "Ordinary Differential Equation")
recommendation_system.add_category("Year 1", "Matrix Algebra")
recommendation_system.add_category("Year 1", "Electrical Engineering Practice")
recommendation_system.add_category("Year 1", "Electrical & Electronic Circuits")
recommendation_system.add_category("Year 1", "Digital Electronics")
recommendation_system.add_category("Year 1", "Fourier Transforms and Complex Analysis")
recommendation_system.add_category("Year 1", "Operating Systems")
recommendation_system.add_category("Year 2", "Electric Machines")
recommendation_system.add_category("Year 2", "Microelectronic Circuits")
recommendation_system.add_category("Year 2", "Sensors and Sensor Circuit Design")
recommendation_system.add_category("Year 2", "Computer Architecture")
recommendation_system.add_category("Year 3", "Machine Learning")
recommendation_system.add_category("Year 3", "Real Time Embedded Systems")
recommendation_system.add_category("Year 3", "Energy Systems")
recommendation_system.add_category("Year 3", "Embedded Digital Signal Processing")
recommendation_system.add_category("Year 3", "Power Electronics and Drives")
recommendation_system.add_category("Year 3", "Data Base Systems and Programming")
recommendation_system.add_category("Year 4", "Theory of Computation and Compiler Design")
recommendation_system.add_category("ECE", "Year 1")
recommendation_system.add_category("ECE", "Year 2")
recommendation_system.add_category("ECE", "Year 3")
recommendation_system.add_category("Year 1", "Biology for Engineers - A")
recommendation_system.add_category("Year 1", "Physics of Electronic Materials")
recommendation_system.add_category("Year 1", "Basic Electrical and Electronics Engineering")
recommendation_system.add_category("Year 1", "Introduction to Internet of Things")
recommendation_system.add_category("Year 1", "Electronic Devices and Circuits")
recommendation_system.add_category("Year 1", "Circuit Theory")
recommendation_system.add_category("Year 2", "Analog Electronic Circuits")
recommendation_system.add_category("Year 2", "Applied Electromagnetics")
recommendation_system.add_category("Year 2", "Digital Electronics and Systems")
recommendation_system.add_category("Year 2", "Signals and Systems")
recommendation_system.add_category("Year 2", "Analog Electronics Lab")
recommendation_system.add_category("Year 3", "Transmission Lines and Radiating Systems")
recommendation_system.add_category("Year 3", "Digital Signal Processing")
recommendation_system.add_category("Year 3", "Linear Integrated Circuits")
recommendation_system.add_category("Year 3", "Communication Theory")
recommendation_system.add_category("Year 3", "Linear Integrated Circuits Lab")


# Add content items
#9th grade 
recommendation_system.add_content_item("RS Agarwal Textbook", ["Mathematics for Class 10 by R.S. Aggarwal (Bharati Bhawan)"], ["https://byjus.com/rs-textbook"])
recommendation_system.add_content_item("Physics Textbook", ["Physics for Dummies"], ["https://toppr.com/physics-textbook"])
recommendation_system.add_content_item("Chemistry Textbook", ["Chemistry Essentials"], ["https://toppr.com/chemistry-textbook"])
recommendation_system.add_content_item("Biology Textbook", ["Biology Fundamentals"], ["https://toppr.com/biology-textbook"])
recommendation_system.add_content_item("Social Studies Textbook", ["World History"], ["https://toppr.com/social-studies-textbook"])
recommendation_system.add_content_item("English Textbook", ["Grammar and Composition"], ["https://byjus.com/english-textbook"])
recommendation_system.add_content_item("NCERT maths Textbook", ["NCERT Mathematics: Textbook for Class 10"], ["https://apnaclass.com/ncert-textbook"])
recommendation_system.add_content_item("Linear Algebra Textbook", ["Linear Algebra for Beginners"], ["https://maths.com/linear-algebra-textbook"])
recommendation_system.add_content_item("Differential Equations Textbook", ["Differential Equations Made Easy"], ["https://byjus.com/diff-eq-textbook"])
recommendation_system.add_content_item("ICSE 10th Textbook", ["ICSE Class 10 Mathematics by Selina Publishers"],["https://selinapublishers.com/icse10-textbook"])
recommendation_system.add_content_item("Secondary school Textbook", ["Secondary School Mathematics for Class 10 by S. L. Loney (Goyal Brothers Prakashan)"],["https://goyalbros.com/textbook"])
recommendation_system.add_content_item("Cengage 10th grade Textbook", ["Mathematics - VIII (Eighth) by Cengage Learning India"],["https://cengage.com/textbook"])

#9th grade
recommendation_system.add_content_item("RS Agarwal Textbook", ["ICSE Class 10 Mathematics by Selina Publishers"],["https://selinapublishers.com/icse10-textbook"])

user_input = input("Enter your category (High School, Intermediate, UG): ")

if user_input == "High School":
    grade_input = input("Enter your grade (8th, 9th, 10th): ")
    subject_input = input("Enter your subject (Mathematics, Physics, Chemistry, Biology, Social Studies, English): ")
    print("Recommended Content:")
    print() 
    if grade_input == "10th" and subject_input == "Mathematics":
        content_item = recommendation_system.search_content_by_name("RS Agarwal Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Material: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
            print()        
        content_item = recommendation_system.search_content_by_name("NCERT maths Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Material: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
            print() 
        content_item = recommendation_system.search_content_by_name("Linear Algebra Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Material: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
            print() 
        content_item = recommendation_system.search_content_by_name("ICSE 10th Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Material: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
            print() 
        content_item = recommendation_system.search_content_by_name("Secondary school Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Material: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
            print() 
        content_item = recommendation_system.search_content_by_name("Cengage 10th grade Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Material: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
            print() 
    elif grade_input == "10th" and subject_input == "Physics":
        content_item = recommendation_system.search_content_by_name("Physics Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Material: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
        content_item = recommendation_system.search_content_by_name("Differential Equations Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Material: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
    else:
        print("No recommended content found.")

elif user_input == "Intermediate":
    grade_input = input("Enter your grade (Plus 1, Plus 2): ")
    subject_input = input("Enter your subject (Mathematics, Physics, Chemistry): ")
    print("Recommended Content:")
    if grade_input == "Plus 1" and subject_input == "Mathematics":
        content_item = recommendation_system.search_content_by_name("Calculus Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
        content_item = recommendation_system.search_content_by_name("Linear Algebra Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
    elif grade_input == "Plus 2" and subject_input == "Mathematics":
        content_item = recommendation_system.search_content_by_name("Differential Equations Textbook")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
    else:
        print("No recommended content found.")

elif user_input == "UG":
    program_input = input("Enter your program (CSE, Mechanical, ECE): ")
    year_input = input("Enter your year (1, 2, 3, 4): ")
    subject_input = input("Enter your subject: ")
    print("Recommended Content:")
    if program_input == "CSE" and year_input == "1":
        content_item = recommendation_system.search_content_by_name("CAD")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
        content_item = recommendation_system.search_content_by_name("System Essentials")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
    elif program_input == "CSE" and year_input == "2":
        content_item = recommendation_system.search_content_by_name("Advanced programming")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
        content_item = recommendation_system.search_content_by_name("DATA STRUCTURES AND ALGORITHMS")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
    elif program_input == "Mechanical" and year_input == "1":
        content_item = recommendation_system.search_content_by_name("Single Variable Calculus")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
        content_item = recommendation_system.search_content_by_name("Electrical & Electronic Circuits")
        if content_item:
            print(f"Name: {content_item.name}")
            print(f"Textbooks: {', '.join(content_item.textbooks)}")
            print(f"Links: {', '.join(content_item.links)}")
    elif program_input == "ECE" and year_input == "1":
        conten
