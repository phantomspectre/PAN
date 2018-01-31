//var fs        = require('fs')
//  , path      = require('path')
//  , Sequelize = require('sequelize')
//  , lodash    = require('lodash')
//  , sequelize = new Sequelize('PAN', 'postgres', 'admin', {
//      host:'localhost',
//      dialect: "postgres", // or 'sqlite', 'postgres', 'mariadb'
//      pool: {
//          max: 5,
//          min: 0,
//          idle:10000
//      },
//      storage: "/tmp/my.db",
//    })
//  , db        = {}
//
//fs
//  .readdirSync(__dirname)
//  .filter(function(file) {
//    return ((file.indexOf('.') !== 0) && (file !== 'index.js') && (file.slice(-3) == '.js'))
//  })
//  .forEach(function(file) {
//    var model = sequelize.import(path.join(__dirname, file))
//    db[model.name] = model
//  })
//
//Object.keys(db).forEach(function(modelName) {
//  if (db[modelName].hasOwnProperty('associate')) {
//    db[modelName].associate(db)
//  }
//})
//
//module.exports = lodash.extend({
//  sequelize: sequelize,
//  Sequelize: Sequelize
//}, db)
//
