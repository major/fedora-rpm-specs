# https://github.com/intel/numatop/pull/53
%undefine _ld_as_needed

Name:           numatop
Version:        2.3
Release:        %autorelease
Summary:        Memory access locality characterization and analysis

License:        BSD-3-Clause
URL:            https://01.org/numatop
Source:         https://github.com/intel/numatop/archive/refs/tags/v%{version}.tar.gz
Patch0:         format.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  check-devel
BuildRequires:  ncurses-devel
BuildRequires:  numactl-devel

# This only works for Intel and Power CPUs
ExclusiveArch:  x86_64 ppc64le


%description
NumaTOP is an observation tool for runtime memory locality characterization and
analysis of processes and threads running on a NUMA system. It helps the user
characterize the NUMA behavior of processes and threads and identify where the
NUMA-related performance bottlenecks reside.

NumaTOP supports the Intel Xeon processors and PowerPC processors.


%prep
%autosetup -p1


%build
autoreconf --force --install --symlink
%configure
%make_build


%install
%make_install


%check
%make_build check


%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
%autochangelog
