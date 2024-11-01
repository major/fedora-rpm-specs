# Generated by go2rpm 1.8.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/mdlayher/socket
%global goipath         github.com/mdlayher/socket
Version:                0.4.1

%gometa -f

%global common_description %{expand:
Package socket provides a low-level network connection type which integrates
with Go's runtime network poller to provide asynchronous I/O and deadline
support. MIT Licensed.}

%global golicenses      LICENSE.md
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Package socket provides a low-level network connection type which integrates with Go's runtime network poller to provide asynchronous I/O and deadline support. MIT Licensed

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
