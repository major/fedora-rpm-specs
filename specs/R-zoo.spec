Name:           R-zoo
Version:        %R_rpm_version 1.8-15
Release:        %autorelease
Summary:        Z's ordered observations for irregular time series

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.8.15

%description
An S3 class with methods for totally ordered indexed observations. It is
particularly aimed at irregular time series of numeric vectors/matrices and
factors. zoo's key design goals are independence of a particular index/date/
time class and consistency with with ts and base R by providing methods to
extend standard generics.

%prep
%autosetup -c
#Fix line endings
sed -i -e 's/\r//' zoo/inst/doc/zoo*.Rnw

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
