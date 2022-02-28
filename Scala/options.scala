object options extends App {


person("abc",Some("dcd"))



def person( fname: String, lname: Option[String] ) = {
lname match {

case Some(lname) => println(lname)
case None => println("some problems")


}

}


}



