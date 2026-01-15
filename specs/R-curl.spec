Name:           R-curl
Version:        %R_rpm_version 7.0.0
Release:        %autorelease
Summary:        A Modern and Flexible Web Client for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libcurl)

%description
The curl() and curl_download() functions provide highly configurable drop-in
replacements for base url() and download.file() with better performance,
support for encryption (https, ftps), gzip compression, authentication, and
other 'libcurl' goodies. The core of the package implements a framework for
performing fully customized requests where data can be processed either in
memory, on disk, or streaming via the callback or connection interfaces. Some
knowledge of 'libcurl' is recommended; for a more-user-friendly web client see
the 'httr' package which builds on this package with http specific tools and
logic.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
