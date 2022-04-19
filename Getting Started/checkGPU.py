import torch

print(f"Is cuda available? {torch.cuda.is_available()}")
print(f"Number of GPUs: {torch.cuda.device_count()}")
curr_dev = torch.cuda.current_device()
print(f"Current device: {curr_dev}")
print(f"Device location: {torch.cuda.device(curr_dev)}")
print(f"Name of GPU: {torch.cuda.get_device_name(curr_dev)}")
