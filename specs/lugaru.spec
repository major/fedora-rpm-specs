# Force out of source build
%undefine __cmake_in_source_build

Name:		lugaru
Version:	1.2
Release:	24%{?dist}
Summary:	Ninja rabbit fighting game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://osslugaru.gitlab.io
Source0:	https://bitbucket.org/osslugaru/lugaru/downloads/%{name}-%{version}.tar.xz

# Patches backported from upstream
Patch0001:	0001-CMake-Define-build-type-before-configuring-version-h.patch
Patch0002:	0002-ImageIO-fix-invalid-conversion.patch
Patch0003:	0003-Dist-Linux-Add-content-ratings-to-AppStream-appdata-.patch

# Fedora-specific patch, do not have CMake install docs,
# we'll grab them ourselves.
Patch1000:	lugaru-1.1-CMake-Do-not-install-documentation.patch

# For autosetup
BuildRequires:	git-core

%if 0%{?rhel}
BuildRequires:	cmake3 >= 3.0
%else
BuildRequires:	cmake >= 3.0
%endif

BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(zlib)

# pkgconfig(libjpeg) doesn't work on EL7
BuildRequires:	libjpeg-turbo-devel

# For deduplicating data files
BuildRequires:	fdupes

# For desktop file validation
BuildRequires:	desktop-file-utils
# For AppStream metainfo validation
BuildRequires:	libappstream-glib

# Ensure the hicolor icon theme dirs exist
Requires:	hicolor-icon-theme

# Ensure matching game data is pulled in
Requires:	lugaru-data = %{version}-%{release}

%description
Lugaru (pronounced Loo-GAH-roo) is a cross-platform third-person action game.
The main character, Turner, is an anthropomorphic rebel bunny rabbit with
impressive combat skills. In his quest to find those responsible for
slaughtering his village, he uncovers a far-reaching conspiracy involving the
corrupt leaders of the rabbit republic and the starving wolves from a nearby
den. Turner takes it upon himself to fight against their plot and save his
fellow rabbits from slavery.


%package data
Summary:	Architecture-independent game data files for Lugaru
License:	CC-BY-SA-3.0 AND (CC-BY-SA-3.0 OR CC-BY-3.0) AND CC-BY-SA-4.0
BuildArch:	noarch

%description data
This package contains the game data files that make up the Lugaru game.

%prep
%autosetup -S git


%build
%{?cmake3:%cmake3}%{!?cmake3:%cmake} -DCMAKE_BUILD_TYPE=RelWithDebInfo \
				     -DSYSTEM_INSTALL=ON \
				     -DLUGARU_VERSION_RELEASE="Fedora %{?epel:EPEL }%{version}-%{release}"
%cmake_build


%install
%cmake_install

%fdupes %{buildroot}%{_datadir}/%{name}

%check
# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Validate AppStream metainfo data
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license COPYING.txt
%doc Docs/* AUTHORS README.md RELEASE-NOTES.md
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

%files data
%license CONTENT-LICENSE.txt
%{_datadir}/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Neal Gompa <ngompa13@gmail.com> - 1.2-13
- Update to new out-of-source build mechanism

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1.2-7
- Append curdir to CMake invokation. (#1668512)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Neal Gompa <ngompa13@gmail.com> - 1.2-2
- Backport AppStream appdata/metainfo file improvements
- Fix package version build flag

* Mon Feb 20 2017 Neal Gompa <ngompa13@gmail.com> - 1.2-1
- Upgrade to v1.2 (#1421396)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Neal Gompa <ngompa13@gmail.com> - 1.1-1
- Initial packaging for Fedora (#1405708)
- Backport patch from upstream to fix builds on ppc64/ppc64le
