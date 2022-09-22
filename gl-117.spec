Name:           gl-117
Version:        1.3.2
Release:        34%{?dist}
Summary:        Action flight simulator
License:        GPLv2
URL:            http://www.heptargon.de/gl-117/gl-117.htm
Source0:        http://dl.sf.net/sourceforge/gl-117/gl-117-%{version}-src.tar.bz2
Source1:        gl-117.desktop
Source2:        gl-117.png
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL-devel, SDL_mixer-devel
BuildRequires:  freeglut-devel
BuildRequires:  desktop-file-utils
BuildRequires: make
Requires:       opengl-games-utils

%description
GL-117 is an action flight simulator. Enter the Eagle Squadron and succeed
in several challanging missions leading though different landscapes. Five
predefined levels of video quality and an amount of viewing ranges let you
perfectly adjust the game to the performance of your system. Joystick,
mouse, sound effects, music...

%prep
%setup -q -n %{name}-%{version}-src

sed -i -e 's/\r//' AUTHORS ChangeLog FAQ NEWS

sed -i -e 's/ -lSDLmain\>//' configure

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications \
         $RPM_BUILD_ROOT/%{_datadir}/pixmaps \
         $RPM_BUILD_ROOT/%{_mandir}/man6

install -m 644 doc/%{name}.6 $RPM_BUILD_ROOT/%{_mandir}/man6/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/pixmaps/

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
    %{SOURCE1}

ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

%files
%doc AUTHORS ChangeLog COPYING FAQ NEWS README doc/%{name}.pdf
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man6/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-30
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.2-18
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.2-14
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 03 2008 Steven Pritchard <steve@kspei.com> 1.3.2-7
- Fix BZ#304841.
  - Use opengl-game-wrapper.
  - Update .desktop file.
  - Drop "--add-category X-Fedora".

* Thu Jul 03 2008 Steven Pritchard <steve@kspei.com> 1.3.2-6
- Update License tag.
- Drop -lSDLmain.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.2-5
- Autorebuild for GCC 4.3

* Mon Apr 09 2007 Steven Pritchard <steve@kspei.com> 1.3.2-4
- Quiet "wrong-file-end-of-line-encoding" warnings from rpmlint.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 1.3.2-3
- Rebuild

* Sat Feb 11 2006 Steven Pritchard <steve@kspei.com> 1.3.2-2
- Drop BR: xorg-x11-devel, since it should be pulled in by SDL-devel
- Don't hard-code path to X libs
- Drop hard-coded LDFLAGS
- Drop redundant "for Linux..." from description

* Mon Sep 26 2005 Steven Pritchard <steve@kspei.com> 1.3.2-1
- Update to 1.3.2 (#169275)
- BR xorg-x11-devel instead of XFree86-devel
- Change URL to the gl-117 home page

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.3.1-2
- rebuilt

* Tue Dec 21 2004 Panu Matilainen <pmatilai@welho.com> 0:1.3.1-1
- update to 1.3.1

* Sat Jun 19 2004 Panu Matilainen <pmatilai@welho.com> 0:1.3-0.lvn.1
- update to 1.3

* Fri May 21 2004 Panu Matilainen <pmatilai@welho.com> 0:1.2-0.lvn.1
- update to 1.2
- dont include document sources
- put manpage where it belongs

* Thu Nov 27 2003 Panu Matilainen <pmatilai@welho.com> 0:1.0.1-0.lvn.2.2
- remove ldflags patch (it would've required autoconf), pass LDFLAGS on
  configure line instead

* Thu Nov 27 2003 Panu Matilainen <pmatilai@welho.com> 0:1.0.1-0.lvn.1.2
- Initial packaging.
