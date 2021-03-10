import os
import sys
import argparse

import const as const
from util import Util
from logger import Logger
from quizer import Quizer


class Main():
    def __init__(self, logger: object):
        self._logger = logger
        self._args = None

    @property
    def info_path(self) -> str:
        return self._args.info_path

    def parse_args(self):
        fn = 'parse_args'
        self._logger.DEBUG(f'{fn} S')

        parser = argparse.ArgumentParser()
        parser.add_argument('--info_path')
        self._args = parser.parse_args()
        if not self._args.info_path:
            self._args.info_path = const.DEFAULT_EXCEL_FILE_NAME

        self._logger.DEBUG(f'{fn} E')

    def run(self):
        fn = 'run'
        self._logger.DEBUG(f'{fn} S')

        print('***********************************************************')
        print('回答は半角数字のみです。複数の場合は半角カンマで区切って下さい。')
        print('途中で終了する場合は、qを入力して下さい。')
        print('***********************************************************')

        quizer = Quizer(logger=self._logger, info_path=self.info_path)

        incorrects = []

        total_cnt = len(quizer.get_random_quiz_list())

        for quiz in quizer.get_random_quiz_list():
            quiz.show()

            # キー入力待ち
            input_answers = input('回答を入力：').split(const.MARK_COMMA)
            if input_answers[0] == 'q':
                break
            result = Quizer.verify(quiz_info=quiz, input_answer=input_answers)

            if result.is_right:
                print('------------')
                print('正解!!')
                print('------------')
            else:
                print('------------')
                print('不正解...')
                print('------------')
                incorrects.append(result)

        if len(incorrects) == 0:
            print('----------------')
            print('全問正解です!!!')
            print('----------------')
        else:
            print('-----------------------------')
            print(f'{total_cnt}問中, {len(incorrects)}問が不正解です...')
            print('-----------------------------')
            for incorrect in incorrects:
                print(f'# {incorrect.num}')

        self._logger.DEBUG(f'{fn} E')


if __name__ == '__main__':
    ret = 0
    logger = Logger()

    try:
        logger.DEBUG('====================================================')
        logger.DEBUG('START')

        Util.change_current_dir()

        main = Main(logger)
        main.parse_args()

        if os.path.exists(main.info_path) is False:
            logger.ERROR(f'Input file not exist! [{main.info_path}]')
            ret = 1
        else:
            main.run()

    except Exception as ex:
        logger.ERROR(Util.get_exception_message(ex))
        ret = 1

    finally:
        logger.DEBUG('END')
        logger.DEBUG('====================================================')
        sys.exit(ret)
