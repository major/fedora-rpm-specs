# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/shogo82148/go-shuffle
%global goipath         github.com/shogo82148/go-shuffle
Version:                1.0.1

%gometa

%global common_description %{expand:
Package Shuffle provides primitives for shuffling slices and user-defined
collections.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Primitives for shuffling slices and user-defined collections

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog