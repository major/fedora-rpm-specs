%bcond_with copr
%bcond_with snapshot

%undefine __cmake_in_source_build

%global archive_suffix tar.gz
%global commit 623777f
%global date 20191012
%global extra rc1
%global github_owner raceintospace

%if %{without snapshot} && %{without copr}
%global gittag v%{version}%{?extra}
%global pkgversion %(echo %{gittag} | sed -e 's/^v//' -e 's/-/./g')
%else
# Use direct commits
%if %{with copr}
# Use fixed archive name, make srpm from current repository
%global pkgversion git
%else
%global pkgversion git%{commit}
%endif
%endif

# Since gcc build is broken, use clang by default
%bcond_with clang

Name:		raceintospace
Version:	2.0.0
Release:	14%{?extra:.%extra}%{?dist}
Summary:	Race into Space game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
#URL:		https://github.com/raceintospace/raceintospace
URL:		http://www.raceintospace.org/

Source0:	https://github.com/%{github_owner}/%{name}/archive/%{gittag}/%{name}-%{pkgversion}.%{archive_suffix}
#Patch1:	# No patches

BuildRequires:	cmake
BuildRequires:	SDL-devel protobuf-devel boost-devel
BuildRequires:	libogg-devel libvorbis-devel libtheora-devel jsoncpp-devel
BuildRequires:	physfs-devel libpng-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	pandoc
%if %{with clang}
BuildRequires:	clang
%else
BuildRequires:	gcc-c++
%endif
Requires:	%{name}-data = %{version}-%{release}

%description
Relive the 1960s Space Race - be the first country to land a man on the Moon!

Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

%package data
BuildArch:	noarch
Summary:	Race into Space game data

%description data
Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

Contains platform independent game data.

%package doc
BuildArch:	noarch
Summary:	Race into Space game manual

%description doc
Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

Contains game manual

%prep
%if %{with clang}
export CC=clang CXX=clang++
# Clang does not support this option
export CFLAGS=`echo '%optflags' | sed -e 's/ -fstack-clash-protection//'`
export CXXFLAGS="$CFLAGS"
%endif
%autosetup -p1 -n %{name}-%{pkgversion}

%build
%cmake -DBUILD_PHYSFS=OFF
%cmake_build
pushd doc/manual
pandoc -o manual.html manual.md
popd

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.raceintospace.Raceintospace.metainfo.xml

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/raceintospace
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_metainfodir}/*.xml

%files data
%{_datadir}/%{name}

%files doc
%doc doc/manual

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-13.rc1
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 2.0.0-5.rc1
- Rebuild (jsoncpp)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 16 2021 Petr Menšík <pemensik@redhat.com> - 2.0.0-3.rc1
- Update to 2.0.0rc1, fix FTBFS (#1923505)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 22:05:33 CEST 2020 Petr Menšík <pemensik@redhat.com> - 2.0.0-1.a3
- Update to 2.0.0 alpha3

* Tue Aug 11 2020 Petr Menšík <pemensik@redhat.com> - 1.2.0-5
- Update macros, fix build in rawhide (#1865359)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Petr Menšík <pihhan@gmail.com> - 1.2test1.fedora.2.g0b4a6ba-2
- Development snapshot (0b4a6ba8)

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 1.1.0-5
- Rebuild (jsoncpp)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.1.0-3
- Rebuild (jsoncpp)

* Sat Oct 12 2019 Petr Menšík <pemensik@redhat.com> - 1.1.0-2
- Fix review comment #2 issues
- Fix appcheck, test installed files

* Fri Jul 19 2019 Petr Menšík <pemensik@redhat.com> - 1.1.0-1.20190719gitbf6c86a
- Initial version


