package gcp_api_gateway

import (
	"fmt"
	"net/http"
)

// HelloGet is an HTTP Cloud Function.
func Hello_go(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello, World!, From Go")
}