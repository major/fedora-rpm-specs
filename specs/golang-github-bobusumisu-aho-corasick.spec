# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/BobuSumisu/aho-corasick
%global goipath         github.com/BobuSumisu/aho-corasick
Version:                1.0.3

%gometa -L -f


%global common_description %{expand:
Aho-Corasick string-searching algorithm in Go.}

%global golicenses      LICENSE test_data/gpl.txt
%global godocs          README.md

Name:           golang-github-bobusumisu-aho-corasick
Release:        %autorelease
Summary:        Aho-Corasick string-searching algorithm in Go

License:        MIT AND GPL-3.0-only
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
