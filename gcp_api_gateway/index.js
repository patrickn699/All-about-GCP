/**
 * Responds to any HTTP request.
 *
 * 
 * 
 
 exports.helloWorld = (req, res) => {
    let message = req.query.message || req.body.message || 'Hello World!';
    res.status(200).send(message);
  };
   */
const functions = require('@google-cloud/functions-framework');

functions.http('helloGET', (req, res) => {
  res.send('Hello World!, from Node JS');
});
  