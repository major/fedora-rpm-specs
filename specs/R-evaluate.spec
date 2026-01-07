Name:           R-evaluate
Version:        %R_rpm_version 1.0.5
Release:        %autorelease
Summary:        Parsing and Evaluation Tools that Provide More Details than the Default

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Parsing and evaluation tools that make it easy to recreate the command line
behaviour of R.

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
