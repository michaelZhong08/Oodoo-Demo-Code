// in file a.js
odoo.define('todo.todo_Widget_Conuter', function (require) {
    "use strict";

    //var widgetRegistry = require('web.widget_registry');
    var Widget = require('web.Widget');

    var Counter1 = Widget.extend({
        //template: 'todo.counterBtnTemp',
        //events: {
        //    'click button': '_onClick',
        //},
        init: function (parent) {//value
            this._super(parent);
            //this.count = 1;
        },
        //_onClick: function () {
        //    this.count++;
        //    this.$('.val').text(this.count);
        //},
        //willStart:function(){
        //    console.log('this is willStart');
        //},
        start:function(){
            console.log('todo counter1 widget');
            this.$el.append('<div>todo counter1 widget</div>');
            var counter2 = new Counter2(this);
            counter2.appendTo(this.$el);
        },
    });

    var Counter2=Widget.extend({
        template: 'counterBtnTemp',
        init: function (parent) {//value
            this._super(parent);
            this.count = 1;
        },
        start:function(){
            console.log('todo counter2 widget');
        },
    })
// Create the instance
var counter1 = new Counter1(this);
// Render and insert into DOM
counter1.appendTo($('.some-div'));

return Counter;
});