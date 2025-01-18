Name:		gnusim8085
Version:	1.4.1
Release:	12%{?dist}
Summary:	Graphical simulator for 8085 assembly language

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://gnusim8085.srid.ca/
Source0:	https://github.com/GNUSim8085/GNUSim8085/archive/%{version}/%{name}-%{version}.tar.gz

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:	gtksourceview3-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:  libappstream-glib
BuildRequires: make

Requires:	electronics-menu

%description
GNUSim8085 is a graphical simulator for Intel 8085 microprocessor assembly
language. It has some very nice features including a keypad which can be used
to write assembly language programs with much ease. It also has stack, memory
and port viewers which can be used for debugging the programs.

%prep
%autosetup -n GNUSim8085-%{version}

%build
aclocal -I m4
autoheader
autoconf
automake -a -c
%configure --docdir %{_pkgdocdir} --disable-silent-rules
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/pixmaps/%{name}
%make_install
%find_lang %{name}

%check
desktop-file-install --vendor "" \
--add-category "Electronics" \
--delete-original \
--dir %{buildroot}%{_datadir}/applications/ \
%{buildroot}%{_datadir}/applications/GNUSim8085.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README.md TODO asm-guide.txt examples/
%license COPYING
%{_mandir}/man1/%{name}.1*
%{_bindir}/gnusim8085
%{_metainfodir}/gnusim8085.appdata.xml
%{_datadir}/applications/GNUSim8085.desktop
%{_datadir}/gnusim8085/
%{_datadir}/pixmaps/gnusim8085/
%{_datadir}/icons/hicolor/scalable/apps/gnusim8085.svg

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.1-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to latest upstream release 1.4.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.7-16
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.3.7-10
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.7-8
- Use %%{_pkgdocdir} instead of hard-coded doc path (FTBFS RHBZ #1106694).
- Append --disable-silent-rules to %%configure.
- Fix broken %%changelog entry.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.3.7-6
- Move doc to %%{_pkgdocdir} for UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.3.7-3
- Fixed comments from review

* Wed Jul 18 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.3.7-2
- Revised for the review again, taken most of the patch of Michael Schwendt

* Wed Jul 18 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.3.7-1
- Rebased to 1.3.7 upstream
- Revised for re-reviewing after deprecation from previous maintainer

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 02 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.6-1
- New upstream release

* Thu Dec 10 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.5-6
- Fixed broken package version naming
- Change docdir in configure.in fix RHBZ 542945
- Reverted sources to stable 1.3.5 : thankfully release 5 was not pushed to repos

* Thu Dec 3 2009 Rangeen Basu Roy Chowdhury <sherry151 AT fedoraproject DOT org> - svn.141-5
- Fixed Bug-542945

* Thu Dec 3 2009 Rangeen Basu Roy Chowdhury <sherry151 AT fedoraproject DOT org> - svn.141-4
- Updated to svn.141 version

* Sun Jun 7 2009 Rangeen Basu Roy Chowdhury <sherry151 AT fedoraproject DOT org> - 1.3.5-4
- Ownership of pixmap/gnusim8085 directory included and some typos fixed.

* Sun Jun 7 2009 Rangeen Basu Roy Chowdhury <sherry151 AT fedoraproject DOT org> - 1.3.5-3
- Changes made to fine tune the package- copy manual, preserve time stamp

* Tue Jun 2 2009 Rangeen Basu Roy Chowdhury <sherry151 AT fedoraproject DOT org> - 1.3.5-2
- Changes made to match Fedora Packaging Guidelines

* Tue Jun 2 2009 Rangeen Basu Roy Chowdhury <sherry151 AT fedoraproject DOT org> - 1.3.5-1
- First Fedora Package
