Name:           R-XML
Version:        %R_rpm_version 3.99-0.20
Release:        %autorelease
Summary:        Tools for Parsing and Generating XML Within R and S-Plus


License:        BSD-3-Clause
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  libxml2-devel

%description
Many approaches for both reading and creating XML (and HTML) documents
(including DTDs), both local and accessible via HTTP or FTP.  Also offers
access to an XPath "interpreter".

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
