Name:           nox
Version:        2024.03.02
Release:        1%{?dist}
Summary:        Flexible test automation

License:        Apache-2.0
URL:            https://github.com/wntrblm/nox
# Using github source files since PyPI doesn't contain "tests" folder anymore
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-flask
BuildRequires:  python3-myst-parser
BuildRequires:  python3-pytest

%description
Nox is a command-line tool that automates testing in multiple Python
environments, similar to tox. Unlike tox, Nox uses a standard Python
file for configuration.

%prep
%autosetup -p1 -n nox-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x tox_to_nox

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nox

%check
%pytest -k "not test__create_venv_options[nox.virtualenv.CondaEnv.create-conda-CondaEnv]"

%files -f %{pyproject_files}
%{_bindir}/nox
%pycached %exclude %{python3_sitelib}/nox/tox_to_nox.py
%exclude %{python3_sitelib}/nox/tox_to_nox.jinja2
%exclude %{_bindir}/tox-to-nox

%pyproject_extras_subpkg -n nox tox_to_nox
%pycached %{python3_sitelib}/nox/tox_to_nox.py
%{python3_sitelib}/nox/tox_to_nox.jinja2
%{_bindir}/tox-to-nox

%changelog
* Mon Mar 04 2024 Lumír Balhar <lbalhar@redhat.com> - 2024.03.02-1
- Update to 2024.03.02 (rhbz#2267571)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.04.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.04.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.04.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2023.04.22-2
- Rebuilt for Python 3.12

* Tue May 02 2023 Lumír Balhar <lbalhar@redhat.com> - 2023.04.22-1
- Update to 2023.04.22 (rhbz#2188881)
- Use SPDX license identifier

* Thu Feb 16 2023 Lumír Balhar <lbalhar@redhat.com> - 2022.11.21-4
- Fix tox_to_nox for tox 4

* Tue Jan 24 2023 Lumír Balhar <lbalhar@redhat.com> - 2022.11.21-3
- Fix FTBFS

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.11.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 ondaaak <ondaaak@gmail.com> - 2022.11.21-1
- Update to 2022.11.21

* Mon Aug 22 2022 ondaaak <ondaaak@gmail.com> - 2022.8.7-1
- Update to 2022.8.7

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2022.1.7-2
- Rebuilt for Python 3.11

* Wed Mar 23 2022 ondaaak <ondaaak@gmail.com> - 2022.1.7-1
- Initial package for Fedora
