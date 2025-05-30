# Generated by go2rpm 1.9.0
# Requires fuse module
%bcond_with check
%global debug_package %{nil}

# https://github.com/hanwen/go-fuse
%global goipath         github.com/hanwen/go-fuse/v2
Version:                2.4.0

%gometa -f


%global common_description %{expand:
FUSE bindings for Go.}

%global golicenses      LICENSE
%global godocs          example AUTHORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        FUSE bindings for Go

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
