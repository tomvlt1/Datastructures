from flask import Blueprint, render_template
from LoadData import data

collaborators_bp = Blueprint('collaborators', __name__)

@collaborators_bp.route('/')
def collaborators():
    filtered_data = data
    return render_template('collaborators.html', tables=filtered_data.to_html(classes='table table-striped table-bordered', index=False)) #boostrapframwork for display, no index displayed

@collaborators_bp.route('/filter', methods=['POST']) #only when the form is submitted


    # Convert filtered data to HTML   
    if filtered_data.empty:
        filtered_data_html = "<p>No results found matching your criteria.</p>"
    else:
        filtered_data_html = filtered_data.to_html(classes='table table-striped table-bordered', index=False)
    return render_template('filter_results.html', tables=filtered_data_html)




