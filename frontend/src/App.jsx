import "./App.css";
import { useState, useRef } from "react";
import { useForm } from "react-hook-form";
function App() {
  const { register, handleSubmit, reset } = useForm();
  const [listQuestionAndAnswer, setListQuestionAndAnswer] = useState([]);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  const answerTemplate = (answer) => {
    return (
      <div className="mb-2 text-left">
        <div className="bg-gray-200 p-2 rounded-lg text-sm inline-block">
          {answer}
        </div>
      </div>
    );
  };

  const questionTemplate = (question) => {
    return (
      <div className="mb-2 text-right">
        <div className="bg-blue-500 text-white p-2 rounded-lg text-sm inline-block">
          {question}
        </div>
      </div>
    );
  };

  const scrollToBottom = () => {
    const timeOut = setTimeout(() => {
      bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }, 0);
    clearTimeout(timeOut);
  };

  const onSubmit = async (data) => {
    const { question } = data;
    setListQuestionAndAnswer((prev) => [...prev, questionTemplate(question)]);
    reset();
    scrollToBottom();
    setLoading(true);
    setLoading(false);
    setListQuestionAndAnswer((prev) => [
      ...prev,
    ]);
    scrollToBottom();
  };

  const TypingIndicator = () => {
    return (
      <div className="flex space-x-1">
        <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></span>
        <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-150"></span>
        <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-300"></span>
      </div>
    );
  };

  return (
    <div className="h-screen flex items-center justify-center">
      <div className="bg-white shadow-lg rounded-lg w-[800px]">
        <div className="bg-blue-500 text-white p-4 rounded-t-lg">
          <h1 className="text-lg font-bold">Chatbot Group 9</h1>
        </div>

        <div id="messages" className="p-4 h-96 overflow-y-auto">
          {listQuestionAndAnswer.map((data) => (
            <>{data}</>
          ))}
          <div ref={bottomRef}></div>
          {loading && answerTemplate(<TypingIndicator />)}
        </div>

        <form
          id="chat-form"
          className="flex p-4 border-t border-gray-200"
          onSubmit={handleSubmit(onSubmit)}
        >
          <input
            type="text"
            id="message-input"
            className="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Type your message..."
            required
            {...register("question")}
          />
          <button
            type="submit"
            className="ml-2 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
