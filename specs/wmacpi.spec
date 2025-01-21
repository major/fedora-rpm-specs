%define _legacy_common_support 1

%global commit d583dfc9603e004b1c6a870f5475a21475b581f7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wmacpi
Version:        2.3
Release:        12.20200618git%{shortcommit}%{?dist}
Summary:        Dockapp for laptop acpi/apm information

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.dockapps.net/wmacpi
Source0:	https://repo.or.cz/dockapps.git/snapshot/%{commit}.tar.gz
#Source0:        https://www.dockapps.net/download/wmacpi-2.3.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libdockapp-devel

%description
Dockapp which displays acpi/apm information.
his is a typical laptop ACPI dockapp. One interesting feature is the "timer" 
mode, where you can keep track of how long the laptop has been "on battery". 
This is opposite of the information usually provided by the BIOS, which is 
"time remaining", and in many cases wrong. This option can be toggled at 
run-time. System messages scroll on the bottom of the window, AC plug flashes 
when battery is charging, and green LED inside the big button flashes red if 
battery level is critical low.

%prep
%autosetup -n dockapps-%{shortcommit}/wmacpi

%build
# -lXpm -lXext are not directly needed, only through libdockapp
CFLAGS="%{build_cflags} -ansi" LDFLAGS="%{build_ldflags} -lX11 -ldockapp" \
      %make_build

%install
%make_install PREFIX="%{_prefix}"


%files
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/wmacpi
%{_mandir}/man1/wmacpi.1*
%{_bindir}/wmacpi-cli
%{_mandir}/man1/wmacpi-cli.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-12.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3-11.20200618gitd583dfc
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-10.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2.20200618gitd583dfc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 2.3-1.20200618gitd583dfc
- Update to make work with libdockapp 0.7.3

* Sun Mar 29 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 2.3-1
- Fix FTBFS for Fedora Rawhide and 32
- Update to 2.3
- Modernize the spec-file

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.24.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.23.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.22.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.21.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.20.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.19.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.18.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.17.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.16.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.15.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.14.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.13.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.12.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.11.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.10.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.2-0.9.rc5
- upgrade to rc5

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.7.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2-0.4.rc1
- Autorebuild for GCC 4.3

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 2.2-0.3.rc1
- Rebuilt for gcc43

* Thu Aug 23 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.2-0.2.rc1
- version upgrade
- new license tag

* Tue Jan 23 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
2.2-0.1.a1
- version upgrade (#201851)

* Wed Jan 10 2007 Patrice Dumas <pertusus[AT]free.fr> 2.1-1
- update to 2.1

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.34-7
- FE6 rebuild

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.34-6
- Rebuild for Fedora Extras 5

* Fri Nov 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.34-5
- modular xorg integration

* Sat Aug 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.34-4
- better description
- add dist tag

* Sat Aug 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.34-3
- fix x86_64 xorg lib dir

* Sat Aug 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.34-2
-minor cleanups

* Fri Jun 03 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.34-1
- Initial Release
