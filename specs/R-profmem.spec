Name:           R-profmem
Version:        %R_rpm_version 0.7.0
Release:        %autorelease
Summary:        Simple Memory Profiling for R

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A simple and light-weight API for memory profiling of R expressions.  The
profiling is built on top of R's built-in memory profiler
('utils::Rprofmem()'), which records every memory allocation done by R (also
native code).

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
