Name:           R-bindr
Version:        %R_rpm_version 0.1.3
Release:        %autorelease
Summary:        Parametrized Active Bindings

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a simple interface for creating active bindings where the bound
function accepts additional arguments.

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
