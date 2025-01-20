Name:           redeclipse
Version:        1.6.0
Release:        17%{?dist}
Summary:        A Free, Casual Arena Shooter

# Game engine is zlib
# Icon and trademark info is CC-BY-SA
# Logo and name covered by "trademark guidelines" see trademark.txt
# Automatically converted from old format: zlib and CC-BY-SA - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-CC-BY-SA
URL:            http://www.redeclipse.net/
Source0:        https://github.com/redeclipse/base/releases/download/v%{version}/redeclipse_%{version}_nix.tar.bz2

# Correctly pass cflags to embedded sqlite build
Patch0:         redeclipse-cflags.patch

# Build using external Enet library from Fedora
# Not wanted upstream
Patch1:         redeclipse-1.5.3-build-with-system-enet.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  enet-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  freetype-devel
BuildRequires:  desktop-file-utils
# This is needed by Makefile
BuildRequires:  ed

Requires:       %{name}-data = %{version}-%{release}

%description
Red Eclipse is a fun-filled new take on the casual first person arena
shooter, built as a total conversion of Cube Engine 2, which lends
itself toward a balanced gameplay, with a general theme of agility in a
variety of environments.

Features:
* Balanced gameplay, with a general theme of agility in a variety of
  environments
* Parkour, impulse boosts, dashing, sliding, and other tricks
* Favourite gamemodes with tons of mutators and variables
* Available for Windows, Linux/BSD and Mac OSX
* Builtin editor lets you create your own maps cooperatively online


%package data
Summary:        Data for the Red Eclipse FPS game
# Game scripts are zlib
# Trademark info is CC-BY-SA
# Game data is mixed (per-directory readme.txt), by default CC-BY-SA
# See the included file 'doc/all-licenses.txt' for license breakdown
# Logo and name covered by "trademark guidelines" see trademark.txt
# Automatically converted from old format: zlib and CC-BY-SA and CC-BY and Public Domain and OFL - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-OFL
BuildArch:      noarch


%description data
This package contains the data content, e.g. maps, models, textures,
sounds, etc. for the Red Eclipse FPS game.


%package server
Summary:        Server for the Red Eclipse FPS game
# Game engine is zlib
# Trademark info is CC-BY-SA
# Name covered by "trademark guidelines" see trademark.txt
# Automatically converted from old format: zlib and CC-BY-SA - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-CC-BY-SA
Requires:       %{name}-data = %{version}-%{release}

%description server
This package contains the dedicated server for the Red Eclipse FPS game,
it also includes some example scripts for configuring the server. 


%package -n cube2font
Summary:        Utility program for creating font bitmaps for Cube Engine games
# Automatically converted from old format: zlib - review is highly recommended.
License:        zlib


%description -n cube2font
cube2font is a utility program designed to create font bitmaps for Cube
Engine games, it works by taking a Truetype font and building it into a
set of coordinates in an image. cube2font is an improved version of the
previous TTF2Font, supporting a much larger range of characters.


%prep
%autosetup -p1


%build
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" -C src/ \
       client server cube2font


%install
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" -C src/ \
        DESTDIR=%{buildroot} prefix=%{_prefix}                         \
        libexecdir=%{buildroot}%{_libexecdir}                          \
        system-install system-install-cube2font


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/redeclipse.desktop


%files
%doc readme.txt doc/changelog.txt doc/trademark.txt
%license doc/license.txt
%{_bindir}/redeclipse
%{_libexecdir}/redeclipse
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_mandir}/man6/redeclipse.6*
%{_docdir}/redeclipse

%files data
%license doc/license.txt doc/all-licenses.txt 
%doc doc/trademark.txt
%{_datadir}/redeclipse

%files server
%license doc/license.txt 
%doc doc/trademark.txt doc/examples/servinit.cfg
%{_bindir}/redeclipse-server
%{_libexecdir}/redeclipse
%{_mandir}/man6/redeclipse-server.6*

