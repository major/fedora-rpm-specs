%global version_tag 13.0w
%global _lto_cflags %nil

Name:           hyperrogue
Version:        13.0
Release:        1.w%{?dist}
Summary:        An SDL roguelike in a non-euclidean world

# The game is under the GPLv2 (savepng.* is under zlib) and the music under CC-BY-SA (v3) and sounds under CC-BY-SA 4.0, CC-BY 4.0 and CC0
# Automatically converted from old format: GPLv2 and BSD and zlib - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD AND Zlib
URL:            http://www.roguetemple.com/z/hyper/
Source0:        https://github.com/zenorogue/hyperrogue/archive/v%{version_tag}/%{name}-%{version_tag}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Source3:        http://roguetemple.com/z/hyper/bigicon-osx.png
Patch0:         %{name}-gccfix.patch

BuildRequires:  gcc, gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel, SDL_ttf-devel, SDL_gfx-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  glew-devel
BuildRequires: make

Requires: dejavu-sans-fonts

Provides: bundled(mtrand)
Provides: bundled(savepng)

Requires: %{name}-data

# Hmm.. it seems that hyperrogue does not build on 32-bit arm anymore?
# "as: out of memory allocating 32 bytes after a total of 3020046336 bytes"
# https://kojipkgs.fedoraproject.org//work/tasks/8579/50098579/build.log
ExcludeArch: armv7hl

%description
You are a lone outsider in a strange, non-Euclidean world.
Fight to find treasures and get the fabulous Orbs of Yendor!

%package data
Requires: %{name}
Obsoletes:     %{name}-music < 12.0
Summary: Data for hyperrogue
BuildArch: noarch
# Automatically converted from old format: CC-BY - review is highly recommended.
License: LicenseRef-Callaway-CC-BY

%description data
Data files for hypperrogue.

%prep
%setup -q -n %{name}-%{version_tag}
%patch -P0 -p1

%build
%make_build CXXFLAGS="%{optflags} -Wno-invalid-offsetof -I%{_includedir}/SDL -DHYPERPATH=\\\"%{_datadir}/%{name}/\\\" -DHYPERFONTPATH=\\\"%{_datadir}/fonts/dejavu-sans-fonts/\\\""

%install
# Upstream not provides "install" target. I have to install files "by hands".
mkdir -p %{buildroot}%{_bindir}
install -pDm755 -p hyperrogue %{buildroot}%{_bindir}/%{name}

