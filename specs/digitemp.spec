Summary:        Dallas Semiconductor 1-wire device reading console application
Name:           digitemp
Version:        3.7.2
Release:        14%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.digitemp.com/
Source0:        https://github.com/bcl/digitemp/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        dthowto.txt
Source2:        DS9097_Schematic.gif
Patch0:         https://github.com/bcl/digitemp/pull/38.patch#/digitemp-3.7.2-prototype.patch
BuildRequires:  gcc
%if 0%{!?_without_libusb:1}
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires:  libusb-compat-0.1-devel
%else
BuildRequires:  libusb-devel
%endif
%endif
BuildRequires:  make

%description
DigiTemp is a simple to use console application for reading values from
Dallas Semiconductor 1-wire devices. Its main use is for reading temperature
sensors, but it also reads counters and understands the 1-wire hubs with
devices on different branches of the network. DigiTemp now supports the
following 1-wire temperature sensors: DS18S20 (and DS1820), DS18B20, DS1822,
the DS2438 Smart Battery Monitor, DS2422 and DS2423 Counters, DS2409
MicroLAN Coupler (used in 1-wire hubs) and the AAG TAI-8540 humidity sensor.

%prep
%autosetup -p1
cp -pf %{SOURCE1} %{SOURCE2} .

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIE -DPIC"
%make_build ds9097
%make_build clean
%make_build ds9097u
%if 0%{!?_without_libusb:1}
%make_build clean
%make_build ds2490
%endif

%install
install -D -p -m 0755 %{name}_DS9097 $RPM_BUILD_ROOT%{_bindir}/%{name}_DS9097
install -D -p -m 0755 %{name}_DS9097U $RPM_BUILD_ROOT%{_bindir}/%{name}_DS9097U
%if 0%{!?_without_libusb:1}
install -D -p -m 0755 %{name}_DS2490 $RPM_BUILD_ROOT%{_bindir}/%{name}_DS2490
%endif
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o ChangeLog.utf8 ChangeLog
touch -c -r ChangeLog ChangeLog.utf8; mv -f ChangeLog.utf8 ChangeLog

%files
%license COPYING COPYRIGHT
%doc ChangeLog CREDITS FAQ README TODO
%doc dthowto.txt DS9097_Schematic.gif
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Robert Scheck <robert@fedoraproject.org> 3.7.2-1
- Upgrade to 3.7.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 08 2013 Robert Scheck <robert@fedoraproject.org> 3.6.0-10
- Solved build failures with "-Werror=format-security" (#1037039)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 13 2009 Robert Scheck <robert@fedoraproject.org> 3.6.0-4
- Run 'make clean' after each make for working USB (#517284)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 3.6.0-2
- Rebuilt against gcc 4.4 and rpm 4.6

* Sun Jan 25 2009 Robert Scheck <robert@fedoraproject.org> 3.6.0-1
- Upgrade to 3.6.0

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 3.5.0-3
- Rebuilt against gcc 4.3

* Tue Aug 28 2007 Robert Scheck <robert@fedoraproject.org> 3.5.0-2
- Updated the license tag according to the guidelines

* Sun Jan 07 2007 Robert Scheck <robert@fedoraproject.org> 3.5.0-1
- Upgrade to 3.5.0
- Initial spec file for Fedora and Red Hat Enterprise Linux
