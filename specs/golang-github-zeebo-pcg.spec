# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/zeebo/pcg
%global goipath         github.com/zeebo/pcg
Version:                1.0.1

%gometa

%global common_description %{expand:
PCG random number generator.}

%global golicenses      LICENSE
%global godocs          README.txt

Name:           %{goname}
Release:        %autorelease
Summary:        PCG random number generator

# Upstream license specification: CC0-1.0
# Automatically converted from old format: CC0 - review is highly recommended.
License:        CC0-1.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

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
