%global pypi_name pulsectl

Name:           python-%{pypi_name}
Version:        24.12.0
Release:        3%{?dist}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio

License:        MIT
URL:            https://pypi.org/project/%{pypi_name}
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pulseaudio-libs

%description
Python (3.x and 2.x) high-level interface and ctypes-based bindings
for PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).


%package     -n python3-%{pypi_name}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio

%description -n python3-%{pypi_name}
Python 3.x high-level interface and ctypes-based bindings for
PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).


%prep
%setup -n %{pypi_name}-%{version}


%build
%{py3_build}


%install
%{py3_install}


%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*egg-info/


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 24.12.0-2
- Rebuilt for Python 3.14

* Thu May 22 2025 Paul W. Frields <pfrields@scarlett> - 24.12.0-1
- Update to version 24.12.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Peter Oliver <rpm@mavit.org.uk> - 24.11.0-1
- Update to version 24.11.0.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 22.3.2-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 22.3.2-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 22.3.2-2
- Rebuilt for Python 3.11

* Fri Mar 25 2022 Paul W. Frields <pfrields@scarlett> - 22.3.2-1
- New upstream release 22.3.2 (#2067029)

* Fri Feb 11 2022 Paul W. Frields <pfrields@scarlett> - 22.1.3-1
- New upstream release 22.1.3 (#2002065)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 21.5.18-2
- Rebuilt for Python 3.10

* Mon May 31 2021 Paul W. Frields <pfrields@scarlett> - 21.5.18-1
- New upstream release 21.5.18 (#1958563)

* Fri Apr 16 2021 Paul W. Frields <pfrields@scarlett> - 21.3.4-1
- New upstream release 21.3.4 (#1932817)

* Sat Mar  6 2021 Paul W. Frields <stickster@gmail.com> - 21.3.2-1
- New upstream release 21.3.2 (#1932817)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Paul W. Frields <stickster@gmail.com> - 20.5.1-2
- New upstream release 20.5.1 (#1837830)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.4.3-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Paul W. Frields <stickster@gmail.com> - 20.4.3-1
- New upstream release 20.4.3 (#1825597)

* Tue Mar  3 2020 Paul W. Frields <stickster@gmail.com> - 20.2.4-1
- New upstream release 20.2.4 (#1808016)

* Tue Feb 11 2020 Paul W. Frields <stickster@gmail.com> - 20.2.2-1
- New upstream release 20.2.2 (#1790078)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov  9 2019 Paul W. Frields <stickster@gmail.com> - 19.10.4-1
- Update to latest upstream 19.10.4 (#1759622)

* Mon Oct 14 2019 Paul W. Frields <stickster@gmail.com> - 19.10.0-1
- Update to latest upstream 19.10.0 (#1759622)

* Wed Sep 25 2019 Paul W. Frields <stickster@gmail.com> - 19.9.5-1
- Update to latest upstream 19.9.5 (#1754263)

* Wed Sep  4 2019 Paul W. Frields <stickster@gmail.com> - 18.12.5-1
- Initial RPM release
