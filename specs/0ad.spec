# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

# enable special maintainer debug build ?
%bcond_with	debug
%if %{with debug}
%global		config			debug
%global		dbg			_dbg
%else
%global		config			release
%global		dbg			%{nil}
%endif

# Does not build with mozjs-78
# source/scriptinterface/ScriptTypes.h:85:2: error: #error Your compiler is trying to use an untested minor version of the SpiderMonkey library. If you are a package maintainer, please make sure to check very carefully that this version does not change the behaviour of the code executed by SpiderMonkey. Different parts of the game (e.g. the multiplayer mode) rely on deterministic behaviour of the JavaScript engine. A simple way for testing this would be playing a network game with one player using the old version and one player using the new version. Another way for testing is running replays and comparing the final hash (check trac.wildfiregames.com/wiki/Debugging#Replaymode). For more information check this link: trac.wildfiregames.com/wiki/Debugging#Outofsync
%bcond_without	system_mozjs115

# Remember to rerun licensecheck after every update:
#	https://bugzilla.redhat.com/show_bug.cgi?id=818401#c46
#	http://trac.wildfiregames.com/ticket/1682

%bcond_without	system_nvtt
%bcond_without	nvtt

# Exclude private libraries from autogenerated provides and requires
%global __provides_exclude_from ^%{_libdir}/0ad/
%global __requires_exclude ^(libAtlasUI.*\.so|libCollada.*\.so|libmozjs78.*\.so)

Name:		0ad
Version:	0.27.1
Release:	2%{?dist}
# BSD License:
#	build/premake/*
#	libraries/source/miniupnpc/*		(not built/used)
#	libraries/source/valgrind/*		(not built/used)
# MIT License:
#	libraries/source/fcollada/*
#	libraries/source/nvtt/*			(not built/used)
#	source/third_party/*
# LGPLv2+
#	libraries/source/cxxtest*/*		(not built/used)
# GPLv2+
#	source/*
# IBM
#	source/tools/fontbuilder2/Packer.py
# MPL-2.0
#	libraries/source/spidermonkey/*		(not built/used)
# Automatically converted from old format: GPLv2+ and BSD and MIT and IBM and MPLv2.0 - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND IPL-1.0 AND MPL-2.0
Summary:	Cross-Platform RTS Game of Ancient Warfare
Url:		http://play0ad.com

%if ! %{with nvtt}
# wget http://releases.wildfiregames.com/%%{name}-%%{version}-alpha-unix-build.tar.xz
# tar Jxf %%{name}-%%{version}-alpha-unix-build.tar.xz
# rm -fr %%{name}-%%{version}-alpha/libraries/nvtt
# rm -f %%{name}-%%{version}-alpha-unix-build.tar.xz
# tar Jcf %%{name}-%%{version}-alpha-unix-build.tar.xz %%{name}-%%{version}-alpha
Source0:	%{name}-%{version}-alpha-unix-build.tar.xz
%else
Source0:	http://releases.wildfiregames.com/%{name}-%{version}-unix-build.tar.xz
%endif

# Simplify checking differences when updating the package
# (also to validate one did not forget to remake the tarball if
# %{without_nvtt} is enabled) Create it with:
# cd BUILD/%%{name}-%%{version}-alpha
# licensecheck -r . | sort > ../../SOURCES/%%{name}-licensecheck.txt
Source1:	%{name}-licensecheck.txt

# adapted from binaries/system/readme.txt
# It is advisable to review this file at on newer versions, to update the
# version field and check for extra options. Note that windows specific,
# and disabled options were not added to the manual page.
Source2:	%{name}.6

# Patches to bundled mozjs for Python 3.11 and setuptools 60+ compatibility
Source3:	0001-Bug-1654457-Update-virtualenv-to-20.0.31.-r-mhentges.patch
Source4:	0001-Python-Build-Use-r-instead-of-rU-file-read-modes.patch

Requires:	%{name}-data = %{version}
Requires:	hicolor-icon-theme

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:  cxxtest
BuildRequires:	desktop-file-utils
BuildRequires:	enet-devel
BuildRequires:	gcc-c++
BuildRequires:	gloox-devel
BuildRequires:	fmt-devel
BuildRequires:	libcurl-devel
BuildRequires:	libdnet-devel
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libsodium-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuilDrequires:  libuuid-devel
BuildRequires:	libzip-devel
BuildRequires:	make
BuildRequires:	miniupnpc-devel
%if %{with system_nvtt}
BuildRequires:	nvidia-texture-tools-devel
%endif
BuildRequires:	openal-soft-devel
BuildRequires:	pkgconfig
BuildRequires:	SDL2-devel
BuildRequires:	subversion
BuildRequires:	valgrind-devel
BuildRequires:	wxGTK-devel
BuildRequires:	/usr/bin/appstream-util

