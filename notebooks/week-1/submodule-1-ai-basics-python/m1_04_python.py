#!/usr/bin/env python
# coding: utf-8

# # Python Review
# 
# This notebook contains all the code examples from the Python Review lesson. The teacher will go throught them together. Markdown cells are left mostly empty. Take notes in these cells for the afternoon class.
# 

# ## Basic Python Concepts
# 

# ### Variables
# 

# In[ ]:


name = "Python"
age = 30
price = 19.99
is_active = True

result = age + 10
message = f"Hello, {name}"

print(result)
print(message)


# ### Lists
# 

# In[ ]:


fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

first_fruit = fruits[0]
last_fruit = fruits[-1]

print(first_fruit)
print(last_fruit)

fruits.append("grape")
fruits.pop()
fruits.insert(1, "mango")

print(fruits)


# ### Dictionaries
# 

# In[ ]:


student = {
    "name": "Alice",
    "age": 25,
    "course": "AI Bootcamp"
}

name = student["name"]
age = student.get("age")

print(name)
print(age)

student["email"] = "alice@example.com"
del student["age"]
keys = student.keys()
values = student.values()

print(keys)
print(values)


# ### Sets
# 

# In[ ]:


numbers = {1, 2, 3, 4, 5}
colors = {"red", "blue", "green"}

numbers.add(6)
numbers.remove(3)
union = numbers | {7, 8}
intersection = numbers & {4, 5, 6}

print(numbers)
print(union)
print(intersection)


# ### If/Else
# 

# In[ ]:


age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

print(status)

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)


# ### For Loops
# 

# In[ ]:


fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# ### While Loops
# 

# In[ ]:


count = 0
while count < 5:
    print(count)
    count += 1


# ### Functions
# 

# In[ ]:


def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

def calculate_total(price, tax_rate=0.1):
    return price * (1 + tax_rate)

total = calculate_total(100)
total_with_custom_tax = calculate_total(100, 0.15)

print(total)
print(total_with_custom_tax)


# ## Advanced Topics
# 

# ### Classes
# 

# In[ ]:


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, studying {self.course}"

student1 = Student("Alice", 25, "AI Bootcamp")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(88)

print(student1.introduce())
print(f"Average: {student1.get_average()}")


# ### Import Libraries - Pandas
# 

# In[ ]:


# Notebook-only setup command: get_ipython().system('pip install pandas')


# In[ ]:


import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85, 90, 88]
}
df = pd.DataFrame(data)

print(df.head())
print(df["age"].mean())
print(df[df["score"] > 85])


# ### Import Libraries - JSON
# 

# In[ ]:


import json

json_string = '{"name": "Alice", "age": 25, "course": "AI Bootcamp"}'

data = json.loads(json_string)
print(data["name"])

student_dict = {
    "name": "Bob",
    "age": 30,
    "grades": [85, 90, 88]
}
json_output = json.dumps(student_dict)
print(json_output)


# ### API Response Parser
# 
# Parse JSON strings from API responses (like from AI models) and extract specific fields.
# 

# In[ ]:


import json

# Simulated API response from an AI model (like OpenAI)
api_response_json = '''
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Python is a versatile programming language used for AI and machine learning."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 15,
    "total_tokens": 25
  }
}
'''

# Parse the JSON string
response_data = json.loads(api_response_json)


# #### Extract Generated Text
# 

# In[ ]:


# Extract the generated text from nested structure
generated_text = response_data["choices"][0]["message"]["content"]
print(f"Generated text: {generated_text}")


# #### Extract Model Information
# 

# In[ ]:


# Extract model name
model_name = response_data["model"]
print(f"Model used: {model_name}")


# #### Extract Token Usage
# 

# In[ ]:


# Extract token usage information
total_tokens = response_data["usage"]["total_tokens"]
prompt_tokens = response_data["usage"]["prompt_tokens"]
completion_tokens = response_data["usage"]["completion_tokens"]
print(f"Token usage - Total: {total_tokens}, Prompt: {prompt_tokens}, Completion: {completion_tokens}")


# #### Extract Additional Fields
# 

# In[ ]:


# Extract multiple fields at once
response_id = response_data["id"]
finish_reason = response_data["choices"][0]["finish_reason"]
print(f"Response ID: {response_id}")
print(f"Finish reason: {finish_reason}")


# #### Multiple Choices Example
# 

# In[ ]:


# Example: Parse another API response with multiple choices
multi_choice_response = '''
{
  "choices": [
    {"text": "Option A", "score": 0.9},
    {"text": "Option B", "score": 0.7},
    {"text": "Option C", "score": 0.5}
  ]
}
'''

data = json.loads(multi_choice_response)
# Extract all choice texts
choice_texts = [choice["text"] for choice in data["choices"]]
print(f"All choices: {choice_texts}")

# Find the highest scoring choice
best_choice = max(data["choices"], key=lambda x: x["score"])
print(f"Best choice: {best_choice['text']} (score: {best_choice['score']})")


# ### Common Import Patterns
# 

# In[ ]:


import pandas as pd


from math import sqrt, pi
print(sqrt(16))
print(pi)

