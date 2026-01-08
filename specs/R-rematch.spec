Name:           R-rematch
Version:        %R_rpm_version 2.0.0
Release:        %autorelease
Summary:        Match Regular Expressions with a Nicer 'API'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A small wrapper on 'regexpr' to extract the matches and captured groups
from the match of a regular expression to a character vector.

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
