const template = title => (
    `<!DOCTYPE html>
    <html gl="en">
        <head>
            <meta charset="utf-8">
            <title>${title}</title>
        </head>
    </html>
    <body>
        <div id="app"></div>
        <script src="/dist/client.js"></script>
    </body>
    `
);

export default template;