Name:           R-progress
Version:        %R_rpm_version 1.2.3
Release:        %autorelease
Summary:        Terminal Progress Bars

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.2.3

%description
Configurable Progress bars, they may include percentage, elapsed time, and/or
the estimated completion time. They work in terminals, in Emacs ESS, RStudio,
Windows Rgui and the macOS R.app. The package also provides a C++ API, that
works with or without Rcpp.

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
