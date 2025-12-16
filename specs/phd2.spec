%global gittag v2.6.14
#%%global commit a205f63238c8505cf641057d8d82734e51f9ab15
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global date 20230212

Name:           phd2
%if "%{?gittag}"
Version:        2.6.14
%else
Version:        2.6.11^dev4^%{date}%{shortcommit}
%endif
Release:        %autorelease
Summary:        Telescope guiding software
License:        BSD-3-Clause AND LGPL-2.1-or-later AND ICU
URL:            http://openphdguiding.org/
%if "%{?gittag}"
# Download upstream tarball from
# https://github.com/OpenPHDGuiding/%%{name}/archive/%%{gittag}.tar.gz
# and then run ./generate-tarball.sh %%{version}
Source0:        %{name}-%{version}-purged.tar.xz
%else
# Download upstream tarball from
# https://github.com/OpenPHDGuiding/%%{name}/archive/%%{commit}/%%{name}-%%{commit}.tar.gz
# and then run ./generate-tarball.sh %%{commit}
Source0:        %{name}-%{commit}-purged.tar.xz
%endif
# Script to purge binaries and unneeded files from downloaded sources
Source1:        generate-tarball.sh

# Do not force c++ std
Patch99:        phd2_2.9.10_std_cflags.patch

# Fix eigen 5.0.0 detection
Patch101:       phd2-eigen3.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
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
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(zlib)

Recommends:     libindi


%description
PHD2 is telescope guiding software that simplifies the process of tracking
a guide star, letting you concentrate on other aspects of deep-sky imaging
or spectroscopy.


%prep
%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

# Remove spurious executable bit set on icons and docs
find icons -type f -print0 |xargs -0 chmod -x
chmod -x doc/PHD_2.0_Architecture.docx


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
%ctest
#env CTEST_OUTPUT_ON_FAILURE=1 make test -C %%{_vpath_builddir}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f %{name}.lang
%doc README.txt doc/PHD_2.0_Architecture.docx
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/phd2/
%{_datadir}/pixmaps/*


%changelog
%autochangelog
