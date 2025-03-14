# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/matrix-org/gomatrix
%global goipath         github.com/matrix-org/gomatrix
%global commit          ceba4d9f75305223c2598cda1b1090f438b1e2fa

%gometa -L -f


%global common_description %{expand:
A Golang Matrix client.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           golang-github-matrix-org-gomatrix
Version:        0
Release:        %autorelease -p
Summary:        A Golang Matrix client

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
