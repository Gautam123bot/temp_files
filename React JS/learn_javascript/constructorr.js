class RailwayForm{
    submit(){
        alert(this.name + ": Your form si submitted for train number: " + this.trainno)
    }
    cancel(){
        alert(this.name + ": This form is cancelled for train number: " + this.trainno)
    }
    fill(name, trainno){
        this.name=name
        this.trainno=trainno
    }
}


let harryForm = new RailwayForm()

let rohanForm1 = new RailwayForm()
let rohanForm2 = new RailwayForm()

rohanForm1.fill("Rohan", 222420)
rohanForm2.fill("Rohan", 2229211)

harryForm.submit()
rohanForm1.submit()
rohanForm2.submit()
rohanForm1.cancel()