Summary: Bluecurve icon theme
Name: bluecurve-icon-theme
Version: 8.0.2
Release: 32%{?dist}
BuildArch: noarch
License: GPL-2.0-or-later
# There is no official upstream yet
Source0: %{name}-%{version}.tar.bz2
URL: http://www.redhat.com

Requires: system-logos
Requires: bluecurve-cursor-theme
Requires(post): coreutils

# we require XML::Parser for our in-tree intltool
BuildRequires: gcc
BuildRequires: perl(XML::Parser)
BuildRequires: perl(Getopt::Long)
BuildRequires: make

%description
This package contains Bluecurve style icons.

%package -n bluecurve-cursor-theme
Summary: Bluecurve cursor theme

%description -n bluecurve-cursor-theme
This package contains Bluecurve style cursors.

%prep
%autosetup

%build
%configure
make

%install
%make_install

# These are empty
rm -f ChangeLog NEWS README

touch %{buildroot}%{_datadir}/icons/Bluecurve/icon-theme.cache

# The upstream packages may gain po files at some point in the near future
# %find_lang %{name} || touch %{name}.lang

%files
%doc AUTHORS
%license COPYING
%{_datadir}/icons/Bluecurve/index.theme
%{_datadir}/icons/Bluecurve/16x16
%{_datadir}/icons/Bluecurve/20x20
%{_datadir}/icons/Bluecurve/24x24
%{_datadir}/icons/Bluecurve/32x32
%{_datadir}/icons/Bluecurve/36x36
%{_datadir}/icons/Bluecurve/48x48
%{_datadir}/icons/Bluecurve/64x64
%{_datadir}/icons/Bluecurve/96x96
%ghost %{_datadir}/icons/Bluecurve/icon-theme.cache

%files -n bluecurve-cursor-theme
%doc AUTHORS
%license COPYING
%dir %{_datadir}/icons/Bluecurve
%{_datadir}/icons/Bluecurve/Bluecurve.cursortheme
%{_datadir}/icons/Bluecurve/cursors
%{_datadir}/icons/Bluecurve-inverse
%{_datadir}/icons/LBluecurve
%{_datadir}/icons/LBluecurve-inverse

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Neal Gompa <ngompa@fedoraproject.org> - 8.0.2-28
- Clean up and use SPDX license identifiers

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.0.2-17
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Filipe Rosset <rosset.filipe@gmail.com> - 8.0.2-14
- Fix FTBFS in rawhide rhbz #1307353 plus spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 23 2009 Ray Strode <rstrode@redhat.com> - 8.0.2-4
- Require coreutils for touch in post (bug 507581)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Matthias Clasen <mclasen@redhat.com> - 8.0.2-2
- Split off cursor theme as a separate package

* Mon Apr  7 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8.0.2-1
- Add some symlinks to make Bluecurve work well with KDE 4 (#408151)

* Fri Feb  1 2008 Matthias Clasen <mclasen@redhat.com> - 8.0.1-1
- Fix some lrt <-> ltr typos
- Flip some redo icons

* Fri Oct 12 2007 Ray Strode <rstrode@redhat.com> - 8.0.0-1
- Add a lot of missing icons back (bug 328391)
- redo Bluecurve Makefile to scale better to all the new icons
- bump version to 8.0.0

* Tue Sep 25 2007 Ray Strode <rstrode@redhat.com> - 1.0.0-1
- Initial import, version 1.0.0
