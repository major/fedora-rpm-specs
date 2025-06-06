# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/andreyvit/diff
%global goipath         github.com/andreyvit/diff
%global commit          c7f18ee00883bfd3b00e0a2bf7607827e0148ad4

%gometa

%global common_description %{expand:
Diff provides quick and easy string diffing functions based on
github.com/sergi/go-diff, mainly for diffing strings in tests.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Quick'n'easy string diffs for Go, mainly for diffing strings in tests

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)

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
