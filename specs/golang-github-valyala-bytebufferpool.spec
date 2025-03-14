# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/valyala/bytebufferpool
%global goipath         github.com/valyala/bytebufferpool
Version:                1.0.0

%gometa

%global common_description %{expand:
An implementation of a pool of byte buffers with anti-memory-waste protection.

The pool may waste limited amount of memory due to fragmentation. This amount
equals to the maximum total size of the byte buffers in concurrent use.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Anti-memory-waste byte buffer pool

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
