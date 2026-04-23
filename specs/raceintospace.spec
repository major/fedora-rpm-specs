%bcond_with copr
%bcond_with snapshot

%undefine __cmake_in_source_build

%global archive_suffix tar.gz
%global commit 623777f
%global date 20191012
#global extra rc1
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
Release:	%autorelease
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
BuildRequires:	physfs-devel
BuildRequires:	(physfs-devel >= 3.2.0-4 if 0%{?fedora} >= 44)
BuildRequires:	libpng-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	pandoc
BuildRequires:	cmake(cereal)
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

# Modify runner to have built-in prefix, not computed on current directory.
sed -e "s|^\(BASEDIR=\).*$|\1%{_prefix}|" -i dist/linux-tgz/run.sh
# Do not use static library enforced, use non-CONFIG mode
sed -e 's|QUIET||' -i src/game/CMakeLists.txt

if ! [ -e "%{_libdir}/libphysfs.a" ]; then
  # stupid issue with cmake physfs interface.
  # It checks presence of file for PhysFS::PhysFS-static, which is not allowed by Fedora
  ln -s %{_libdir}/libphysfs.so %{_libdir}/libphysfs.a || true
fi

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
pushd doc/manual
pandoc -o manual.html manual.md
popd

%install
%cmake_install
mv %{buildroot}%{_prefix}/run.sh %{buildroot}%{_bindir}/raceintospace-launcher

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.raceintospace.Raceintospace.metainfo.xml

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/raceintospace*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_metainfodir}/*.xml

%files data
%{_datadir}/%{name}

%files doc
%doc doc/manual

%changelog
%autochangelog
