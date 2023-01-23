Summary:       X11 composite manager
Name:          xcompmgr
Version:       1.1.8
Release:       6%{?dist}
License:       MIT
URL:           https://gitlab.freedesktop.org/xorg/app/xcompmgr
Source0:       https://www.x.org/archive/individual/app/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: libX11-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrender-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXext-devel
BuildRequires: pkgconfig

%description
xcompmgr is a sample compositing manager for X servers supporting the XFIXES,
DAMAGE, and COMPOSITE extensions. It enables basic eye-candy effects

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md ChangeLog
%{_bindir}/xcompmgr
%{_mandir}/man1/xcompmgr.1*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.1.8-2
- Unretire package
- Update URL
- Install README as doc
- Use the appropriate macro to install the license
- Relax globbing for man pages
- Convert specfile from tabs to spaces

* Mon Feb 17 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.8-1
- Update to 1.1.8 fixes rhbz#1692187
- Updated sources URL plus spec cleanup and modernization

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.7-1
- Rebuilt for new upstream release 1.1.7, fixes rhbz #1213038

* Sat Dec 10 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.6-9
- Spec clean up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Deji Akingunola <dakingun@gmail.com> - 1.1.6-1
- Update to version 1.1.6

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 02 2009 Deji Akingunola <dakingun@gmail.com> - 1.1.5-1
- New release 1.1.5

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Deji Akingunola <dakingun@gmail.com> - 1.1.4-1
- New release 1.1.4

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 1.1.3-8
- Rebuild for gcc43

* Wed Aug 22 2007 Deji Akingunola <dakingun@gmail.com> - 1.1.3-7
- Update License tag and Rebuild

* Mon Aug 28 2006 Deji Akingunola <dakingun@gmail.com> - 1.1.3-6
- Rebuild for FC6

* Mon Jul 24 2006 Deji Akingunola <dakingun@gmail.com> 1.1.3-5
- Add pkgconfig to the BRs

* Thu Jun 29 2006 Deji Akingunola <dakingun@gmail.com> 1.1.3-4
- Use STL in the license field

* Sat Apr 22 2006 Deji Akingunola <dakingun@gmail.com> 1.1.3-3
- Fix Changelog typo
- Explicitly use MIT license as opposed to to MIT/X11

* Tue Nov 08 2005 Deji Akingunola <dakingun@gmail.com> 1.1.3-2
- Fix rpmlint error on description line
- Package the changelog file as doc

* Tue Nov 08 2005 Deji Akingunola <dakingun@gmail.com> 1.1.3-1
- Initial build.
