Name:           R-docopt
Version:        %R_rpm_version 0.7.2
Release:        %autorelease
Summary:        Command-Line Interface Specification Language

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Define a command-line interface by just giving it a description in the specific
format.

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
