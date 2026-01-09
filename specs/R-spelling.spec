Name:           R-spelling
Version:        %R_rpm_version 2.3.2
Release:        %autorelease
Summary:        Tools for Spell Checking in R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Spell checking common document formats including latex, markdown, manual
pages, and description files. Includes utilities to automate checking of
documentation and vignettes as a unit test during 'R CMD check'. Both
British and American English are supported out of the box and other
languages can be added. In addition, packages may define a 'wordlist' to
allow custom terminology without having to abuse punctuation.

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
