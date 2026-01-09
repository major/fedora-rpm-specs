Name:           R-here
Version:        %R_rpm_version 1.0.2
Release:        %autorelease
Summary:        A Simpler Way to Find Your Files

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Constructs paths to your project's files. Declare the relative path of a
file within your project with 'i_am()'. Use the 'here()' function as a
drop-in replacement for 'file.path()', it will always locate the files
relative to your project root.

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
