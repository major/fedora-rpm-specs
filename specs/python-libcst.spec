%bcond_with bootstrap

%if 0%{?rhel}
%bcond_with tests
%else
%if %{with bootstrap}
# need updated libcst to update hypothesmith
# and older hypothesmith does not work with newer hypothesis
%bcond_with tests
%else
%bcond_without tests
%endif
%endif

# Use --with all_tests to run all tests
%bcond_with all_tests

Name:           python-libcst
Version:        1.6.0
Release:        %autorelease
Summary:        A concrete syntax tree with AST-like properties for Python 3

# see LICENSE in the upstream sources for the breakdown
License:        MIT AND (MIT AND PSF-2.0) AND Apache-2.0
URL:            https://github.com/Instagram/LibCST
Source:         %{pypi_source libcst}
# * drop unused, benchmark-only criterion dev-dependency
Patch:          libcst-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  python3-devel

%if %{with tests}
# test dependencies are intermingled with dev dependencies
# so list them manually for now
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(hypothesmith)
BuildRequires:  python3dist(pytest)
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
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# MIT
# MIT AND (MIT AND PSF-2.0)
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        MIT AND (MIT AND PSF-2.0) AND Apache-2.0 AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

# Documentation is hard to build since libcst.native is not available to import until %%install
Obsoletes:      python-libcst-doc < 1.1.0-1

%description -n python3-libcst %_description


%prep
%autosetup -N -n libcst-%{version}
# Apply patches up to 99
%autopatch -p1 -M 99

# remove version locks
rm native/Cargo.lock

%cargo_prep

%generate_buildrequires
for p in libcst_derive libcst; do
  cd native/$p
  # dev dependencies need to be included, setuptools_rust seems to include them unconditionally
  %cargo_generate_buildrequires -t
  cd ../..
done
%pyproject_buildrequires -r


%build
export RUSTFLAGS="%{build_rustflags}"
%pyproject_wheel

# write license summary and breakdown
cd native
%{cargo_license_summary}
%{cargo_license} > ../LICENSE.dependencies
cd ..


%install
%pyproject_install
%pyproject_save_files libcst


%check
%pyproject_check_import -e 'libcst.tests.*'
%if %{with tests}
# libcst.native is not available in build directory
# test the pure Python codepath for now
# (TODO: test *both* paths)
export LIBCST_PARSER_TYPE=pure
%pyproject_check_import -e 'libcst.tests.*'
%if %{with all_tests}
%pytest
%else
# =========================== short test summary info ============================
### these fail with this:
###    AssertionError: False is not true : libcst._typed_visitor needs new codegen, see `python -m libcst.codegen.generate --help` for instructions, or run `python -m libcst.codegen.generate all`
# FAILED libcst/codegen/tests/test_codegen_clean.py::TestCodegenClean::test_codegen_clean_matcher_classes
# FAILED libcst/codegen/tests/test_codegen_clean.py::TestCodegenClean::test_codegen_clean_return_types
# FAILED libcst/codegen/tests/test_codegen_clean.py::TestCodegenClean::test_codegen_clean_visitor_functions
### these need pyre, not available yet
# ERROR libcst/metadata/tests/test_type_inference_provider.py::TypeInferenceProviderTest::test_gen_cache_0
# ERROR libcst/metadata/tests/test_type_inference_provider.py::TypeInferenceProviderTest::test_simple_class_types_0
# ERROR libcst/metadata/tests/test_type_inference_provider.py::TypeInferenceProviderTest::test_with_empty_cache
EXCLUDES="not ... and not ..."
EXCLUDES+=...
#%%pytest -k "$EXCLUDES"
%pytest \
  --ignore=libcst/codegen/tests/test_codegen_clean.py \
  --ignore=libcst/metadata/tests/test_type_inference_provider.py
# end all_tests
%endif
# end tests
%endif


%files -n python3-libcst -f %{pyproject_files}
%license LICENSE.dependencies


%changelog
%autochangelog
