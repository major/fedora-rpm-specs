# Generated by go2rpm 1.14.0
# testing brittle on non x86
%ifarch x86_64
%bcond check 1
%else
%bcond check 0
%endif


%global debug_package %{nil}

# https://github.com/chewxy/math32
%global goipath         github.com/chewxy/math32
Version:                1.11.1

%gometa -L -f

%global common_description %{expand:
A float32 version of Go's math package. The majority \
of code in this library is a thin float32 wrapper over \
the results of the math package that comes in the \
standard lib.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-chewxy-math32
Release:        %autorelease
Summary:        A float32 version of Go's math package

License:        BSD-2-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A

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
