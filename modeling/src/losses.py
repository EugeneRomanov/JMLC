from dataclasses import dataclass
from typing import List
import torch
from torch import nn
from config import LossConfig 
from train_utils import load_object 


@dataclass
class Loss:
    name: str
    weight: list # float
    loss: nn.Module

def get_losses(losses_cfg: List[LossConfig]) -> List[Loss]:
    return [
        Loss(
            name=loss_cfg.name,
            weight=torch.tensor(loss_cfg.weight,device='cuda:0'), 
            loss=load_object(loss_cfg.loss_fn)(**loss_cfg.loss_kwargs),
        )
        for loss_cfg in losses_cfg
    ]
