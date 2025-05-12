import json
import os
from Generation_cfd_episode_info_Package import generation_cfd_episode_info
from Pic_generation_from_one_info_list_files_Package import pic_generation_from_cfd_record_episode_files
from Pic_generation_fom_total_reward_10_envs_Package import pic_generation_fom_total_reward_10_envs

# # The structure of the info_list is as follows:
# self.exec_info = {
#             "episode": self.num_episode,
#             "trajectory": self.num_trajectory,
#             "start_time_float": start_time_float,
#             "end_time_float": end_time_float,
#             "timestampStart": self.trajectory_start_time,
#             "timestampEnd": self.trajectory_end_time,
#             "current_trajectory_reward": reward,
#             "episode_reward": self.episode_reward,
#             "actions": new_action,
#             "cfd_running_time": simulation_end_time - simulation_start_time,
#             "number_cfd_timestep": int(
#                 np.around(
#                     (end_time_float - start_time_float) / self.foam_params["delta_t"]
#                 )
#             ),
#             "envName": self.foam_root_path.split("/")[-1],
#             "current_state": self.state_data[-2],
#             # 这里我有一些疑惑，运行实例文件的时候研究下，是否会报错
#             # 20250416
#             "next_state": next_state,
#         }
#         self.info_list.append(self.exec_info)

def pic_generation_for_all_info_list_files():

    generation_cfd_episode_info()

    cfd_episode_info_list_path = os.path.join(os.getcwd(), 'cfd_episode_info_list.json')    
    cfd_episode_info_list = json.load(open(cfd_episode_info_list_path))

    for env_info in cfd_episode_info_list:
        for env_name, episode_envno_reward in env_info.items():
            os.mkdir(env_name + "_pics")
            for episode_no, episode_reward in episode_envno_reward:
                pic_generation_from_cfd_record_episode_files(env_name, episode_no, episode_reward)
    
    pic_generation_fom_total_reward_10_envs(os.getcwd())

if __name__ == '__main__':
    pic_generation_for_all_info_list_files()