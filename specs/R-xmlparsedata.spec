Name:           R-xmlparsedata
Version:        %R_rpm_version 1.0.5
Release:        %autorelease
Summary:        Parse Data of 'R' Code as an 'XML' Tree

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Convert the output of 'utils::getParseData()' to an 'XML' tree, that one
can search via 'XPath', and easier to manipulate in general.

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
