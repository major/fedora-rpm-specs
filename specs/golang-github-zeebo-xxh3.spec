# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# Avoid noarch package built differently on different architectures
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(github.com/klauspost/cpuid/v2\\)$

# https://github.com/zeebo/xxh3
%global goipath         github.com/zeebo/xxh3
Version:                1.0.2

%gometa -f


%global common_description %{expand:
XXH3 algorithm in Go.}

%global golicenses      LICENSE
%global godocs          README.md

%global godevelheader %{expand:
Requires:               golang(github.com/klauspost/cpuid/v2)}

Name:           %{goname}
Release:        %autorelease
Summary:        XXH3 algorithm in Go

License:        BSD-2-Clause
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
