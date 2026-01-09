Name:           R-prettycode
Version:        %R_rpm_version 1.1.0
Release:        %autorelease
Summary:        Pretty Print R Code in the Terminal

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Replace the standard print method for functions with one that performs syntax
highlighting, using ANSI colors, if the terminal supports them.

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