%files -n cube2font
%{_bindir}/cube2font
%{_mandir}/man1/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 12 2023 Pete Walter <pwalter@fedoraproject.org> - 1.6.0-11
- ExcludeArch i686 for https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Pete Walter <pwalter@fedoraproject.org> - 1.6.0-2
- Correctly pass cflags to embedded sqlite build

* Thu Dec 05 2019 Pete Walter <pwalter@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0
- Packaging cleanup

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.6-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.5.6-2
- Removed redundant data from server subpackage

* Sun Nov 20 2016 Link Dupont <linkdupont@fedoraproject.org> - 1.5.6-1
- Update to 1.5.6 upstream release
- Update SDL build requires to SDL2
- Rebase required patches

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.5.3-1
- Update to 1.5.3 upstream release
- drop upstream patches
- rebase required patches

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-10
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.4-9
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Bruno Wolff III <bruno@wolff.to> 1.4-5
- Rebuild for enet soname change

* Sat Jun 15 2013 Bruno Wolff III <bruno@wolff.to> 1.4-4
- Rebuild for enet 1.3.8 soname bump

* Wed May 01 2013 Martin Erik Werner <martinerikwerner@gmail.com> 1.4-3
- Add patch with note that Akashi-Font is OFL-licensed
- Updated descriptions

* Sat Apr 27 2013 Bruno Wolff III <bruno@wolff.to> 1.4-2
- Rebuild for enet 1.3.7 soname bump

* Mon Mar 25 2013 Martin Erik Werner <martinerikwerner@gmail.com> 1.4-1
- New upstream release
- Remove cube2font build fix
  + Applied upstream
- Update generate-tarball script
- Add upstream desktop file fix patch
- Add upstream server install fix patch
- Add upstream patch for starting server without data

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.3.1-1
- New upstream release
- Remove security text command fix patch
  + Applied upstream
- Remove icon patch
  + Applied upstream
- Remove all-licenses
  + Installed from upstream
- Removed versioning on windowed and enet patches
- Add patch for cube2font install target


* Fri Jul 27 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.2-12
- Add security-text-command-fix.patch
  + File access security fix


* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 27 2012 martinerikwerner@gmail.com
- 1.2-10
- Fix unowned dir /usr/libexec/redeclipse/

* Wed May 02 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.2-9
- Use desktop-file-validate in %%install step
- Typo fix in cube2font %%description: utiliy -> utility
- Added versioned Requires: redeclipse-data = %%{version}-%%{release}

* Mon Mar 26 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.2-8
- Set flags for make install to avoid strip and get a useful -debuginfo

* Tue Mar 20 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.2-7
- Move removal of Enet & fonts from %%prep to generate-tarball script
- Re-add generate-tarball script as Source1

* Mon Mar 19 2012 Martin Erik Werner <martinerikwerner@gmail.com>r
- 1.2-6 
- Remove fonts in %%prep
- Corrections in all-licenses
  + Adapt comment about font generation (source URL & cube2font)
  + Remove superfluous overview "License:" field (copy of license.txt)

* Tue Mar 13 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.2-5
- Add Icon Cache scriptlet snippet
- Add BuildArch: noarch for -data subpackage
- Use %%{version} for Source0 and <version> in gen-tarball comment

* Mon Mar 12 2012 Martin Erik Werner <martinerikwerner@gmail.com> 
- 1.2-4
- Move back to repacking source rpm

* Sun Mar 11 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.2-3
- Enable building with Enet

* Fri Mar 09 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.2-2
- Start doing minor releases + changelog for review
- Wrap spec file at 72 chars
- Group %%package and %%description sections
- Drop rm -rf %%{buildroot} from %%install section
- Use wildcard to support different manpage compression
- One BuildRequires: per line
- Some indentation fixes
- Drop "in the -data package" since licesene.txt is included in -server

* Wed Feb 29 2012 Martin Erik Werner <martinerikwerner@gmail.com>
- 1.2-1
- Initial Fedora package
- Add patch from upstream SVN to fix icon sizes
- Add patch to build with Fedora's Enet
- Add patch to start in windowed mode by default
