# Generated by go2rpm 1.13.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/cncf-tags/container-device-interface
%global goipath     tags.cncf.io/container-device-interface
%global forgeurl    https://github.com/cncf-tags/container-device-interface
Version:            0.8.0

%gometa -L -f

%global common_description %{expand:
CDI (Container Device Interface), is a specification, for container-runtimes,
to support third-party devices.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md code-of-conduct.md SPEC.md

Name:       %{goname}
Release:    %autorelease
Summary:    Specification for container-runtimes to support third-party devices

License:    Apache-2.0
URL:        %{gourl}
Source:     %{gosource}

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
