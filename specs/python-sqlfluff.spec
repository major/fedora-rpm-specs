Name:           python-sqlfluff
Version:        4.5.0
Release:        %autorelease
Summary:        The SQL Linter for Humans
License:        MIT
URL:            https://www.sqlfluff.com
Source:         %{pypi_source sqlfluff}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
SQLFluff is a dialect-flexible and configurable SQL linter. Designed with ELT
applications in mind, SQLFluff also works with Jinja templating and dbt.
SQLFluff will auto-fix most linting errors, allowing you to focus your time
on what matters.}

%description %_description

%package -n     python3-sqlfluff
Summary:        %{summary}

%description -n python3-sqlfluff %_description

%prep
%autosetup -p1 -n sqlfluff-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sqlfluff

%check
%pyproject_check_import

%files -n python3-sqlfluff -f %{pyproject_files}
%{_bindir}/sqlfluff
%license LICENSE.md

%changelog
%autochangelog
