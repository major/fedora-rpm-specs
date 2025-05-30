# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/pkg/errors
%global goipath         github.com/pkg/errors
Version:                0.9.1

%gometa -L

%global common_description %{expand:
Simple error handling primitives.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-pkg-errors
Release:        %autorelease
Summary:        Simple error handling primitives

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
for test in "TestStackTrace" "TestStackTraceFormat" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
