# Import necessary modules
from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datasets')
def datasets():
    biomedical_datasets = [
        {'name': 'Foundational Biomedical Datasets', 'links': [
            {'name': 'The Cancer Genome Atlas', 'link': 'https://portal.gdc.cancer.gov/'},
            {'name': 'Genome-Wide Association Studies (GWAS) Catalog', 'link': 'https://www.ebi.ac.uk/gwas/'},
            {'name': 'UK Biobank', 'link': 'https://biobank.ndph.ox.ac.uk/showcase/'},
            {'name': '1000 Genomes Project', 'link': 'https://www.internationalgenome.org/data'},
            {'name': 'ENCODE (Encyclopedia of DNA Elements)', 'link': 'https://www.encodeproject.org/'},
            {'name': 'Protein Data Bank (PDB)', 'link': 'https://www.rcsb.org/#Category-download'},
            {'name': "National Alzheimer's Coordinating Center (NACC)", 'link': 'https://naccdata.org/'},
            {'name': 'PubMed Central (PMC)', 'link': 'https://aws.amazon.com/marketplace/pp/prodview-qh4qqd6ebnqio#usage'},
            {'name': 'DrugBank', 'link': 'https://go.drugbank.com/releases/latest'},
            {'name': 'dbSNP (Single Nucleotide Polymorphism Database)', 'link': 'https://www.ncbi.nlm.nih.gov/snp/'},
            {'name': 'OMIM (Online Mendelian Inheritance in Man)', 'link': 'https://www.omim.org/'},
            {'name': 'ClinVar', 'link': 'https://www.ncbi.nlm.nih.gov/clinvar/'},
            {'name': 'Allen Brain Atlas', 'link': 'https://portal.brain-map.org/'},
            {'name': 'Human Microbiome Project', 'link': 'https://portal.hmpdacc.org/'},
            {'name': 'Stanford HIV Drug Resistance Database', 'link': 'https://hivdb.stanford.edu/'}
        ]},
        {'name': 'Transfer Learning Purpose (Space Biology Dataset)', 'links': [
            {'name': 'NASA GeneLab Data', 'link': 'https://genelab.nasa.gov/'},
            {'name': 'NASA Space Radiation Omics', 'link': 'https://genelab.nasa.gov/datasets_and_counting'},
            {'name': 'NASA Twin Study', 'link': 'https://www.kaggle.com/code/anshumoudgil/iiot-digital-twins-categorical-data-eda'},
            {'name': 'Astrobiology Field Research', 'link': 'https://ahed.nasa.gov/'},
            {'name': 'Microgravity Experiments on Earth', 'link': 'https://ecommons.cornell.edu/items/bfbbf048-4f29-43ea-a637-aff3f86159f9'}
        ]}
    ]
    return render_template('datasets.html', biomedical_datasets=biomedical_datasets)


@app.route('/models')
def models():
    # Define your model links here
    model_links = [
        {'name': 'Model 1', 'link': 'http://example.com/model1'},
        {'name': 'Model 2', 'link': 'http://example.com/model2'}
    ]
    return render_template('models.html', model_links=model_links)

# Run the app
if __name__ == '__main__':
    app.run(debug=False)
