# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/simplesurance/bunny-go
%global goipath         github.com/simplesurance/bunny-go
%global commit          e11d9dc91f04059bf8f32d81cc36206af16b847b

%gometa -f

%global common_description %{expand:
Go library for the bunny.net CDN API.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Go library for the bunny.net CDN API

License:        MIT
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