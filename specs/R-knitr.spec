Name:           R-knitr
Version:        %R_rpm_version 1.51
Release:        %autorelease
Summary:        A General-Purpose Package for Dynamic Report Generation in R

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Recommends:     tex(framed.sty)
Recommends:     tex(listings.sty)

%description
Provides a general-purpose tool for dynamic report generation in R using
Literate Programming techniques.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
