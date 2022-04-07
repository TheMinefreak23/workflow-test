"""
This program has been developed by students from the bachelor Computer Science at
Utrecht University within the Software Project course.
© Copyright Utrecht University (Department of Information and Computing Sciences)
"""

from fairreckitlib.pipelines.data.callback import DataPipelineConsole
from fairreckitlib.pipelines.data.run import run_data_pipeline
from fairreckitlib.pipelines.evaluation.run import run_evaluation_pipelines
from fairreckitlib.pipelines.model.callback import ModelPipelineConsole
from fairreckitlib.pipelines.model.run import run_recommender_model_pipelines
from fairreckitlib.experiment.config import EXP_KEY_DATASETS, EXP_KEY_MODELS, EXP_KEY_EVALUATION
from fairreckitlib.experiment.config import EXP_KEY_TOP_K
from fairreckitlib.experiment.config import EXP_KEY_TYPE, EXP_TYPE_PREDICTION, EXP_TYPE_RECOMMENDATION


def run_experiment(output_dir, data_registry, config):
    if config[EXP_KEY_TYPE] == EXP_TYPE_PREDICTION:
        run_predictor_experiment(
            output_dir,
            data_registry,
            config
        )
    elif config[EXP_KEY_TYPE] == EXP_TYPE_RECOMMENDATION:
        run_recommender_experiment(
            output_dir,
            data_registry,
            config
        )
    else:
        raise NotImplementedError()


def run_predictor_experiment(output_dir, data_registry, config):
    raise NotImplementedError()


def run_recommender_experiment(output_dir, data_registry, config):
    data_tuples = run_data_pipeline(
        output_dir,
        data_registry,
        config[EXP_KEY_DATASETS],
        DataPipelineConsole()
    )

    for dataset, data_dir, train_path, test_path in data_tuples:
        model_dirs = run_recommender_model_pipelines(
            dataset,
            data_dir,
            train_path,
            test_path,
            config[EXP_KEY_MODELS],
            config[EXP_KEY_TOP_K],
            ModelPipelineConsole()
        )

        run_evaluation_pipelines(
            dataset,
            train_path,
            test_path,
            model_dirs,
            config[EXP_KEY_EVALUATION],
            None,
            num_items=config[EXP_KEY_TOP_K]
        )
