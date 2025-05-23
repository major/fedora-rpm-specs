# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/creack/pty
%global goipath         github.com/creack/pty
Version:                1.1.24

%gometa -L

%global common_description %{expand:
Pty is a Go package for using unix pseudo-terminals.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-creack-pty
Release:        %autorelease
Summary:        PTY interface for Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
# requires access to /dev/pts/0
for test in "TestReadWriteText" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