%if %{without system_mozjs115}
# bundled mozjs
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	readline-devel
BuildRequires:	rustc
BuildRequires:	cargo
BuildRequires:	/usr/bin/zip
# for patching bundled mozjs
BuildRequires:	git-core
%else
BuildRequires:	pkgconfig(mozjs-115)
%endif

# bundled mozjs: For build time tests only
BuildRequires:	python3.11-devel
BuildRequires:	perl-devel

ExclusiveArch:	%{ix86} x86_64 %{arm} aarch64

%if %{without system_mozjs115}
Provides: bundled(mozjs) = 115
%endif

# Only do fcollada debug build with enabling debug maintainer mode
# It also prevents assumption there that it is building in x86
Patch1:		%{name}-debug.patch
Patch2:		%{name}-check.patch
Patch3:		%{name}-python311.patch
Patch4:		0001-Fix-the-removal-of-implicit-conversions-in-libfmt-10.patch
Patch5:		0001-Fix-compilation-with-GCC-13.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2255223
Patch6:		0ad-gcc-14.patch
Patch7:		0001-Fix-build-with-libxml2-v2.12.1.patch
# https://gitea.wildfiregames.com/0ad/0ad/commit/38e3f5cec04f29f747515248ca3f002bd1cc52a8
Patch8:     %{name}-miniupnp228.patch
# https://gitea.wildfiregames.com/0ad/0ad/commit/5643e90b19ea443d69b3d83dab5b79bd2c7ca8db
Patch9:		0ad-icu76.patch
# https://gitea.wildfiregames.com/0ad/0ad/pulls/7234
# pulled from https://gitlab.archlinux.org/archlinux/packaging/packages/0ad/-/blob/a26-20/49507c04e027b0d48e050bfc38ae2b631d7403c7.patch
# due to 500 errors upstream
Patch10:        49507c04e027b0d48e050bfc38ae2b631d7403c7.patch

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

The game has been in development by Wildfire Games (WFG), a group of volunteer,
hobbyist game developers, since 2001.

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}

%if ! %{with debug}
# disable debug build, and "int 0x3" to trap to debugger (x86 only)
#%%patch -P1 -p0
%endif
#%%patch -P2 -p0

# Patch bundled mozjs for Python 3.11 and setuptools 60+ compatibility
#%%patch -P3 -p1
#sed -e 's|__SOURCE3__|%{SOURCE3}|' \
#    -e 's|__SOURCE4__|%{SOURCE4}|' \
#    -i libraries/source/spidermonkey/patch.sh

#%%patch -P4 -p1
#%%patch -P5 -p1
#%%patch -P6 -p1
#%%patch -P7 -p1
#%%patch -P8 -p1
#%%patch -P9 -p1
#%%patch -P10 -p1

%if %{with system_nvtt}
rm -fr libraries/source/nvtt
%endif

rm -fr libraries/source/valgrind

#-----------------------------------------------------------------------
%build
# LTO appears to break hotkey tests in GuiManager test suite.
# Disable LTO to fix the failing tests.
%define _lto_cflags %{nil}

%set_build_flags

# Unset RUSTFLAGS to work around mozjs not supporting taking more than one flag
# https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/243#comment-134252
unset RUSTFLAGS

./libraries/source/premake-core/build.sh
./libraries/source/cxxtest-4.4/build.sh
./libraries/source/fcollada/build.sh

build/workspaces/update-workspaces.sh	\
    --bindir=%{_bindir}			\
    --datadir=%{_datadir}/%{name}	\
    --libdir=%{_libdir}/%{name}		\
%if %{with system_mozjs115}
    --with-system-mozjs			\
%endif
%if %{with system_nvtt}
    --with-system-nvtt			\
%endif
%if ! %{with nvtt}
    --without-nvtt			\
%endif
    %{?_smp_mflags}

make %{?_smp_mflags} -C build/workspaces/gcc config=%{config} verbose=1

#-----------------------------------------------------------------------
%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 build/resources/0ad.sh %{buildroot}%{_bindir}/0ad
install -p -m 755 binaries/system/pyrogenesis%{dbg} %{buildroot}%{_bindir}/pyrogenesis%{dbg}

install -d -m 755 %{buildroot}%{_libdir}/%{name}
for name in AtlasUI%{dbg} Collada%{dbg}; do
    install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
