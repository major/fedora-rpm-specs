Name:           R-ggplot2
Version:        %R_rpm_version 4.0.1
Release:        %autorelease
Summary:        Create Elegant Data Visualisations Using the Grammar of Graphics

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A system for 'declaratively' creating graphics, based on "The Grammar of
Graphics". You provide the data, tell 'ggplot2' how to map variables to
aesthetics, what graphical primitives to use, and it takes care of the
details.

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
