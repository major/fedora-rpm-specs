Name:           sopwith
Version:        2.7.0
Release:        1%{?dist}
Summary:        SDL port of the sopwith game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/fragglet/sdl-sopwith/
Source0:        https://github.com/fragglet/sdl-sopwith/archive/refs/tags/sdl-sopwith-%{version}.tar.gz
Source1:        sopwith.png

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  SDL2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  autoconf
BuildRequires:  automake

%description
This is a port of the classic computer game "Sopwith" to run on modern
computers and operating systems.


%prep
%setup -q -n sdl-sopwith-sdl-sopwith-%{version}
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_docdir}/sdl-sopwith

cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=Sopwith
Type=Application
Comment=The classic sopwith game
Exec=sopwith
Terminal=false
Icon=sopwith
EOF

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications           \
  --add-category ArcadeGame                            \
  --add-category Game                                  \
  %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%files
%doc AUTHORS COPYING.md CODE_OF_CONDUCT.md ChangeLog FAQ.md NEWS.md PHILOSOPHY.md README.md TODO doc/origdoc.txt 
%license COPYING.md
%{_bindir}/sopwith
%{_mandir}/man6/sopwith*
%{_mandir}/man5/sopwith*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/metainfo/*.xml

%changelog
* Sat Feb 08 2025 josef radinger <cheese@nosuchhost.net> - 2.7.0-1
- bump version
- source is now on github
- patches 0+1 no lomger needed
- add/remove/change several %%docs
- switch to SDL2-devel
- add manpages, icon + metainfo

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.4-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 20 2014 Adrian Reber <adrian@lisas.de> - 1.8.4-1
- updated to 1.8.4
- dropped upstreamed patches

* Mon Nov 17 2014 Adrian Reber <adrian@lisas.de> - 1.8.3-2
- updated to 1.8.3 (fixes #1102618)
- added patch for "Crash on start in single -> novice mode" (#1164516)
- cleaned up spec

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 1.7.1-15
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.7.1-12
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 21 2010 Adrian Reber <adrian@lisas.de> - 1.7.1-10
- fixed a 32/64 bit bug in the GTK version (#583417)
- added a few patches from debian
- now also using the %%{dist} tag

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Adrian Reber <adrian@lisas.de> - 1.7.1-7
- replaced %%makeinstall with make DESTDIR=... install
- removed X-Fedora category from desktop-file-install
- removed Application category from desktop-file-install (#485354)
- added ArcadeGame category from desktop-file-install (#485354)
- removed ".png" from "Icon=" in desktop file to silence a warning
- fixed "wrong-script-end-of-line-encoding" of readme.txt

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.7.1-6
- Autorebuild for GCC 4.3

* Thu Oct 11 2007 Adrian Reber <adrian@lisas.de> - 1.7.1-5
- rebuilt for BuildID
- updated license tag
- fixed sourceforge URL

* Sat Sep 16 2006 Adrian Reber <adrian@lisas.de> - 1.7.1-4
- rebuilt

* Sun Mar 12 2006 Adrian Reber <adrian@lisas.de> - 1.7.1-3
- rebuilt

* Tue Mar 29 2005 Adrian Reber <adrian@lisas.de> - 1.7.1-2
- added patch to fix gcc4 compiler error

* Wed Jun 18 2003 Adrian Reber <adrian@lisas.de> - 0:1.7.1-0.fdr.1
- updated to 1.7.1
- changed category from desktop entry from "Games" to "Game"
- changed description
- removed redundant and useless documentation

* Sun Jun 08 2003 Adrian Reber <adrian@lisas.de> - 0:1.7.0-0.fdr.1
- Initial RPM release.
