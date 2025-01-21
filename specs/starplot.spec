Summary:	3-dimensional perspective star map viewer
Name:		starplot
Version:	0.95.5
Release:	41%{?dist}

# See README
# SPDX confirmed
License:	GPL-2.0-or-later
URL:		http://starplot.org/
Source0:	http://starplot.org/downloads/%{name}-%{version}.tar.gz

Patch0:		%{name}-%{version}-desktop.patch
# Fix build with -Werror=format-security"
Patch1:         %{name}-%{version}-rhbz1037339.patch
# C++11 build fix
Patch2:         %{name}-%{version}-rhbz1308152.patch
# Fix segv on startup (bug 1322030)
Patch3:		starplot-0.95.5-qsort_vs_new-bz1322030.patch
# SpecClass::initialize: Fix invalid access when luminosity class ends at
# the end of the line (bug 2029228)
Patch4:		starplot-0.95.5-specclass-init-at-operator.patch

Requires:	xdg-utils

BuildRequires:  make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gtk2-devel
BuildRequires:	xdg-utils

%description
StarPlot is a GTK+ based program, written in C++, which can be used
interactively to view three-dimensional perspective charts of stars.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .format
%patch -P2 -p1 -b .c++11
%patch -P3 -p1 -b .new_qsort
%patch -P4 -p1 -b .specclass_init

# Suppress rpmlint error.
iconv --from-code ISO8859-1 --to-code UTF-8 ./doc/examples/example.spec \
  --output example.utf-8 && mv example.utf-8 ./doc/examples/example.spec

# Fix "_STRING_H" name conflict
sed -i src/classes/strings.h \
	-e '\@def.*_STRINGS_H@s@_STRINGS_H@STARPLOT_STRINGS_H@'

%build
%configure \
  --docdir=%{_pkgdocdir} \
  --disable-rpath \
  --with-webbrowser=xdg-open
%make_build

%install
%make_install

# Remove *.stars files from documentation.
rm -f ./doc/examples/*.stars

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS
%doc ChangeLog
%license COPYING
%doc NEWS
%doc NLS-TEAM
%doc README
%doc TODO
%doc doc/examples
%doc doc/html

%{_bindir}/%{name}
%{_bindir}/starconvert
%{_bindir}/starpkg
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}32x32.xpm
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/starconvert.1*
%{_mandir}/man1/starpkg.1*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sample.stars
%{_datadir}/%{name}/test.stars

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 10 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.95.5-38
- SPDX migration

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec  6 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.95.5-33
- SpecClass::initialize: Fix invalid access when luminosity class ends at
  the end of the line (bug 2029228)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.95.5-24
- Fix FTBFS on F-27: aviod _STRING_H inclusion guard name confusion

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May  8 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.95.5-20
- Don't do sort new'ed class array with qsort, instead use vector and
  std::sort (bug 1322030)

* Wed Mar 09 2016 Debarshi Ray <rishi@fedoraproject.org> - 0.95.5-19
- Bump to fix FTBFS. (Red Hat Bugzilla #1308152)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.95.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.95.5-17
- Add starplot-0.95.5-rhbz1037339.patch (Fix FTBFSs
  RHBZ#1037339, RHBZ#1107375).
- Modernize spec.
- Add %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.95.5-13
- Reflect docdir changes (FTBFS RHBH#993380).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.95.5-11
- Remove --vendor from desktop-file-isntall on f19+ https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-8
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.95.5-6
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 22 2010 Debarshi Ray <rishi@fedoraproject.org> - 0.95.5-4
- Bump to fix FTBFS. (Red Hat Bugzilla #555518)

* Sun Jul 26 2009 Release Engineering <rel-eng@fedoraproject.org> - 0.95.5-3
- Autorebuild for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Release Engineering <rel-eng@fedoraproject.org> - 0.95.5-2
- Autorebuild for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 28 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.95.5-1
- Version bump to 0.95.5. Closes Red Hat Bugzilla bug #446948.
- .desktop file, and docdir and gcc-4.3 patches included by upstream.

* Mon Feb 11 2008 Debarshi Ray <rishi@fedoraproject.org> - 0.95.4-6
- Rebuilding with gcc-4.3 in Rawhide.

* Fri Jan 04 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.95.4-5
- Added one missing hunk to the gcc-4.3 patch.

* Thu Jan 03 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.95.4-4
- Added missing includes to fix build with gcc-4.3.

* Sat Nov 24 2007 Debarshi Ray <rishi@fedoraproject.org> - 0.95.4-3
- Added 'BuildRequires: gettext'.
- Removed Encoding from Desktop Entry for all distributions, except Fedora 7.

* Sat Nov 17 2007 Debarshi Ray <rishi@fedoraproject.org> - 0.95.4-2
- Added 'BuildRequires: desktop-file-utils' and a .desktop file.
- Added 'BuildRequires: xdg-utils'.
- Fixed faulty documentation directory path.
- Fixed build stanza to correctly detect xdg-open.

* Mon Nov 12 2007 Debarshi Ray <rishi@fedoraproject.org> - 0.95.4-1
- Initial build.
