%bcond check 1

Name:           python-astdoc
Version:        1.3.0
Release:        %autorelease
Summary:        Library for parsing AST and extracting docstring information

License:        MIT
URL:            https://github.com/daizutabi/astdoc
Source:         %{pypi_source astdoc}

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with check}
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
%endif

%global _description %{expand:
This package provides a lightweight Python library for parsing and analyzing
abstract syntax trees (AST) and extracting docstring information. Designed to
facilitate the documentation process, astdoc provides tools for developers to
easily access, manipulate, and generate documentation from Python code.}

%description %_description

%package -n     python3-astdoc
Summary:        %{summary}

%description -n python3-astdoc %_description

%prep
%autosetup -p1 -n astdoc-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l astdoc

%check
%if %{with check}
# https://github.com/daizutabi/astdoc/issues/22
%pytest -v \
  --deselect src/astdoc/ast.py::astdoc.ast._iter_defaults \
  --deselect src/astdoc/ast.py::astdoc.ast._iter_parameters \
  --deselect src/astdoc/ast.py::astdoc.ast.get_assign_type

%else
%pyproject_check_import
%endif

%files -n python3-astdoc -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
