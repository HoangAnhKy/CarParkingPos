<div align="center">
<h1> NGHIÊN CỨU ỨNG DỤNG PHÁT HIỆN VÀ ĐẾM CHỖ TRỐNG BÃI GIỮ XE THÔNG QUA HỆ THỐNG CAMERA AN NINH </h1>

</div>

Tóm tắt
Nghiên cứu xây dựng ý tưởng áp dụng kỹ thuật xử lý ảnh trong thư viện mã nguồn mở OpenCV và ngôn ngữ lập trình Python để viết chương trình phát hiện và đếm chỗ trống bãi đỗ xe. Kết quả là video hiển thị số lượng chỗ giữ xe còn trống. 
Từ khóa: OpenCV, Python, đếm chỗ trống, bãi giữ xe.

<div>
  <h3> 1.	Mở đầu </h3> 
Đi cùng với tốc độ tăng trưởng dân số thì các trung tâm thương mại, khu dân cư, chung cư cũng mọc lên với tốc độ rất nhanh. Từ đó nhu cầu chỗ đỗ xe cũng tăng cao và quy mô của các khu đỗ xe cũng vậy. Câu hỏi thường gặp khi các chủ xe thấy bãi đỗ xe đông là: “Ở đây có còn chỗ trống để đỗ xe không” và các bảo vệ hay nhân viên phải kiểm tra bằng cách đi từ đầu đến cuối bãi đỗ hoặc phải check từng camera dẫn tới việc này mất rất nhiều thời gian. Ở thời đại 4.0 họ có thể dùng các phần mềm chuyên dụng để hỗ trợ cho các bảo vệ hay nhân viên giữ xe. Từ đó ứng dụng ở bài nghiên cứu này được đưa vào thực hiện bằng ngôn ngữ Python kèm theo đó là sự hỗ trợ của thư viện OpenCV với chức năng chính là phát hiện và đếm số lượng chỗ trống trong bãi đỗ xe. OpenCV có khả năng xử lý ảnh để đưa ảnh về 2 màu đen trắng, sau đó dựa vào số lượng điểm sáng để có thể xác định vị trí đó có vật thể nào không, rồi từ đó xác định chỗ trống bằng cách đưa ra các vị trí có tần suất điểm sáng thấp hoặc không có điểm sáng. Tuy nhiên cũng có một cách khác là gắn các thiết bị cảm biến ở từng vị trí đỗ xe, nhưng nó lại không tối ưu vì không cung cấp cụ thể vật thể mà máy cảm biến nhận dạng là xe hay là một con vật kèm theo đó là mức chi phí cao, còn ở kỹ thuật xử lý ảnh mà chúng tôi sắp áp dụng ở đây thì có thể khắc phục hoàn toàn điểm yếu của phương thức trên.
</div>
<div>
<h3> 2. Nội dung </h3> 
Xây dựng một chương trình có chức năng phát hiện và đếm chỗ trống của bãi đỗ xe. Chúng tôi sẽ dùng 1 package của python đó là pickle để lưu lại 1 array chứa các vị trí đỗ xe trong bãi. Sau đó, chúng tôi sẽ kiểm tra với hình ảnh được đưa vào từ camera để xác định số lượng chỗ trống trong bãi đỗ xe.
<h3> 2.1 Tạo danh sách lưu vị trí vùng quan sát các chỗ đỗ xe</h3>
       Hãy đảm bảo rằng vị trí camera đặt cố định không thay đổi, chúng tôi sẽ lấy 1 hình chụp bãi xe từ camera. Khi chương trình chạy bức hình sẽ được mở lên để xử lý. Sau đó chúng tôi tiến hành  click chuột vào hình để tạo các vùng quan sát lưu các vị trí của bãi đổ xe và các vị trí đó sẽ được lưu xuống file danh sách vị trí quan sát các chỗ đỗ xe tên là carParkingPos.
       
  <div align="center">
  <img src="https://github.com/HoangAnhKy/CarParkingPos/blob/main/image/%E1%BA%A2nh%20x%E1%BB%AD%20l%C3%BD%20t%E1%BA%A1o%20v%C3%B9ng%20quan%20s%C3%A1t.png" alt="html logo"/>
  
Hình 1. Ảnh xử lý tạo vùng quan sát
 </div>
  
  <h3> 2.2. Đếm vị trí chỗ trống trong bãi đỗ xe. </h3> 
	Sau khi đã có danh sách carParkingPos, chúng tôi chạy chương trình chính. Bước 1, tôi import video của bãi đỗ xe. Video tôi sử dụng là 1 file mp4 trích xuất từ camera . Bước 2, chúng tôi dùng danh sách carParkingPos để đưa vào xử lý video. Chương trình sẽ vẽ trực tiếp lên đoạn video đang được phát. Bước 3, Khi có xe ở trong vùng quan sát chương trình sẽ xử lý dựa vào điểm sáng để video có thể hiển thị những chỗ có thể đỗ xe (màu xanh), không thể đỗ xe (màu đỏ) , chỗ đỗ xe không hợp lệ (màu cam) và đếm số lượng chỗ còn trống trên tổng số lượng chỗ đỗ xe của bãi đồng thời đưa ra cảnh báo về số chỗ đỗ xe không hợp lệ.
 
 
