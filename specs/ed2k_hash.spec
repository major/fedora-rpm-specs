%define _iconsdir %{_datadir}/icons/hicolor/24x24/apps

Summary: Edonkey 2000 file hash calculator
Name: ed2k_hash
Version: 0.4.0
URL: https://ed2k-tools.sourceforge.net/index.shtml
Release: 45%{?dist}
Source0: https://downloads.sourceforge.net/sourceforge/ed2k-tools/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
# Taken from http://dl.sourceforge.net/sourceforge/ed2k-gtk-gui/ed2k-gtk-gui-0.6.4.tar.bz2
Source2: ed2k-logo-mini.png
Patch0: %{name}-64bit.patch
Patch1: %{name}-warnings.patch
Patch2: %{name}-gcc43.patch
Patch3: %{name}-ld.patch
License: GPL-2.0-or-later
BuildRequires: desktop-file-utils
BuildRequires: fltk-devel
BuildRequires: gcc-c++
BuildRequires: make

%description
A tool that outputs ed2k-links for given files.

%package gui
Summary: Edonkey 2000 file hash calculator with FLTK GUI

%description gui
A GUI tool that outputs ed2k-links for given files.

%prep
%autosetup -p1

%build
export CFLAGS="$CXXFLAGS -DPROTOTYPES"
%configure
%make_build

%install
%make_install
rm -rv %{buildroot}%{_docdir}/%{name}

iconv -f iso8859-1 -t utf8 AUTHORS > AUTHORS.utf8 &&\
touch -r AUTHORS AUTHORS.utf8 &&\
mv AUTHORS.utf8 AUTHORS
mkdir -p %{buildroot}%{_iconsdir}
install -pm 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO ed2k_hash/docs/en/*.html
%{_bindir}/%{name}

%files gui
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO ed2k_hash/docs/en/*.html
%{_bindir}/%{name}_gui
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Dominik Mierzejewski <rpm@greysector.net> - 0.4.0-31
- Add BR: gcc-c++ for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Use HTTPS URL for Source0:
- Clean-up: use modern macros, preserve AUTHORS file timestamp

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-28
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.0-22
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-21
- rebuild(fltk)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4.0-17
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fix desktop file to follow specification

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-14
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 13 2011 Ralf Corsépius <corsepiu@fedoaproject.org> - 0.4.0-12
- Rebuild for fltk-1.3.0.
- Rebase ed2k_hash-gcc43.patch (Caused FTBS).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 15 2010 Dominik Mierzejewski <rpm@greysector.net> 0.4.0-10
- fixed FTBFS (rhbz#565191)
- fixed source URL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-7
- Autorebuild for GCC 4.3

* Sun Jan 06 2008 Dominik Mierzejewski <rpm@greysector.net> 0.4.0-6
- fix compilation with gcc-4.3

* Wed Oct 24 2007 Dominik Mierzejewski <rpm@greysector.net> 0.4.0-5
- fix hash miscalculation on 64bit (bug #255321)
- fix compilation warnings

* Wed Aug 29 2007 Dominik Mierzejewski <rpm@greysector.net> 0.4.0-4
- fix desktop file
- rebuild for BuildID
- fix license tag

* Wed Sep 27 2006 Dominik Mierzejewski <rpm@greysector.net> 0.4.0-3
- run scripts for gui, not main package

* Sun Sep 24 2006 Dominik Mierzejewski <rpm@greysector.net> 0.4.0-2
- added dist tag
- converted AUTHORS to utf8
- added an icon from ed2k-gtk-gui

* Sun Sep 10 2006 Dominik Mierzejewski <rpm@greysector.net> 0.4.0-1
- initial build
