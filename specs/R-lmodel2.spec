Name:           R-lmodel2
Version:        %R_rpm_version 1.7-4
Release:        %autorelease
Summary:        Model II Regression

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Computes model II simple linear regression using ordinary least squares
(OLS), major axis (MA), standard major axis (SMA), and ranged major axis

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
