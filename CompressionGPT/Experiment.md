# Lossy Compression of Language Model Context Using Black Box Summarization

## Research Question
**How can context be effectively compressed while retaining or exceeding performance of an uncompressed control?**

## Hypothesis
**Language model context can be compressed effectively using summarization and have comparable performance to the uncompressed control.**

## Design
The experiment will follow two groups of ChatGPT clone configurations, a control and an experimental group. All configurations will support and be tested with the `gpt-3.5-turbo` and `gpt-4` models from OpenAI.

#### Control Configuration Group:
The control configuration will work at a simple terminal-based chat interface for ChatGPT. The interface will utilize a `message` object with the following schema:

```ts
interface Message {
    role: "system" | "user" | "assistant";
    content: string;
}
```

The OpenAI API accepts an array of `message` objects as input. Therefore, as the conversation progresses, the `messages` array will grow, and be sent to the OpenAI API with every prompt.

#### Experimental Configuration Group: