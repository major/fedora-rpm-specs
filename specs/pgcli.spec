Name:           pgcli
Version:        4.1.0
Release:        2%{?dist}
Summary:        CLI for Postgres Database. With auto-completion and syntax highlighting

License:        BSD-3-Clause
URL:            https://www.pgcli.com/
Source:         %{pypi_source pgcli}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  help2man

# Workaround for missing dependency for pure-Python implementation and missing
# python_c module in python-psycopg3,
# https://bugzilla.redhat.com/show_bug.cgi?id=2266555.
%if %{defined fc41}
# Require the version in which the bug was fixed.
BuildRequires:  python-psycopg3 >= 3.1.19-1
Requires:       python-psycopg3 >= 3.1.19-1
%elif %{defined fc40}
# This was never fixed in Fedora 40, so we must keep the workaround
# indefinitely there.
BuildRequires:  libpq
Requires:       libpq
%endif

# Additional BuildRequires for tests, not in the package metadata. Versions
# come from tox.ini, https://github.com/dbcli/pgcli/blob/%%{version}/tox.ini.
# Note that upstream wants pytest <= 3.0.7, and we will have to unpin it and
# hope for the best; and that upstream wants mock, which is deprecated
# (https://fedoraproject.org/wiki/Changes/DeprecatePythonMock) and unnecessary.
BuildRequires:  python3dist(pytest) >= 2.7
BuildRequires:  python3dist(behave) >= 1.2.4
BuildRequires:  python3dist(pexpect) >= 3.3
BuildRequires:  python3dist(sshtunnel) >= 0.4

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-pgcli

%description
CLI for Postgres Database. With auto-completion and syntax highlighting

%pyproject_extras_subpkg -n python3-pgcli keyring

%generate_buildrequires
%pyproject_buildrequires -x keyring

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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 4.1.0-1
- Update to 4.1.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 4.0.1-6
- Rebuilt for Python 3.13

* Thu Mar 28 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 4.0.1-5
- Work around a python-psycopg3 package bug

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 01 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 4.0.1-2
- Small changes to simplify and modernize packaging
- Assert that the .dist-info directory contains a license file
- Generate a man page

* Thu Nov 02 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.0.1-1
- Update to 4.0.1 (close RHBZ#2246795)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.0-2
- Update License to SPDX

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
