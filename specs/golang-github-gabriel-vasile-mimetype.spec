# Generated by go2rpm 1.12.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/gabriel-vasile/mimetype
%global goipath         github.com/gabriel-vasile/mimetype
Version:                1.4.5

%gometa -L -f

%global common_description %{expand:
A fast Golang library for media type and file extension detection, based on
magic numbers.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md\\\
                        supported_mimes.md

Name:           golang-github-gabriel-vasile-mimetype
Release:        %autorelease
Summary:        Fast golang library for MIME type and file extension detection

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
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