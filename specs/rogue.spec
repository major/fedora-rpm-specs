Name:             rogue
Version:          5.4.5
Release:          42%{?dist}
Summary:          The original graphical adventure game
License:          BSD-3-Clause
# TODO: Fix the source url
Source0:          https://github.com/phs/rogue/archive/v5.4.4/%{name}-5.4.4.tar.gz
URL:              https://github.com/phs/rogue
Patch0:           rogue-5.4.4-to-5.4.5.patch
Patch1:           rogue-5.4.5-writesave.patch
Patch2:           rogue-5.4.5-backspace.patch
Patch3:           rogue-5.4.5-ncurses.patch
Patch4:           rogue-5.4.5-setgroups.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:      %{ix86}

BuildRequires:    binutils
BuildRequires:    coreutils
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    hostname
BuildRequires:    make
BuildRequires:    ncurses-devel
BuildRequires:    sed

%description
The one, the only, the original graphical adventure game that spawned
an entire genre.

%prep
%setup -q -n %{name}-5.4.4
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
CFLAGS='%{build_cflags} -std=gnu17'
%configure \
    --enable-setgid=games \
    --enable-scorefile=%{_localstatedir}/games/roguelike/rogue54.scr \
    --enable-lockfile=%{_localstatedir}/games/roguelike/rogue54.lck \
    --docdir=%{_docdir}/%{name}
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/rogue
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/games/roguelike
%make_install
install -D -p -m644 \
    %{name}.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications %{name}.desktop

%files
%license LICENSE.TXT
%exclude %{_docdir}/%{name}/LICENSE.TXT
%doc %{_docdir}/%{name}
%attr(2755,games,games) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%dir %attr(0775,games,games) %{_localstatedir}/games/roguelike
%config(noreplace) %attr(0664,games,games) %{_localstatedir}/games/roguelike/%{name}54.scr

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Jerry James <loganjerry@gmail.com> - 5.4.5-41
- Fix FTBFS due to ncurses change
- Update license to BSD-3-Clause
- Stop building for 32-bit x86
- Build in C17 mode to avoid FTBFS with GCC 15

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 5.4.5-40
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Wart <wart@kobold.org> - 5.4.5-27
- Remove unnecessary pre/post Requires
- Update build scripts to match latest Fedora guidelines

* Tue Feb 12 2019 Wart <wart@kobold.org> - 5.4.5-26
- Add ncurses patch to fix build
- Add setgroups patch to drop supplementary groups
- New upstream URL, but for an older version
- Added patch to migrate from upstream version to previous upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.4.5-23
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 09 2015 Petr Šabata <contyk@redhat.com> - 5.4.5-18
- Fix the dep list, hopefully
- Update the icons snippets
- Handle the desktop file correctly
- Install the license text with the %%license macro

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 Petr Šabata <contyk@redhat.com> - 5.4.5-14
- Switch to unversioned docdir (#993933)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 5.4.5-12
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Petr Šabata <contyk@redhat.com> - 5.4.5-10
- Recognize the backspace key as the erase character
- Thanks to John Haxby <jch@thehaxbys.co.uk> (#847852)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Apr 24 2010 Wart <wart at kobold.org> 5.4.5-6
- Add patch for fixing corrupt writing of savefiles (BZ #560790)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Wart <wart at kobold.org> 5.4.5-3
- Add coreutils requirement for rpm post scripts (BZ #475924)

* Fri Feb 8 2008 Wart <wart at kobold.org> 5.4.5-2
- Rebuild for gcc 4.3

* Tue Jan 1 2008 Wart <wart at kobold.org> 5.4.5-1
- Update to 5.4.5
- Drop two files that are now included in the upstream tarball

* Sun Sep 2 2007 Wart <wart at kobold.org> 5.4.4-1
- Update to 5.4.4

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 5.4.2-10
- Rebuild for selinux ppc32 issue.

* Sun Jul 15 2007 Wart <wart at kobold.org> 5.4.2-9
- New upstream home page and download URL
- Add patch when reading long values from the save file on 64-bit arch
  (BZ #248283)
- Add patch removing many compiler warnings
- Use proper version in the .desktop file

* Sat Mar 3 2007 Wart <wart at kobold.org> 5.4.2-8
- Use better sourceforge download url
- Use more precise desktop file categories

* Mon Aug 28 2006 Wart <wart at kobold.org> 5.4.2-7
- Rebuild for Fedora Extras

* Tue May 16 2006 Wart <wart at kobold.org> 5.4.2-6
- Added empty initial scoreboard file.

* Mon May 15 2006 Wart <wart at kobold.org> 5.4.2-5
- Better setuid/setgid handling (again) (BZ #187392)

* Thu Mar 30 2006 Wart <wart at kobold.org> 5.4.2-4
- Better setuid/setgid handling (BZ #187392)
- Resize desktop icon to match directory name

* Mon Mar 13 2006 Wart <wart at kobold.org> 5.4.2-3
- Added icon for .desktop file.

* Sun Mar 12 2006 Wart <wart at kobold.org> 5.4.2-2
- Added missing BR: ncurses-devel, desktop-file-utils

* Sat Feb 25 2006 Wart <wart at kobold.org> 5.4.2-1
- Initial spec file.
