%define ver 8_41

Name:           quake2
Version:        8.41
Release:        2%{?dist}
Summary:        Quake II (Yamagi version)

License:        GPL-2.0-or-later
URL:            http://www.yamagi.org/quake2 
Source0:        https://github.com/yquake2/yquake2/archive/QUAKE2_%{ver}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires:  zlib-devel

%description
This package contains the enhanced GPL YamagiQuake2 version of the Quake 2 
engine.
To run the game you will need the original data files from demo or 
full versions.

Full version setup:
Copy the baseq2 folder contents from the CD-ROM/Steam to ~/.yq2/baseq2/ 
(or to use the data files system-wide copy the data files to 
%{_libdir}/games/%{name}/baseq2/)
Enjoy the full version.

Demo version setup:
Get the demo from http://deponie.yamagi.org/quake2/idstuff/q2-314-demo-x86.exe 
and extract it. 
It's just an ordinary, self-extract ZIP file. 
An archiver or even the unzip command can be used. 
copy the extracted folder contents /Install/Data/baseq2/* to ~/.yq2/baseq2/ 
(or to use the data files system-wide copy the data files to 
%{_libdir}/games/%{name}/baseq2/)
Enjoy the demo version.

Not patched full version setup:
If your full version of quake 2 isn't patched you need to do some more steps
Please note that the patch is required for all full versions of the game, 
even the newer ones like Steam. Without it Yamagi Quake II will not work!

Download the patch: 
http://deponie.yamagi.org/quake2/idstuff/q2-3.20-x86-full-ctf.exe
Extract the patch into an empty directory. The patch is just an ordinary 
self-extracting ZIP file. On Windows it can be extracted by double clicking 
on it, on other systems an archiver or even the unzip command can be used.

Now it's time to remove the following files from the extracted patch. 
They're the original executables, documentation and so on. 
They aren't needed anymore:

3.20_Changes.txt
quake2.exe
ref_gl.dll
ref_soft.dll
baseq2/gamex86.dll
baseq2/maps.lst
ctf/ctf2.ico
ctf/gamex86.dll
ctf/readme.txt
ctf/server.cfg
xatrix/gamex86.dll
rogue/gamex86.dll

Copy the pak0.pak file and the video/ sub-directory from your Quake II 
distribution (CD, Steam download, etc) into the baseq2/ sub-directory 
of the extracted patch.


%prep
%autosetup -n yquake2-QUAKE2_%{ver}


%build
# Use -std=gnu17 to work around build issues with C23 that gcc 15 defaults to
%global optflags %optflags -std=gnu17

%make_build \
    WITH_RPATH=no \
    WITH_SYSTEMWIDE=yes \
    WITH_SYSTEMDIR='%{_libdir}/games/%{name}'


%install
mkdir -p %{buildroot}%{_bindir}
ln -rs %{_libdir}/games/%{name}/quake2 %{buildroot}%{_bindir}/quake2
ln -rs %{_libdir}/games/%{name}/q2ded %{buildroot}%{_bindir}/q2ded

install -D -p -m 755 release/quake2 \
    %{buildroot}%{_libdir}/games/%{name}/quake2
install -D -p -m 755 release/q2ded \
    %{buildroot}%{_libdir}/games/%{name}/q2ded
install -D -p -m 755 release/ref_gl1.so \
    %{buildroot}%{_libdir}/games/%{name}/ref_gl1.so
install -D -p -m 755 release/ref_gl3.so \
    %{buildroot}%{_libdir}/games/%{name}/ref_gl3.so
install -D -p -m 755 release/ref_gles3.so \
    %{buildroot}%{_libdir}/games/%{name}/ref_gles3.so
install -D -p -m 755 release/ref_soft.so \
    %{buildroot}%{_libdir}/games/%{name}/ref_soft.so
install -D -p -m 755 release/baseq2/game.so \
    %{buildroot}%{_libdir}/games/%{name}/baseq2/game.so
install -D -p -m 644 stuff/yq2.cfg \
    %{buildroot}%{_libdir}/games/%{name}/baseq2/yq2.cfg
install -D -p -m 644 stuff/icon/Quake2.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/quake2.png
install -D -p -m 644 stuff/icon/Quake2.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/quake2.svg
install -D -p -m 755 stuff/cdripper.sh \
    %{buildroot}%{_defaultdocdir}/%{name}/examples/cdripper.sh
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%files
%license LICENSE
%doc CHANGELOG README.md
%doc doc/*
%{_bindir}/*
%{_libdir}/games/*
%{_datadir}/icons/hicolor/512x512/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/* 
%{_defaultdocdir}/%{name}/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 12 2024 Kalev Lember <klember@redhat.com> - 8.41-1
- Update to 8.41

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 08 2023 Kalev Lember <klember@redhat.com> - 8.30-1
- Update to 8.30
- Migrate to SPDX license identifiers
- Ship documentation
- Ship svg icon

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 09 2022 Kalev Lember <klember@redhat.com> - 8.20-1
- Update to 8.20

* Sun Aug 28 2022 Kalev Lember <klember@redhat.com> - 8.10-1
- Update to 8.10
- Drop armv7hl excludearch

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 6.00-14
- fix FTBS rhbz#1799959

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.00-10
- Remove obsolete scriptlets

* Sun Feb 05 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-9
- excluded arch armv7hl

* Sun Feb 05 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-8
- added full relro flags

* Sun Feb 05 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-7
- removed PIE cflag and added relro cflag

* Sun Feb 05 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-6
- added PIE custom flag

* Sun Feb 05 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-5
- altered icon and icon folder folder

* Sun Feb 05 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-4
- added update icon cache scriptlet

* Sat Feb 04 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-3
- fixed missing Icon

* Sat Feb 04 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-2
- Added an patch to remove the rpaths from the makefile

* Fri Feb 03 2017 Frederico Lima <fredlima@fedoraproject.org> - 6.00-1
- Changed the package version from 5.34 to 6.00

* Fri Jul 29 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-5
- Updated file section to remove a few files left behing

* Thu Jul 28 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-4
- Removed unnecessary sections
- Use of install macro instead of mkdir and cp

* Thu Jul 28 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-3
- Fixed issues taken from rpmlint

* Thu Jul 28 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-2
- Changed the package version from 2.5.34 to 5.34

* Sun Jul 24 2016 Frederico Lima <fredlima@fedoraproject.org> - 5.34-1
- Initial Fedora RPM release
- Added allow-custom-cflags.patch from rpm@fthiessen.de to allow custom cflags
- Compile with optflags
