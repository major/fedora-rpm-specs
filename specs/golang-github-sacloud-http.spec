# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/sacloud/go-http
%global goipath         github.com/sacloud/go-http
Version:                0.1.6

%gometa -f

%global common_description %{expand:
HTTP client library for SAKURA cloud in Go.}

%global golicenses      LICENSE includes/LICENSE
%global godocs          AUTHORS README.md includes/AUTHORS includes/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        HTTP client library for SAKURA cloud in Go

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

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