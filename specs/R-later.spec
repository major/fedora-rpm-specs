Name:           R-later
Version:        %R_rpm_version 1.4.5
Release:        %autorelease
Summary:        Utilities for Scheduling Functions to Execute Later with Event Loops

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}
# Remove bundled tinycthread and use C11 threads directly.
Source:         tinycthread-threads-wrapper.h

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.4.4

%description
Executes arbitrary R or C functions some time after the current time, after the
R execution stack has emptied. The functions are scheduled in an event loop.

%prep
%autosetup -c
rm -f later/tests/testthat/test-run_now.R # unconditional suggest
# Ensure we don't use this bundled code.
rm later/src/{badthreads.h,tinycthread.c}
cp %{SOURCE1} later/src/tinycthread.h
sed -i -e '/badthread/d' -e '/tinycthread/d' later/MD5

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
# A file used in tests; tests aren't installed.
rm %{buildroot}%{_R_libdir}/later/bgtest.cpp
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
