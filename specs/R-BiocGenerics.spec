Name:           R-BiocGenerics
Version:        %R_rpm_version 0.56.0
Release:        %autorelease
Summary:        Generic functions for Bioconductor

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
S4 generic functions needed by many other Bioconductor packages.

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
