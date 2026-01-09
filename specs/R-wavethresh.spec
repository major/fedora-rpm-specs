Name:           R-wavethresh
Version:        %R_rpm_version 4.7.3
Release:        %autorelease
Summary:        R module, Software to perform wavelet statistics and transforms

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Software to perform 1-d and 2-d wavelet statistics and transforms

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
