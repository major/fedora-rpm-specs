# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/hashicorp/errwrap
%global goipath         github.com/hashicorp/errwrap
Version:                1.1.0

%gometa

%global common_description %{expand:
Errwrap is a package for Go that formalizes the pattern of wrapping errors and
checking if an error contains another error.

There is a common pattern in Go of taking a returned error value and then
wrapping it (such as with fmt.Errorf) before returning it. The problem with this
pattern is that you completely lose the original error structure.

Arguably the correct approach is that you should make a custom structure
implementing the error interface, and have the original error as a field on that
structure, such as this example. This is a good approach, but you have to know
the entire chain of possible rewrapping that happens, when you might just care
about one.

Errwrap formalizes this pattern (it doesn't matter what approach you use above)
by giving a single interface for wrapping errors, checking if a specific error
is wrapped, and extracting that error.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go library for wrapping and querying errors

# Upstream license specification: MPL-2.0
License:        MPL-2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
