%global libapogee_pkg indi-3rdparty-libapogee
%global libfli_pkg indi-3rdparty-libfli

%global indi_version 2.1.2

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Name:           indi-3rdparty-libraries
Version:        %{indi_version}
Release:        %autorelease
Summary:        INDI 3rdparty libraries
License:        LGPL-2.0-or-later
URL:            http://indilib.org

# Tar is generated from the huge all-in-one tar from INDI
# by using ./generate-libraries-tarball.sh %%{version}
# The main source from upstream is at
# https://github.com/indilib/indi-3rdparty/archive/refs/tags/v%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.zst
Source1:        generate-libraries-tarball.sh

# Upstream injects -fPIE flag, let Fedora choose
Patch:          modify_cmake_common_flags.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libindi) = %{version}

# We want this metapackage to install all libraries at once.
# Just use weak dependencies to avoid possible errors.
Recommends:     %{libapogee_pkg}%{?_isa} = %{version}-%{release}
Recommends:     %{libfli_pkg}%{?_isa} = %{version}-%{release}

%description
This is a metapackage for installing all INDI 3rdparty libraries
at once. You probably don't want to install everything, but just pick
the libraries you need from the appropriate subpackage.

We currently ship the following libraries:
- %{libapogee_pkg}
- %{libfli_pkg}


%package -n %{libapogee_pkg}
License:        GPL-2.0-or-later AND MPL-2.0
Summary:        Library for Apogee CCD Cameras

Provides:       libapogee = 1:%{version}-%{release}
Obsoletes:      libapogee <= 1:1.9.3-2

%description -n %{libapogee_pkg}
Apogee library is used by applications to control Apogee CCDs.

%package -n %{libapogee_pkg}-devel
Summary:        Development files %{libapogee_pkg}
Requires:       %{libapogee_pkg}%{?_isa} = %{version}-%{release}

Provides:       libapogee-devel = 1:%{version}-%{release}
Obsoletes:      libapogee-devel <= 1:1.9.3-2

%description -n %{libapogee_pkg}-devel
These are the header files needed to develop a
%{libapogee_pkg} application


%package -n %{libfli_pkg}
License:        BSD-2-Clause AND BSD-3-Clause
Summary:        Library for FLI CCD Camera & Filter Wheels

Provides:       libfli = 1:%{version}-%{release}
Obsoletes:      libfli <= 1:1.9.3-2

%description -n %{libfli_pkg}
Finger Lakes Instrument library is used by applications to control FLI 
line of CCDs and Filter wheels

%package -n %{libfli_pkg}-devel
Summary:        Development files %{libfli_pkg}
Requires:       %{libfli_pkg}%{?_isa} = %{version}-%{release}

Provides:       libfli-devel = 1:%{version}-%{release}
Obsoletes:      libfli-devel <= 1:1.9.3-2

%description -n %{libfli_pkg}-devel
These are the header files needed to develop a
%{libfli_pkg} application


%prep
%autosetup -p1

# For Fedora we want to put udev rules in %%{_udevrulesdir}
find . -mindepth 2 -name CMakeLists.txt \
    -exec echo 'Processing {}' \; \
    -exec sed -i 's#\/\(etc\|lib\)\/udev\/rules\.d#%{_udevrulesdir}#g' {} \;

%build
%cmake -DBUILD_LIBS=ON \
    -DNO_PRE_BUILT=ON

%cmake_build


%install
%cmake_install


%check
# no tests provided


%files
%license LICENSE
%doc README.md


%files -n %{libapogee_pkg}
%license libapogee/LICENSE
%doc libapogee/README
%{_libdir}/libapogee.so.3*
# The following are config files not intended to be modified by users
# I've asked upstream to move them in a more appropriate place
%config %{_sysconfdir}/Apogee
%{_udevrulesdir}/99-apogee.rules

%files -n %{libapogee_pkg}-devel
%{_includedir}/libapogee
%{_libdir}/libapogee.so


%files -n %{libfli_pkg}
%license libfli/LICENSE.BSD
%{_libdir}/libfli.so.2*
%{_udevrulesdir}/99-fli.rules

%files -n %{libfli_pkg}-devel
%{_includedir}/libfli.h
%{_libdir}/libfli.so


%changelog
%autochangelog
