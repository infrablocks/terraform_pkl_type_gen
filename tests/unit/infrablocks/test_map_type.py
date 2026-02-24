from infrablocks.terraform_pkl_type_gen import map_type


class TestTerraformPklTypeMapping:
    def test_string_type_mapping(self):
        assert map_type("string") == "String"

    def test_number_type_mapping(self):
        assert map_type("number") == "Number"

    def test_bool_type_mapping(self):
        assert map_type("bool") == "Boolean"

    def test_list_of_dynamic_type_mapping(self):
        assert map_type("list of dynamic") == "Listing | List"

    def test_list_of_any_type_mapping(self):
        assert map_type("list(any)") == "Listing | List"

    def test_list_of_string_type_mapping(self):
        assert map_type("list of string") == "Listing<String> | List<String>"

    def test_list_of_number_type_mapping(self):
        assert map_type("list of number") == "Listing<Number> | List<Number>"

    def test_list_of_bool_type_mapping(self):
        assert map_type("list of bool") == "Listing<Boolean> | List<Boolean>"

    def test_map_of_dynamic_type_mapping(self):
        assert (
            map_type("map of dynamic")
            == "Mapping<String, Any> | Map<String, Any>"
        )

    def test_map_of_string_type_mapping(self):
        assert (
            map_type("map of string")
            == "Mapping<String, String> | Map<String, String>"
        )

    def test_map_of_number_type_mapping(self):
        assert (
            map_type("map of number")
            == "Mapping<String, Number> | Map<String, Number>"
        )

    def test_map_of_bool_type_mapping(self):
        assert (
            map_type("map of bool")
            == "Mapping<String, Boolean> | Map<String, Boolean>"
        )

    def test_object_type_mapping(self):
        assert map_type("object") == "Mapping<String, Any> | Map<String, Any>"
