Name:           python-gpiozero
Version:        2.0.1
Release:        4%{?dist}
Summary:        Interface to GPIO on Raspberry Pi

License:        BSD-3-Clause
URL:            https://github.com/RPi-Distro/python-gpiozero
Source:         %{pypi_source gpiozero}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A simple interface to GPIO devices with Raspberry Pi.

%package -n     python3-gpiozero
Summary:        %{summary}
# Several files have `import pkg_resources`
Requires:       python3dist(setuptools)
Recommends:     python3dist(pigpio)

%description -n python3-gpiozero
A simple interface to GPIO devices with Raspberry Pi.


%prep
%autosetup -n gpiozero-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gpiozero gpiozerocli

%check
# running the actual testsuite requires a real Raspberry Pi
%pyproject_check_import -e 'gpiozero.pins.*io'

%files -n python3-gpiozero -f %{pyproject_files}
%doc README.rst
%{_bindir}/pinout
%{_bindir}/pintest

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.13

* Wed Feb 21 2024 Benson Muite <benson_muite@emailplus.org> - 2.0.1-1
- Upgrade to latest release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Cristian Delgado <crissdell@protonmail.com> - 2.0-1
- Update to 2.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.2-9
- Rebuilt for Python 3.12

* Fri Mar 31 2023 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-8
- Require runtime dependencies during build
- Run import check during the build
- Convert the license tag to SPDX
- Install the LICENSE.rst file
- Fixes: rhbz#2183380

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.2-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.2-2
- Rebuilt for Python 3.10

* Thu Apr 01 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.6.2-1
- Update to 1.6.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.9

* Wed Mar 18 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-1
- Initial package
