# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/gdamore/encoding
%global goipath         github.com/gdamore/encoding
Version:                1.0.1

%gometa
%global common_description %{expand:
Package encoding provides a number of encodings that are missing from the
standard Go encoding package.

We hope that we can contribute these to the standard Go library someday. It
turns out that some of these are useful for dealing with I/O streams coming
from non-UTF friendly sources.

The UTF8 Encoder is also useful for situations where valid UTF-8 might be
carried in streams that contain non-valid UTF; in particular I use it for
helping me cope with terminals that embed escape sequences in otherwise valid
UTF-8.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Various character map encodings missing from golang.org/x/net/encoding

# Upstream license specification: Apache-2.0
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/transform)

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