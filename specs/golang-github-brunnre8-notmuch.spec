# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/brunnre8/go.notmuch
%global goipath         github.com/brunnre8/go.notmuch
%global commit          caa2daf7093c998ed18e1b85a42c4105713e9dda

%gometa

%global godevelheader %{expand:
Requires:       notmuch-devel}

%global common_description %{expand:
Go language bindings for notmuch mail.}

%global golicenses      COPYING license.txt
%global godocs          example AUTHORS README-INTERNALS.md README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Go language bindings for notmuch mail

License:        GPL-3.0-only
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://notmuchmail.org/releases/test-databases/database-v1.tar.xz

Patch0:         https://patch-diff.githubusercontent.com/raw/brunnre8/go.notmuch/pull/2.patch

BuildRequires:  notmuch-devel

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
sed -i "s|github.com/zenhack/go.notmuch|github.com/brunnre8/go.notmuch|" $(find . -name "*.go" -type f)

# Unzip fixtures for tests
tar -C fixtures -xf %{SOURCE1}

%install
%gopkginstall

%if %{with check}
%check
for test in "TestOpenWithConfig" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
