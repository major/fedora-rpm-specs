%global POSTYEAR 2020
%global POSTMONTH 12
%global POSTNUM 1

%global _description %{expand:
Project Ubertooth is an open source wireless development platform suitable
for Bluetooth experimentation. Ubertooth ships with a capable BLE (Bluetooth
Smart) sniffer and can sniff some data from Basic Rate (BR) Bluetooth Classic
connections.}

Name:           ubertooth
Version:        %{POSTYEAR}.%{POSTMONTH}.R%{POSTNUM}
Release:        21%{?dist}
Summary:        Bluetooth wireless development platform for experimentation
# This package is only includes host part of the Ubertooth project, which is licensed under GPLv2.
# But parts of the firmware, which is running on the board, licensed under BSD (3 clause): lpcusb,
# and GPL v2 or later.
License:        GPL-2.0-only
URL:            https://github.com/greatscottgadgets/ubertooth
Source:         %{url}/releases/download/%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}/%{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}.tar.xz
Patch:          ubertooth-0001-remove-shebang-from-library-script.patch

BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libbtbb-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb1-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros

Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-specan-ui = %{version}-%{release}

%description    %_description

%package        -n lib%{name}
Summary:        Shared library for Bluetooth experimentation
Requires:       systemd-udev

%description    -n lib%{name} %_description

This package provides the the ubertooth shared library.

%package        devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        specan-ui
Summary:        Graphical spectrum analyzer for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-QtPy python3-pyside6%{?_isa}

%description    specan-ui
The %{name}-specan-ui is a basic spectrum analysis tool for the Ubertooth.


%prep
%autosetup -p1 -n %{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}

# Fix udev rules
sed -i -e 's/GROUP="@UBERTOOTH_GROUP@"/ENV{ID_SOFTWARE_RADIO}="1"/g' \
  host/misc/udev/40-ubertooth.rules.in

# Use the correct version
sed -i "s/version\s*=.*/version = '%{version}',/" \
  host/python/specan_ui/setup.py.in \
  host/python/specan_ui/setup.py

%build
%cmake \
    -DINSTALL_UDEV_RULES=on \
    -DUDEV_RULES_GROUP=plugdev \
    -DUDEV_RULES_PATH:PATH=%{_udevrulesdir} \
    -S host

%cmake_build

(
  cd host/python/specan_ui
  %py3_build
)


%install
%cmake_install
(
  cd host/python/specan_ui
  %py3_install
  install -Dp -m755 ubertooth-specan-ui %{buildroot}%{_bindir}
)

%files
%license COPYING TRADEMARK
%doc README.md
%{_bindir}/%{name}*
%exclude %{_bindir}/%{name}-specan-ui
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man7/%{name}.7*

%files -n lib%{name}
%license COPYING TRADEMARK
%doc README.md
%{_libdir}/lib%{name}.so.*
%{_udevrulesdir}/40-ubertooth.rules

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%files specan-ui
%doc host/python/specan_ui/README
%{_bindir}/%{name}-specan-ui
%{python3_sitelib}/specan
%{python3_sitelib}/specan-%{POSTYEAR}.%{POSTMONTH}.post%{POSTNUM}-py%{python3_version}.egg-info


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2020.12.R1-20
- Rebuilt for Python 3.14

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 27 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 2020.12.R1-18
- Make it build with the latest Python
  Fixes: RHBZ#2259655, RHBZ#2242706, RHBZ#2242709
- Update summary and description
- Drop deprecated macros

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2020.12.R1-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2020.12.R1-15
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2020.12.R1-12
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2020.12.R1-9
- Rebuilt for Python 3.11

* Thu Jun 16 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 2020.12.R1-8
- Fix build issues; Resolves: RHBZ#2069144

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2020.12.R1-7
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2020.12.R1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Sergey Avseyev <sergey.avseyev@gmail.com> 2020.12.R1-2
- Fix build with python 3.10

* Mon Jan 04 2021 Sergey Avseyev <sergey.avseyev@gmail.com> 2020.12.R1-1
- Update to 2020-12-R1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Sergey Avseyev <sergey.avseyev@gmail.com.com> - 2018.12.R1-8
- Rebuilt with python3-pyside2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.12.R1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.12.R1-6
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2018.12.R1-4
- Fix pyside imports in ubertooth-specan-ui

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.12.R1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2018.12.R1-2
- Add explicit curdir on CMake invocation

* Thu Dec 06 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.12.R1-1
- Update to 2018-12-R1

* Fri Aug 10 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.08.R1-1
- Update to 2018-08-R1

* Sun Jul 15 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2018.07.R1-3
- Added systemd as build requirement for _udevrulesdir macro

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.06.R1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2018.06.R1-1
- Update to 2018-06-R1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2017.03.R2-2
- Rebuilt for Python 3.7

* Mon Apr 23 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2017.03.R2-1
- Initial import
