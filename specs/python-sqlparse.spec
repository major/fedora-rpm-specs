Name:           python-sqlparse
Version:        0.5.3
Release:        %autorelease
Summary:        A non-validating SQL parser
License:        BSD-3-Clause
URL:            https://github.com/andialbrecht/sqlparse
Source:         %{pypi_source sqlparse}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
sqlparse is a non-validating SQL parser for Python. It provides support for
parsing, splitting and formatting SQL statements.}


%description %_description


%package -n     python3-sqlparse
Summary:        %{summary}


%description -n python3-sqlparse %_description


%prep
%autosetup -n sqlparse-%{version}

# fix ambiguous python shebang
%py3_shebang_fix sqlparse/cli.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l sqlparse


%check
%pytest -v tests


%files -n python3-sqlparse -f %{pyproject_files}
%doc CHANGELOG README.rst
%{_bindir}/sqlformat


%changelog
%autochangelog
