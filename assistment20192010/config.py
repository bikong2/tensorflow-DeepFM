# -*- coding: utf-8 -*-
# config for numeric/ignore columns

TRAIN_FILE = "./data/train.csv"
TEST_FILE = "./data/test.csv"

SUB_DIR = "./output"

NUM_SPLITS = 5
RANDOM_SEED = 2020

# types of columns of the dataset dataframe
CATEGORICAL_COLS = [
#"original",          # main problem=1 | scaffolding problem=0
#"tutor_mode",        # tutor/test/pretest/posttest
#"answer_type",       # 答题类型
]

NUMERIC_COLS = [
#"order_id",          # 时间顺序的logid
#"assignment_id",     # 
#"user_id",           #
#"assistment_id",     # 
#"problem_id",        # 题目id
#"original",          # main problem=1 | scaffolding problem=0
#"correct",           # 正确=1 ｜ 错误=0
"attempt_count",     # 尝试同一题目的次数
#"ms_first_response", # 学生第一次提交对应题目答案的时间
#"tutor_mode",        # tutor/test/pretest/posttest
#"answer_type",       # 答题类型
#"sequence_id",       #
#"student_class_id",  # class ID
#"position",          # 
#"type",              # 
#"base_sequence_id",  # 
#"skill_id",          # skill_id 针对multi-skill问题 拆分到多行
#"skill_name",        # skill_name
#"teacher_id",        # 
#"school_id",         #
"hint_count",        # 尝试对应题目的学生数目
"hint_total",        # 尝试对应题目的次数
#"overlap_time",      #
#"template_id",       # 
#"answer_id",         # 多选题的answer_id
#"answer_text",       # 
#"first_action",      #
#"bottom_hint",       # 学生是否ask for all hints
"opportunity",       # 
#"opportunity_original",
]

IGNORE_COLS = [
"order_id",          # 时间顺序的logid
"assignment_id",     # 
#"user_id",           #
"assistment_id",     # 
#"problem_id",        # 题目id
#"original",          # main problem=1 | scaffolding problem=0
"correct",           # 正确=1 ｜ 错误=0
#"attempt_count",     # 尝试同一题目的次数
"ms_first_response", # 学生第一次提交对应题目答案的时间
#"tutor_mode",        # tutor/test/pretest/posttest
#"answer_type",       # 答题类型
"sequence_id",       #
"student_class_id",  # class ID
"position",          # 
"type",              # 
"base_sequence_id",  # 
#"skill_id",          # skill_id 针对multi-skill问题 拆分到多行
"skill_name",        # skill_name
#"teacher_id",        # 
#"school_id",         #
#"hint_count",        # 尝试题目的学生数目
#"hint_total",        # 
"overlap_time",      #
"template_id",       # 
"answer_id",         # 多选题的answer_id
"answer_text",       # 
"first_action",      #
"bottom_hint",       # 学生是否ask for all hints
#"opportunity",       # 
"opportunity_original",
]
