from infrablocks.terraform_pkl_type_gen.pkl_generator import generate_pkl_type

with_module_example = generate_pkl_type(
    "examples/with_module", "WithModuleExample"
).split("\n")


class TestGeneratePklTypeWithModule:
    def test_includes_root_variables(self):
        labels = [
            line.split(":")[0].strip()
            for line in with_module_example
            if ":" in line and not line.startswith("//")
        ]
        assert "root_string" in labels
        assert "root_number" in labels

    def test_excludes_submodule_variables(self):
        labels = [
            line.split(":")[0].strip()
            for line in with_module_example
            if ":" in line and not line.startswith("//")
        ]
        assert "sub_variable" not in labels
