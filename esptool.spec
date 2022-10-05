Name:           esptool
Version:        4.3
Release:        1%{?dist}
Summary:        A utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32

License:        GPLv2+
URL:            https://github.com/espressif/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Provides:       %{name}.py = %{version}-%{release}


%description
%{name}.py A command line utility to communicate with the ROM bootloader in
Espressif ESP8266 & ESP32 WiFi microcontroller. Allows flashing firmware,
reading back firmware, querying chip parameters, etc.
Developed by the community, not by Espressif Systems.


%prep
%autosetup -p1

# Remove shebangs from site-packages
grep -r '^#!' esp{efuse,secure,tool}/
sed -i 1d $(grep -rl '^#!' esp{efuse,secure,tool}/)


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files esptool espefuse espsecure
for NAME in %{name} espefuse espsecure ; do
  ln -s ./$NAME.py %{buildroot}%{_bindir}/$NAME
done


%check
%pyproject_check_import


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}.py
%{_bindir}/espefuse
%{_bindir}/espefuse.py
%{_bindir}/espsecure
%{_bindir}/espsecure.py


%changelog
* Wed Sep 21 2022 Karolina Surma <ksurma@redhat.com> - 4.3-1
- Update to 4.3
Resolves: rhbz#2126964

* Wed Aug 10 2022 Karolina Surma <ksurma@redhat.com> - 4.2.1-1
- Update to 4.2.1
Resolves: rhbz#2114692

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Karolina Surma <ksurma@redhat.com> - 4.1-3
- Gracefully finish esptool when port can't be open
Resolves: rhbz#2092910

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.1-2
- Rebuilt for Python 3.11

* Fri May 27 2022 Karolina Surma <ksurma@redhat.com> - 4.1-1
- Update to 4.1
Resolves: rhbz#2084581

* Mon Apr 11 2022 Karolina Surma <ksurma@redhat.com> - 3.3-1
- Update to 3.3
Resolves: rhbz#2066963

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Karolina Surma <ksurma@redhat.com> - 3.2-1
- Update to 3.2
Resolves: rhbz#2017113

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Karolina Surma <ksurma@redhat.com> - 3.1-1
- Update to 3.1
Resolves: rhbz#1965558

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0-2
- Rebuilt for Python 3.10

* Tue Apr 06 2021 Karolina Surma <ksurma@redhat.com> - 3.0-1
- Update to 3.0
Resolves: rhbz#1894863

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.8-1
- Update to 2.8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7-4
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7-1
- Updated to 2.7 (#1742098)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-1
- Updated to 2.6 (#1642062)

* Tue Jul 31 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Updated to 2.5.0 (#1609436)

* Mon Jul 16 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-1
- Updated to 2.4.1 (#1592835)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-2
- Rebuilt for Python 3.7

* Sat Mar 03 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-1
- Updated to 2.3.1 (#1551162)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-1
- Updated to 2.2.1 (#1539948)
- Update shebang handling
- Use automatic dependency generator

* Wed Aug 23 2017 Miro Hrončok <mhroncok@redhat.com> - 2.1-1
- New version 2.1 (#1484381)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-1
- New version 2.0.1 (#1465005)

* Thu Jun 22 2017 Miro Hrončok <mhroncok@redhat.com> - 2.0-1
- New version 2.0 (#1425422)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Miro Hrončok <mhroncok@redhat.com> - 1.3-1
- New version (#1392643)
- Use Python 3

* Tue Sep 06 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-1
- Initial package.
