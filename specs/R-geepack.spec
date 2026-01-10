Name:           R-geepack
Version:        %R_rpm_version 1.3.13
Release:        %autorelease
Summary:        Generalized Estimating Equation Package

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.3.13

%description
Generalized estimating equations solver for parameters in mean, scale, and
correlation structures, through mean link, scale link, and correlation
link. Can also handle clustered categorical responses.

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
