package chat

import (
	"context"
	"fmt"
	"os"

	dotenv "github.com/joho/godotenv"
	openai "github.com/sashabaranov/go-openai"
)

func getAPIKEY() string {
	err := dotenv.Load()
	if err != nil {
		panic(err)
	}
	return os.Getenv("OPENAI_API_KEY")
}

func getOpenAIClient() *openai.Client {
	return openai.NewClient(getAPIKEY())
}

func GetChatCompletion(messages []openai.ChatCompletionMessage, model string) string {
	client := getOpenAIClient()

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model:    model,
			Messages: messages,
		},
	)

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(resp)
	}

	return resp.Choices[0].Message.Content
}
