Name:           R-highr
Version:        %R_rpm_version 0.11
Release:        %autorelease
Summary:        Syntax Highlighting for R Source Code

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides syntax highlighting for R source code. Currently it supports LaTeX and
HTML output. Source code of other languages is supported via Andre Simon's
highlight package (<http://www.andre-simon.de>).

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
