# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/quic-go/qpack
%global goipath         github.com/quic-go/qpack
Version:                0.4.0

%gometa -f

%global common_description %{expand:
A minimal QPACK RFC9204 implementation in Go.}

%global golicenses      LICENSE.md
%global godocs          example README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A minimal QPACK RFC9204 implementation in Go

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
