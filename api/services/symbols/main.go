package main

import (
	"context"
	"encoding/json"
	"fmt"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"net/http"
)

type symbol struct {
	Id          string `json:"id"`
	Symbol      string `json:"symbol"`
	CompanyName string `json:"companyName"`
}

var symbols = []symbol{
	{Id: "1", Symbol: "AAPL", CompanyName: "Apple"},
}

func main() {
	router := gin.Default()
	router.GET("/symbols", getSymbols)
	//router.GET("/symbols/:id", getAlbumByID)
	//router.POST("/symbols", postAlbums)
	//router.Run("localhost:8080")

	client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI("mongodb://admin:admin@0.0.0.0:27017/symbols"))
	if err != nil {
		panic(err)
	}
	defer func() {
		if err := client.Disconnect(context.TODO()); err != nil {
			panic(err)
		}
	}()
	coll := client.Database("symbols").Collection("symbols")
	title := "Back to the Future"
	var result bson.M
	err = coll.FindOne(context.TODO(), bson.D{{"title", title}}).Decode(&result)
	if err == mongo.ErrNoDocuments {
		fmt.Printf("No document was found with the title %s\n", title)
		return
	}
	if err != nil {
		panic(err)
	}
	jsonData, err := json.MarshalIndent(result, "", "    ")
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", jsonData)
}

func getSymbols(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, symbols)
}
