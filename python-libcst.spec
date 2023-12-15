%if 0%{?rhel}
%bcond_with docs
%bcond_with tests
%else
%bcond_without docs
%bcond_without tests
%endif

# Rust parser has unsatisfied dependencies:
# chic is out of date and require an old version of annotate-snippets
%bcond_with rust

# Use --with all_tests to run all tests
%bcond_with all_tests

Name:           python-libcst
Version:        0.4.10
Release:        %autorelease
Summary:        A concrete syntax tree with AST-like properties for Python 3

# see LICENSE in the upstream sources for the breakdown
License:        MIT AND (MIT OR PSF-2.0) AND Apache-2.0
URL:            https://github.com/Instagram/LibCST
Source:         %{pypi_source libcst}
# Optional patches
# Disable building Rust code
Patch100:       libcst-no-rust.diff

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
# test dependencies are intermingled with dev dependencies
# so list them manually for now
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(hypothesmith)
BuildRequires:  python3dist(pytest)
%endif
%if %{with docs}
BuildRequires:  graphviz
BuildRequires:  sed
BuildRequires:  python3-docs
BuildRequires:  python3-metakernel-python
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(nbsphinx) >= 0.4.2
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.4.3
%endif


%global _description %{expand:
LibCST parses Python source code as a CST tree that keeps all formatting
details (comments, whitespaces, parentheses, etc). It's useful for building
automated refactoring (codemod) applications and linters.

LibCST creates a compromise between an Abstract Syntax Tree (AST) and a
traditional Concrete Syntax Tree (CST). By carefully reorganizing and naming
node types and fields, it creates a lossless CST that looks and feels like an
AST.}


%description %_description

%package -n     python3-libcst
Summary:        %{summary}

%description -n python3-libcst %_description


%if %{with docs}
%package        doc
Summary:        %{name} documentation
Requires:       python3-docs

%description    doc
Documentation for %{name}
%endif


%prep
%autosetup -N -n libcst-%{version}
# Apply patches up to 99
%autopatch -p1 -M 99
%if %{without rust}
%autopatch -p1 100
%endif
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/source/conf.py
%endif


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install
%pyproject_save_files libcst


%check
%pyproject_check_import -e 'libcst.tests.*'
%if %{with tests}
%if %{with all_tests}
%pytest
%else
# test_codegen_clean is tracked in https://github.com/Instagram/LibCST/issues/304
# test_codemod_cli is tracked in https://github.com/Instagram/LibCST/issues/331
# test_type_enforce is tracked in https://github.com/Instagram/LibCST/issues/305
# test_type_inference_provider requires pyre which is not packaged
#
# FAILED libcst/codegen/tests/test_codegen_clean.py::TestCodegenClean::test_codegen_clean_matcher_classes
# FAILED libcst/codegen/tests/test_codegen_clean.py::TestCodegenClean::test_codegen_clean_return_types
# FAILED libcst/codegen/tests/test_codegen_clean.py::TestCodegenClean::test_codegen_clean_visitor_functions
# FAILED libcst/tests/test_type_enforce.py::TypeEnforcementTest::test_basic_pass_19
EXCLUDES="not test_codegen_clean_matcher_classes and not test_codegen_clean_return_types"
EXCLUDES+=" and not test_codegen_clean_visitor_functions and not test_basic_pass_19"
# ERROR libcst/metadata/tests/test_type_inference_provider.py::TypeInferenceProviderTest::test_gen_cache_0
# ERROR libcst/metadata/tests/test_type_inference_provider.py::TypeInferenceProviderTest::test_simple_class_types_0
# ERROR libcst/metadata/tests/test_type_inference_provider.py::TypeInferenceProviderTest::test_with_empty_cache
EXCLUDES+=" and not test_gen_cache_0 and not test_simple_class_types_0 and not test_with_empty_cache"
%pytest -k "$EXCLUDES"
# end all_tests
%endif
# end tests
%endif


%files -n python3-libcst -f %{pyproject_files}


%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif


%changelog
%autochangelog
