# DeepSeek_Code_Finetuning

### 환경
OS : Window
GPU : 3060 * 2 (12GB)
Lang : Python - 3.10.12
Lib : Transformers, Datasets, Torch, Trl
Datasets : code_search_net - Python

#### 방법
DeepSeek-R1-Distill-Llama-8B 모델을 Lora와 양자화를 사용하여 FineTuning

### 파라미터
3060 * 2 으로는 양자화 후에도 
* Max_length = 128
* per_device_batch_size = 8
* gradient_accumulation_steps = 2
* 학습 시 1epoch당 28시간 가량 소요

---

같은 하드웨어 환경 데이터 Docstring 추가 파라미터 변경
3060 * 2 으로는 양자화 후에도 
* Max_length = 512
* per_device_batch_size = 2
* gradient_accumulation_steps = 2
* 학습 시 1epoch당 122시간 가량 소요
* 결과 TrainOutput(global_step=103044, training_loss=1.2967534739197164, metrics={'train_runtime': 442653.9183, 'train_samples_per_second': 0.931, 'train_steps_per_second': 0.233, 'total_flos': 9.507085746142446e+18, 'train_loss': 1.2967534739197164, 'epoch': 0.9999951477274381})

### 🚀 모델 학습 결과

#### 📌 학습 개요  
- **총 학습 스텝**: `103,044`  
- **총 학습 시간**: `약 123시간 (442,653초)`  
- **에포크(epoch)**: `1`  
- **최종 손실 값 (Loss)**: `1.2967`  

## 📊 학습 지표  

| 메트릭 | 값 | 설명 |
|--------|--------------------------|-----------------------------------------------|
| **global_step** | `103044` | 총 학습 스텝 수 |
| **training_loss** | `1.2967` | 최종 손실 값 (낮을수록 성능 향상) |
| **train_runtime** | `442,653.9183 초` | 전체 학습 소요 시간 (약 123시간) |
| **train_samples_per_second** | `0.931` | 초당 처리한 샘플 수 |
| **train_steps_per_second** | `0.233` | 초당 처리한 스텝 수 |
| **total_flos** | `9.51 × 10¹⁸ FLOPs` | 총 연산량 (FLOPs: Floating Point Operations) |
| **epoch** | `0.99999` | 학습된 에포크 수 (≈ 1 에포크) |

## 🔍 분석 및 개선 방안  
- 학습 속도가 상대적으로 느리므로, **배치 크기 증가, 데이터 로딩 최적화, GPU 성능 향상** 등을 고려
- 손실 값을 더 낮추려면, **학습률 조정, 데이터 증강(Augmentation), 모델 구조 개선** 등을 시도 
