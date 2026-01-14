Name:           R-doParallel
Version:        %R_rpm_version 1.0.17
Release:        %autorelease
Summary:        Foreach Parallel Adaptor for the 'parallel' Package

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a parallel backend for the %%dopar%% function using the parallel
package.

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
