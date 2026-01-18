from pprint import pprint

if __name__ == "__main__":
    new_ics = []
    with open('icalendar.ics', 'r') as f:
        data = f.readlines()
        data = [line[:-1] for line in data]

        is_ignoring = False
        for line in data:
            if "DESCRIPTION:" in line:
                is_ignoring = True
            
            if line == "END:VEVENT":
                is_ignoring = False
                
            if not is_ignoring:
                new_ics.append(line+'\n')

    
    with open('filtered_calendar.ics', 'w') as f:
        f.writelines(new_ics)
