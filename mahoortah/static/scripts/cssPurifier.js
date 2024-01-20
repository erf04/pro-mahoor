import unCss from 'uncss';

const files = ['index.html'];

const options = {
    stylesheets: ['style.css']
}

unCss(files, options, (error, output) => {
    console.log(output);
})