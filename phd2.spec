Name:           phd2
Version:        2.6.11
Release:        %autorelease
Summary:        Telescope guiding software
# Main program files are BSD licensed
# Some components have different licenses:
# QHY camera headers are GPLv2+
# SX camera headers are ICU
# INDI GUI is LGPLv2+
License:        BSD and (GPLv2+ and MIT and LGPLv2+)
URL:            http://openphdguiding.org/
# Download upstream tarball from
# https://github.com/OpenPHDGuiding/%%{name}/archive/v%%{version}.tar.gz
# and then run ./generate-tarball.sh %%{version}
Source0:        %{name}-%{version}-purged.tar.xz
# Script to purge binaries and unneeded files from downloaded sources
Source1:        generate-tarball.sh

# Do not force c++ std
Patch99:        phd2_2.9.10_std_cflags.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  gtest-devel
BuildRequires:  libappstream-glib
BuildRequires:  libindi-static
BuildRequires:  libnova-devel
BuildRequires:  wxGTK-devel

BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libindi) >= 1.5
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)

Recommends:     libindi


%description
PHD2 is telescope guiding software that simplifies the process of tracking
a guide star, letting you concentrate on other aspects of deep-sky imaging
or spectroscopy.


%prep
%autosetup -p1

# Remove spurious executable bit set on icons and docs
find icons -type f -print0 |xargs -0 chmod -x
chmod -x PHD_2.0_Architecture.docx


%build
%{cmake} -DUSE_SYSTEM_CFITSIO=ON \
            -DUSE_SYSTEM_LIBUSB=ON \
            -DUSE_SYSTEM_EIGEN3=ON \
            -DUSE_SYSTEM_GTEST=ON \
            -DUSE_SYSTEM_LIBINDI=ON \
            -DOPENSOURCE_ONLY=ON

# Build is not parallel safe
# https://github.com/OpenPHDGuiding/phd2/issues/972
%cmake_build -j1


%install
%cmake_install

%find_lang %{name}

%check
env CTEST_OUTPUT_ON_FAILURE=1 make test -C %{_vpath_builddir}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f %{name}.lang
%doc README.txt PHD_2.0_Architecture.docx
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/phd2/
%{_datadir}/pixmaps/*


%changelog
%autochangelog
