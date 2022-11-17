%global pypi_name pgcli

Name:           %{pypi_name}
Version:        3.5.0
Release:        1%{?dist}
Summary:        CLI for Postgres Database. With auto-completion and syntax highlighting

License:        BSD
URL:            https://www.pgcli.com/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# Additional BuildRequires for tests, not in the package metadata. Versions
# come from tox.ini in unreleased upstream sources. Note that upstream wants
# pytest <= 3.0.7, and we will have to unpin it and hope for the best.
BuildRequires:  python3dist(pytest) >= 2.7
BuildRequires:  python3dist(behave) >= 1.2.4
BuildRequires:  python3dist(pexpect) >= 3.3
BuildRequires:  python3dist(sshtunnel) >= 0.4

%py_provides python3-%{pypi_name}

%description
CLI for Postgres Database. With auto-completion and syntax highlighting

%pyproject_extras_subpkg -n python3-%{pypi_name} keyring

%generate_buildrequires
%pyproject_buildrequires -x keyring

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -f %{pyproject_files}
%doc README.rst changelog.rst
%{_bindir}/%{pypi_name}

%changelog
* Thu Nov 03 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.0-1
- Update to 3.5.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Python Maint <python-maint@redhat.com> - 3.1.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.10

* Mon Mar 29 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.1.0-2
- Resolve RHBZ#1923075
- Use pyproject-rpm-macros to eliminate error-prone manual BR’s
- Do not manually duplicate automatic Requires
- Drop obsolete sed invocation on setup.py
- Do not use obsolete python_provide macro; use py_provides macro instead
- Add the Python extras metapackage for the keyring extra
- Use the pytest macro
- Stop removing bundled egg-info
- Switch to HTTPS URL

* Sat Feb 20 2021 Dick Marinus <dick@mrns.nl - 3.1.0-1
- Update to v3.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.0-4
- lower requirements to prompt_toolkit 2.0.6 +

* Tue Jun 2 2020 Dick Marinus <dick@mrns.nl> - 3.0.0-3
- Add tests

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.0-1
- Initial package.
- fix autosetup macro usage
