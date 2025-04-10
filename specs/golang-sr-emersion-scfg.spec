# Generated by go2rpm 1.8.1
#
# This specfile is licensed under:
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html
# SPDX-FileCopyrightText: 2022 Maxwell G <gotmax@e.email>
# SPDX-FileCopyrightText: Fedora Project Authors

%bcond_without check
%global debug_package %{nil}

# https://git.sr.ht/~emersion/go-scfg
%global goipath         git.sr.ht/~emersion/go-scfg
%global commit          2ae16e7820824363fc2e198c97a6f69d670ffd9c
%global scm             git
%global topdir          go-scfg-%{commit}
%global archivename     %{name}-%{commit}
%global archiveext      tar.gz

%gometa -f

%global common_description %{expand:
This is a go library for the [scfg](https://git.sr.ht/~emersion/scfg)
configuration file format.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Go library for scfg

License:        MIT
URL:            %{gourl}
# The forge macros don't support Sourcehut.
# https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/209
Source:         %{gourl}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

%description %{common_description}

%gopkg

%prep
%goprep

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
