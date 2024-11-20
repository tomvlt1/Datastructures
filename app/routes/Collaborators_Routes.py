from flask import Blueprint, render_template, request
from LoadData import data
from filterplusembedding import Final_Sort

collaborators_bp = Blueprint('collaborators', __name__)

@collaborators_bp.route('/')
def collaborators():
    filtered_data = data
    return render_template('collaborators.html', 
                           tables=filtered_data.to_html(classes='table table-striped table-bordered', index=False))  # Bootstrap framework for display, no index displayed

@collaborators_bp.route('/filter', methods=['POST'])
def datafilter():
    filtered_data = Final_Sort()
    
    # Convert filtered data to HTML
    if filtered_data.empty:
        filtered_data_html = "<p>No results found matching your criteria.</p>"
    else:
        filtered_data_html = filtered_data.to_html(classes='table table-striped table-bordered', index=False)
    
    return render_template('results.html', tables=filtered_data_html)






