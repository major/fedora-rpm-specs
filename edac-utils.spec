Name:           edac-utils
Version:        0.18
%global so_version 1
Release:        %autorelease
Summary:        Userspace helper for kernel EDAC drivers

# The entire source is GPL-2.0-or-later.
#
# Any files under different licenses are part of the build system and do not
# contribute to the license of the binary RPM:
#   - configure is FSFUL or more likely (FSFUL AND GPL-2.0-or-later)
#   - install-sh is X11
License:        GPL-2.0-or-later
URL:            https://github.com/grondo/edac-utils
Source0:        %{url}/archive/%{version}/edac-utils-%{version}.tar.gz
Source1:        edac.service

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Update obsolete FSF postal addresses
# https://github.com/grondo/edac-utils/pull/13
#
# Since upstream merged the PR, we feel justified in patching the COPYING file.
Patch:          %{url}/pull/13.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators

BuildRequires:  libsysfs-devel
BuildRequires:  systemd-rpm-macros

Requires:       libedac = %{version}-%{release}
Requires:       edac-util = %{version}-%{release}
Requires:       edac-ctl = %{version}-%{release}

%global common_description %{expand:
EDAC (Error Detection and Correction) is a set of Linux kernel modules that
handle reporting of hardware-related errors. Currently these modules mainly
handle detection of ECC memory errors for many x86 and x86-64 chipsets and PCI
bus parity errors.

The edac-utils project currently has three components: libedac, edac-util, and
edac-ctl. The libedac library presents a standard API for reading EDAC error
counts and other information from sysfs, and edac-util uses this API to
generate standard reports from the commandline. The edac-ctl utility is a perl
script which uses config files to load the appropriate EDAC driver for a given
chipset and register motherboard DIMM labels if they are configured. An init
script is also provided which uses edac-ctl to initialize EDAC at system
startup.}

%description %{common_description}

This is a metapackage that installs all three components.


%package -n libedac
Summary:        Standard API for reading EDAC error counts from sysfs

%description -n libedac %{common_description}

This package provides the libedac library.


%package -n libedac-devel
Summary:        Development files for libedac

Requires:       libedac%{?_isa} = %{version}-%{release}

Provides:       edac-utils-devel%{?_isa} = %{version}-%{release}
Provides:       edac-utils-devel = %{version}-%{release}
Obsoletes:      edac-utils-devel < 0.18-18

%description -n libedac-devel %{common_description}

This package contains the development headers and libraries and the man page
for libedac.


%package -n edac-util
Summary:        Command-line tool to generate standard EDAC reports

Requires:       libedac%{?_isa} = %{version}-%{release}

%description -n edac-util %{common_description}

This package provides the edac-util command-line tool.


%package -n edac-ctl
Summary:        Script to load EDAC driver and register DIMM labels

# Require dmidecode where it is available. Architecture list from
# ExclusiveArch in dmidecode.spec; updated 2021-12-06.
%ifarch %{ix86} x86_64 ia64 aarch64
Requires:       dmidecode
%endif
Requires:       hwdata
# for modprobe:
Requires:       kmod

# This subpackage would be BuildArch: noarch, except for the arch-conditional
# dependency on dmidecode.

%description -n edac-ctl %{common_description}

This package provides the edac-ctl script and the edac service.


%prep
%autosetup -p1


%build
autoreconf --force --install --verbose
%configure --disable-static
%make_build


%install
%make_install
find '%{buildroot}' -type f -name '*.la' -print -delete

install -D -p -m 0644 '%{SOURCE1}' '%{buildroot}%{_unitdir}/edac.service'
rm -f '%{buildroot}%{_sysconfdir}/init.d/edac'
install -d -m 0755 '%{buildroot}%{_sysconfdir}/edac/labels.d' \
    '%{buildroot}%{_sysconfdir}/edac/mainboard'


%post -n edac-ctl
%systemd_post edac.service


%preun -n edac-ctl
%systemd_preun edac.service


%postun -n edac-ctl
%systemd_postun_with_restart edac.service


%files
# Empty; the base package is now a metapackage


%files -n libedac
%license AUTHORS COPYING DISCLAIMER
%{_libdir}/libedac.so.%{so_version}{,.*}


%files -n libedac-devel
%doc README NEWS
%{_libdir}/libedac.so
%{_includedir}/edac.h
%{_mandir}/man3/edac.3*


%files -n edac-util
%{_bindir}/edac-util
%{_mandir}/man1/edac-util.1*


%files -n edac-ctl
%license AUTHORS COPYING DISCLAIMER
%doc README NEWS

%{_sbindir}/edac-ctl
%{_mandir}/man8/edac-ctl.8*
# The explicit directory permissions don’t seem necessary, but we don’t see a
# reason to change them now, either.
%dir %attr(0755,root,root) %{_sysconfdir}/edac
%config(noreplace) %{_sysconfdir}/edac/labels.db
%dir %attr(0755,root,root) %dir %{_sysconfdir}/edac/labels.d
%dir %attr(0755,root,root) %dir %{_sysconfdir}/edac/mainboard
%{_unitdir}/edac.service


%changelog
%autochangelog
