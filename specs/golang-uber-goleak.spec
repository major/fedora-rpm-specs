# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/uber-go/goleak
%global goipath         go.uber.org/goleak
%global forgeurl        https://github.com/uber-go/goleak
Version:                1.3.0

%gometa

%global common_description %{expand:
Goroutine leak detector.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Goroutine leak detector

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
