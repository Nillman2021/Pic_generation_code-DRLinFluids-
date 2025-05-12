# Pic_generation_code-DRLinFluids-
This code is made to draw some pics, which use the data generaterd in the DRLinFluids simulation process.

We donot need care about the code that end with "Package", what only useful is the code end with "Run", yes, just run it. 

But what shoud care about is that, there should have the files in /env01(or /env02 or /env03 ...) named like "cfd_record_episode_1_episodic_reward_-57.35210136077975" or "cfd_record_episode_283_episodic_reward_-46.807446563400276", in which, 1(or 283) mean that, until now, the episode 1(283) is best episode that have the highest total reward.

需要在DRLinFluids中环境文件的reset模块中，对目前的episode总奖励与之前的最最高奖励做对比，若当前episode的奖励为目前最高，则保存当前的全部仿真文件到env01文件夹下(以"cfd_record_episode_283_episodic_reward_-46.807446563400276"模式命名，其内存贮了当前episode的openfoam运行文件)，当然如果是10个环境用不同的种子学习的话，会有十个env文件，如env01,env02....env10。每个env文件夹下都应有以"cfd_record_episode_283_episodic_reward_-46.807446563400276"模式命名的文件夹。


# 1 Generation_cfd_episode_info_Package:
which was uesd to generate one json file, in which total reward and No. of best episode till now will be shown.

# 2 Pic_generation_fom_total_reward_10_envs_Package #
which was used to generate 10+1 pics, in which the change of total reward among 10 env files was shown, and also, the pic of mean total reward among episodes was shown in the "1" another pic.

# 3 Pic_generation_from_one_info_list_files_Package #
which was used to shown the reward data among trajectory in the episode (that we have mentioned before) that have the best total reward until now. But here we just use the "info_list_*"files in the /env01(or /env02 or /env03 ...)

# 4  #
