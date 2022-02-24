projects = {}
contributors = {}

def main(input_case):
    try:
        file = open(input_case, "r")
        evaluateInput(file)
        print(contributors)
        print()
        print(projects)
        

    except Exception as e:
        print(e)
    else:
        return 0
    finally:
        file.close()



def evaluateInput(file):
        base_line = file.readline()
        base = base_line.rstrip('\n')
        project_plan_array = base.split(' ')
        
        contribs = project_plan_array[0]
        projs = project_plan_array[1]

        for i in range(int(contribs)):
            contrib_line_content = file.readline()
            contrib_array = contrib_line_content.rstrip('\n').split(' ')

            skillsets = contrib_array[1]

            contributors[contrib_array[0]] = []

            for a in range(int(skillsets)):
                contrib_skill_line = file.readline()
                contrib_skill_array = contrib_skill_line.rstrip('\n').split(' ')
                contributors[contrib_array[0]].append({contrib_skill_array[0] : contrib_skill_array[1]})

        for i in range(int(projs)):
            proj_line_content = file.readline()
            proj_array = proj_line_content.rstrip('\n').split(' ')

            roles = proj_array[4]

            projects[proj_array[0]] = []

            for a in range(int(roles)):
                role_line_content = file.readline()
                role_array = role_line_content.rstrip('\n').split(' ')
                projects[proj_array[0]].append({role_array[0] : role_array[1]})


if __name__ == "__main__":
    main("sample.txt")