def calculate_bmi(weight : float, height : float) -> float:
    """Calculate the Body Mass Index (BMI).

    The BMI is calculated by dividing the person's weight in kilograms
    by the square of their height in meters.

    Args:
        weight: Weight in kilograms.
        height: Height in meters.

    Returns:
        The calculated Body Mass Index (BMI).
    """
    bmi = weight / (height ** 2)
    return bmi