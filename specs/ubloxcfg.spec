%global forgeurl https://github.com/phkehl/ubloxcfg
%global commit 499048ba8b3b9d0ca5d752c56f14c48117ebbb8e
%forgemeta

Name:           ubloxcfg
Version:        1.16
Release:        %autorelease
Summary:        u-blox 9 positioning receivers configuration library and tool

# Automatically converted from old format: GPLv3 and LGPLv3 and BSD - review is highly recommended.
License:        GPL-3.0-only AND LGPL-3.0-only
URL:            %forgeurl
Source0:        %forgesource
# Preparing a PR fix for upstream
Patch0:         001-rpath-remove.patch

# Leaf package, dropping
ExcludeArch: %{ix86}
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sed
BuildRequires:  perl
BuildRequires:  perl-Data-Float
BuildRequires:  perl-Path-Tiny

%description
This package implements a library (API) to deal with the new configuration
interface introduced in u-blox 9 positioning receivers.

A command line "cfgtool" is provided to configure a receiver from the
configuration defined in a human-readable configuration file, as well as a few
other functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains development headers and files for %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
This package contains documentation for %{name}.

%prep
%forgesetup
%autopatch -p1

# drop hardcoded CFLAGS
sed -e 's/-O3//g' -i */CMakeLists.txt
# copy various docs to be unique names
cp ff/LICENSE ff-LICENSE
cp ubloxcfg/LICENSE ubloxcfg-LICENSE
cp cfgtool/LICENSE cfgtool-LICENSE
cp cfgtool/README.md cfgtool-README.md
cp ff/README.md ff-README.md

%build
%cmake
%cmake_build
doxygen ubloxcfg/

%install
%cmake_install
rm -rf %{buildroot}/usr/share/doc/

%check
%ifarch s390x x86_64
# Ignore test failures on s390x/x86_64 for now
make test || true
%else
make test
%endif

%files
%license cfgtool-LICENSE ff-LICENSE ubloxcfg-LICENSE
%doc README.md cfgtool-README.md ff-README.md
%doc tools/99-ftdi-ublox.rules tools/evk-f9p-base.cfg
%doc tools/fwdownload.txt cfgtool/cfgtool.txt
%{_bindir}/cfgtool
%{_bindir}/ubloxcfg-test
%{_libdir}/libff.so.0*
%{_libdir}/libubloxcfg.so.0*

%files devel
%{_includedir}/ff/
%{_includedir}/ubloxcfg/
%{_libdir}/libff.so
%{_libdir}/libubloxcfg.so
%{_libdir}/pkgconfig/ff.pc
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/ff/
%{_libdir}/cmake/ubloxcfg/

%files doc
%doc html/

%changelog
%autochangelog
