Name:           R-microbats
Version:        %R_rpm_version 0.1-1
Release:        %autorelease
Summary:        An implementation of Bat Algorithm in R

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A nature-inspired metaheuristic algorithm based on the echolocation behavior
of microbats that uses frequency tuning to optimize problems in both
continuous and discrete dimensions. This R package makes it easy to
implement the standard bat algorithm on any user-supplied function.
The algorithm was first developed by Xin-She Yang in 2010 
(<doi:10.1007/978-3-642-12538-6_6>, <doi:10.1109/CINTI.2014.7028669>.

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
