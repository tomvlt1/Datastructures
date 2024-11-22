import pandas as pd


def FilterAge(data, min_age, max_age):
    data['Age'] = pd.to_numeric(data['Age'], errors='coerce').fillna(0).astype(int)
    if min_age is not None:
        data = data[data['Age'] >= min_age]
    if max_age is not None:
        data = data[data['Age'] <= max_age]
    print(f"FilterAge: {len(data)} rows after filtering by age.")
    return data


def FilterNationality(data, nationality):
    if nationality:
        data = data[data['Nationality'].str.lower() == nationality.lower()]
    print(f"FilterNationality: {len(data)} rows after filtering by nationality.")
    return data


def FilterCountryOfResidence(data, country):
    if country:
        data = data[data['Country of Residence'].str.lower() == country.lower()]
    print(f"FilterCountryOfResidence: {len(data)} rows after filtering by country of residence.")
    return data


def FilterDegree(data, field):
    if field:
        data = data[data['Degree'].str.lower() == field.lower()]
    print(f"FilterDegree: {len(data)} rows after filtering by degree.")
    return data


def FilterGPA(data, min_gpa, max_gpa):
    data['GPA'] = pd.to_numeric(data['GPA'], errors='coerce').fillna(0).astype(float)
    if min_gpa is not None:
        data = data[data['GPA'] >= min_gpa]
    if max_gpa is not None:
        data = data[data['GPA'] <= max_gpa]
    print(f"FilterGPA: {len(data)} rows after filtering by GPA.")
    return data


def FilterAvailability(data, min_hours=None, max_hours=None):
    data['Availability'] = pd.to_numeric(data['Availability'], errors='coerce').fillna(0).astype(int)
    if min_hours is not None and max_hours is not None:
        data = data[(data['Availability'] >= min_hours) & (data['Availability'] <= max_hours)]
    elif min_hours is not None:
        data = data[data['Availability'] >= min_hours]
    elif max_hours is not None:
        data = data[data['Availability'] <= max_hours]
    print(f"FilterAvailability: {len(data)} rows after filtering by availability.")
    return data


def FilterGraduationYear(data, graduation_year):
    if graduation_year:
        data = data[data['Graduation Year'] == str(graduation_year)]
    print(f"FilterGraduationYear: {len(data)} rows after filtering by graduation year.")
    return data



def Filtered_Data(data, min_age, max_age, min_gpa, max_gpa, min_hours, max_hours, nationality, country_of_residence, degree, graduation_year):
    filtered_data = data
    filtered_data = FilterAge(filtered_data, min_age, max_age)
    filtered_data = FilterGPA(filtered_data, min_gpa, max_gpa)
    filtered_data = FilterAvailability(filtered_data, min_hours, max_hours)
    if nationality != "":
        filtered_data = FilterNationality(filtered_data, nationality)
    if country_of_residence != "":
        filtered_data = FilterCountryOfResidence(filtered_data, country_of_residence)
    if degree != "":
        filtered_data = FilterDegree(filtered_data, degree)
    if graduation_year != '0':
        filtered_data = FilterGraduationYear(filtered_data, graduation_year)
    return filtered_data



def main():
   
    try:
        data = pd.read_csv('generated_database.csv')
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return

 
    filtered_data = Filtered_Data(
        data,
        min_age=20,
        max_age=25,
        min_gpa=8.0,
        max_gpa=10.0,
        min_hours=10,
        max_hours=None,
        nationality="",
        country_of_residence="",
        degree="",
        graduation_year=""
    )


    #print(f"Final Filtered Data: {len(filtered_data)} rows remaining.")
    #print(filtered_data)
    return filtered_data


if __name__ == "__main__":
    main()
