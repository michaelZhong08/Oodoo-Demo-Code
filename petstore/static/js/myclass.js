
odoo.define('petstore.mcylass', function(require){
    'use strict';
    
    var Class = require('web.Class');
    var Widget = require('web.Widget');
    var Web = require('web.web');

    //var MyClass = Class.extend({
    //    init: function(name){
    //        this.name=name
    //    },
    //    say_hello: function() {
    //        console.log("hello",this.name);
    //    },
    //});

    //var MySpanishClass = MyClass.extend({
    //    say_hello: function() {
    //        this._super();
    //        console.log("translation in Spanish: hola", this.name);
    //    },
    //});


    var HomePage = Widget.extend({
        start: function() {
            //this.$el.append(QWeb.render("HomePageTemplate"));
            console.log("pet store home page loaded");
        },
    });


    //var my_object = new MySpanishClass("Michael");
    //my_object.say_hello();

    return HomePage;
});

