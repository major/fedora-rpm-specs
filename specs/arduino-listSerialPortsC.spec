%global shortname listSerialPortsC

Name:		arduino-%{shortname}
Version:	1.4.0
Release:	21%{?dist}
Summary:	Simple multiplatform program to list serial ports with vid/pid/iserial fields
# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:	LGPL-3.0-or-later
URL:		http://www.arduino.cc
Source0:	https://github.com/arduino/listSerialPortsC/archive/%{version}.tar.gz#/%{shortname}-%{version}.tar.gz
BuildRequires:	libserialport-devel
%ifarch %{java_arches}
BuildRequires:	java-devel
%endif
BuildRequires:	gcc

%description
Simple environment to test libserialport in a single build machine fashion.

%prep
%setup -q -n %{shortname}-%{version}

%build
gcc `pkg-config --cflags libserialport` %{optflags} main.c `pkg-config --libs libserialport` -o listSerialC
%ifarch %{java_arches}
gcc `pkg-config --cflags libserialport` %{optflags} jnilib.c -I/usr/lib/jvm/java/include/ -I/usr/lib/jvm/java/include/linux -shared -fPIC `pkg-config --libs libserialport` -o liblistSerialsj.so
%endif

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 listSerialC %{buildroot}%{_bindir}
# Yes, this is not normal, but this isn't really a useful lib, it's only for arduino.
%ifarch %{java_arches}
mkdir -p %{buildroot}%{_datadir}/arduino/lib/
install -m755 liblistSerialsj.so %{buildroot}%{_datadir}/arduino/lib/
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/listSerialC
%ifarch %{java_arches}
%{_datadir}/arduino/lib/liblistSerialsj.so
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.0-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.4.0-14
- conditionalize the java bits of this weird old package

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.0-12
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.4.0-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Tom Callaway <spot@fedoraproject.org> - 1.4.0-1
- initial package
