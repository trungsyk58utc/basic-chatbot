# Bài tập lớn nhóm 9: Chatbot for basic customer

Thành viên nhóm:
- Đặng Trung Sỹ - 24025180 
- Nông Thái Sơn - 24025179

Công nghệ sử dụng
- Model AI: Ollama
- Frontend: ReactJS, Tailwind CSS

## Cài đặt và khởi chạy model AI 📦
Để khởi chạy hệ thống AI ollama cần
- Python (version 3 trở lên)
- Ollama (hệ thống AI được sử dụng cho dự án, chạy tại máy local)

1. Download model AI tại
```sh
https://ollama.com
```
2. Mở ollama
3. Mở terminal chạy lệnh sau
```sh
ollama run llama3.2:1
```
Nếu lần đầu khởi chạy, sẽ cần chờ hệ thống pull model về máy, thời gian sẽ tùy thuộc vào lượng parameter của model.
Như trong câu lệnh ở trên sẽ là 1b(1 tỷ) parameter. Bạn có thể thay thế bằng một model khác có dung lượng lớn hơn tùy
thuộc vào cấu hình máy. 

### Cài đặt và khởi chạy frontend 📦
Để khởi chạy được hệ thống chatbot bằng local cần
- Node.js version 20 trở lên
- npm version 10 trở lên
- yarn version 1.22 trở lên

1. Clone dự án
```sh
git clone https://github.com/trungsyk58utc/basic-customer-support-chatbot.git
```
2. Cài đặt node modules
```sh
yarn
```
- Nếu chưa cài đặt yarn thì chạy lệnh sau
```sh
npm i -g yarn
```
3. Khởi chạy dự án trên local
```sh
yarn dev
```
Dự án sẽ chạy tại local tại cổng 5173 theo đường dẫn:
```sh
http://localhost:5173
```