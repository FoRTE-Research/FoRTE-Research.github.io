from flask import Flask, render_template, Response
from flask_frozen import Freezer  # Import the Freezer extension

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'  # Replace 'build' with your desired directory
freezer = Freezer(app)  # Initialize the Freezer extension



@app.route('/')
def index():
    advdata=[
    "Advice for Prospective Research Students on Contacting Potential Advisors by David Evans",
    "A course on Preparation for Statistical Research offered at NCSU Stat Dept",
    "Principles of Effective Research by Michael A. Nielsen",
    "The Ph.D Experience by Mihir Bellare",
    "Tom Henzinger's advice on doing research",
    "The scientific method by Jeff Offutt",
    "Thoughts on choosing an advisor by Jeff Offutt",
    "Thoughts on writing a Ph.D. proposal by Jeff Offutt",
    "Thoughts on reading papers by Jeff Offutt",
    "Advice for Computer Science College Students by Joel Spolsky",
    "How to Be a Good Graduate Student by Marie desJardins, Indiana University",
    "Excellent advice about graduate school life by Ronald T. Azuma, University of Virginia",
    "Discussion on Ph.D. thesis proposals in computing science by H. C. Lauer",
    "How to write a PhD Thesis given at the doctoral symposium at ASE'03 (Oct 2003) by Steve Easterbrook",
    "Advice for finishing a Ph.D. (pdf document containing slides by Prof. Daniel M. Berry) Lecture",
    "How to Organize your Thesis, by John W. Chinneck.",
    "Chris Riesbeck on What is a Thesis Defense?",
    "How to write a thesis in an Experimental area of Computer Science by Doug Comer.",
    "How to escape during a Ph.D. Final Exam by Doug Comer.",
    "An explanation of language used in CS Departments by Doug Comer.",
    "For anyone considering a Ph.D. in Computer Science by Doug Comer.",
    "How to measure research by Doug Comer.",
    "How to write a Ph.D. thesis by Joe Wolfe.",
    "Tips for Writing and Presentation of Thesis or Dissertation by Joseph Levine.",
    "Dissertation Advice, by Olin Shivers",
    "Resources for Students interested in the PhD by Norman Ramsey",
    "How to get admitted to a PhD program, by Norman Ramsey.",
    "Graduate School Advice",
    "Advice collection",
    "What Am I Doing Here? A Guide to the Unwritten Rules of Grad School in the Sciences by Cory Kerens, Ph.D.",
    "For anyone considering a Ph.D. in Computer Science, by Doug Comer",
    "PhD rants-and-raves",
    "Tips on research and writing, by Renee Miller.",
    "So long, and thanks for the Ph.D.!, by Ronald Azuma",
    "A Letter to Research Students, by Duane A. Bailey",
    "Networking on the Network: A Guide to Professional Skills for PhD Students",
    "Thoughts on Ph.D. Qualifiers by Phil Koopman",
    "Tom Martin's qual page for some good hints from the student point of view.",
    "Graduate Study in the Computer and Mathematical Sciences : A Survival Manual, Dianne O'Leary",
    "How to be a Good Graduate Student by Marie desJardins.",
    "Guide to working with Norman Ramsey expectations and obligations as an advisor.",
    "A Dictionary of Useful Research Phrases",
    "Burnout Prevention and Recovery at MIT",
    "How to be terrible graduate student (by Graeme Hirst, University of Toronto).",
    "Choosing an Advisor by Marshall Lev Dermer, UW-Milwaukee.",
    "Computer Science Graduate School Survival Guide by Ronald Azuma.",
    "Notes On The PhD Degree",
    "Re-Envisioning the Ph.D. by the graduate school of UW",
    "Acronyms Frequently Heard Around the School of Computer Science by Paul Heckbert"
]
    return render_template('index.html', advdata=advdata)

@app.route('/team.html')
def team():
    return Response(render_template('team.html'), mimetype='text/html')



if __name__ == '__main__':
    freezer.freeze()

