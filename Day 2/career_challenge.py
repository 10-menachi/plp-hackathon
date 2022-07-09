career_options=['computer science','animal science','teaching']
career_advices=[
    '1.Remember that a job does not give your life meaning\n',
    '2.Every job will have unexpected inconveniences\n',
    '3.Be willing to sacrifice some things to build the career you want\n',
    '4.Embrace failure\n',
    '5.Use your intuition\n',

]
#convert to string
career_string=' ' .join([str(item) for item in career_advices])
career_questions=[
    '1.do you like interacting with people,animals or machines?\n',
    '2.do you like  solving problems,sharing knowledge or treating animals\n'

]
#convert to string
career_questions_string=' ' .join([str(item) for item in career_questions])
print("before venturing into any career you should consider the following:\n",career_string)
print("your answers to the following questions will determine your your career path\n")



quiz1=input(career_questions[0])
quiz2=input(career_questions[1])


if quiz1 =="machines"and quiz2 =="solving problems":
    print("your career path is:",career_options[0])
elif quiz1 =="animals"and quiz2 =="treating animals":
     print("your career path is:",career_options[1])
elif quiz1 =="people"and quiz2 =="sharing knowledge":
    print("your career path is:",career_options[2])  

else:
     print("your choice combination does not match the career we offer") 


    
     

    
        
    
    