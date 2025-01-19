Summary:       Library for interfacing Music Player Daemon
Name:          libmpdclient
Version:       2.22
Release:       3%{?dist}
License:       BSD-2-Clause OR BSD-3-Clause
URL:           https://www.musicpd.org/
Source0:       %{url}download/libmpdclient/2/libmpdclient-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: meson
BuildRequires: gcc

%package devel
Summary: Header files for developing programs with %{name}
Requires: %{name} = %{version}-%{release}

%description
A stable, documented, asynchronous API library for interfacing MPD
in the C, C++ & Objective C languages.

%description devel
%{name}-devel is a sub-package which contains header files and
libraries for developing programs with %{name}.

%prep
%autosetup

%build
%meson -D documentation=true
%meson_build

%install
%meson_install
# move the API documentation to the devel package
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-devel
mv %{buildroot}%{_defaultdocdir}/%{name}/html %{buildroot}%{_defaultdocdir}/%{name}-devel
rm %{buildroot}%{_defaultdocdir}/%{name}/BSD-[23]-Clause.txt

%files
%license LICENSES/BSD-2-Clause.txt LICENSES/BSD-3-Clause.txt
%doc AUTHORS README.rst NEWS
%{_libdir}/libmpdclient.so.2*

%files devel
%{_defaultdocdir}/%{name}-devel
%{_libdir}/libmpdclient.so
%{_libdir}/pkgconfig/libmpdclient.pc
%{_includedir}/mpd/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 2.22-1
- Update to 2.22

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 2.20-1
- Update to 2.20

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 19 2020 Vasiliy Glazov <vascom2@gmail.com> - 2.19-1
- Update to 2.19

* Tue May 19 2020 Vasiliy Glazov <vascom2@gmail.com> - 2.18-1
- Update to 2.18

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jul 30 2019 Vasiliy Glazov <vascom2@gmail.com> - 2.16-1
- Update to 2.16

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Adrian Reber <adrian@lisas.de> - 2.14-1
- updated to 2.14
- added BR gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Adrian Reber <adrian@lisas.de> - 2.13-1
- updated to 2.13 (#1476754)
- adapted to new build system (meson)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.9-1
- update to upstream release 2.9
- update URL
- add detached signature as Source1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 21 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 2.7-1
- update to upstream version 2.7
- remove obsolete BuildRoot tag, %%clean section and %%defattr

* Wed Mar 02 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.4-1
- version upgrade

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Adrian Reber <adrian@lisas.de> - 2.2-1
- fixes "FTBFS libmpdclient-2.1-3.fc13" (#631331)
- updated to 2.2

* Wed Jan 27 2010 Adrian Reber <adrian@lisas.de> - 2.1-3
- make devel subpackage require %%{name} = %%{version}-%%{release}

* Fri Jan 08 2010 Michal Nowak <mnowak@redhat.com> - 2.1-2
- spec file fixes

* Thu Jan 07 2010 Adrian Reber <adrian@lisas.de> - 2.1-1
- updated to 2.1

* Thu Dec 03 2009 Adrian Reber <adrian@lisas.de> - 2.0-1
- initial spec file (based on libmpd)
