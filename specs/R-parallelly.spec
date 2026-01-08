Name:           R-parallelly
Version:        %R_rpm_version 1.46.0
Release:        %autorelease
Summary:        Enhancing the 'parallel' Package

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Utility functions that enhance the 'parallel' package and support the
built-in parallel backends of the 'future' package.  For example,
availableCores() gives the number of CPU cores available to your R process
as given by the operating system, 'cgroups' and Linux containers, R
options, and environment variables, including those set by job schedulers
on high-performance compute clusters. If none is set, it will fall back to
parallel::detectCores(). Another example is makeClusterPSOCK(), which is
backward compatible with parallel::makePSOCKcluster() while doing a better
job in setting up remote cluster workers without the need for configuring
the firewall to do port-forwarding to your local computer.

%prep
%autosetup -c
rm -f parallelly/tests/test-makeNodePSOCK.R # ssh test

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
