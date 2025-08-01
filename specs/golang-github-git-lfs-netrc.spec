# Generated by go2rpm 1.16.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

%global debug_package %{nil}

# https://github.com/git-lfs/go-netrc
%global goipath         github.com/git-lfs/go-netrc
%global commit          ba0029b43d1190baf66986a87418593ed1a07f42

%gometa -L -f

%global common_description %{expand:
A Golang package for reading and writing netrc files. This package can
parse netrc files, make changes to them, and then serialize them back to
netrc format, while preserving any whitespace that was present in the
source file.}

%global golicenses      LICENSE
%global godocs          README.md examples

Name:           golang-github-git-lfs-netrc
Version:        0
Release:        %autorelease -p
Summary:        Netrc file parser for Go programming language

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -q -p1

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