# Install music files.
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/music
install -pDm644 music/* %{buildroot}%{_datadir}/%{name}/music/
mkdir -p %{buildroot}%{_datadir}/%{name}/sounds
install -pDm644 sounds/* %{buildroot}%{_datadir}/%{name}/sounds/
mkdir -p %{buildroot}%{_datadir}/%{name}/rogueviz
install -pDm644 rogueviz/*.cpp rogueviz/*.h %{buildroot}%{_datadir}/%{name}/rogueviz/
install -pDdm644 rogueviz/ads rogueviz/dhrg rogueviz/models rogueviz/nilrider rogueviz/sag rogueviz/som %{buildroot}%{_datadir}/%{name}/rogueviz/
install -pDm644 hyperrogue-music.txt %{buildroot}%{_datadir}/%{name}/
chmod a+x %{buildroot}%{_datadir}/%{name}/rogueviz/
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
install -pDm644 README.md %{buildroot}%{_defaultdocdir}/%{name}/

# Install the desktop file.
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -pDm644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Install the appdata file.
mkdir %{buildroot}%{_datadir}/appdata/
install -pDm644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/

%check
#Test the appdata file.
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files
#%%license COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_defaultdocdir}/%{name}/README.md

%files data
%{_datadir}/%{name}


%changelog
* Fri Dec 27 2024 Dennis Payne <dulsi@identicalsoftware.com> - 13.0-1.w
- Latest release

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 12.0-16.m
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-15.m
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-14.m
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-13.m
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-12.m
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-11.m
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-10.m
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 09 2022 Dennis Payne <dulsi@identicalsoftware.com> - 12.0-9.m
- Fix makefile patch.

* Sat Apr 09 2022 Dennis Payne <dulsi@identicalsoftware.com> - 12.0-8.m
- Add makefile patch.

* Sat Apr 09 2022 Dennis Payne <dulsi@identicalsoftware.com> - 12.0-7.m
- Update to the latest release and remove lto because it caused compile failure.

* Tue Feb 08 2022 Dennis Payne <dulsi@identicalsoftware.com> - 12.0-6.j
- Add patch to workaround gcc bug.

* Tue Feb 08 2022 Dennis Payne <dulsi@identicalsoftware.com> - 12.0-5.j
- Update to the latest release.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-4.f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 20 2021 Dennis Payne <dulsi@identicalsoftware.com> - 12.0-3.f
- Add obsoletes to data package.

* Wed Nov 17 2021 Dennis Payne <dulsi@identicalsoftware.com> - 12.0-2.f
- Add patch to remove -march=native

* Tue Nov 16 2021 Dennis Payne <dulsi@identicalsoftware.com> - 12.0-1.f
- Updated to latest release.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-3.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-2.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Ben Rosser <rosser.bjr@gmail.com> - 11.3-1.a
- Update to newer upstream release, fix FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-11.d
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-10.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-9.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-8.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-7.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 10.0-6.d
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-5.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-4.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-3.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-2.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 <nobrakal@cthugha.org> 10.0-1.d
- Update to new upstream

* Wed Jun 21 2017 <nobrakal@cthugha.org> 9.4-1.n
- Update to new upstream on github

* Mon Feb 06 2017 <nobrakal@gmail.com> 8.3-3.j
- Update destkop file to match current icon name

* Sat Nov 19 2016 <nobrakal@gmail.com> 8.3-2.j
- Add mtrand as a bundled lib, and add BSD licence
- Add savepng as a bundled lib, and add zlib license
- Update appdata.xml file with new licence and open age rating

* Sat Mar 12 2016 Alexandre Moine <nobrakal@gmail.com> 8.3-1.j
- Update to new upstream
- Make music subpackage a noarch subpackage
- Add lipng-devel as a new BuildRequires
- Update appdata file
- Update desktop file (thanks Rémi Verschelde)

* Sat Mar 12 2016 Alexandre Moine <nobrakal@gmail.com> 7.4-1.h
- Update to new upstream
- Force code relocation with -fPIC
- Remove license: COPYING, since the file was removed by upstream (I contact them about it)

* Thu Aug 06 2015 Alexandre Moine <nobrakal@gmail.com> 6.6-1
- Update to new upstream.
- Create a subpackage for music.
- Set the correct path for the music-info file.
- Fix typo.

* Sat May 09 2015 Alexandre Moine <nobrakal@gmail.com> 5.5-0.3.a
- Use right versioning rules.

* Tue Mar 24 2015 Alexandre Moine <nobrakal@gmail.com> 5.5a-2
- Use install instead of cp.
- Add a correct test of the .appadata.xml file

* Tue Mar 17 2015 Alexandre Moine <nobrakal@gmail.com> 5.5a-1
- Update to the new 5.5a
- Remove the manual install of VeraBD.ttf, not used anymore, replaced by DejaVuSans-Bold.ttf.
- Patch the code to use the fedora DejaVuSans-Bold.ttf file.
- The problem with the executable is solved, put it back in %%{_bindir}

* Sat Nov 15 2014 Alexandre Moine <nobrakal@gmail.com> 4.4-4
- Remove the explicit Requires: SDL_mixer SDL_ttf SDL_gf

* Mon Oct 27 2014 Alexandre Moine <nobrakal@gmail.com> 4.4-3
- Chmod the executable to 755
- Change the icon for a wider
- Add an appdata file

* Sat Oct 25 2014 Alexandre Moine <nobrakal@gmail.com> 4.4-2
- Change %%{_datadir} to %%{_libdir} for the arch-dependent binairie

* Wed Oct 22 2014 Alexandre Moine <nobrakal@gmail.com> 4.4-1
- Original spec
