Name:           R-styler
Version:        %R_rpm_version 1.11.0
Release:        %autorelease
Summary:        Non-Invasive Pretty Printing of R Code

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Pretty-prints R code without changing the user's formatting intent.

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
