# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/jedib0t/go-pretty
%global goipath         github.com/jedib0t/go-pretty/v6
Version:                6.6.4

%gometa -f

%global common_description %{expand:
Table-writer and more in golang!}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md SECURITY.md

Name:           golang-github-jedib0t-pretty-6
Release:        %autorelease
Summary:        Table-writer and more in golang

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
