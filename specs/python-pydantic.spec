%bcond tests 1

%global commit 0c4a22b64b23dfad27387750cf07487efc45eb05
%global snapdate 20250615

Name:           python-pydantic
Version:        2.11.7^%{snapdate}git%{sub %{commit} 1 7}
%global srcversion %{lua:return(rpm.expand("%{version}"):gsub("~",""))}
Release:        %autorelease
Summary:        Data validation using Python type hinting

# SPDX
License:        MIT
URL:            https://github.com/pydantic/pydantic
%dnl Source:         %{url}/archive/v%{srcversion}/pydantic-%{srcversion}.tar.gz
Source:         %{url}/archive/%{commit}/pydantic-%{commit}.tar.gz

# Add initial support for Python 3.14
# https://github.com/pydantic/pydantic/pull/11991
Patch:          %{url}/pull/11991.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli
# For check phase
%if %{with tests}
# We could generate test dependencies using dependency groups, but there are so
# many unwanted dependencies that it is easier to list them manually.

# From the dev dependency group:
# coverage[toml] is for coverage analysis, therefore unwanted downstream
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist dirty-equals}
# eval-type-backport is only needed for older Pythons
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
# pytest-pretty is purely cosmetic
# pytest-examples is not packaged (and not mandatory)
# faker is only used in a benchmark, which we do not run
# pytest-benchmark is only for benchmarking
# pytest-codspeed is only for benchmarking
# pytest-run-parallel might be useful, but is not packaged
BuildRequires:  %{py3_dist packaging}
BuildRequires:  %{py3_dist jsonschema}

# From the testing-extra dependency group:
BuildRequires:  %{py3_dist cloudpickle}
# devtools is not packaged; ansi2html is used only with devtools
# sqlalchemy is "used in docs tests" that we do not run
# pytest-memray is a profiler, therefore unwanted downstream
%endif

%global _description %{expand:
Data validation and settings management using python type hinting.}

%description %{_description}


%package -n     python3-pydantic
Summary:        %{summary}
Recommends:     python3-pydantic+email

%description -n python3-pydantic %{_description}


%package        doc
Summary:        Documentation for Pydantic

%description    doc
This package includes the documentation for Pydantic in Markdown format.


%prep
%dnl %autosetup -n pydantic-%{srcversion} -p1
%autosetup -n pydantic-%{commit} -p1

# Delete pytest addopts. We don't care about benchmarking or coverage.
tomcli-set pyproject.toml del 'tool.pytest.ini_options.addopts'
# Work around patched-out pytest-run-parallel plugin dependency (avoid
# "pytest.PytestUnknownMarkWarning: Unknown pytest.mark.thread_unsafe" error)
tomcli-set pyproject.toml append 'tool.pytest.ini_options.markers' \
    'thread_unsafe: mark as incompatible with patched-out pytest-run-parallel'


%generate_buildrequires
%pyproject_buildrequires -x email -x timezone


%build
%pyproject_wheel


# Docs are in MarkDown, and should be added since mkdocs is now available in Fedora.

%install
%pyproject_install
%pyproject_save_files -l pydantic


%check
%pyproject_check_import -e pydantic.mypy -e pydantic.v1.mypy
%if %{with tests}
# We don't build docs or care about benchmarking
ignore="${ignore-} --ignore=tests/test_docs.py"
ignore="${ignore-} --ignore=tests/benchmarks"

# Upstream Python 3.14 support is not done yet. These are the remaining test
# failures:
k="${k-}${k+ and} not test_annotated_optional_field"
k="${k-}${k+ and} not test_annotated_with_field_default_factory"
k="${k-}${k+ and} not test_annotation_with_double_override"
k="${k-}${k+ and} not test_annotations_valid_for_field_inheritance_with_existing_field"
k="${k-}${k+ and} not test_callable_json_schema_extra_dataclass"
k="${k-}${k+ and} not test_create_model_must_not_reset_parent_namespace"
k="${k-}${k+ and} not test_cross_module_cyclic_reference_dataclass"
k="${k-}${k+ and} not test_dataclass_alias_generator"
k="${k-}${k+ and} not test_dataclass_docs_extraction"
k="${k-}${k+ and} not test_default_factory_field[Field]"
k="${k-}${k+ and} not test_field_title_generator_in_dataclass_fields"
k="${k-}${k+ and} not test_forward_ref_auto_update_no_model"
k="${k-}${k+ and} not test_forward_ref_one_of_fields_not_defined"
k="${k-}${k+ and} not test_incomplete_superclass"
k="${k-}${k+ and} not test_init_false_not_in_signature"
k="${k-}${k+ and} not test_init_false_with_default"
k="${k-}${k+ and} not test_init_false_with_post_init"
k="${k-}${k+ and} not test_init_var_field"
k="${k-}${k+ and} not test_kw_only_subclass"
k="${k-}${k+ and} not test_model_rebuild_localns"
k="${k-}${k+ and} not test_pickle_dataclass_nested_in_model[NonImportableNestedDataclassModel-True]"
k="${k-}${k+ and} not test_pickle_model[NonImportableModel-True]"
k="${k-}${k+ and} not test_pickle_nested_model[NonImportableNestedModel-True]"
k="${k-}${k+ and} not test_rebuild_dataclass"
k="${k-}${k+ and} not test_repr_false[Field]"
k="${k-}${k+ and} not test_root_validator"
k="${k-}${k+ and} not test_schema"
k="${k-}${k+ and} not test_signature"
k="${k-}${k+ and} not test_top_level_fwd_ref"
k="${k-}${k+ and} not test_undefined_types_warning_1a_raised_by_default_2a_future_annotations"

%pytest ${ignore-} -k "${k-}" -rs
%endif


%files -n python3-pydantic -f %{pyproject_files}
%doc CITATION.cff
%doc HISTORY.md
%doc README.md

# Note that the timezone extra has no dependencies on our platform.
%pyproject_extras_subpkg email timezone -n python3-pydantic

%files doc
%license LICENSE
%doc docs/*

%changelog
%autochangelog
