Name:    prboom-plus
Version: 2.6.66
Release: 8%{?dist}
Summary: Free enhanced DOOM engine
URL:     https://github.com/coelckers/prboom-plus/tags
License: BSD-3-Clause AND MIT AND LGPL-2.0-or-later

Source0: https://github.com/coelckers/prboom-plus/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:  pointer-types.patch

Requires:      freedoom

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: dumb-devel pkgconfig(fluidsynth) pkgconfig(libpcre2-32) pkgconfig(libpng)
BuildRequires: pkgconfig(SDL2_image) pkgconfig(SDL2_mixer) pkgconfig(SDL2_net) pkgconfig(glu)
BuildRequires: pkgconfig(alsa) portmidi-devel pkgconfig(mad) pkgconfig(vorbis)
BuildRequires: desktop-file-utils

%description
Doom is a classic 3D shoot-em-up game.
PrBoom+ is a Doom source port developed from the original PrBoom project
by Andrey Budko.
The target of the project is to extend the original port with features
that are necessary or useful.

%package        bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %{name}.

%prep
%setup -qn %{name}-%{version}

%patch -P 0 -p0

%build
pushd prboom2
%cmake -DDOOMWADDIR=%{_datadir}/doom
%cmake_build

%install
pushd prboom2
%cmake_install

# desktop + icons
desktop-file-install --dir=%{buildroot}%{_datadir}/applications ICONS/%{name}.desktop
install -Dpm 644 ICONS/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

# Completions
install -Dpm 644 ICONS/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}.bash

%files
%license prboom2/COPYING
%{_docdir}/*
%{_bindir}/*
%{_datadir}/prboom-plus/*
%{_mandir}/man5/*
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}.bash

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.66-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.66-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.6.66-6
- Patch for stricter flags.

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.6.66-1
- 2.6.66

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.6.2-6
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.6.2-4
- Move to pcre2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 21 2022 Alastor Tenebris <livingnightmare@thelivingnightmare.xyz> - 2.6.2-2
- Fix dependencies
- Use provided icon and desktop file
- Remove uneeded patch
- Added bash-completion subpackage

* Fri Feb 11 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.6.2-1
- 2.6.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.6.1-2
- Add alsa, portmidi, libmad, vorbis support.

* Tue Aug 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.6.1-1
- 2.6.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.6-2
- Rebuild for fluidsynth.

* Mon Jun 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.6-1
- Move to new, maintained upstream.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.5.1.4-18
- Patch for CVE-2019-20797.

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.5.1.4-17
- Rebuild against fluidsynth2

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.5.1.4-16
- Fix FTBFS.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.5.1.4-1
- 2.5.1.4.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 07 2013 Jaromir Capik <jcapik@redhat.com> - 2.5.1.3-3
- Replacing mktemp with mkstemp to satisfy rpmlint

* Thu Nov 07 2013 Jaromir Capik <jcapik@redhat.com> - 2.5.1.3-2
- Fixing the license tag

* Mon Nov 04 2013 Jaromir Capik <jcapik@redhat.com> - 2.5.1.3-1
- Initial package
