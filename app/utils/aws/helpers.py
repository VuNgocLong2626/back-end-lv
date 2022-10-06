from app.utils.aws.dynamodb import table


def delete_item(
    pk, sk
) -> None:
    _ = table.delete_item(
        Key={
            "PK": pk,
            "SK": sk
        }
    )


def put_item_not_exists_PK_And_SK(
    item: dict
) -> None:
    table.put_item(
        Item=item,
        ConditionExpression="attribute_not_exists(PK) \
            AND attribute_not_exists(SK)"
    )


def put_item_not_exists_PK(
    item: dict
) -> None:
    table.put_item(
        Item=item,
        ConditionExpression="attribute_not_exists(PK)"
    )


def put_item(
    item: dict
) -> None:
    _ = table.put_item(
        Item=item
    )


def put_item_w(
    item: dict
) -> None:
    with table.batch_write as batch:
        batch.put_item(
            Item=item
        )
    response = item
    return response


def update_item(
    item: dict
) -> None:
    response = table.update_item(
        Key={
            'PK': item.pop('pk'),
            'SK': item.pop('sk')
        },
        AttributeUpdates=item
    )
    return response
