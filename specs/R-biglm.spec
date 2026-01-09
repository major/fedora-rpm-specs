Name:           R-biglm
Version:        %R_rpm_version 0.9-3
Release:        %autorelease
Summary:        Bounded memory linear and generalized linear models

License:        GPL-1.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Regression for data too large to fit in memory.

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
