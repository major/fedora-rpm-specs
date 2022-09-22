%define _legacy_common_support 1
%global commit be2f4b3010e78f7d6c68922db36641ab743f9db9

Name:           wmweather+
Version:        2.18^20211125gitbe2f4b30
Release:        1%{?dist}
Summary:        Weather status dockapp

License:        GPLv2+
URL:            http://sourceforge.net/projects/wmweatherplus/
#Source0:        https://downloads.sourceforge.net/project/wmweatherplus/%%{name}/%%{name}-%%{version}.tar.gz
Source0:	https://sourceforge.net/code-snapshots/git/w/wm/wmweatherplus/git.git/wmweatherplus-git-%{commit}.zip

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequireS:  libXpm-devel
BuildRequires:  WINGs-devel
BuildRequires:  pcre2-devel
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  autoconf automake

%description
wmweather+ will download the National Weather Serivce METAR bulletins; AVN,
ETA, and MRF forecasts; and any weather map for display in a WindowMaker
dockapp. Think wmweather with a smaller font, forecasts, a weather map, and a
sky condition display.

%prep
%autosetup -n wmweatherplus-git-%{commit}

autoreconf -fvi

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING README
%{_bindir}/wmweather+
%{_mandir}/man1/*

%changelog
* Tue Sep 20 2022 Jani Juhani Sinervo <jani@sinervo.fi> - 2.18^20211125gitbe2f4b30-1
- Update to latest upstream version
- Change to PCRE2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 11 2021 Jani Juhani Sinervo <jani@sinervo.fi> - 2.17-10
- Fix FTBFS with Autoconf 2.71

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 Jani Juhani Sinervo - 2.17-7
- Fix FTBFS on Rawhide and 32
- Modernize the spec-file

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 2.17-1
- version upgrade

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Andreas Bierfert <andreas.bierfert@lowlatency.de> - 2.15-7
- rebuilt

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 2.15-4
- rebuild for new windowmaker release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.15-2
- run autoreconf before configure for aclocal

* Tue Oct 14 2014 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.15-1
- version upgrade

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 2.11-5
- Rebuild against PCRE 8.30
- wraster headers moved from WindowMaker-devel to WINGs-devel

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 28 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.11-2
- add libcurl to BR

* Sun Mar 28 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.11-1
- fix FTBFS #564623
- version upgrade

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.9-12
- rebuilt with new openssl

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 2.9-9
- rebuild with new openssl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.9-8
- Autorebuild for GCC 4.3

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 2.9-7
- Rebuilt for gcc43

* Wed Dec 05 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.9-6
- bump

* Thu Aug 23 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.9-5
- new license tag
- rebuild for buildid

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.9-4
- FE6 rebuild

* Thu Sep 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.9-2
- add dist tag
- don't doc ChangeLog

* Fri Jun 03 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.9-1
- Initial Release
