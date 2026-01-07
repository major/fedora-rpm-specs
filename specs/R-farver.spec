Name:           R-farver
Version:        %R_rpm_version 2.1.2
Release:        %autorelease
Summary:        High Performance Colour Space Manipulation

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
The encoding of colour can be handled in many different ways, using different
colour spaces. As different colour spaces have different uses, efficient
conversion between these representations are important. The 'farver' package
provides a set of functions that gives access to very fast colour space
conversion and comparisons implemented in C++, and offers speed improvements
over the 'convertColor' function in the 'grDevices' package.

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
