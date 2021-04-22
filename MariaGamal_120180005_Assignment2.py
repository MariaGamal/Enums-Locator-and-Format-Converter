import os
import re
import enum
import zipfile

class Extract:
    def __init__(self, extensions, directory):
        self.ext = extensions
        self.required_files = []
        self.dir = directory

    def extract_files(self):
        '''
        Input : Directory string
        Extracts zip folders in the given directory and
        Returns a list containing path of all files that agree with specific given extensions.

        '''
        for dirpath, dirnames, filenames in os.walk(self.dir):
            for file in filenames:
                if file.endswith(".zip"):
                    file_path = os.path.normpath(os.path.join(dirpath, file))
                    with zipfile.ZipFile(file_path, 'r') as myzip:
                        myzip.extractall(path = dirpath)
                elif file.endswith(self.ext):
                    name_path = os.path.normpath(os.path.join(dirpath,file))
                    self.required_files.append(name_path) 
        return self.required_files  

class Enums_Parsing:
    def __init__(self, file_paths):
        self.enums = []
        self.files = file_paths
        self.list_of_enums_dic = []
        self.python_enums = []
    
    def extract_enums(self):
        '''
        Given a list of file paths as strings,
        Reads through this files and extracts enum data types,
        Returns a list containing those enums as strings.

        '''
        for file in self.files:
            with open(file, 'r') as f:
                matches = re.findall('enum[\w\s]*\{[^}]+\}[^;]*', f.read())
                for match in matches:
                    if re.search('#',match) is None and re.search('= \(int\)', match) is None:
                        self.enums.append(match)
        return self.enums

    def analyze_enums(self):
        '''
        Given a list of enums written as strings
        Extracts the name and data of the enum,
        Returns a list of dictionaries, each dictionary contains an enum with its name and data.

        '''
        for i in self.enums:
            d = {}
            #Part 1: Finding Names of enums. Names can be found either between the
            #keywoard enum and the starting curly bracket or after the closing curly bracket
            name_matches = re.findall('(enum[\s\w]*\{|\}[^;]*)', i)
            name = ''
            for item in name_matches:
                matches = re.findall('\w+',item)  #Names contain only word characters
                for match in matches:
                    if match !='enum' and name == "":  #If the name is found after the keywoard enum, then what might be found after the closing bracket is a variable not the enum name.
                        name = match
            d['Name'] = name

            #Part 2: Finding enum members and values. There are 2 ways of commenting in C/C++. 
            #Either adding // before the comment or /*. So we use two different patterns for the 2 cases
            # to extract the data(enum members and values) without the comments from inside the curly brackets
            if re.search('//',i) is None:
                data_matches = re.findall('([\w=\-\+ ,]+\/\*|[\w=\-\+ ]+,|[\w=\-\+\s]+\})', i)
            else:
                data_matches = re.findall('([\w=\-\+ ,]+\/\*|[\w=\-\+ ]+,)' , i)
            replacements = [' ', '\n', ',', '}', '/', '*']
            for n in range(len(data_matches)):
                for r in replacements:
                    if r in data_matches[n]:
                        data_matches[n] = data_matches[n].replace(r,'')
            data_matches = [i for i in data_matches if i!='']
            d['Data'] = data_matches
            self.list_of_enums_dic.append(d)

        return self.list_of_enums_dic

    def convert_to_python(self):
        '''
        Returns enums in python format using Enum() method.

        '''
        for dic in self.list_of_enums_dic:
            for i in range(len(dic['Data'])):
                if re.search('=', dic['Data'][i]) is None:
                    dic['Data'][i] = (dic['Data'][i] , enum.auto())
                else:
                    index = dic['Data'][i].index('=')
                    dic['Data'][i] = (dic['Data'][i][:index] , int(dic['Data'][i][index+1 :] , 0 ))
            
            self.python_enums.append(enum.Enum(dic['Name'], dic['Data']))
        return self.python_enums

extensions = (".c", ".cpp", ".h", ".hpp")
directory = 'D:/Ejust/3rd year/Semester One/Advanced Programming/assignment_2/project' 
test_files = Extract(extensions, directory)
files = test_files.extract_files()

test_enums = Enums_Parsing(files)
enums_strings = test_enums.extract_enums()
enums_dic = test_enums.analyze_enums()
python_enums = test_enums.convert_to_python()

with open('D:/Ejust/3rd year/Semester One/Advanced Programming/assignment_2/Enums_in_python.py', 'w') as f:
    f.write("import enum \n\n")
    for enum in python_enums:
        f.write(f"class {str(enum)[7:-2]}(enum.Enum): \n")
        for member in enum:
            f.write(f"\t{member.name} = {member.value} \n")
        f.write("\n")
    