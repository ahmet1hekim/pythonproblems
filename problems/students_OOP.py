class fileio:
    f = open("students.txt","a")
    f.close

    def addStudent(self,studentinfo):
        with open('students.txt', 'r') as file:
            allStudents = file.readlines()
        allStudents.append(studentinfo) 
        with open('students.txt', 'w') as file:
            for x in range(len(allStudents)):
                file.writelines(allStudents[x])
            file.writelines("\n")

    def rmvStudent(self,id):
        with open('students.txt', 'r') as file:
            allStudents = file.readlines()

            for student in allStudents:
                if id in student:
                    allStudents.remove(student)
        with open('students.txt', 'w') as file:
            for x in range(len(allStudents)):
                file.writelines(allStudents[x])
            file.writelines("\n")
    def listStudent(self,id):
        with open('students.txt', 'r') as file:
            allStudents = file.readlines()

            for student in allStudents:
                if id in student:
                    print(student)

mf=1
while(mf==1):
    print("\nekle(1),cikar(2),gor(3),cik(4)\n")
    flag = input("sec: ")
    mf=0
    files = fileio()
    if(int(flag)==1):
        s = input("\nbilgiler(id,ad,soyad,sinif,yas,cinsiyet):\n").split(",")
        files.addStudent(s)
        mf=1
    elif(int(flag)==2):
        files.rmvStudent(input("\nid:\n"))
        mf=1
    elif(int(flag)==3):
        files.listStudent(input("\nid:\n"))
        mf=1
    elif(int(flag)==4):
        mf=0        