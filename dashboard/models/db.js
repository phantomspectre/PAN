module.exports = {
  getRecords: function(req, res) {
        var pg = require('pg');
        //You can run command "heroku config" to see what is Database URL from Heroku belt
        var conString = process.env.DATABASE_URL || "postgres://postgres:admin@localhost:5432/PAN";
        var client = new pg.Client(conString);
        client.connect();
        var query = client.query("select distinct t1.*, t2.eta, t3.count from vessel_info as t1 left join eta as t2 on t2.imo = t1.imo2 left join test2 as t3 on t3.imo = t1.imo2");
        // var query2 = client.query("SELECT COUNT(gender) FROM crew WHERE gender='M'");
        // console.log(query2)
        query.on("row", function (row, result) {
            result.addRow(row);

        });
        query.on("end", function (result) {
            client.end();
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.write(JSON.stringify(result.rows, null, "    ") + "\n");
            res.end();
        });
  },
 peopleRec: function(req, res) {
        var pg = require('pg');
        var conString = process.env.DATABASE_URL || "postgres://postgres:admin@localhost:5432/PAN";
        var client = new pg.Client(conString);
        client.connect();
          //  console.log("in the db imo is "+req.params.imo)
        var query = client.query("SELECT distinct * FROM crew WHERE imo = " +req.params.imo+";");
        query.on("row", function (row, result) {
            result.addRow(row);

        });
        query.on("end", function (result) {
            client.end();
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.write(JSON.stringify(result.rows, null, "    ") + "\n");
            res.end();
        });
  },
weaponsRec: function(req, res) {
        var pg = require('pg');
        var conString = process.env.DATABASE_URL || "postgres://postgres:admin@localhost:5432/PAN";
        var client = new pg.Client(conString);
        client.connect();
           // console.log("in the db imo is "+req.params.imo)
        var query = client.query("SELECT distinct weapons FROM weapons WHERE imo = " +req.params.imo+";");
        query.on("row", function (row, result) {
            result.addRow(row);

        });
        query.on("end", function (result) {
            client.end();
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.write(JSON.stringify(result.rows, null, "    ") + "\n");
            res.end();
        });
  },
 person: function(req, res) {
        var pg = require('pg');
        var conString = process.env.DATABASE_URL || "postgres://postgres:admin@localhost:5432/PAN";
        var client = new pg.Client(conString);
        client.connect();
        // console.log('in the db tdn is' +req.params.tdn);
        var tdn = req.params.tdn;
//     console.log('in the db tdn is '+TDN);
        var query = client.query("SELECT distinct * FROM crew WHERE travel_document_number ='" +req.params.tdn+ "';");
         query.on("row", function (row, result) {
            result.addRow(row);
        });
        query.on("end", function (result) {
            client.end();
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.write(JSON.stringify(result.rows, null, "    ") + "\n");
            res.end();
        });

  },


    femRec: function(req, res) {
        var pg = require('pg');

        var conString = process.env.DATABASE_URL || "postgres://postgres:admin@localhost:5432/PAN";
        var client = new pg.Client(conString);
        client.connect();
        // var query = client.query("select * from vessel_info");
        var query = client.query("select imo,count(gender) from crew where gender = 'F' or gender = 'FEMALE' group by imo");
        // console.log(query2)
        query.on("row", function (row, result) {
            result.addRow(row);

        });
        query.on("end", function (result) {
            client.end();
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.write(JSON.stringify(result.rows, null, "    ") + "\n");
            res.end();
        });
  },

  etaRec: function(req, res) {
      var pg = require('pg');

      var conString = process.env.DATABASE_URL || "postgres://postgres:admin@localhost:5432/PAN";
      var client = new pg.Client(conString);
      client.connect();
      // var query = client.query("select * from vessel_info");
      var query = client.query("select imo,eta from eta");
      // console.log(query2)
      query.on("row", function (row, result) {
          result.addRow(row);

      });
      query.on("end", function (result) {
          client.end();
          res.writeHead(200, {'Content-Type': 'text/plain'});
          res.write(JSON.stringify(result.rows, null, "    ") + "\n");
          res.end();
      });
},

};
