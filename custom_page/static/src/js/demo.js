odoo.define("custom_page.home_page",function(require){
    var core = require('web.core');
    var Widget = require('web.Widget');
    var data = require('web.data');
    var HomePage=Widget.extend({
        template:'counterBtnTemp',
        className:'oe_demo_homepage',
        init:function(parent){
            this._super(parent);
            this.Name='NameTest';
        },
        start:function(){
            var self=this;
            console.log('demo homepage widget');
            self.$el.append('<div>homepage widget</div>');
        },
    });
    core.action_registry.add('demo_home_page',HomePage);
    return HomePage;
});