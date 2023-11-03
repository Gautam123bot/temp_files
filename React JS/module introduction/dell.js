import { Computer } from "./computer.js"

class Dell extends Computer{
    constructor(name,company){
        super(name)
        this.company=company
    }

    logIn(){
        console.log("You are looged into a Dell "+this.name)
    }
}

export default Dell