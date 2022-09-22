%bcond_without check

# https://github.com/coocood/freecache
%global goipath         github.com/coocood/freecache
Version:                1.2.2

%gometa

%global common_description %{expand:
A cache library for Go with zero GC overhead.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Cache library with zero GC overhead

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cespare/xxhash)

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

