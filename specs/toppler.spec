%global commit 5e3e581bb7b58098f54df9b634c7bd4a23ba66b5

Name:           toppler
Version:        1.3
Release:        5%{?dist}
Summary:        Platform game
License:        GPL-3.0-only
URL:            https://gitlab.com/roever/toppler/
Source0:        https://gitlab.com/roever/toppler/-/archive/v%{version}/%{name}-%{version}.tar.bz2
Source1:        toppler.desktop
Patch2:         toppler-1.1.5-highscore.patch
Patch100:       toppler-1.3-fix_makefile.patch
Patch101:       toppler-1.3-format_security.patch
Patch102:       toppler-1.3-head.patch
Patch103:       toppler-1.3-missing_include.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  zlib-devel
# Needed to rebuild the graphics from source
# This is currently segfault'ing
%if 0
BuildRequires:  gimp
BuildRequires:  ImageMagick
BuildRequires:  povray
BuildRequires:  pygtk2
%endif


%description
Help a cute little green animal switch off some kind of "evil" mechanism. The
"power off switch" is hidden somewhere in high towers. On your way to the
target you need to avoid a lot of strange robots that guard the tower.


%prep
%setup -q -n %{name}-v%{version}-%{commit}
#patch -P2 -p1
%patch -P100 -p1
%patch -P101 -p1
%patch -P102 -p1
%patch -P103 -p1


%build
%set_build_flags
%make_build \
  CXXFLAGS="$CXXFLAGS" \
  LDFLAGS="$LDFLAGS" \
  STATEDIR=%{_localstatedir}/games \
  toppler translation


%install
%set_build_flags
%make_install \
  CXXFLAGS="$CXXFLAGS" \
  LDFLAGS="$LDFLAGS" \
  STATEDIR=%{_localstatedir}/games

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_localstatedir}/games/
touch %{buildroot}%{_localstatedir}/games/toppler.hsc

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -p -m 0644 dist/toppler*.xpm %{buildroot}%{_datadir}/pixmaps/

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md doc/changelog.md
%{_bindir}/toppler
%{_datadir}/toppler
%{_datadir}/applications/toppler.desktop
%{_datadir}/pixmaps/toppler*.xpm
%verify(not md5 size mtime) %config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/toppler.hsc
%{_mandir}/man6/toppler.6.*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 16 2023 Xavier Bachelot <xavier@bachelot.org> - 1.3-3
- Add patches to update to current git and fix missing includes (RHBZ#2261760)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Xavier Bachelot <xavier@bachelot.org> - 1.3-1
- Update to 1.3 (RHBZ#890426)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Xavier Bachelot <xavier@bachelot.org> - 1.1.5-16
- Add BR: gcc.
- Clean up spec.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.5-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.5-7
- Rebuilt to fix FTBFS, format-security patch, fixes rhbz #1107454, #1037362 and #926648

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 03 2011 Xavier Bachelot <xavier@bachelot.org> 1.1.5-1
- Update to 1.1.5.
- Add better highscore patch (from Hans de Goede).
- Add patch to remove strncpy (from Hans de Goede).
- Clean up spec.

* Sun Oct 11 2009 Xavier Bachelot <xavier@bachelot.org> 1.1.4-1
- Update to 1.1.4.
- Drop upstream'ed patches.

* Fri Oct 02 2009 Xavier Bachelot <xavier@bachelot.org> 1.1.3-4
- Fix highscores file lock creation patch to use a better mode.

* Fri Oct 02 2009 Xavier Bachelot <xavier@bachelot.org> 1.1.3-3
- Fix License.
- Fix buffer overflow in level editor.

* Tue Sep 22 2009 Xavier Bachelot <xavier@bachelot.org> 1.1.3-2
- Fix Source0 URL.
- Fix BuildRequires.
- Keep timestamp on files encoding conversion.
- Fix highscores directory ownership and mode.
- Add patch to create highscores file if missing.
- Ghost highscores file.

* Sat Nov 29 2008 Xavier Bachelot <xavier@bachelot.org> 1.1.3-1
- Initial build.
