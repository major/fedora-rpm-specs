%global forgeurl https://github.com/npwoods/bletchmame

Name:           bletchmame
Version:        2.15
Release:        %autorelease
Summary:        MAME emulator frontend

License:        GPLv3
URL:            https://www.bletchmame.org
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        README.fedora
# Use the distribution MAME by default
Patch0:         bletchmame-default-paths.patch
# Disable broken tests on 32 bit architectures
# https://github.com/npwoods/bletchmame/issues/256
Patch1:         bletchmame-disable-broken-tests.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  libappstream-glib
BuildRequires:  libxkbcommon-devel
BuildRequires:  observable-devel
BuildRequires:  perl
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  quazip-qt6-devel
BuildRequires:  zlib-devel

Recommends:     mame
Recommends:     mame-data-software-lists

%description
BletchMAME is a new experimental front end for MAME. Unlike existing front ends
(which function as launchers, keeping MAME's internal UI), BletchMAME replaces
the internal MAME UI with a more conventional point and click GUI to provide a
friendlier experience in a number of areas (such as profiles, input
configuration and a number of others). While BletchMAME is intended to support
all machines supported by MAME, it should be particularly suitable to computer
emulation.

%prep
%setup -q
%patch0 -p1
# Disable broken tests on 32 bit architectures
%ifarch armv7hl i686 s390x
%patch1 -p1
%endif

cp -p %{SOURCE1} .

# remove bundled libraries
rm -r lib/*
ln -s %{_includedir}/observable lib/observable

# Set build version
mkdir include
echo "v%{version}" | \
  perl scripts/process_version.pl --versionhdr > include/version.gen.h

%build
# Disable libraries as they're only for internal use and not meant to be
# installed
%cmake \
  -DUSE_SHARED_LIBS=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DHAS_VERSION_GEN_H=1
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr plugins %{buildroot}%{_datadir}/%{name}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
install -Dpm0644 -t %{buildroot}%{_metainfodir} %{name}.metainfo.xml
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
%ctest

%files
%license LICENSE.rtf
%doc README.md README.fedora
%{_bindir}/BletchMAME
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
