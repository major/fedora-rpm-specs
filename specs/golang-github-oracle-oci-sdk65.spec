# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/oracle/oci-go-sdk
%global goipath         github.com/oracle/oci-go-sdk/v65
Version:                65.71.0

%gometa -L -f

%global common_description %{expand:
Go SDK for Oracle Cloud Infrastructure.}

%global golicenses      LICENSE.txt
%global godocs          example CHANGELOG.md CONTRIBUTING.md README.md

Name:           golang-github-oracle-oci-sdk65
Release:        %autorelease
Summary:        Go SDK for Oracle Cloud Infrastructure

License:        UPL-1.0 OR Apache-2.0
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
for test in "TestSeek" "TestSeekable"\
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -d objectstorage/transfer
%endif
%endif

%gopkgfiles

%changelog
%autochangelog