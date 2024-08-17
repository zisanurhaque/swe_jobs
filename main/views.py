from django.shortcuts import render
import pandas as pd
from .forms import FilterForm

#Utility Functions
def get_days(date_str):
    """Extract the number of days from a date string."""
    return int(''.join(filter(str.isdigit, date_str)))

def extract_salary(salary_str):
    """Converts salary string into a yearly salary for comparison"""
    if 'Per Hour' in salary_str:
        hourly_rate = float(''.join(filter(lambda x: x.isdigit() or x == '.', salary_str.split(' ')[0])))
        return hourly_rate * 2080
    else:
        salary = ''.join(filter(str.isdigit, salary_str.split('-')[0]))
        return int(salary) * 1000 if salary else 0


# Main View
def main_view(request):
    raw_data = pd.read_csv('main/static/swe_salaries.csv')
    raw_data.columns = raw_data.columns.str.replace(" ","_")
    raw_data['Company'] = raw_data['Company'].fillna('Unknown Company').astype(str)
    raw_data['Salary'] = raw_data['Salary'].fillna('N/A').astype(str)
    data = raw_data.to_dict(orient='records')

    # Initialize form and filtered data
    form = FilterForm(request.GET or None)
    filtered_data = []
    if form.is_valid():
        # Search filter
        search_query = form.cleaned_data.get('search')
        if search_query:
            filtered_data = [item for item in data if search_query.lower() in str(item).lower()]
        else:
            filtered_data = data

        # Company sorting
        company = form.cleaned_data.get('company')
        if company == 'asc':
            data.sort(key=lambda x: x['Company'].lower())
            filtered_data = data
        else:
            data.sort(key=lambda x: x['Company'].lower(), reverse=True)
            filtered_data = data

        # Date Sorting
        published_time = form.cleaned_data.get('published_time')
        if published_time == 'asc':
            data.sort(key=lambda x: get_days(x['Date']))
            filtered_data = data
        else:
            data.sort(key=lambda x: get_days(x['Date']), reverse=True)
            filtered_data = data
        
        # Salary Sorting
        sort_by_salary = form.cleaned_data.get('salary')
        if sort_by_salary == 'asc':
            data.sort(key=lambda x: extract_salary(x['Salary']))
            filtered_data = data
        else:
            data.sort(key=lambda x: extract_salary(x['Salary']), reverse=True)
            filtered_data = data

        data = filtered_data
    else:
        data = data
    return render(request, 'job_list.html', {"data": data, "query": form})