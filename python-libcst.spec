%global _without_docs 1
%global _without_tests 1
%if 0%{?rhel}
%bcond_with docs
%bcond_with tests
%else
%bcond_without docs
%bcond_without tests
%endif

# Created by pyp2rpm-3.3.5
%global pypi_name libcst

%global common_description %{expand:
LibCST parses Python source code as a CST tree that keeps all formatting
details (comments, whitespaces, parentheses, etc). It's useful for building
automated refactoring (codemod) applications and linters.

LibCST creates a compromise between an Abstract Syntax Tree (AST) and a
traditional Concrete Syntax Tree (CST). By carefully reorganizing and naming
node types and fields, it creates a lossless CST that looks and feels like an
AST.}

Name:           python-%{pypi_name}
Version:        0.3.21
Release:        %autorelease
Summary:        A concrete syntax tree with AST-like properties for Python 3

# see LICENSE in the upstream sources for the breakdown
License:        MIT and (MIT and Python) and ASL 2.0
URL:            https://github.com/Instagram/LibCST
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml) >= 5.2
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(hypothesmith)
%endif
BuildRequires:  python3dist(typing-inspect) >= 0.4
%if %{with docs}
BuildRequires:  graphviz
BuildRequires:  sed
BuildRequires:  python3-docs
BuildRequires:  python3-metakernel-python
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(nbsphinx) >= 0.4.2
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.4.3
%endif

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%if %{with docs}
%package        doc
Summary:        %{name} documentation
Requires:       python3-docs

%description    doc
Documentation for %{name}
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/source/conf.py
%endif

%build
%py3_build
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
# test_codegen_clean is tracked in https://github.com/Instagram/LibCST/issues/304
# test_codemod_cli is tracked in https://github.com/Instagram/LibCST/issues/331
# test_type_enforce is tracked in https://github.com/Instagram/LibCST/issues/305
# test_type_inference_provider requires pyre which is not packaged
%if %{with tests}
%pytest \
  --ignore=libcst/codegen/tests/test_codegen_clean.py \
  --ignore=libcst/codemod/tests/test_codemod_cli.py \
  --ignore=libcst/tests/test_type_enforce.py \
  --ignore=libcst/metadata/tests/test_type_inference_provider.py
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
