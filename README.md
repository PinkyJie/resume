MyResume [![Travis](https://img.shields.io/travis/PinkyJie/resume.svg?style=flat-square)](https://travis-ci.org/PinkyJie/resume)
========

[http://pinkyjie.com/resume](http://pinkyjie.com/resume)

Theme by [Flatty Resume](http://amindiary.com/demo/flatty-cv/)

Built with [Yeoman](http://yeoman.io/)


### JSON Data Driven

* All HTML templates are put in `app/partials`, these files are just layouts with variables.
* PDF layout is defined in `app/pdf/pdf.py`.
* All Data for different languages are put in `app/i18n`, these files are just plain JSON.

### One data source, multiple outputs (HTML/PDF)

* Use [jade](https://github.com/jadejs/jade) to generate HTML.
* <del>Use [pdfkit](https://github.com/devongovett/pdfkit) to generate PDF.</del> (pdfkit has some issues for displaying Chinese characters [devongovett/pdfkit#144](https://github.com/devongovett/pdfkit/issues/114))
* Use [pyfpdf](https://github.com/reingart/pyfpdf) (a python library) to generate PDF.

### Build

* Install Node, Ruby(for sass compiling), Python(for PDF generation)
* `npm install -g grunt-cli` and `gem install compass` and `pip install fpdf`
* `npm run bower`
* `npm install`
* `npm start` for live reload preview
* `npm run build` to generate HTML in `dist` folder
* `python app/pdf/pdf.py` to generate PDF files in `dist` folder

### Generate your own Resume

* Fork this project.
* Change JSON files under folder `app/i18n`.
* If you don't want include all sections, just delete the `include xxx` in `app/index.jade`.

### Host resume on your Github Pages

* Use your github account to access [TravisCI](https://travis-ci.org/), activate your repo.
* Add 2 Environment Variables to your TravisCI project settings page:
    * `GitHub_REF`: your Github resume repo URL, like `github.com/PinkyJie/resume.git`
    * `Github_TOKEN`: generate a personal access token for your Github account on [settings page](https://github.com/settings/tokens)
* Push code to your forked repo, then Travis will automatically deploy build on your Github Pages.


