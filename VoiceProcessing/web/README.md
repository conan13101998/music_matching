### Họ và tên: Đỗ Xuân Anh
### MSSV: 16020192
### Lớp: K61-CA-CLC1

# Project: Music matching



### Link github: https://github.com/conan13101998/music_matching/tree/master/VoiceProcessing/web

### Link Youtube demo: https://youtu.be/DH7L9_aZEEw

### Ý tưởng tham khảo: [Shazam](https://www.shazam.com/apps)
## Mô tả dự án: 

- Đôi khi chúng ta đi ra quán cafe hoặc ở ngoài đường nghe được 1 đoạn nhạc nào đó rất hay nhưng lại không biết được tên bài hát để có thể tìm và tải về máy vậy nên project này giúp cho người dùng có thể thu âm 1 đoạn nhạc sau đó sẽ nhận lại được tên bài hát với điều kiện bài hát đó đã được phân tích và lưu trong CSDL của project.

- Dự án được phát triển dựa trên Python (chương trình phân tích, lưu trữ và nhận dạng bài hát) và Node.js (Web app để người dùng có thể thu âm đoạn nhạc cần nhận diện tên bài hát)

## Cách hoạt động của dự án:

- Phân tích và lưu trữ bài hát lên CSDL: với mỗi bài hát ta thực hiện các bước sau

    - Lấy ra spectrogram của bài hát
    - Tìm kiếm những điểm peak trong spectrogram (những điểm có giá trị cao hơn hẳn so với những điểm xung quanh)
    - Sử dụng hàm hash sha1 để mã hóa những spectrogram với đầu vào là tần số của những peaks và thời gian giữa các peaks. Với đầu vào như vậy ta luôn nhận được duy nhất 1 output duy nhất cho mọi lần tương ứng với 1 input và sẽ rất ít khi gặp những input có chung output
    - Lưu lại đoạn mã hóa vừa nhận được, chia theo thành nhiều offset và lưu vào CSDL
- Nhận diện bài hát:
    - Bước đầu tiên ta cũng làm tương tự với phân tích và lưu trữ bài hát là lấy ra spectrogram của đoạn ghi âm
    - Sử dụng hàm hash tương tự như trên, ta nhận được 1 output
    - Output này có thể tương ứng với 1 hoặc nhiều đoạn offset tồn tại sẵn trong CSDL với sự tương đồng khác nhau
    - Ta sẽ tính toán sự khác biệt giữa output nhận được từ đoạn ghi âm sau đó cho ra đoạn offset tồn tại trong CSDL giống với đoạn ghi âm nhất và kết luận bài hát cần tìm là bài hát có chứa đoạn offset đó
## Kết quả project: 

- Đã phát hiện được chính xác tên bài hát sau 5-10s thu âm.

- Hiện trong CSDL đang chứa bản ghi của 50 bài hát với 6896460 bản ghi đặc trưng

## Hướng dẫn sử dụng web (Yêu cầu bắt buộc phải có CSDL phân tích bài hát):

- Người dùng clone clone repo project từ github:
```
$ git clone https://github.com/conan13101998/music_matching/tree/master/VoiceProcessing/web
```
- Khởi chạy web server:
```
$ cd web
$ nodemon app.js
```
- Truy cập địa chỉ localhost:8080 từ trình duyệt

- Click vào nút thu âm và phát đoạn nhạc cần nhận diện tên bài hát

- Click nút stop để dừng thu âm và nhận lại kết quả là tên bài hát sau 3-5s
