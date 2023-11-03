function mobile() {
    this.model = "2210";
    this.price=function() {
        document.writeln(this.model + "Price Rs. 3000");        
    }

}

var samsung=new mobile();
samsung.price();