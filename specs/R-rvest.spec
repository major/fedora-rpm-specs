Name:           R-rvest
Version:        %R_rpm_version 1.0.5
Release:        %autorelease
Summary:        Easily Harvest (Scrape) Web Pages

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Wrappers around the 'xml2' and 'httr' packages to make it easy to download,
then manipulate, HTML and XML.

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
