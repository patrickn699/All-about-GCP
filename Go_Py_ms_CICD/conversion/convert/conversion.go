package convert

import (
	"bytes"
	"fmt"
	"image"
	"image/jpeg"
	"image/png"
	"io"
	"io/ioutil"
	"mime/multipart"
	"net/http"
	"os"
)

func Convert_file(img string, height,width,percent,watermark int, filename string){

	fmt.Println("Converting file: ", img)
	
	//fil, er := os.OpenFile("ccd/output.png", os.O_RDWR|os.O_CREATE, 0666)
	//fmt.Println(fil)
	//check_error(er)
	//err := os.Mkdir("./converted", os.ModePerm)
	//check_error(err)

	opend, err := os.Open(img)
	check_error(err)

	_, format, err := image.DecodeConfig(opend)
	check_error(err)

	if format == "jpeg" || format == "jpg" {
		fmt.Println("File is jpeg")
		opend.Seek(0, 0)
		img, err := jpeg.Decode(opend)
		check_error(err)
		my_sub_image := img.(interface {
			SubImage(r image.Rectangle) image.Image
		}).SubImage(image.Rect(height, width, percent, watermark))
	
		output_file, outputErr := os.Create("output.png")
		check_error(outputErr)
		png.Encode(output_file, my_sub_image)
	
	} else if format == "png" {
		fmt.Println("File is png")
		opend.Seek(0, 0)
		img, err := png.Decode(opend)
		check_error(err)
		my_sub_image := img.(interface {
			SubImage(r image.Rectangle) image.Image
		}).SubImage(image.Rect(height, width, percent, watermark))
	
		output_file, outputErr := os.Create("output.png")
		check_error(outputErr)
		png.Encode(output_file, my_sub_image)
		//saved, er1 := os.OpenFile("output.png",os.O_RDWR|os.O_CREATE, 0666)
		//check_error(er1)
		//by,e := io.Copy(fil, saved)
		//check_error(e)
		//fmt.Println("Bytes written: ", by)
	}

}

func SendImageasPost(){

	file, err := os.Open("output.png")
	check_error(err)
	defer file.Close()

	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)
	part, err := writer.CreateFormFile("image", "output.png")
	check_error(err)

	_, err = io.Copy(part, file)
	check_error(err)
	writer.Close()
    ur := os.Getenv("FRONT_SERVICE_HOST")
	po := os.Getenv("FRONT_SERVICE_PORT")
	url := "http://"+ur+":"+po+"/uploaded"
	//"http://0.0.0.0:5000/uploaded"
	request, err := http.NewRequest("POST",url, body)
	check_error(err)
	

	request.Header.Add("Content-Type", writer.FormDataContentType())
	client := &http.Client{}
	response, err := client.Do(request)
	check_error(err)
	//fmt.Println(request.Body)

	
	fmt.Println("from send data")
	content, err := ioutil.ReadAll(response.Body)
	check_error(err)
	fmt.Println(string(content))
	defer response.Body.Close()


}


func check_error(err error){
	if err != nil {
		fmt.Println(err)
	}
}