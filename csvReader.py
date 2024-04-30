from __future__ import annotations

def csvToSortedList(fileName: str):
    studentList=[]
    with open(fileName, 'r') as file:
        #Extraction des donnée
        data=file.readlines()
        for studentData in data:
            studentData=studentData.split(',')
            studentINE=studentData[0]
            studentGrade=studentData[1]
            studentWishList=studentData[2:]
            
            #Enlever les retours à la lignes éventuel
            for i in range(len(studentWishList)):
                studentWishList[i] = studentWishList[i].replace("\n", "")
            while '' in studentWishList:
                studentWishList.remove('')
            
            #Crer le profil étudiant et le rajoute à la liste               
            student={'INE': studentINE, 'grade': studentGrade, 'wishList': studentWishList, 'givenSchool': None}
            studentList.append(student)

    #Trie la liste en fonction des grades
    studentList.sort(key=lambda student: student['grade'], reverse=True)
    
    #Ajoute le rang de chaque élève
    rang=1
    for student in studentList:
        student['Rang']=rang
        rang+=1
    return studentList

def csvToEcole(fileName):
    schoolList=[]    
    with open(fileName, 'r') as file:
        #Extraction des donnée
        data=file.readlines()
        for schoolData in data:
            schoolData=schoolData.split(',')
            schoolName=schoolData[0]
            schoolPlaces=schoolData[1]
            
            #Crer le profil école et le rajoute à la liste               
            school={'name': schoolName, 'placesNumber': schoolPlaces, 'remainingPlaces': schoolPlaces}
            schoolList.append(school)
    return schoolList