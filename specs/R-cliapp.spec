Name:           R-cliapp
Version:        %R_rpm_version 0.1.2
Release:        %autorelease
Summary:        Create Rich Command Line Applications

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Create rich command line applications, with colors, headings, lists, alerts,
progress bars, etc. It uses CSS for custom themes.

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
