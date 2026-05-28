Name:           python-gast
Version:        0.7.0
Release:        %autorelease
Summary:        Python AST that abstracts the underlying Python version
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/gast/
Source:         %{pypi_source gast}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description %{expand:
A generic AST to represent Python2 and Python3's Abstract Syntax Tree (AST).
GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.}
%description %_description


%package -n     python3-gast
Summary:        %{summary}

%description -n python3-gast %_description


%prep
%autosetup -p1 -n gast-%{version}


%generate_buildrequires
# Don't use tox options to avoid an unwanted dependency in RHEL
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files gast


%check
%pytest -v


%files -n python3-gast -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
