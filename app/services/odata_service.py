import pandas as pd


VALID_OPERATORS = ["eq", "ne", "gt", "ge", "lt", "le"]


def apply_select(df: pd.DataFrame, select: str) -> pd.DataFrame:
    columns = [col.strip() for col in select.split(",")]

    missing_columns = [col for col in columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Invalid $select columns: {missing_columns}")

    return df[columns]


def apply_orderby(df: pd.DataFrame, orderby: str) -> pd.DataFrame:
    parts = orderby.strip().split()

    column = parts[0]
    direction = parts[1].lower() if len(parts) > 1 else "asc"

    if column not in df.columns:
        raise ValueError(f"Invalid $orderby column: {column}")

    if direction not in ["asc", "desc"]:
        raise ValueError(f"Invalid $orderby direction: {direction}")

    return df.sort_values(by=column, ascending=(direction == "asc"))


def parse_filter_value(value: str):
    value = value.strip()

    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]

    if value.lower() == "true":
        return True

    if value.lower() == "false":
        return False

    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def apply_filter(df: pd.DataFrame, filter_query: str) -> pd.DataFrame:
    parts = filter_query.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Invalid $filter format. Use: column operator value")

    column, operator, raw_value = parts
    value = parse_filter_value(raw_value)

    if column not in df.columns:
        raise ValueError(f"Invalid $filter column: {column}")

    if operator not in VALID_OPERATORS:
        raise ValueError(f"Invalid $filter operator: {operator}")

    if operator == "eq":
        return df[df[column] == value]

    if operator == "ne":
        return df[df[column] != value]

    if operator == "gt":
        return df[df[column] > value]

    if operator == "ge":
        return df[df[column] >= value]

    if operator == "lt":
        return df[df[column] < value]

    if operator == "le":
        return df[df[column] <= value]

    return df


def apply_odata_query(
    df: pd.DataFrame,
    select: str | None = None,
    filter: str | None = None,
    orderby: str | None = None,
    top: int = 100,
    skip: int = 0,
    count: bool = False,
):
    total_count = len(df)

    if filter:
        df = apply_filter(df, filter)

    filtered_count = len(df)

    if orderby:
        df = apply_orderby(df, orderby)

    if skip:
        df = df.iloc[skip:]

    if top:
        df = df.head(top)

    if select:
        df = apply_select(df, select)

    response = {"value": df.to_dict(orient="records")}

    if count:
        response["count"] = filtered_count
        response["total_count"] = total_count

    return response


def apply_odata(
    df: pd.DataFrame,
    select: str | None = None,
    filter: str | None = None,
    orderby: str | None = None,
    top: int = 100,
    skip: int = 0,
    count: bool = False,
):
    return apply_odata_query(
        df=df,
        select=select,
        filter=filter,
        orderby=orderby,
        top=top,
        skip=skip,
        count=count,
    )
