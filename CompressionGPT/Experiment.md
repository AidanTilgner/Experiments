# Lossy Compression of Language Model Context Using Black Box Summarization

## Research Question

**How can context be effectively compressed while retaining or exceeding performance of an uncompressed control?**

## Hypothesis

**Language model context can be compressed effectively using summarization and have comparable performance to the uncompressed control.**

## Design

The experiment will follow two groups of ChatGPT clone configurations, a control and an experimental group. All configurations will support and be tested with both the `gpt-3.5-turbo` and `gpt-4` models from OpenAI.

### Control Configuration Group:

The control configuration will work as a simple terminal-based chat interface for ChatGPT. The interface will utilize a `message` object with the following schema:

```ts
interface Message {
  role: "system" | "user" | "assistant";
  content: string;
}
```

The [OpenAI chat completions API](https://platform.openai.com/docs/api-reference/chat) accepts an array of `message` objects as input. Therefore, as the conversation progresses, the `messages` array will grow, and be sent to the OpenAI API with every prompt. This is meant to mimic that way that most chat applications that utilize OpenAI's chat models will behave.

### Experimental Configuration Group:

There may be multiple different experimental configurations. For now we'll start with two. Both will utilize a summarization technique, which will reduce the number of tokens sent to the API per request. Other than the summarization technique, the configuration will be identical to the default.

#### Summarization Function

The summarization function will utilize an LLM to summarize, which will be recorded as part of the summarization function. The additional overhead of the summarization model will be tracked.

#### Summarization Techniques

- Conversation Essence Summarization: The first summarization technique will try to preserve the essence of the conversation as a whole. This will include overarching themes, important subjects, key events, etc. Precision is not the goal here, but rather keeping the natural, conversational tone. The summarization function will take the `messages` array, and return a summarization no more than a fixed amount of tokens in length. This will then be injected into either the `user` message, or the `system` messsage. This will effectively mimic a `one-shot` prompt, but will preserve conversation context due to the summary.

- Conversation Precision Summarization: The second summarization technique will focus on preserving precision, and instead of creating one big summary of the conversation, will instead preserve the initial `messages` array, but summarize each individual message into a more concise version of itself. The summarization function will also specifically instruct the LLM to preserve any information where precision may be considered important, and wouldn't be preserved by reference. For example, a number or an equation, vs a quote from a famous author. An equation or number would be difficult for an LLM to recall by reference, whereas a quote from a famous author likely already exists in its training set.

## Variables

This experiment aims to evaluate the performance of LLMs with various levels of compression of the context they operate on. The independent variables are as follows and will be recorded for each configuration:

- `The language model`: gpt-4 or gpt-3.5-turbo
- `The inclusion of a summarization function`: control or experimental group
- `The summarization function used, if applicable`: multiple summarization functions will be used

With the goal of testing the performance of each configuration, the following dependent variables will be tracked:

- `Average number of tokens sent to the chat LLM per user message`: the number of tokens sent and received when requesting a chat completion
- `Average number of tokens sent to the summarization model per user message`: the number of tokens sent and received when summarizing the chat history
- `Average number of tokens used per user message (total)`: the total number of tokens used in both summarization and chat completion for a user message
- `User satisfaction with the chat response`: a 1-5 scale measuring satisfaction
  1: Does not meet expectations
  2: Somewhat meets expectations
  3: Meets expectations
  4: Somewhat exceeds expectations
  5: Exceeds expectations
- `Chat response quality`: this will involve multiple factors:
  `Correctness`: the accuracy of objective statements made by the model
  `Correctness on context`: how accurately the model utilizes important contextual information from the chat history
  `Contextual sensitivity`: the model's ability to reference prior statements and draw from context
  `Coherence`: from chat to chat, are the bot's messages logically connected?
- `Total cost per user message`: the cost for every user submitted message
- `Average cost per user message`: the average cost per user message for a configuration

## Testing
The experiment will employ a custom testing setup, which will allow a single prompt to be tested on a variable number of configurations concurrently. When a user submits a response, every configuration will process the request concurrently, and log all of the dependant variables. This technique will minimize the impact of confounding variables, such as current API load, and overall allow for a better tester experience.

