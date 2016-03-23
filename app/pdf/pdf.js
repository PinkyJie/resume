var fs = require('fs');
var path = require('path');
var PDFDocument = require('pdfkit');

// page/font size
var pageSize = {
    left: 30,
    top: 40,
    middleX: 330,
    endX: 565,
    sectionIndent: 20,
    sectionMargin: 0.3
};

var fontSize = {
    text: 10,
    headerTitle: 28,
    headerSubTitle: 17,
    sectionTitle: 16
};

// split column function
function applyTwoColumn (docInstance, arr, drawFunc) {
    var isEnd = false;
    var i = 0;
    var top = docInstance.y;
    while (!isEnd) {
        if (i + 2 >= arr.length) {
            isEnd = true;
        }
        // 2 projects one row
        var twoElementArr = arr.slice(i, i + 2);
        var heights = [];
        twoElementArr.forEach(function (item, idx) {
            var left = idx > 0 ? pageSize.middleX : pageSize.left + pageSize.sectionIndent;
            drawFunc(item, left, top);
            heights.push(docInstance.y);
        });
        top = Math.max.apply(null, heights);
        i = i + 2;
    }
}

// generate pdf for every language
var langs = fs.readdirSync(path.join(__dirname, '/../i18n/'));
langs.forEach(function (file) {
    // load json
    var data = require(path.join(__dirname, '/../i18n/', file));
    // set page size
    var doc = new PDFDocument({
        size: 'A4',
        margins: {
            top: pageSize.top,
            bottom: pageSize.top,
            left: pageSize.left,
            right: pageSize.left
        }
    });
    // set output file name
    doc.pipe(fs.createWriteStream('./dist/' + data.badge.pdfLink));

    // set metadata
    doc.info.Title = data.badge.pdfName;
    doc.info.Author = data.header.name;
    doc.info.Subject = data.html.title;

    // font defination
    var titleFontData = data.pdf.fonts.title;
    var textFontData = data.pdf.fonts.text;
    if (titleFontData.type === "standard") {
        doc.registerFont('title-font', titleFontData.name);
    } else {
        doc.registerFont('title-font', path.join(__dirname, titleFontData.path), titleFontData.name);
    }
    if (textFontData.type === "standard") {
        doc.registerFont('text-font', textFontData.name);
    } else {
        doc.registerFont('text-font', path.join(__dirname, textFontData.path), textFontData.name);
    }

    // header section
    // left
    doc.font('title-font')
        .fontSize(fontSize.headerTitle)
       .text(data.header.name);

    doc.fontSize(fontSize.headerSubTitle)
        .fillColor('grey')
        .text(data.header.title)
        .fillColor('black');

    doc.fontSize(fontSize.text + 2)
        .fillColor('grey')
        .text(data.pdf.online.text, {continued: true})
        .fillColor('blue')
        .text(data.pdf.online.url, {link: data.pdf.online.url})
        .fillColor('black');

    // right
    doc.moveUp(4.5);
    doc.font('text-font')
        .fontSize(fontSize.text)
        .text(data.about.location, {align: 'right'})
        .text(data.about.phone, {align: 'right'})
        .text(data.about.email, {align: 'right'})
        .fillColor('blue')
        .text(data.about.socials.blog.url, {link: data.about.socials.blog.url, align: 'right'})
        .text(data.about.socials.github.url, {link: data.about.socials.github.url, align: 'right'})
        .fillColor('black');

    // hr
    doc.moveTo(pageSize.left, 105)
        .lineTo(pageSize.endX, 105)
        .dash(5, {space: 2})
        .stroke();

    doc.moveDown(2.5);

    // about section
    doc.font('title-font')
        .fontSize(fontSize.sectionTitle)
        .text(data.sections.about)
        .moveDown(pageSize.sectionMargin);

    doc.font('text-font')
        .fontSize(fontSize.text);

    var col1Count = data.about.introduction.length / 2;
    data.about.introduction.forEach(function (desc, idx) {
        var isBelongToCol1 = idx < col1Count;
        doc.text(desc, isBelongToCol1 ? pageSize.left + pageSize.sectionIndent : pageSize.middleX);
        if (idx === col1Count - 1) {
            doc.moveUp(2);
        }
    });

    doc.moveDown(pageSize.sectionMargin);

    // education section

    doc.font('title-font')
        .fontSize(fontSize.sectionTitle)
        .text(data.sections.education, pageSize.left)
        .moveDown(pageSize.sectionMargin);

    doc.font('text-font')
        .fontSize(fontSize.text);

    data.education.universities.forEach(function (univ, idx) {
        doc.fontSize(fontSize.text + 1)
            .fillColor('brown')
            .text(univ.name, pageSize.left + pageSize.sectionIndent)
            .fontSize(fontSize.text)
            .fillColor('black')
            .text(univ.major)
            .fillColor('grey')
            .text(univ.location + ' -- ' + univ.year)
            .fillColor('black');
        doc.moveUp(3);
        univ.items.map(function (item) {
            if (item.link) {
                doc.list([' '], pageSize.middleX, doc.y, {continued: true})
                    .text(item.textBefore, pageSize.middleX + 10, doc.y, {continued: true})
                    .fillColor('blue')
                    .text(item.link.text, {link: item.link.url, continued: true})
                    .fillColor('black')
                    .text(item.textAfter);
                doc.moveDown();
            } else {
                doc.list([item.text], pageSize.middleX);
            }
        });
        doc.moveDown(1.5);
    });

    doc.moveDown(pageSize.sectionMargin);

    // employment section

    doc.font('title-font')
        .fontSize(fontSize.sectionTitle)
        .text(data.sections.employment, pageSize.left)
        .moveDown(pageSize.sectionMargin);

    doc.font('text-font')
        .fontSize(fontSize.text);

    applyTwoColumn(doc, data.employment.jobs, function (job, left, top) {
        doc.fontSize(fontSize.text + 1)
            .fillColor('brown')
            .text(job.name, left, top, {width: pageSize.endX / 2})
            .fontSize(fontSize.text)
            .fillColor('black')
            .text(job.position)
            .fillColor('grey')
            .text(job.year)
            .moveDown(0.3)
            .fillColor('black')
            .list(job.description);
        doc.moveDown(0.5);
    });

    doc.moveDown(pageSize.sectionMargin);

    // skill section

    doc.font('title-font')
        .fontSize(fontSize.sectionTitle)
        .text(data.sections.skill, pageSize.left)
        .moveDown(pageSize.sectionMargin);

    doc.font('text-font')
        .fontSize(fontSize.text);

    var skillArr = [];
    data.skill.programming.children.forEach(function (item) {
        var skillNames = item.skills.map(function (i) {
            return i.name;
        });
        var text = item.text + ': ' + skillNames.join(', ');
        skillArr.push(text);
    });

    skillArr.push(data.skill.library.text + ': ' + data.skill.library.children.join(', '));
    doc.list(skillArr, pageSize.left + pageSize.sectionIndent);

    doc.moveDown(pageSize.sectionMargin + 0.3);

    // project section

    doc.font('title-font')
        .fontSize(fontSize.sectionTitle)
        .text(data.sections.project, pageSize.left, doc.y, {continued: true});

    doc.font('text-font')
        .fontSize(fontSize.text);

    doc.fillColor('grey')
        .text(data.pdf.github.text, pageSize.left + pageSize.sectionIndent, doc.y + 3, {continued: true})
        .fillColor('blue')
        .text(data.about.socials.github.url, {link: data.about.socials.github.url})
        .fillColor('black');

    doc.moveDown(pageSize.sectionMargin + 0.3);

    var projects = data.project.col1.concat(data.project.col2);
    applyTwoColumn(doc, projects, function (proj, left, top) {
        doc.fontSize(fontSize.text + 1)
            .fillColor('brown')
            .text(proj.name + ' (' + proj.year + ')', left, top, {width: pageSize.endX / 2})
            .fontSize(fontSize.text)
            .fillColor('black')
            .moveDown(0.2)
            .text('[ ' + proj.library.join(', ') + ' ]')
            .moveDown(0.3)
            .list(proj.description);
        doc.moveDown(0.5);
    });

    // end
    doc.end();
});