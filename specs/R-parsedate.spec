Name:           R-parsedate
Version:        %R_rpm_version 1.3.2
Release:        %autorelease
Summary:        Recognize and Parse Dates in Various Formats

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Parse dates automatically, without the need of specifying a format.  Currently
it includes the git date parser. It can also recognize and parse all ISO 8601
formats.

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
