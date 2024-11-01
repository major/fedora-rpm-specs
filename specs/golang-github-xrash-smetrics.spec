# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/xrash/smetrics
%global goipath         github.com/xrash/smetrics
%global commit          039620a656736e6ad994090895784a7af15e0b80

%gometa

%global common_description %{expand:
This library contains implementations of the Levenshtein distance, Jaro-Winkler
and Soundex algorithms written in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        String metrics library written in Go

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
