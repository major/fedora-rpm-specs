# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/yuin/goldmark-meta
%global goipath         github.com/yuin/goldmark-meta
Version:                1.1.0

%gometa -L -f

%global common_description %{expand:
A YAML metadata extension for the goldmark markdown parser.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-yuin-goldmark-meta
Release:        %autorelease
Summary:        A YAML metadata extension for the goldmark markdown parser

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
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
