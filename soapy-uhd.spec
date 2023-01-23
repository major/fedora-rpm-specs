Name:		soapy-uhd
Version:	0.4.1
Release:	10%{?dist}
Summary:	Soapy SDR plugins for UHD supported SDR devices
License:	GPLv3
URL:		https://github.com/pothosware/SoapyUHD
Source:		%{URL}/archive/%{name}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	uhd-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	boost-devel
# For module directories
Requires:	uhd
Requires:	SoapySDR

%description
Soapy SDR plugins for UHD supported SDR devices.

%prep
%autosetup -n SoapyUHD-%{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md Changelog.txt
%{_libdir}/SoapySDR/modules*.*/*.so
%{_libdir}/uhd/modules/*.so

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-9
- Rebuilt for new uhd
  Resolves: rhbz#2129788

* Sat Jul 30 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-8
- Rebuilt for new uhd

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-6
- Rebuilt for new uhd
  Resolves: rhbz#2077806

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Matt Domsch <matt@domsch.com> - 0.4.1-4
- Rebuilt for SoapySDR 0.8.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul  2 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-2
- Rebuilt for new uhd

* Mon Feb  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-1
- New version

* Mon Feb  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.6-5
- Rebuilt for new uhd
  Resolves: rhbz#1925575
- Updated cmake macros

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 0.3.6-2
- Use __cmake_in_source_build

* Thu Apr 16 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.6-1
- Initial version
