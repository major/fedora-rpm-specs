Name:           R-timeSeries
Version:        %R_rpm_version 4052.112
Release:        %autorelease
Summary:        Financial Time Series Objects (Rmetrics)

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
'S4' classes and various tools for financial time series: Basic functions such
as scaling and sorting, subsetting, mathematical operations and statistical
functions.

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
