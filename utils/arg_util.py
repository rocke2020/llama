import argparse
import logging
from datetime import datetime
from pathlib import Path

DATE_TIME = "%Y_%m_%d %H:%M:%S"


class ArgparseUtil(object):
    """
    参数解析工具类
    """
    def __init__(self):
        """ Basic args """
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--seed", default=1, type=int)
        self.parser.add_argument("--model_type", default='cnn', type=str)
        self.parser.add_argument("--data_type", default=None, type=str)
        self.parser.add_argument("--save_predicted_test", default=0, type=int, help="0 is false, 1 is true")
        self.parser.add_argument("--save_model_per_epoch", type=int, default=0, help="0 is false, 1 is true")
        self.parser.add_argument("--predict_on_separate_length", type=int, default=0, help="0 is false, 1 is true")
        self.parser.add_argument("--plot_proba_hist_kde", type=int, default=0, help="0 is false, 1 is true")

    def predictor(self):
        """  """
        self.parser.add_argument("--generate_data_type", type=str, default='', help="")
        self.parser.add_argument("--read_cached_input_data", type=int, default=0, help="")
        args = self.parser.parse_args()
        return args


def parse_args():
    """ Basic args usage """
    parser = argparse.ArgumentParser(description="")
    
    parser.add_argument(
        "--cuda_devices", type=str, default='0', help="visible cuda devices."
    )
    parser.add_argument("--output_dir", type=str, default=None, help="Where to store the final model.")
    parser.add_argument("--seed", type=int, default=42, help="")
    args = parser.parse_args()
    # Sanity checks
    if args.task_name is None:
        raise ValueError("Need a task name.")
    args = parser.parse_args()
    save_args(args)


def save_args(args, output_dir='.', with_time_at_filename=False):
    if args.output_dir is not None:
        output_dir = args.output_dir
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    t0 = datetime.now().strftime(DATE_TIME)
    if with_time_at_filename:
        out_file = output_dir / f"args-{t0}.txt"
    else:
        out_file = output_dir / f"args.txt"
    with open(out_file, "w", encoding='utf-8') as f:
        f.write(f'{t0}\n')
        for arg, value in vars(args).items():
            f.write(f"{arg}: {value}\n")


def log_args(args, logger=None, save_dir=None):
    if logger is None:
        logger = logging.getLogger()
        logging.basicConfig(level=logging.INFO,
            format='%(asctime)s %(filename)s %(lineno)d: %(message)s',
            datefmt='%y-%m-%d %H:%M')

    for arg, value in vars(args).items():
        logger.info(f"{arg}: {value}")

    if save_dir is not None:
        logger.info('Save args to the dir %s', save_dir)
        save_args(args, save_dir)
