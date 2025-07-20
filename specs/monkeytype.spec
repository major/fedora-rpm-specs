%global srcname MonkeyType

%if 0%{?python3_version_nodots} >= 312
# some tests currently fail
%bcond_with all_tests
%else
%bcond_without all_tests
%endif

Name:           monkeytype
Version:        23.3.0
Release:        %autorelease
Summary:        Generating Python type annotations from sampled production types
License:        BSD-3-Clause
URL:            https://github.com/instagram/%{srcname}
# PyPI source has no tests
# Source:        %%{pypi_source %%{srcname}}
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
# Pipfile not supported yet
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(django)

%py_provides python%{python3_pkgversion}-%{name}

%global _description %{expand:
MonkeyType collects runtime types of function arguments and return values, and
can automatically generate stub files or even add draft type annotations
directly to your Python code based on the types collected at runtime.}

%description %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}


%check
%pyproject_check_import
%if %{with all_tests}
%pytest -v
%else
%if 0%{?python3_version_nodots} >= 314
# FAILED tests/test_encoding.py::TestTypeConversion::test_type_round_trip[Union0]
# FAILED tests/test_encoding.py::TestTypeConversion::test_type_round_trip[Union1]
# FAILED tests/test_encoding.py::TestTypeConversion::test_type_round_trip[Dict3]
# FAILED tests/test_encoding.py::TestTypeConversion::test_type_round_trip[List2]
# FAILED tests/test_encoding.py::TestTypeConversion::test_type_round_trip[Dict4]
# FAILED tests/test_stubs.py::TestRenderAnnotation::test_render_annotation[Union-Optional[int]]
# FAILED tests/test_stubs.py::TestRenderAnnotation::test_render_annotation[List-List[Optional[int]]]
# FAILED tests/test_stubs.py::TestFunctionStub::test_optional_parameter_annotation
# FAILED tests/test_stubs.py::TestFunctionStub::test_optional_union_parameter_annotation
# FAILED tests/test_stubs.py::TestFunctionStub::test_optional_return_annotation
# FAILED tests/test_stubs.py::TestFunctionStub::test_split_parameters_across_multiple_lines
# FAILED tests/test_stubs.py::TestFunctionStub::test_default_none_parameter_annotation
# FAILED tests/test_stubs.py::TestFunctionStub::test_forward_ref_annotation - a...
# FAILED tests/test_stubs.py::TestClassStub::test_render - AssertionError: asse...
# FAILED tests/test_stubs.py::TestModuleStub::test_render - AssertionError: ass...
# FAILED tests/test_stubs.py::TestBuildModuleStubs::test_build_module_stubs - A...
# FAILED tests/test_stubs.py::TestGetImportsForAnnotation::test_special_case_types[Union-expected1]
# FAILED tests/test_stubs.py::TestGetImportsForAnnotation::test_container_types[Union-expected5]
%pytest -v \
  --deselect tests/test_encoding.py::TestTypeConversion::test_type_round_trip[Union0] \
  --deselect tests/test_encoding.py::TestTypeConversion::test_type_round_trip[Union1] \
  --deselect tests/test_encoding.py::TestTypeConversion::test_type_round_trip[Dict3] \
  --deselect tests/test_encoding.py::TestTypeConversion::test_type_round_trip[List2] \
  --deselect tests/test_encoding.py::TestTypeConversion::test_type_round_trip[Dict4] \
  --deselect tests/test_stubs.py::TestRenderAnnotation::test_render_annotation[Union-Optional[int]] \
  --deselect tests/test_stubs.py::TestRenderAnnotation::test_render_annotation[List-List[Optional[int]]] \
  --deselect tests/test_stubs.py::TestFunctionStub::test_optional_parameter_annotation \
  --deselect tests/test_stubs.py::TestFunctionStub::test_optional_union_parameter_annotation \
  --deselect tests/test_stubs.py::TestFunctionStub::test_optional_return_annotation \
  --deselect tests/test_stubs.py::TestFunctionStub::test_split_parameters_across_multiple_lines \
  --deselect tests/test_stubs.py::TestFunctionStub::test_default_none_parameter_annotation \
  --deselect tests/test_stubs.py::TestFunctionStub::test_forward_ref_annotation \
  --deselect tests/test_stubs.py::TestClassStub::test_render \
  --deselect tests/test_stubs.py::TestModuleStub::test_render \
  --deselect tests/test_stubs.py::TestBuildModuleStubs::test_build_module_stubs \
  --deselect tests/test_stubs.py::TestGetImportsForAnnotation::test_special_case_types[Union-expected1] \
  --deselect tests/test_stubs.py::TestGetImportsForAnnotation::test_container_types[Union-expected5]
%else
%if 0%{?python3_version_nodots} >= 312
# FAILED tests/test_tracing.py::TestTraceCalls::test_callee_throws_recovers - A...
# FAILED tests/test_tracing.py::TestTraceCalls::test_nested_callee_throws_recovers
# FAILED tests/test_tracing.py::TestTraceCalls::test_caller_handles_callee_exception
# FAILED tests/test_tracing.py::TestTraceCalls::test_generator_trace - Assertio...
# FAILED tests/test_tracing.py::TestTraceCalls::test_return_none - AssertionErr...
# FAILED tests/test_tracing.py::TestTraceCalls::test_access_property - Assertio...
%pytest -v \
  --deselect tests/test_tracing.py::TestTraceCalls::test_callee_throws_recovers \
  --deselect tests/test_tracing.py::TestTraceCalls::test_nested_callee_throws_recovers \
  --deselect tests/test_tracing.py::TestTraceCalls::test_caller_handles_callee_exception \
  --deselect tests/test_tracing.py::TestTraceCalls::test_generator_trace \
  --deselect tests/test_tracing.py::TestTraceCalls::test_return_none \
  --deselect tests/test_tracing.py::TestTraceCalls::test_access_property
%else
%pytest -v
# Python < 3.12
%endif
# Python < 3.14
%endif
# not all_tests
%endif


%files -f %{pyproject_files}
%license LICENSE
%doc CHANGES.rst CODE_OF_CONDUCT.md CONTRIBUTING.rst README.rst
%{_bindir}/%{name}


%changelog
%autochangelog
