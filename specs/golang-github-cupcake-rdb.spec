# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/cupcake/rdb
%global goipath         github.com/cupcake/rdb
%global commit          43ba34106c765f2111c0dc7b74cdf8ee437411e0

%gometa

%global common_description %{expand:
Rdb is a Go package that implements parsing and encoding of the Redis RDB file
format.}

%global golicenses      LICENCE
%global godocs          examples README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Redis RDB parser for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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