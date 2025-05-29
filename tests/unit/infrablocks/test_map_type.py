from infrablocks.terraform_pkl_type_gen import map_type


class TestTerraformPklTypeMapping:
    def test_string_type_mapping(self):
        assert map_type("string") == "String"

    def test_number_type_mapping(self):
        assert map_type("number") == "Number"

    def test_bool_type_mapping(self):
        assert map_type("bool") == "Boolean"

    def test_list_of_dynamic_type_mapping(self):
        assert map_type("list of dynamic") == "Listing"

    def test_list_of_any_type_mapping(self):
        assert map_type("list(any)") == "Listing"

    def test_list_of_string_type_mapping(self):
        assert map_type("list of string") == "Listing<String>"

    def test_list_of_number_type_mapping(self):
        assert map_type("list of number") == "Listing<Number>"

    def test_list_of_bool_type_mapping(self):
        assert map_type("list of bool") == "Listing<Boolean>"

    def test_map_of_dynamic_type_mapping(self):
        assert map_type("map of dynamic") == "Mapping<String, Any>"

    def test_map_of_string_type_mapping(self):
        assert map_type("map of string") == "Mapping<String, String>"

    def test_map_of_number_type_mapping(self):
        assert map_type("map of number") == "Mapping<String, Number>"

    def test_map_of_bool_type_mapping(self):
        assert map_type("map of bool") == "Mapping<String, Boolean>"
