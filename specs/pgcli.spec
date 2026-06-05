Name:           pgcli
Version:        4.5.0
Release:        %autorelease
Summary:        CLI for Postgres Database. With auto-completion and syntax highlighting

License:        BSD-3-Clause
URL:            https://www.pgcli.com/
Source:         %{pypi_source pgcli}

BuildArch:      noarch

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
%pyproject_buildrequires --extras keyring --extras sshtunnel

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files --assert-license pgcli

# We must do this in %%install rather than in %%build in order to use the
# generated entry point:
install --directory '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man --no-info --version-string='%{version}' \
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
