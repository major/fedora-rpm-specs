Name:		screenruler
Version:	1.2.1
Release:	4%{?dist}

Summary:	GNOME screen ruler
# SPDX confirmed
License:	GPL-2.0-or-later
URL:		https://salsa.debian.org/georgesk/screenruler

Source0:	https://salsa.debian.org/georgesk/screenruler/-/archive/upstream/%{version}/%{name}-upstream-%{version}.tar.bz2
Source2:	%{name}.appdata.xml
# Workaround for screenruler not showing window properly at startup
# bug 2275166
# Need reporting upstream
Patch0:	screenruler-1.2-gtkwidget-show_all-workaround.patch

BuildRequires:	make
BuildRequires:	desktop-file-utils
BuildRequires:	/usr/bin/appstream-util
BuildRequires:	/usr/bin/gettext
BuildRequires:	/usr/bin/msgmerge
BuildRequires:	/usr/bin/rxgettext

Requires:		rubygem(cairo)
Requires:		rubygem(gettext)
Requires:		rubygem(gtk3)

BuildArch:		noarch

%description
ScreenRuler lets you measure objects on your desktop
using six different metrics.

* Horizontal and vertical measurement in 6 different metrics: pixels,
  centimeters, inches, picas, points, and as a percentage of the ruler’s
  length.
* Color and font are customizable.
* Keyboard control for precise positioning.
* Ruler can be set to stay always on top of other windows.

%prep
%setup -q -n %{name}-upstream-%{version}
%patch -P0 -p1

%build
%make_build

%install
%make_install

# Add AppStream metadata
mkdir -p %{buildroot}%{_metainfodir}
install -cpm 0644 %{SOURCE2} \
	%{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license	COPYING
%doc	AUTHORS
%doc	README.md

%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%{_bindir}/%{name}
%dir	%{_datadir}/screenruler/
%{_datadir}/screenruler/*.glade
%{_datadir}/screenruler/*.png
%{_datadir}/screenruler/*.rb
%{_datadir}/screenruler/locale/
%{_datadir}/screenruler/utils/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-2
- Workaround for screenruler not showing window properly at startup
  (bug 2275166)

* Thu Apr 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-1
- 1.2.1

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 21 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2-1
- 1.2 (bug 2203515)
- upstream changed to salsa.debian.org
- switch to GTK3
- SPDX migration

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.96-9
- Patch to work with ruby25 for overriding loop issue

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.96-4
- Add appdata file to show this application in gnome-software
- Thanks to Samuel Gyger for appdata file (rh#1192923)
- Clean the spec to follow current packaging guidelines

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Deji Akingunola <dakingun@gmail.com> - 0.96-1
- Update to the latest upstream release
- Patch to wirk with ruby-1.9 (Russell Harrison, BZ #831501)

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.90-0.5.bzr27
- Remove --vendor from desktop-file-install for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-0.4.bzr27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-0.3.bzr27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-0.2.bzr27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 20 2011 Deji Akingunola <dakingun@gmail.com> - 0.90-0.1
- Update to 0.9 bzr snapshot

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.85-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 01 2008 Deji Akingunola <dakingun@gmail.com> - 0.85-2
- Spec clean-ups from package review 

* Mon Sep 22 2008 Deji Akingunola <dakingun@gmail.com> - 0.85-1
- Follow upstream renaming to Screenruler

* Mon Jan 14 2008 Deji Akingunola <dakingun@gmail.com> - 0.8-3
- Package review update (Bugzilla #430455)

* Mon Jan 14 2008 Deji Akingunola <dakingun@gmail.com> - 0.8-2
- Explicitly require ruby
- Also require versions of ruby-libglade2 which have been fixed of bug 428781

* Mon Jan 14 2008 Deji Akingunola <dakingun@gmail.com> - 0.8-1
- Initial package
