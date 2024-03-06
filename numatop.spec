Name:           numatop
Version:        2.4
Release:        %autorelease
Summary:        Memory access locality characterization and analysis

License:        BSD-3-Clause
URL:            https://01.org/numatop
Source:         https://github.com/intel/numatop/archive/refs/tags/v%{version}.tar.gz

# https://github.com/intel/numatop/pull/71
Patch:          0001-common-Use-sym_type_t-in-elf64_binary_read-signature.patch
Patch:          0002-common-Add-format-strings-to-mvwprintw-calls.patch
Patch:          0003-common-Remove-unnecessary-temp-buffer.patch
Patch:          0004-common-Use-memcpy-to-the-process-name-to-a-line.patch
Patch:          0005-common-Replace-malloc-strncpy-with-strdup.patch
Patch:          0006-common-Build-node-string-with-bound-checks.patch
Patch:          0007-common-Increase-node-string-buffer-size.patch
Patch:          0008-x86-Add-missing-fields-to-s_emr_config.patch

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

NumaTOP supports the Intel Xeon processors, AMD Zen processors and PowerPC
processors.


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
