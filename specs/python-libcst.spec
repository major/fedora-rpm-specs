# need updated libcst to update hypothesmith
# and older hypothesmith does not work with newer hypothesis
%bcond bootstrap 0
%bcond tests %{without bootstrap}
# Use --with all_tests to run all tests
%bcond all_tests 0

Name:           python-libcst
Version:        1.9.0
Release:        %autorelease
Summary:        A concrete syntax tree with AST-like properties

# See LICENSE in the upstream sources for the breakdown.
# MIT AND (MIT AND PSF-2.0) AND Apache-2.0 → MIT AND PSF-2.0 AND Apache-2.0
License:        MIT AND PSF-2.0 AND Apache-2.0
# Licenses from statically-linked Rust dependencies (output of
# %%{cargo_license_summary}):
#
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# MIT
# MIT AND (MIT AND PSF-2.0)
# MIT OR Apache-2.0
# Unlicense OR MIT
#
# Licenses above that are *not* in the source license expression:
%global additional_rust_licenses %{shrink:
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (MIT OR Apache-2.0) AND
    (Unlicense OR MIT)}
# LICENSE.dependencies contains a full license breakdown
URL:            https://github.com/Instagram/LibCST
Source:         %{pypi_source libcst}

BuildRequires:  cargo-rpm-macros
BuildRequires:  tomcli

%if %{with tests}
# test dependencies are intermingled with dev dependencies
# so list them manually for now
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
LibCST parses Python source code as a CST tree that keeps all formatting
details (comments, whitespaces, parentheses, etc). It’s useful for building
automated refactoring (codemod) applications and linters.

LibCST creates a compromise between an Abstract Syntax Tree (AST) and a
traditional Concrete Syntax Tree (CST). By carefully reorganizing and naming
node types and fields, it creates a lossless CST that looks and feels like an
AST.}

%description %_description

%package -n     python3-libcst
Summary:        %{summary}
License:        %{license} AND %{additional_rust_licenses}
# LICENSE.dependencies contains a full license breakdown

# Documentation is hard to build since libcst.native is not available to import until %%install
Obsoletes:      python-libcst-doc < 1.1.0-1

%description -n python3-libcst %_description


%prep
%autosetup -p1 -C

# remove version locks
find . -name Cargo.lock -print -delete

# drop unused, benchmark-only dev-dependencies
tomcli set native/libcst/Cargo.toml del dev-dependencies.criterion
tomcli set native/libcst/Cargo.toml del dev-dependencies.rayon

%cargo_prep

%generate_buildrequires
for p in libcst_derive libcst; do
  cd native/$p
  # dev dependencies need to be included, setuptools_rust seems to include them unconditionally
  %cargo_generate_buildrequires -t
  cd ../..
done
%pyproject_buildrequires


%build
# write license summary and breakdown
cd native
%{cargo_license_summary}
%{cargo_license} > ../LICENSE.dependencies
cd ..

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files --assert-license libcst


%check
# Guard against accidental loss of LICENSE.dependencies from the .dist-info
# directory.
[ -n "$(find '%{buildroot}%{python3_sitearch}' -name LICENSE.dependencies)" ]

%pyproject_check_import --exclude='libcst.tests.*'

%if %{with tests}
mod='%{buildroot}%{python3_sitearch}/libcst'
# Omit fuzz tests. These don’t make much sense downstream, and would require
# hypothesmith, which hasn’t been successfully rebuilt for Python 3.15.
ignore="${ignore-} --ignore=${mod}/tests/test_fuzz.py"

%if %{without all_tests}
ignore="${ignore-} --ignore=${mod}/codegen/tests/test_codegen_clean.py"
ignore="${ignore-} --ignore=${mod}/metadata/tests/test_type_inference_provider.py"
%endif

# A few tests aren’t practical to run when not building in-place
# Some kind of PYTHONPATH issue, it looks like
ignore="${ignore-} --ignore=${mod}/codemod/tests/test_codemod_cli.py"
# Broken path to fixtures for native tests (tries to find them at
# %%{buildroot}%%{python3_sitearch/native/libcst/tests/fixtures)
ignore="${ignore-} --ignore=${mod}/tests/test_roundtrip.py"

# Pure-Python parser
LIBCST_PARSER_TYPE=pure %pytest --import-mode=append ${ignore-} -v "${mod}"

# Rust (native) parser
%pytest --import-mode=append ${ignore-} -k "${k-}" -v "${mod}"

%dnl Cargo tests fail to build on ppc64le due to a linker error related to the
%dnl Python C API. It’s not obvious what’s going wrong here.
%ifnarch %{power64}
cd native
%cargo_test
%endif
%endif


%files -n python3-libcst -f %{pyproject_files}


%changelog
%autochangelog
