# Generated by go2rpm 1.8.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/docker/go-units
%global goipath         github.com/docker/go-units
Version:                0.5.0

%gometa

%global common_description %{expand:
Go-units is a library to transform human friendly measurements into machine
friendly values.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Parse and print size and time units in human-readable format

License:        Apache-2.0
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
