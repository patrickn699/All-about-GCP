package main

import (
	"demo/convert"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"
)


func main(){

	fmt.Println("Hello World, from main")

	mux := http.NewServeMux()
	mux.HandleFunc("/convert", cont)
	fmt.Println("conversion service is listening on port http://localhost:9000")
	log.Fatal(http.ListenAndServe(":9000", mux))
	
}

func cont(w http.ResponseWriter, r *http.Request){
	if r.Method != "POST" {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	file, header, err := r.FormFile("file")
	check_error(err)
	height := r.FormValue("height")
	width := r.FormValue("width")
	percent := r.FormValue("percent")
	watermark := r.FormValue("watermark")
	fmt.Println(height)
	height_int, err := strconv.Atoi(height)
	check_error(err)
	width_int, err := strconv.Atoi(width)
	check_error(err)
	percent_int, err := strconv.Atoi(percent)
	check_error(err)
	watermark_int, err := strconv.Atoi(watermark)
	defer file.Close()
	fmt.Println(header.Filename)
	f, err := os.OpenFile("./received/"+header.Filename, os.O_WRONLY|os.O_CREATE, 0666)
	check_error(err)
	io.Copy(f, file)
	convert.Convert_file("received/"+header.Filename,height_int,width_int,percent_int,watermark_int, header.Filename)
	convert.SendImageasPost()
}

func check_error(err error){
	if err != nil {
		log.Fatal(err)
	}
}