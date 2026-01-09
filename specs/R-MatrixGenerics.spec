Name:           R-MatrixGenerics
Version:        %R_rpm_version 1.22.0
Release:        %autorelease
Summary:        S4 Generic Summary Statistic Functions that Operate on Matrix-Like Objects

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
S4 generic functions modeled after the 'matrixStats' API for alternative matrix
implementations. Packages with alternative matrix implementation can depend on
this package and implement the generic functions that are defined here for a
useful set of row and column summary statistics. Other package developers can
import this package and handle a different matrix implementations without
worrying about incompatibilities.

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
