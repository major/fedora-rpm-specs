# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/projectdiscovery/freeport
%global goipath         github.com/projectdiscovery/freeport
Version:                0.0.5

%gometa -f

%global common_description %{expand:
Free listening port from the OS.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Free listening port from the OS

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