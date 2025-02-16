# DeepSeek_Code_Finetuning

### 환경
OS : Window
GPU : 3060 * 2 (12GB)
Lang : Python - 3.10.12
Lib : Transformers, Datasets, Torch, Trl
Datasets : code_search_net - Python

#### 방법
DeepSeek-R1-Distill-Llama-8B 모델을 Lora와 양자화를 사용하여 FineTuning

### 한계
3060 * 2 으로는 양자화 후에도 Max_length 128  per_device_batch_size = 8, gradient_accumulation_steps=2로 학습 시 1epoch당 28시간 가량 소요
-> 해당 한계로 인해 현재는 code만 학습 추후 결과를 확인 후 docstring과 Max_lenth를 늘력 학습 예정
