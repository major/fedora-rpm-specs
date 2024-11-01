# Generated by go2rpm 1.11.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/pion/sdp
%global goipath         github.com/pion/sdp/v3
Version:                3.0.9

%gometa -L -f

%global common_description %{expand:
A Go implementation of the SDP.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-pion-sdp3
Release:        %autorelease
Summary:        A Go implementation of the SDP

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
