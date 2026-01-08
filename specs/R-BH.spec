Name:           R-BH
Version:        %R_rpm_version 1.90.0-1
Release:        %autorelease
Summary:        Boost C++ Header Files for R

# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.90.0-1

%description
Boost provides free peer-reviewed portable C++ source libraries. A large part 
of Boost is provided as C++ template code which is resolved entirely at 
compile-time without linking. This package aims to provide the most useful 
subset of Boost libraries for template use among CRAN package. By placing 
these libraries in this package, we offer a more efficient distribution 
system for CRAN as replication of this code in the sources of other packages 
is avoided. 

%prep
%autosetup -c
# Remove spurious exec permissions
for i in `find %{packname}/inst/include/boost |grep hpp`; do chmod -x $i; done

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
