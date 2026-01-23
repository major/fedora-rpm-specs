Name:           R-cpp11
Version:        %R_rpm_version 0.5.3
Release:        %autorelease
Summary:        A C++11 Interface for R's C Interface

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.5.2

%description
Provides a header only, C++11 interface to R's C interface.  Compared to
other approaches 'cpp11' strives to be safe against long jumps from the C
API as well as C++ exceptions, conform to normal R function semantics and
supports interaction with 'ALTREP' vectors.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
