# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/gosimple/unidecode
%global goipath         github.com/gosimple/unidecode
Version:                1.0.1

%gometa -L -f

%global common_description %{expand:
Unicode transliterator in Golang - Replaces non-ASCII characters with their
ASCII approximations.}

%global golicenses      LICENSE
%global godocs          README.md table.txt

Name:           golang-github-gosimple-unidecode
Release:        %autorelease
Summary:        Unicode transliterator in Golang

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
