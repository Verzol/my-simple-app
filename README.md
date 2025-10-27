# Midterm - Thực hiện pipeline CI/CD sử dụng Github Actions và ArgoCD

## 1. Chuẩn bị

- 2 Repo GitHub: my-simple-app và https://github.com/Verzol/my-app-manifests (ArgoCD sẽ theo dõi repo này).
- Kubernetes Cluser (K8S) (Docker Desktop).
- Cài đặt ArgoCD (Kết nối K8S và Git).

## 2. Truy cập ArgoCD UI

<img width="1370" height="143" alt="image" src="https://github.com/user-attachments/assets/0213fcbb-f585-484a-8fe8-372d6fc0b305" />

Truy cập https://localhost:8080 để vào giao diện ArgoCD.

### Tạo Application trên ArgoCD UI

#### General:

- Application Name: my-simple-app
- Project Name: default
- Sync Policy: Automatic (và tích vào Prune Resources + Self Heal)

#### Source (Quan trọng nhất):

- Repository URL: Dán URL của repo my-app-manifests (ví dụ: https://github.com/dem-username/my-app-manifests.git).
- Revision: HEAD
- Path: . (nghĩa là dùng thư mục gốc của repo)

<img width="1919" height="880" alt="image" src="https://github.com/user-attachments/assets/b23d4e8f-eb3c-48e0-8fff-2e2ac510373d" />

#### Destination:

- Cluster URL: https://kubernetes.default.svc (nghĩa là deploy vào chính cluster mà ArgoCD đang chạy).
- Namespace: default

<img width="1919" height="878" alt="image" src="https://github.com/user-attachments/assets/61366607-356f-427d-ac0d-e52fea98dc09" />

## 3. Thiết lập Pipeline CI (GitHub Actions)

### Tạo PAT (Personal Access Token)

<img width="1919" height="882" alt="image" src="https://github.com/user-attachments/assets/046fbdfe-c55b-45c4-9863-a2b62f63bc84" />

### Thêm Action secrets

Thêm Secrets vào Repo: 

<img width="1919" height="875" alt="Screenshot 2025-10-27 112213" src="https://github.com/user-attachments/assets/57a73b9c-2c70-4a29-a424-9f7bcad591be" />

Tạo file .github/workflows/ci-cd-pipeline.yml:

<img width="1919" height="880" alt="image" src="https://github.com/user-attachments/assets/3cd56669-d4aa-471a-b3e5-5755837551fa" />

## 4. Test luồng chạy

Sửa trong app.py:

<img width="1919" height="1033" alt="image" src="https://github.com/user-attachments/assets/24b593b8-64f7-459b-82e5-44f9ea598b15" />

Sửa thành "2.0.0"

Push code lên lại repo GitHub "my-simple-app"
- Commit "Update text v2"

Xuất hiện 1 workflow mới trong tab "Actions":

<img width="1915" height="877" alt="image" src="https://github.com/user-attachments/assets/23b4586c-caeb-4cab-ad20-5a5c1ce19700" />

Có 2 jobs là build-and-push và update-manifest:

<img width="1919" height="884" alt="image" src="https://github.com/user-attachments/assets/b068165f-e430-4001-8666-50969fbf47dc" />

<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/def655e5-8750-4e00-9a8a-b55c80642a2d" />

Giao diện ArgoCD UI sau khi phát hiện thay đổi:

<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/f3cf0e72-7872-474c-b8fc-ac2c8cdd4182" />

Kiểm tra pods:

<img width="682" height="93" alt="image" src="https://github.com/user-attachments/assets/8b19bb01-9d74-4137-b0cf-78c2040daf00" />

Dùng 1 terminal mới chạy lệnh "kubectl port-forward svc/my-simple-app-service 9090:80" để kiểm tra. Sau khi chạy truy cập "http://localhost:9090":

<img width="1919" height="977" alt="image" src="https://github.com/user-attachments/assets/1c90ea78-93e1-4441-aa38-c85d240d61b8" />




