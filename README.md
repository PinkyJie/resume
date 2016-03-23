MyResume [![Travis](https://img.shields.io/travis/PinkyJie/resume.svg?style=flat-square)](https://travis-ci.org/PinkyJie/resume)
========

[http://pinkyjie.com/resume](http://pinkyjie.com/resume)

Theme by [Flatty Resume](http://amindiary.com/demo/flatty-cv/)

Built with [Yeoman](http://yeoman.io/)


### JSON Data Driven

* All HTML templates are put in `app/partials`, these files are just layouts with variables.
* PDF layout is defined in `app/pdf/pdf.js`.
* All Data for different languages are put in `app/i18n`, these files are just plain JSON.

### One data source, multiple outputs (HTML/PDF)

* Use [jade](https://github.com/jadejs/jade) to generate HTML.
* Use [pdfkit](https://github.com/devongovett/pdfkit) to generate PDF.

### Build

* Install Node and Ruby
* `npm install -g grunt-cli` and `gem install compass`
* `npm run bower`
* `npm install`
* `npm start` for live reload preview
* `npm run build` to generate HTML in `dist` folder
* `npm run pdf` to generate PDF files in `dist` folder

### Generate your own Resume

* Fork this project.
* Change JSON files under folder `app/i18n`.
* If you don't want include all sections, just delete the `include xxx` in `app/index.jade`.

### Host resume on your Github Pages

* Use your github account to access [TravisCI](https://travis-ci.org/), activate your repo.
* Update `env` in `.travis.yml` (check my blog: [用TravisCI来做持续集成](http://pinkyjie.com/2016/02/27/continuous-integration-with-travis-ci/))
* Push code to your forked repo, then Travis will automatically deploy build on your Github Pages.


