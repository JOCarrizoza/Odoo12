odoo.define('carwash.models', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    models.load_fields("res.partner", ["car_brand", "car_model", "car_color", "car_plates"]);

    models.load_models([
    {
        model: 'car.brands',
        condition: function(self){return true;},
        fields: ['name','models_ids'],
        loaded: function(self, brands){
            if(brands.length){
                self.car_brands = brands;
            }
        },

    },
    {
        model: 'car.models',
        condition: function(self){return true;},
        fields: ['name', 'brand_id'],
        //domain: function(self){return [['id','=', self.car_brands.models_ids]];},
        loaded: function(self, car_models){
            //console.log("brands")
            //console.log(self.car_brands.models_ids)
            if(car_models.length){
                // do operation as you like, here setting the value in a variable
                //self.set('brands', brands[0]);
                //console.log("models");
                //console.log(car_models);
                self.car_models = car_models;
            }
        },
        
    }],{'after': 'product.product'});

});