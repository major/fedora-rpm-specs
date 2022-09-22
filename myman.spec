Name:           myman
Version:        0.7.0
Release:        15%{?dist}
Summary:        Text-mode video-game inspired by Namco's Pac-Man

License:        MIT
URL:            https://myman.sourceforge.io
Source0:        https://sourceforge.net/projects/myman/files/myman/%{name}-%{version}/%{name}-%{version}.tar.gz

Patch0:         myman-0.7.0-makefile_clean.patch

BuildRequires: make
BuildRequires: ncurses-devel groff gcc
Requires: man-db

Provides: myman

%package data
Summary: game data files for %{name}

%description
Basic premise of the MyMan video game:

  "Those scary ghosts are back, and this time they've spotted
   you! What's worse is that they've mistaken you for their old
   rival Pac, and they're out for (yellow) blood!"

MyMan displays (A) on a text terminal or terminal emulator (using
ncurses, slang, PDCurses, SysV curses, or the raw stdio terminal
driver), (B) on an X Window System display (using PDCurses for X,
a.k.a. XCurses), (C) on any terminal or display supported by PDCurses
for SDL, libcaca, LibGGI/LibGII, Allegro, TWin, aalib, Carbon/Toolbox,
or (D) in a Win32 command prompt window (using the raw Win32 terminal
driver).  Since MyMan is fairly fast-moving, you'll need a reasonably
fast computer and display.  It once ran acceptably fast on a 486-66
under Linux, and may still.

%description data
Various data files as level mazes, characters and sprites for myman videogame

%prep
%autosetup
chmod 545 src/myman.c
chmod 545 src/myman.c

%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
#deleting superfluous files
rm $RPM_BUILD_ROOT/%{_bindir}/myman-%{version}
rm $RPM_BUILD_ROOT/%{_mandir}/man6/myman-%{version}.6
rm $RPM_BUILD_ROOT/%{_bindir}/myman.command
rm $RPM_BUILD_ROOT/%{_mandir}/man6/myman.command.6
rm $RPM_BUILD_ROOT/%{_docdir}/myman/INSTALL
rm $RPM_BUILD_ROOT/%{_docdir}/myman/VERSION

%files
%license COPYRIGHT LICENSE
%doc COPYRIGHT LICENSE ChangeLog NEWS ONEWS README TODO myman.html myman.ps

%{_bindir}/myman
%{_mandir}/man6/myman.6.gz

%files data
%{_datadir}/myman

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jiri Vymazal <jvymazal@redhat.com> - 0.7.0-6
- adding gcc to biuldrequires following f29 system-wide change

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 02 2017 jvymazal <jvymazal@redhat.com> 0.7.0-1
- initial package
