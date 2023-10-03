%bcond_without check
%global debug_package %{nil}

# https://github.com/pkg/xattr
%global goipath         github.com/pkg/xattr
Version:                0.4.9

%gometa

%global common_description %{expand:
Extended attribute support for Go (linux + darwin + freebsd + netbsd).

"Extended attributes are name:value pairs associated permanently with files and
directories, similar to the environment strings associated with a process. An
attribute may be defined or undefined. If it is defined, its value may be empty
or non-empty."}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Extended attribute support for Go

License:        BSD-2-Clause
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
