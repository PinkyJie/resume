MyResume
========

[http://pinkyjie.com/resume](http://pinkyjie.com/resume)

Theme by [Flatty Resume](http://amindiary.com/demo/flatty-cv/)

Built with [Yeoman](http://yeoman.io/)


### JSON Data Driven

* All templates are put in `app/partials`, these files are just layouts with variables.
* All Data for different languages are put in `app/i18n`, these files are just plain JSON.

### Build

* Install Node and Ruby
* `npm install -g bower grunt-cli`
  `gem install compass`
* `bower install`
* `npm install`
* `npm start` for live reload preview
* `npm run build` for build

### Generate your own Resume

* Fork this project.
* Change JSON files under folder `app/i18n`.
* If you don't want include all sections, just delete the `include xxx` in `app/index.jade`.


