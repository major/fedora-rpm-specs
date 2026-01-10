Name:           R-rematch2
Version:        %R_rpm_version 2.1.2
Release:        %autorelease
Summary:        Tidy Output from Regular Expression Matching

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Wrappers on 'regexpr' and 'gregexpr' to return the match results in tidy
data frames.

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
