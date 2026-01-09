Name:           R-wesanderson
Version:        %R_rpm_version 0.3.7
Release:        %autorelease
Summary:        Wes Anderson Palette Generator

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Palettes generated mostly from 'Wes Anderson' movies.

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
