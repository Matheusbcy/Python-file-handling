courses = []
with open ("dados/courses.csv", "r", encoding="UTF-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        course = {"language": language, "category": category}
        courses.append(course)
        
    
    
for course in sorted(courses, key=lambda course: course["category"]):
    print(f"{course['language']} - {course['category']}")