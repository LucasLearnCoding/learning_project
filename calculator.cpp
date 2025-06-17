  #include <iostream>
  #include <string>
  #include <cctype>
  using namespace std;

  // Hàm xử lý thứ tự ưu tiên nhân chia trước
  string xu_ly_thu_tu(string pheptinh) {
      // Xử lý nhân chia trước
      for (int i = 0; i < pheptinh.length(); i++) {
          if (pheptinh[i] == 'x' || pheptinh[i] == '/') {
              // Tìm số bên trái
              int left_start = i - 1;
              while (left_start >= 0 && isdigit(pheptinh[left_start])) {
                  left_start--;
              }
              left_start++;
              
              // Tìm số bên phải
              int right_end = i + 1;
              while (right_end < pheptinh.length() && isdigit(pheptinh[right_end])) {
                  right_end++;
              }
              
              // Lấy số trái và phải
              int so_trai = 0, so_phai = 0;
              for (int j = left_start; j < i; j++) {
                  so_trai = so_trai * 10 + (pheptinh[j] - '0');
              }
              for (int j = i + 1; j < right_end; j++) {
                  so_phai = so_phai * 10 + (pheptinh[j] - '0');
              }
              
              // Tính toán
              int ket_qua_tinh;
              if (pheptinh[i] == 'x') {
                  ket_qua_tinh = so_trai * so_phai;
              } else {
                  if (so_phai == 0) {
                      cout << "Lỗi: Không thể chia 1 số cho 0!";
                      return "";
                  }
                  ket_qua_tinh = so_trai / so_phai;
              }
              
              // Thay thế trong chuỗi
              string phan_truoc = pheptinh.substr(0, left_start);
              string phan_sau = pheptinh.substr(right_end);
              pheptinh = phan_truoc + to_string(ket_qua_tinh) + phan_sau;
              i = left_start + to_string(ket_qua_tinh).length() - 1;
          }
      }
      
      return pheptinh;
  }



  int main() {
    string pheptinh;
  int so;
  int so2 = 0;
  int so_moi;
  int ket_qua = 0;
  auto cong = [](float a,float b) {return a+b;};
  auto tru = [](float a,float b) {return a-b;};
  auto nhan = [](float a,float b) {return a*b;};
  auto chia = [](float a,float b) {return a/b;};
  cout << "Hãy nhập vào phép tính của bạn: \n";
  getline(cin, pheptinh);
  pheptinh = xu_ly_thu_tu(pheptinh);
      if (pheptinh.empty()) return 0;
  for (int i = 0; i < pheptinh.length(); i++) {
    if(isdigit(pheptinh[i])){
      so = pheptinh[i] - '0';
      if (i > 0) {
      if (isdigit(pheptinh[i-1])) {
        ket_qua = ket_qua*10 + so;
      }
      else {
        switch(pheptinh[i-1]) {
          int n;
          case '+':
              n = 0;
                so2 = 0;
          while (i+n<pheptinh.length() && isdigit(pheptinh[i +n])) {
          so_moi = pheptinh[i+n] - '0';
          so2 = so2*10 +so_moi;
          n++;
          }
          ket_qua = cong(ket_qua,so2);
          i += n -1;
          break;
          case '-':
              n = 0;
                so2 = 0;
          while (i+n<pheptinh.length() && isdigit(pheptinh[i +n])) {
          so_moi = pheptinh[i+n] - '0';
          so2 = so2*10 +so_moi;
          n++;
          }
          ket_qua = tru(ket_qua,so2);
          i += n -1;
          break;
          case 'x':
              n = 0;
                so2 = 0;
          while (i+n<pheptinh.length() && isdigit(pheptinh[i +n])) {
          so_moi = pheptinh[i+n] - '0';
          so2 = so2*10 +so_moi;
          n++;
          }
          ket_qua = nhan(ket_qua,so2);
          i += n -1;
          break;

          case '/':
          n = 0;
                so2 = 0;
          while (i+n<pheptinh.length() && isdigit(pheptinh[i +n])) {
          so_moi = pheptinh[i+n] - '0';
          so2 = so2*10 +so_moi;
          n++;
          }
          if (so2 == 0) {
            cout << "Lỗi: Không thể chia 1 số cho 0!";
            break;
          }
          ket_qua = chia(ket_qua,so2);
          i += n -1;
          break;
        }
      }
      } else {
        ket_qua = so;
      }
    }
  }
  cout << ket_qua;
  return 0;
  }
