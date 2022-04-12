package main

import ("fmt"
		"net/http"
		"html/template"
		"github.com/gorilla/mux"
		)

var t1 *template.Template
var t2 *template.Template

func main() {

	

	r := mux.NewRouter()

	t1 = template.Must(template.ParseFiles("templates/index.html"))
	t2 = template.Must(template.ParseFiles("templates/about.html"))

	r.HandleFunc("/", Home)
	r.HandleFunc("/about", About)
	fmt.Println("Server is running on http://localhost:8005")
	http.ListenAndServe(":8005", r)
}


func Home(w http.ResponseWriter, r *http.Request) {
	
	//check(err)
	t1.Execute(w, nil)


	
}

func About(w http.ResponseWriter, r *http.Request) {
	//fmt.Fprintf(w, "Welcome to the About page!")
	t2.Execute(w, nil)

}

