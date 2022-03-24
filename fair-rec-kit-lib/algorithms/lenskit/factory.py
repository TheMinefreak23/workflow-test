""""
This program has been developed by students from the bachelor Computer Science at
Utrecht University within the Software Project course.
© Copyright Utrecht University (Department of Information and Computing Sciences)
"""

from ..common import *
from .common import *
from .params import *
from .recommenders import *


def get_lenskit_recommender_factory():
    return LENSKIT_API, {
        ALS_BIASED_MF: {
            GET_DEFAULT_PARAMS_FUNC: get_defaults_als_biased_mf,
            CREATE_FUNC: create_recommender_als_biased_mf
        },
        ALS_IMPLICIT_MF: {
            GET_DEFAULT_PARAMS_FUNC: get_defaults_als_implicit_mf,
            CREATE_FUNC: create_recommender_als_implicit_mf
        },
        POP_SCORE: {
            GET_DEFAULT_PARAMS_FUNC: get_defaults_pop_score,
            CREATE_FUNC: create_recommender_pop_score
        },
        USER_ITEM_BIAS: {
            GET_DEFAULT_PARAMS_FUNC: get_defaults_bias,
            CREATE_FUNC: create_recommender_bias
        },
        FUNK_SVD: {
            GET_DEFAULT_PARAMS_FUNC: get_defaults_funk_svd,
            CREATE_FUNC: create_recommender_funk_svd
        },
        KNN_ITEM_ITEM: {
            GET_DEFAULT_PARAMS_FUNC: get_defaults_knn_item_item,
            CREATE_FUNC: create_recommender_knn_item_item
        },
        KNN_USER_USER: {
            GET_DEFAULT_PARAMS_FUNC: get_defaults_knn_user_user,
            CREATE_FUNC: create_recommender_knn_user_user
        }
    }


def get_lenskit_recommender_names():
    return LENSKIT_API, [
        ALS_BIASED_MF,
        ALS_IMPLICIT_MF,
        POP_SCORE,
        USER_ITEM_BIAS,
        FUNK_SVD,
        KNN_ITEM_ITEM,
        KNN_USER_USER
    ]


def is_lenskit_recommender(recommender_name):
    _, names = get_lenskit_recommender_names()

    for rec_name in names:
        if rec_name is recommender_name:
            return True

    return False
