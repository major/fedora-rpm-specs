# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/insomniacslk/dhcp
%global goipath         github.com/insomniacslk/dhcp
%global commit          8c70d406f6d24a17219a5f543174c1f3f3ad9e35

%gometa -f


%global common_description %{expand:
DHCPv6 and DHCPv4 packet library, client and server written in Go.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTORS.md README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        DHCPv6 and DHCPv4 packet library, client and server written in Go

License:        BSD-3-Clause
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