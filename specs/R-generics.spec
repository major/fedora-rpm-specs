Name:           R-generics
Version:        %R_rpm_version 0.1.4
Release:        %autorelease
Summary:        Common S3 Generics not Provided by Base R Methods Related to Model Fitting

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
In order to reduce potential package dependencies and conflicts, generics
provides a number of commonly used S3 generics.

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
