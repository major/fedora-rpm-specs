# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/seancfoley/ipaddress-go
%global goipath         github.com/seancfoley/ipaddress-go
Version:                1.7.0

%gometa -f


%global common_description %{expand:
Go library for handling IP addresses and subnets, both IPv4 and IPv6.}

%global golicenses      LICENSE ipaddr/LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go library for handling IP addresses and subnets, both IPv4 and IPv6

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
