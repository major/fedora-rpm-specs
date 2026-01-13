Name:           R-webfakes
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        Fake Web Apps for HTTP Testing

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Create a web app that makes it easier to test web clients without using the
internet. It includes a web app framework with path matching, parameters
and templates. Can parse various 'HTTP' request bodies. Can send 'JSON'
data or files from the disk. Includes a web app that implements the
<https://httpbin.org> web service.

%prep
%autosetup -c
rm -f webfakes/tests/testthat/test-httpbin.R # network tests

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