done

%if %{with nvtt} && ! %{with system_nvtt}
for name in nvcore nvimage nvmath nvtt; do
    install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
done
%endif

%if %{without system_mozjs115}
%if %{with debug}
name=mozjs115-ps-debug
%else
name=mozjs115-ps-release
%endif
install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
%endif

install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 build/resources/0ad.appdata.xml %{buildroot}%{_datadir}/metainfo/0ad.appdata.xml

install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 build/resources/0ad.desktop %{buildroot}%{_datadir}/applications/0ad.desktop

install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 build/resources/0ad.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/0ad.png

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -a binaries/data/* %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man6/%{name}.6
ln -sf %{name}.6 %{buildroot}%{_mandir}/man6/pyrogenesis.6

%if %{with debug}
export STRIP=/bin/true
%endif

#-----------------------------------------------------------------------
%check
# Depends on availablity of nvtt
#%%if %{with nvtt}
#LD_LIBRARY_PATH=binaries/system binaries/system/test%{dbg} -libdir binaries/system
#%%endif

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/0ad.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/0ad.desktop

#-----------------------------------------------------------------------
%files
%doc README.md
%license LICENSE.md
%license license_gpl-2.0.txt license_lgpl-2.1.txt license_mit.txt
%{_bindir}/0ad
%{_bindir}/pyrogenesis%{dbg}
%{_libdir}/0ad/
%{_datadir}/0ad/
%{_datadir}/applications/0ad.desktop
%{_datadir}/icons/hicolor/128x128/apps/0ad.png
%{_datadir}/metainfo/0ad.appdata.xml
%{_mandir}/man6/*.6*

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 17 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.27.1-1
- 0.27.1

* Mon Jul 14 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.27.0-1
- 0.27.0, drop ppc64le, unsupported by premake.

* Mon Jul 14 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.0.26-31
- miniupnp rebuild.

* Thu Mar 13 2025 Dennis Gilmore <dennis@ausil.us> - 0.0.26-30
- add patch for audio device crash

* Tue Feb 18 2025 Dennis Gilmore <dennis@ausil.us> - 0.0.26-29
- Rebuild for updated dependencies.

* Tue Jan 28 2025 Simone Caronni <negativo17@gmail.com> - 0.0.26-28
- Rebuild for updated dependencies.

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 09 2024 Pete Walter <pwalter@fedoraproject.org> - 0.0.26-25
- Rebuild for ICU 76

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 0.0.26-24
- Rebuild for updated miniupnpc.

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.26-23
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 19 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.0.26-21
- Rebuild for gloox 1.0.28

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 0.0.26-20
- Rebuild for ICU 74

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.0.26-15
- Rebuilt for Boost 1.83

* Wed Oct 18 2023 Kalev Lember <klember@redhat.com> - 0.0.26-14
- Use python3.11 during build time to fix FTBFS (#2225686)

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 0.0.26-13
- rebuild for new libsodium

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 0.0.26-11
- Rebuilt for ICU 73.2

* Wed Jun 28 2023 Kalev Lember <klember@redhat.com> - 0.0.26-10
- Backport an upstream patch to fix the build with fmt 10
- Backport an upstream patch to fix atlas build with gcc 13

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.0.26-9
- Rebuilt due to fmt 10 update.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 0.0.26-7
- Rebuild for ICU 71

* Tue Dec 06 2022 Kalev Lember <klember@redhat.com> - 0.0.26-6
- Drop unused openjpeg-devel build dep

* Wed Nov 23 2022 Kalev Lember <klember@redhat.com> - 0.0.26-5
- Rebuild for wxGLCanvas ABI change

* Thu Oct 20 2022 Scott Talbert <swt@techie.net> - 0.0.26-4
- Rebuild with wxWidgets 3.2

* Sat Oct 01 2022 Kalev Lember <klember@redhat.com> - 0.0.26-3
- Fix a self test failure when building under systemd-nspawn based mock
- Re-enable self tests for all arches

* Fri Sep 30 2022 Kalev Lember <klember@redhat.com> - 0.0.26-2
- Fix FTBFS with Python 3.11 and setuptools 60+ in F37 (#2045149)

* Mon Sep 26 2022 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.26-1
- Update to 0.0.26

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.0.25b-6
- Rebuilt for ICU 71.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.25b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.0.25b-4
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.25b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Bruno Wolff III <bruno@wolff.to> - 0.0.25b-2
- Fix for building bundled spidermonkey with python3.10

* Mon Sep 06 2021 Kalev Lember <klember@redhat.com> - 0.0.25b-1
- Update to 0.0.25b

* Sun Aug 08 2021 Kalev Lember <klember@redhat.com> - 0.0.25-1
- Update to 0.0.25

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.0.24b-6
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Richard Shaw <hobbes1069@gmail.com> - 0.0.24b-4
- Rebuild for new fmt version.

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 0.0.24b-3
- Rebuild for ICU 69

* Sat Feb 27 2021 Kalev Lember <klember@redhat.com> - 0.0.24b-2
- Use set_build_flags macro to set CFLAGS/CXXFLAGS/LDFLAGS
- Disable LTO to fix self test failures

* Mon Feb 22 2021 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.24b-1
- Update to 0.0.24b

* Wed Feb 03 2021 Kalev Lember <klember@redhat.com> - 0.0.23b-24
- Drop unused gamin-devel build dep

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 14:23:02 GMT 2021 Jonathan Wakely <jwakely@redhat.com> - 0.0.23b-22
- Rebuilt for Boost 1.75

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 0.0.23b-20
- Disable LTO on i686 for now

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Björn Esser <besser82@fedoraproject.org> - 0.0.23b-18
- Rebuilt for Boost 1.73 again

* Sun May 31 2020 Björn Esser <besser82@fedoraproject.org> - 0.0.23b-17
- Rebuild (gloox)

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.0.23b-16
- Rebuilt for Boost 1.73

* Sat May 23 2020 Kalev Lember <klember@redhat.com> - 0.0.23b-15
- Backport workaround for Ryzen 3000 CPU support (#1822835)

* Sun May 17 2020 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-14
- Rebuild for ICU 67

* Tue Mar 31 2020 <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.23b-13
- Fix Fedora 32 FTBFS (#1799112)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-11
- Rebuild for ICU 65

* Mon Sep 30 2019 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.23b-10
- Add build conditional for system mozjs38

* Wed Sep 11 2019 Kalev Lember <klember@redhat.com> - 0.0.23b-9
- Correctly install bundled mozjs38 (#1751250)
- Exclude private libraries from autogenerated provides and requires

* Tue Aug 13 2019 dftxbs3e <dftxbs3e@free.fr> - 0.0.23b-8
- Fix build on ppc64le

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 0.0.23b-6
- Rebuilt for miniupnpc soname bump

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 0.0.23b-5
- Correctly set RPATH for private libraries
- Install the icon to the hicolor icon theme
- Move the appdata file to metainfo directory
- Validate the appdata file

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 0.0.23b-3
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-2
- Rebuild for ICU 63

* Thu Dec 27 2018 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-1
- Update to 0.0.23b

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.0.23-2
- Rebuild for ICU 62

* Thu May 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.23-1
- Update to 0.0.23

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0.0.22-8
- Rebuild for ICU 61.1

* Wed Mar 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.22-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.0.22-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 0.0.22-4
- Rebuilt for Boost 1.66

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 0.0.22-3
- Rebuild for ICU 60.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.22-1
- Update to 0.0.22

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Jonathan Wakely <jwakely@redhat.com> - 0.0.21-5
- Patched for new GCC and rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.0.21-3
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.0.21-2
- Rebuilt for Boost 1.63

* Wed Nov 09 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.21-1
- Update to 0.0.21

* Fri Jun 24 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.20-4
- Rebuild for miniupnpc 2.0

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 0.0.20-3
- rebuild for ICU 57.1

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.20-2
- Upstream now supports aarch64 (tests currently fail)

* Sat Apr 02 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.0.20-1
- Update to 0.0.20

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 0.0.19-2
- Rebuilt for Boost 1.60

* Sat Nov 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.19
- 0.0.19

* Sun Nov 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.19-0.1.rc2
- 0.0.19-rc2

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 0.0.18-8
- rebuild for ICU 56.1

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.0.18-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.0.18-5
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.18-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 17 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.18-2
- Use bcond for rpm conditional macros
- Add rpm conditional to build with sdl2

* Sat Mar 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.18-1
- Update to latest upstream release
- Change to -p0 patches

* Thu Feb 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.17-3
- Rebuild for gloox 1.0.13

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.0.17-2
- Rebuild for boost 1.57.0

* Sun Oct 12 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.17-1
- Update to latest upstream release
- Remove no longer needed miniupnpc patch
- Remove backport changeset_15334 patch

* Sun Sep 14 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.16-11
- Remove unused valgrind sources and use system valgrind.h (#1141464)

* Thu Aug 28 2014 David Tardon <dtardon@redhat.com> - 0.0.16-10
- rebuild for ICU 53.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.16-7
- Rebuild for latest gloox

* Wed Jun 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.16-6
- Add proper patch for gcc 4.9 build

* Fri Jun  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.16-5
- Remove old Fedora release conditionals

* Fri Jun 06 2014 Dennis Gilmore <dennis@ausil.us> - 0.0.16-4
- add %%{arm} tp the ExclusiveArch list

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.0.16-2
- Rebuild for boost 1.55.0

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.16-1
- Update to latest upstream release

* Mon May  5 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-5
- Rebuild for newer enet

* Fri Apr 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-4
- Add workaround for %%check failure with gcc 4.9 on i686

* Fri Apr 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-3
- Rebuild with minupnpc 1.9

* Tue Jan 21 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-2
- Rebuild for latest gloox

* Fri Dec 27 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-1
- Update to latest upstream release
- Add new gloox and minupnpc build requires
- Use 0ad.appdata.xml from upstream tarball

* Sat Oct 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.14-2
- Install appdata file (#1018385)

* Thu Sep  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.14-1
- Update to latest upstream release

* Wed Aug  7 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.13-8
- Make package x86_64 and ix86 only as arm support is not finished.

* Wed Aug  7 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.13-7
- Correct build with boost 1.54.0 (#991906).

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.0.13-5
- Rebuild for boost 1.54.0

* Thu Jun 27 2013 Bruno Wolff III <bruno@wolff.to> - 0.0.13-4
- Rebuild for enet soname change

* Sat Jun 15 2013 Bruno Wolff III <bruno@wolff.to> - 0.0.13-3
- Rebuild for enet 1.3.8 soname bump

* Sat Apr 27 2013 Bruno Wolff III <bruno@wolff.to> - 0.0.13-2
- Rebuild for enet 1.3.7 soname bump

* Wed Apr 3 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.13-1
- Update to latest upstream release
- Update the manual page for new and renamed options
- Regenerate the licensecheck text file and patches

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.0.12-5
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.0.12-4
- Rebuild for Boost-1.53.0

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.0.12-3
- rebuild due to "jpeg8-ABI" feature drop

* Wed Dec 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.12-2
- Enable build with system nvtt as it is now approved in Fedora (#823096)
- Correct release date in manual page
- Minor consistency correction in manual page formatting
- Regenerate the licensecheck text file to match pristine tarball

* Tue Dec 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.12-1
- Update to latest upstream release
- Remove no longer required gamin patch
- Rediff rpath patch
- Remove libxml2 patch already applied upstream
- Update 0ad manpage for newer options and release information
- Add versioned requires to data files
- Add 0ad licensecheck text file to simplify checking changes

* Sat Nov 3 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-4
- Add %%with_debug maintainer mode build
- Disable fcollada debug build if %%with_debug is false
- Add patch to not crash and display helful messages in editor (#872801)

* Tue Sep 11 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-3
- Clarify source tree licenses information in spec (#818401)
- Preserve time stamp of installed files (#818401)

* Sat Sep 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-2
- Correct manpage group and symlink 0ad manual to pyrogenesis manual (#818401)
- Correct some typos and wrong information in 0ad.6

* Sat Sep 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-1
- Update to latest upstream release
- Switch to new versioning pattern
- Remove rpath patch already applied upstream
- Remove without-nvtt patch already applied upstream
- Remove boost patch already applied upstream
- Remake rpath patch to avoid package build special conditions

* Thu Sep 6 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-6
- Repackage tarball to not redistribute patented s3tc implementation (#818401)
- Add patch to rebuild with newer libxml2.
- Add upstream trac patch for build with newer boost.
- Rename patches to remove %%version and use %%name in source files.

* Fri Jul 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-5
- Clearly state nvtt is not mean't to be used (unless user build from sources).
- Update to use patch in wildfire trac instead of my patch to remove rpath.

* Fri Jun  1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-4
- Actually remove %%defattr.
- Correct wrong fedora release check for enet-devel build requires.

* Sat May 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-4
- Make package build in Fedora 16 (rpmfusion #2342).
- Add conditionals to build with or without system nvtt or disable nvtt.

* Tue May 22 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-3
- Remove %%defattr from spec (#823096).
- Run desktop-file-validate (#823096).

* Mon May 21 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-2
- Disable dependency on nvidia-texture-tools (#823096).
- Disable %%check as it requires nvtt.
- Add manual page.

* Sat May 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-1
- Correct package license.
- Update to latest upstream release.
- Remove license_dbghelp.txt as dbghelp.dll is not in sources neither installed.

* Tue May 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11339-1
- Initial 0ad spec.
