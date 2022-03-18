params = {
    'type': 'BMPO',
    'universe': 'gym',
    'domain': 'Walker2d',
    'task': 'v2',

    'log_dir': '~/ray_mbpo/',
    'exp_name': 'defaults',

    'kwargs': {
        'epoch_length': 1000,
        'train_every_n_steps': 1,
        'n_train_repeat': 20,
        'eval_render_mode': None,
        'eval_n_episodes': 1,
        'eval_deterministic': True,

        'discount': 0.99,
        'tau': 5e-3,
        'reward_scale': 1.0,
        'model_train_freq': 250,
        'rollout_batch_size': 100e3,
        'model_retain_epochs': 1,
        'deterministic': False,
        'num_networks': 7,
        'num_elites': 5,
        'real_ratio': 0.05,
        'target_entropy': -3,
        'max_model_t': None,

        'forward_rollout_schedule': [20, 150, 1, 1],
        'backward_rollout_schedule': [20, 150, 1, 1],
        'beta_schedule': [0, 100, 0.01, 0],
        'last_n_epoch': 10,
        'planning_horizon': 1,
        'backward_policy_var': 0.01,
        'n_initial_exploration_steps': 5000,
    }
}