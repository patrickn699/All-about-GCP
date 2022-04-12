FROM golang:alpine AS Builder

#RUN mkdir /app
ADD . /go/src/app
WORKDIR /go/src/app
RUN apk add git
RUN go build -o main . 

FROM alpine
WORKDIR /app
COPY --from=Builder /go/src/app/ /app/
CMD ["/app/main"]  


