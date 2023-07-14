package cli

type ChatCompletionMessageRoles string

const (
	Assistant ChatCompletionMessageRoles = "assistant"
	User      ChatCompletionMessageRoles = "user"
	System    ChatCompletionMessageRoles = "system"
)

type Chat struct {
	role    ChatCompletionMessageRoles
	content string
	model   string
}

type Conversation struct {
	id                      int
	file                    string
	model                   string
	history                 []Chat
	compressed              bool
	summarization_technique string
}

type model struct {
	conversations []Conversation
}
