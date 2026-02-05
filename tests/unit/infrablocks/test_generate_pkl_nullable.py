from typing import List

from infrablocks.terraform_pkl_type_gen.pkl_generator import generate_pkl_type


def has_attribute_of_name(lines: List[str], name: str, with_type: str) -> bool:
    """
    Check if the generated PKL type contains an attribute with the given name.

    Args:
        lines (List[str]): The lines of the generated PKL type.
        name (str): The name of the attribute to check for.

    Returns:
        bool: True if the attribute exists, False otherwise.
    """
    matching_line = next(
        line for line in lines if line.lstrip().startswith(name + ":")
    )
    type_signature = matching_line.split(":")[1].lstrip()
    return type_signature == with_type


nullable_example = generate_pkl_type(
    "examples/nullable", "NullableExample"
).split("\n")


class TestGeneratePklNullableTypes:
    def test_plain_number_is_not_nullable(self):
        assert has_attribute_of_name(
            lines=nullable_example, name="plain_number", with_type="Number"
        )

    def test_plain_string_is_not_nullable(self):
        assert has_attribute_of_name(
            lines=nullable_example, name="plain_string", with_type="String"
        )

    def test_nullable_number_is_nullable(self):
        assert has_attribute_of_name(
            lines=nullable_example, name="nullable_number", with_type="Number?"
        )

    def test_nullable_string_is_nullable(self):
        assert has_attribute_of_name(
            lines=nullable_example, name="nullable_string", with_type="String?"
        )

    def test_default_null_number_is_nullable(self):
        assert has_attribute_of_name(
            lines=nullable_example,
            name="default_null_number",
            with_type="Number?",
        )

    def test_default_null_string_is_nullable(self):
        assert has_attribute_of_name(
            lines=nullable_example,
            name="default_null_string",
            with_type="String?",
        )

    def test_default_value_number_is_not_nullable(self):
        assert has_attribute_of_name(
            lines=nullable_example,
            name="default_value_number",
            with_type="Number",
        )

    def test_default_value_string_is_not_nullable(self):
        assert has_attribute_of_name(
            lines=nullable_example,
            name="default_value_string",
            with_type="String",
        )
