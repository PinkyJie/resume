MyResume
========

[http://pinkyjie.com/resume](http://pinkyjie.com/resume)

Theme by [Flatty Resume](http://amindiary.com/demo/flatty-cv/)

Built with [Yeoman](http://yeoman.io/)

Build
========
* Install Node and Ruby
* `npm install -g bower grunt-cli`
  `gem install compass`
* `bower install`
* `npm install`
* `grunt serve` for preview
* `grunt build` for build

Fork me
========

The project has two branches:

* [master](https://github.com/PinkyJie/resume/tree/master)  branch for development, change code and run `grunt serve` to preview the page in live-reload, when done, run `grunt build` ready for production
* [gh-pages](https://github.com/PinkyJie/resume/tree/gh-pages)  branch for production, using the Github naming convention for branch naming, after running `grunt build` in master branch, switch to this branch using `git checkout gh-pages` and run 'build.bat'(easily to transform to Linux platform)