<div align="center">
  <img src="https://github.com/HoangAnhKy/CarParkingPos/blob/main/image/%E1%BA%A2nh%20ph%C3%A2n%20t%C3%ADch%20video%20nh%E1%BB%8B%20ph%C3%A2n%20x%E1%BB%AD%20l%C3%BD%20d%E1%BB%B1a%20v%C3%A0o%20%C4%91i%E1%BB%83m%20s%C3%A1ng.png"/>
  
<p>Hình 2. Ảnh phân tích video nhị phân xử lý dựa vào điểm sáng</p>
   </div>
  <div align="center">
    <img src="https://github.com/HoangAnhKy/CarParkingPos/blob/main/image/%E1%BA%A2nh%20video%20x%E1%BB%AD%20l%C3%BD%20ho%C3%A0n%20ch%E1%BB%89nh%20ph%C3%A1t%20hi%E1%BB%87n%20v%C3%A0%20%C4%91%E1%BA%BFm%20ch%E1%BB%97%20tr%E1%BB%91ng.png"/>
  
<p>Hình 2.1. Ảnh video xử lý hoàn chỉnh phát hiện và đếm chỗ trống</p>
 </div>
 
<h3> 2.3. Mô tả thuật toán  </h3>

  <p> *Thuật toán tạo vùng quan sát : </p>
 
   <div align="center">
  <img src="https://github.com/HoangAnhKy/CarParkingPos/blob/main/image/%E1%BA%A2nh%20thu%E1%BA%ADt%20to%C3%A1n%20l%C6%B0u%20%C4%91%E1%BB%93%20t%E1%BA%A1o%20v%C3%B9ng%20quan%20s%C3%A1t.png"/>
  

Hình 3. Ảnh thuật toán lưu đồ tạo vùng quan sát
 </div>
Đối với thuật toán tạo vùng quan sát (Vùng nhận dạng) được tạo áp dụng lưu đồ hình 3. Vùng quan sát đã tạo sẽ được lưu vào danh sách vị trí (CarParkingPos). Chúng tôi cũng có thể xóa các vùng quan sát nếu vị trí lựa chọn chưa hợp lý. 

  <p> *Thuật toán kiểm tra chỗ đậu xe </p>
<div align="center">
  
  <img src="https://github.com/HoangAnhKy/CarParkingPos/blob/main/image/%E1%BA%A2nh%20l%C6%B0u%20%C4%91%E1%BB%93%20thu%E1%BA%ADt%20to%C3%A1n%20ki%E1%BB%83m%20tra%20b%C3%A3i%20%C4%91%E1%BB%97%20xe.png"/>
  
Hình 4. Ảnh lưu đồ thuật toán kiểm tra bãi đỗ xe
</div>
Chúng tôi nhận diện phương tiện là car dựa vào vùng quan sát do camera phát hiện. Vật thể được nhận diện trải qua các bước như trên lưu đồ và sau đó phân theo loại. Theo góc quay của camera trong trường hợp của chúng tôi thì nếu vật thể được hiển thị trong vùng quan sát có kích thước nhỏ hơn 300 px thì vùng quan sát hiển thị có màu xanh (chỗ đỗ xe trống). Nếu vật thể hiển thị trong vùng quan sát có kích thước lớn hơn hoặc bằng 300 px và nhỏ hơn 1400 px thì vùng quan sát hiển thị có màu cam (chỗ đỗ xe có xe đỗ không hợp lệ hoặc có vật thể lạ). Trường hợp còn lại thì vùng quan sát hiển thị màu đỏ (chỗ đỗ xe này đã có xe đỗ). Cuối cùng hiển thị thông báo số chỗ đỗ xe còn trống và cảnh báo số chỗ đỗ xe đang xảy ra sự cố vấn đề. 
  
 </div>
 <div>
  <h3> 3.Kết luận </h3>
Ý tưởng chương trình đếm chỗ trống bãi đỗ xe được xây dựng nhờ việc áp dụng kỹ thuật xử lý ảnh trong OpenCV và ngôn ngữ lập trình Python. Đây là một chương trình được sử dụng để giúp các bãi đỗ xe thêm phần linh hoạt và tự động hóa, có thể hỗ trợ rất nhiều cho nhân viên hay bảo vệ giám sát bãi đỗ xe. Qua đó định hướng nghiên cứu tiếp theo là điều chỉnh thích nghi với việc tải trực tiếp video từ camera. Canh chỉnh các thông số, tối ưu hóa phần mềm để trở nên phù hợp với nhiều bãi đỗ xe khác nhau. 
 </div>

