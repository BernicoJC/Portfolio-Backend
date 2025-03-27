const Resume = () => {
    return (
        <div id="content">
            <h1>Resume</h1>
            <h3>The resume displayed here might be outdated. Please email me at bernicojc113@gmail.com for my up to date resume. Thank you!</h3>
            <div id="pdf_container">
                <object data="other_files/resume_bernico.pdf" type="application/pdf">
                    <p>Your browser does not support PDFs. <a href="resume_bernico.pdf">Download the PDF</a>.</p>
                </object>
            </div>
        </div>
    )
}

export default Resume