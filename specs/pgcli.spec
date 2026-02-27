Name:           pgcli
Version:        4.4.0
Release:        %autorelease
Summary:        CLI for Postgres Database. With auto-completion and syntax highlighting

License:        BSD-3-Clause
URL:            https://www.pgcli.com/
Source:         %{pypi_source pgcli}

# Bump click minimum version to 8.3.1
Patch:          https://github.com/dbcli/pgcli/commit/d0a6cc2.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  help2man

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(behave)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(sshtunnel)

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-pgcli

%description
CLI for Postgres Database. With auto-completion and syntax highlighting

%pyproject_extras_subpkg -n python3-pgcli keyring sshtunnel

%generate_buildrequires
%pyproject_buildrequires -x keyring -x sshtunnel

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pgcli

# We must do this in %%install rather than in %%build in order to use the
# generated entry point:
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    PYTHONDONTWRITEBYTECODE=1 \
    help2man --no-info --version-string='%{version}' \
        --output='%{buildroot}%{_mandir}/man1/pgcli.1' \
        %{buildroot}%{_bindir}/pgcli

%check
%pytest

%files -f %{pyproject_files}
%doc README.rst changelog.rst
%{_bindir}/pgcli
%{_mandir}/man1/pgcli.1*

%changelog
%autochangelog
