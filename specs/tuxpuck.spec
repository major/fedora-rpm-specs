Name:           tuxpuck
Version:        0.8.2
Release:        42%{?dist}
Summary:        3D Shufflepuck Pong Game

License:        GPL-2.0-only
URL:            http://www.efd.lth.se/~d00jkr/tuxpuck/
Source0:        http://www.efd.lth.se/~d00jkr/tuxpuck/%{name}-%{version}.tar.gz
Source1:        tuxpuck.desktop
Patch0:         tuxpuck-0.8.2-mandest.patch
Patch1:         tuxpuck-0.8.2-utils-werror.patch
Patch2:		tuxpuck-0.8.2-libpng15.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel, freetype-devel, libvorbis-devel
BuildRequires:  libpng-devel, libjpeg-devel, desktop-file-utils
BuildRequires:	ImageMagick

Requires: hicolor-icon-theme

%description
TuxPuck is a shufflepuck game written in C using SDL. The player moves a pad
around a board and tries to shoot down the puck through the opponents defense.
Easy to play, difficult to win.

%prep
%setup -q
%patch -P0 -p0 -z .mandest
%patch -P1 -p0 -z .utils-werror
%patch -P2 -p0 -z .libpng15

%build
export CFLAGS="%{optflags}"
make
convert -transparent white data/icons/%{name}.ico %{name}.png

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install %{name}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
        %{SOURCE1}

%files
%doc COPYING readme.txt bugs.txt thanks.txt todo.txt
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/applications/tuxpuck.desktop
%{_datadir}/icons/hicolor/32x32/apps/tuxpuck.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.2-38
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.2-26
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 1 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.2-17
- Drop desktop vendor tag.

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.8.2-16
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.8.2-15
- rebuild against new libjpeg

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Jon Ciesla <limburgher@gmail.com> - 0.8.2-13
- Patch for libpng 1.5.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.8.2-11
- Rebuild for new libpng

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> 0.8.2-10
- Rebuild for libpng 1.5.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 16 2008 Jon Ciesla <limb@jcomserv.net> 0.8.2-6
- FTBFS rebuild, BZ440791.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> 0.8.2-5
- GCC 4.3 rebuild.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> 0.8.2-4
- License tag correction.

* Fri Mar 30 2007 Jon Ciesla <limb@jcomserv.net> 0.8.2-3
- Applied cleanup fixes from Hans de Goede's BZ 234566/234307

* Wed Sep 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8.2-2
- Rebuilt for FC6

* Thu Aug  3 2006 Hugo Cisneiros <hugo@devin.com.br> 0.8.2-1
- Initial RPM provided by Che
- Extras Release
