Name:           R-rhub
Version:        %R_rpm_version 2.0.1
Release:        %autorelease
Summary:        Connect to 'R-hub'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Run 'R CMD check' on any of the 'R-hub' (<https://builder.r-hub.io/>)
architectures, from the command line. The current architectures include
Windows, macOS, Solaris and various Linux distributions.

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
