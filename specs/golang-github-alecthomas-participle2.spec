# Generated by go2rpm 1.11.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/alecthomas/participle
%global goipath         github.com/alecthomas/participle/v2
Version:                2.1.1

%gometa -L -f

%global common_description %{expand:
A parser library for Go.}

%global golicenses      COPYING
%global godocs          _examples CHANGES.md TUTORIAL.md README.md\\\
                        bin/README.hermit.md

Name:           golang-github-alecthomas-participle2
Release:        %autorelease
Summary:        A parser library for Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}
Source:         %{name}.rpmlintrc

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
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
