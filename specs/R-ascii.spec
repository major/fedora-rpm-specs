Name:           R-ascii
Version:        %R_rpm_version 2.6
Release:        %autorelease
Summary:        Export R Objects to Several Markup Languages

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Coerce R object to asciidoc, txt2tags, restructuredText, org, textile or pandoc
syntax. Package comes with a set of drivers for Sweave.

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
