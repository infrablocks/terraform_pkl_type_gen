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


basic_example = generate_pkl_type("examples/basic", "BasicExample").split("\n")


class TestGeneratePklType:
    def test_generated_class_leads_with_comment(self):
        assert basic_example[0].startswith("//")

    def test_generated_class_name(self):
        assert basic_example[1] == ("class BasicExample {")

    def test_generated_class_ends_with_brace(self):
        assert basic_example[-1] == ("}")

    def test_generated_class_has_string_member(self):
        assert has_attribute_of_name(
            lines=basic_example, name="string", with_type="String"
        )

    def test_generated_class_has_number_member(self):
        assert has_attribute_of_name(
            lines=basic_example, name="number", with_type="Number"
        )

    def test_generated_class_has_bool_member(self):
        assert has_attribute_of_name(
            lines=basic_example, name="bool", with_type="Boolean"
        )

    def test_generated_class_has_list_of_string_member(self):
        assert has_attribute_of_name(
            lines=basic_example,
            name="list_of_strings",
            with_type="Listing<String> | List<String>",
        )

    def test_generated_class_has_list_of_number_member(self):
        assert has_attribute_of_name(
            lines=basic_example,
            name="list_of_numbers",
            with_type="Listing<Number> | List<Number>",
        )

    def test_generated_class_has_list_of_bool_member(self):
        assert has_attribute_of_name(
            lines=basic_example,
            name="list_of_booleans",
            with_type="Listing<Boolean> | List<Boolean>",
        )

    def test_generated_class_has_map_of_string_member(self):
        assert has_attribute_of_name(
            lines=basic_example,
            name="map_of_strings",
            with_type="Mapping<String, String> | Map<String, String>",
        )

    def test_generated_class_has_map_of_number_member(self):
        assert has_attribute_of_name(
            lines=basic_example,
            name="map_of_numbers",
            with_type="Mapping<String, Number> | Map<String, Number>",
        )

    def test_generated_class_has_map_of_bool_member(self):
        assert has_attribute_of_name(
            lines=basic_example,
            name="map_of_booleans",
            with_type="Mapping<String, Boolean> | Map<String, Boolean>",
        )

    def test_generated_class_has_object_of_things_member(self):
        assert has_attribute_of_name(
            lines=basic_example,
            name="object_of_things",
            with_type="Mapping<String, Any> | Map<String, Any>",
        )
