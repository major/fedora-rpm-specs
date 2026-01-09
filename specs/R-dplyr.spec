Name:           R-dplyr
Version:        %R_rpm_version 1.1.4
Release:        %autorelease
Summary:        A Grammar of Data Manipulation

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel < 0.8.5-4

%description
A fast, consistent tool for working with data frame like objects, both in
memory and out of memory.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
