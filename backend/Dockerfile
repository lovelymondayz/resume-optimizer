FROM golang:1.18-alpine AS builder

RUN apk add --no-cache gcc musl-dev

WORKDIR /app

COPY go.mod ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=1 GOOS=linux go build -o server ./cmd/server

FROM alpine:3.18

WORKDIR /app

RUN apk add --no-cache ca-certificates curl

COPY --from=builder /app/server .

RUN mkdir -p /app/data /app/output

EXPOSE 8000

CMD ["./server"]

# Run as non-root
USER 1000:1000
