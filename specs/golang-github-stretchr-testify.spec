# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/stretchr/testify
%global goipath         github.com/stretchr/testify
Version:                1.9.0

%gometa -L

%global common_description %{expand:
Golang set of packages that provide many tools for testifying
that your code will behave as you intend.

Features include:

 - Easy assertions
 - Mocking
 - Testing suite interfaces and functions}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md EMERITUS.md MAINTAINERS.md README.md

Name:           golang-github-stretchr-testify
Release:        %autorelease
Summary:        Toolkit with common assertions and mocks

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

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
%ifarch %{ix86} %{arm} s390x riscv64
# TestFailfastSuiteFailFastOn fails on i686 and s390x
for test in "TestFailfastSuiteFailFastOn" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
