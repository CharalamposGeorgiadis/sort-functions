def execution_time_to_real_world(execution_time: float) -> None:
    """
    Converts the execution time to millenniums, centuries, decades, years, months, days, hours, minutes and seconds.
    :param execution_time: Execution time.
    :return: None.
    """
    # Convert total sorting time to millenniums, centuries, decades, years, months, days, hours, minutes, and seconds
    millenniums, remainder = divmod(execution_time, 60 * 60 * 24 * 365 * 1000)
    centuries, remainder = divmod(remainder, 60 * 60 * 24 * 365 * 100)
    decades, remainder = divmod(remainder, 60 * 60 * 24 * 365 * 10)
    years, remainder = divmod(remainder, 60 * 60 * 24 * 365)
    months, remainder = divmod(remainder, 60 * 60 * 24 * 30)
    days, remainder = divmod(remainder, 60 * 60 * 24)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)

    # Print
    print(
        f"Sorting Time:\n"
        f"{int(millenniums)} Millenniums\n"
        f"{int(centuries)} Centuries\n"
        f"{int(decades)} Decades\n"
        f"{int(years)} Years\n"
        f"{int(months)} Months\n"
        f"{int(days)} Days\n"
        f"{int(hours)} Hours\n"
        f"{int(minutes)} Minutes\n"
        f"{int(seconds)} Seconds\n"
    )
