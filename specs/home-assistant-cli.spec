Name:           home-assistant-cli
Version:        1.0.0
Release:        1%{?dist}
Summary:        Command-line tool for Home Assistant

License:        Apache-2.0
URL:            https://github.com/home-assistant/home-assistant-cli
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# Slightly adapted version of https://github.com/home-assistant-ecosystem/home-assistant-cli/pull/458 based on 1.0.0
Patch0:         458.patch

BuildRequires:  python3-devel

%description
The Home Assistant Command-line interface (hass-cli) allows one to work with
a local or a remote Home Assistant instance directly from the command-line.

%prep
%autosetup -n %{name}-%{version} -p1

# Main dependencies
%pyproject_patch_dependency packaging:drop_upper
%pyproject_patch_dependency regex:drop_upper
%pyproject_patch_dependency tabulate:drop_upper

# Test dependencies
%pyproject_patch_dependency pre-commit:drop_upper
%pyproject_patch_dependency pytest-cov:drop_upper
%pyproject_patch_dependency pytest:drop_constraints
%pyproject_patch_dependency types-dateparser:ignore
%pyproject_patch_dependency types-requests:drop_constraints
%pyproject_patch_dependency types-tabulate:ignore

%generate_buildrequires
%pyproject_buildrequires -g test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files homeassistant_cli

%check
%pytest -k "not test_commands_loads[template]"

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.md
%{_bindir}/hass-cli

%changelog
* Thu Apr 30 2026 Daniel Milnes <daniel@daniel-milnes.uk> - 1.0.0-1
- Update to 1.0.0 (rhbz#2457679)
- Migrate to pyproject-srpm-macros (rhbz#2377284)
- Fix Fedora 44 FTBFS (rhbz#2429404)

* Wed Apr 08 2026 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.6-19
- Omit some unwanted test dependencies

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.9.6-17
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.9.6-16
- Rebuilt for Python 3.14.0rc2 bytecode

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.9.6-14
- Rebuilt for Python 3.14

* Tue Mar 11 2025 Daniel Milnes <daniel@daniel-milnes.uk> - 0.9.6-13
- Apply patch to allow modern DateParser rhbz#2349396

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9.6-10
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Daniel Milnes <daniel@daniel-milnes.uk> - 0.9.6-7
- Migrate license to SPDX

* Sat Dec 30 2023 Daniel Milnes <daniel@daniel-milnes.uk> - 0.9.6-6
- Allow newer ruamel (closes rhbz#2246610)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.9.6-4
- Rebuilt for Python 3.12

* Sat Mar 11 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.6-3
- Allow later dateparser

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.6-1
- Update to latest upstream release 0.9.6

* Sat Oct 01 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Update to latest upstream release 0.9.5 (closes rhbz#2058155)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.9.4-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.4-1
- Update to latest upstream release 0.9.4 (closes rhbz#1946226)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.1-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Update to latest upstream release 0.9.1

* Mon Apr 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to latest upstream release 0.9.0

* Tue Mar 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-2
- Add missing BR

* Sun Nov 17 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Update to latest upstream release 0.8.0

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Initial package for Fedora
