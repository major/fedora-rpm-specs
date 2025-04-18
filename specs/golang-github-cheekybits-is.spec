# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/cheekybits/is
%global goipath         github.com/cheekybits/is
%global commit          68e9c0620927fb5427fda3708222d0edee89eae9

%gometa

%global common_description %{expand:
A mini testing helper for Go.

 - Simple interface (is.OK and is.Equal)
 - Plugs into existing Go toolchain (uses testing.T)
 - Obvious for newcomers and newbs
 - Also gives you is.Panic and is.PanicWith helpers - because testing panics is ugly}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Mini testing helper for Go

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
