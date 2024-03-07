import sys
import os
tensor_path = os.path.abspath(os.path.join(os.path.basename(__file__), os.pardir, os.pardir, os.pardir))
sys.path.append(tensor_path)

import random 
from typing import Dict, List, Mapping, Tuple, Set
from entity_gym.env import Observation
from entity_gym.runner import CliRunner
from entity_gym.env import *
from TensorRTS import Agent
from enn_trainer import load_checkpoint, RogueNetAgent

class SwagBot(Agent):
    def __init__(self, init_observation : Observation, action_space : Dict[ActionName, ActionSpace]) -> None: 
        super().__init__(init_observation, action_space)
        checkpoint = load_checkpoint("./checkpoint")
        self.current = RogueNetAgent(checkpoint.state.agent)

    def take_turn(self, current_game_state : Observation) -> Mapping[ActionName, Action]:
        return self.current.act(Observation)
    
    def on_game_start(self) -> None:
        return super().on_game_start()
    
    def on_game_over(self, did_i_win : bool, did_i_tie : bool) -> None:
        return super().on_game_over(did_i_win, did_i_tie)
    
def agent_hook(init_observation : Observation, action_space : Dict[ActionName, ActionSpace]) -> Agent: 
    return SwagBot(init_observation, action_space)

def student_name_hook() -> str: 
    return 'Jansen'
