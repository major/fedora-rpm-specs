Name:           R-Rhtslib
Version:        %R_rpm_version 3.6.0
Release:        %autorelease
Summary:        HTSlib high-throughput sequencing library as an R package

License:        LGPL-2.0-or-later
URL:            %{bioc_url}
Source:         %{bioc_source}
Patch:          R-Rhtslib-buildroot-fix.patch

BuildRequires:  R-devel
BuildRequires:  libcurl-devel
Obsoletes:      %{name}-devel <= 3.6.0

# Do not check for Provides in internal shared libraries
%global __provides_exclude_from ^%{_R_libdir}/Rhtslib/usrlib/.*\\.so.*$

%description
This package provides version 1.15.1 of the 'HTSlib' C library for
high-throughput sequence analysis. The package is primarily useful to
developers of other R packages who wish to make use of HTSlib. Motivation and
instructions for use of this package are in the vignette,
vignette(package="Rhtslib", "Rhtslib").

%prep
%autosetup -c -p1

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
