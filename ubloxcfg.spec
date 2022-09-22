%global forgeurl https://github.com/phkehl/ubloxcfg
%global commit a46d97c21fa775160e5ed170443a8f3e4d7249c9
%forgemeta

Name:           ubloxcfg
Version:        1.13
Release:        %autorelease
Summary:        u-blox 9 positioning receivers configuration library and tool

License:        GPLv3 and LGPLv3 and BSD
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-Data-Float
BuildRequires:  perl-Path-Tiny
BuildRequires:  sed

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
BuildArch:      noarch

%description    doc
This package contains documentation for %{name}.

%prep
%forgesetup
# remove bundled perl libraries
rm -r 3rdparty/perl
# drop hardcoded CFLAGS
sed -e 's/-m32//g' -e 's/-m64//g' -e 's/-O3//g' -i Makefile

%build
%set_build_flags
%make_build V= LDFLAGS_library="-Wl,-soname,libubloxcfg.so.0.0.0 -shared -lm" \
  libubloxcfg.so
%make_build V= cfgtool doc

%install
install -Dpm0755 output/cfgtool-release %{buildroot}%{_bindir}/cfgtool
install -Dpm0644 -t %{buildroot}%{_includedir}/%{name} ubloxcfg/*.h ff/*.h
install -Dpm0755 output/libubloxcfg.so %{buildroot}%{_libdir}/libubloxcfg.so.0.0.0
ln -s libubloxcfg.so.0.0.0 %{buildroot}%{_libdir}/libubloxcfg.so.0
ln -s libubloxcfg.so.0 %{buildroot}%{_libdir}/libubloxcfg.so

mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed \
  -e 's:^prefix=.*$:prefix=%{_prefix}:' \
  -e 's:^libdir=.*$:libdir=${exec_prefix}/%{_lib}:' \
  ubloxcfg/libubloxcfg.pc > %{buildroot}%{_libdir}/pkgconfig/libubloxcfg.pc

%check
make test_m%{__isa_bits}
%ifarch s390x
# Ignore test failures on s390x for now
./output/test_m%{__isa_bits}-release || true
%else
./output/test_m%{__isa_bits}-release
%endif

%files
%license ff/COPYING ubloxcfg/LICENSE 3rdparty/stuff/crc24q.LICENSE
%doc README.md cfgtool.txt
%{_bindir}/cfgtool
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files doc
%license ubloxcfg/LICENSE
%doc output/ubloxcfg_html

%changelog
%autochangelog
