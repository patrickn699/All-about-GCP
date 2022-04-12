FROM golang:alpine as builder

ADD . /go/src/app
WORKDIR /go/src/app
RUN go get -u github.com/gorilla/mux
RUN go build -o main .


FROM alpine
WORKDIR /app
COPY --from=builder /go/src/app/ /app/
CMD ["/app/main"]