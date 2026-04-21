import input_module
import calc_module
import logger


def main():
    user_data = input_module.get_data_gui()

    if user_data:
        results = calc_module.process_calculation(user_data)

        report = logger.generate_report(user_data, results)

        logger.output_gui(report)


if __name__ == "__main__":
    main()
