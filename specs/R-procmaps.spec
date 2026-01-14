Name:           R-procmaps
Version:        %R_rpm_version 0.0.5
Release:        %autorelease
Summary:        Portable Address Space Mapping

# Overall: GPL-3.0-only; bundled gperftools code: BSD-3-Clause
# Note, gperftools code is some internal portion of it, so cannot be unbundled.
License:        GPL-3.0-only AND BSD-3-Clause
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Portable '/proc/self/maps' as a data frame. Determine which library or
other region is mapped to a specific address of a process. -- R packages
can contain native code, compiled to shared libraries at build or
installation time. When loaded, each shared library occupies a portion of
the address space of the main process. When only a machine instruction
pointer is available (e.g. from a backtrace during error inspection or
profiling), the address space map determines which library this instruction
pointer corresponds to.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
