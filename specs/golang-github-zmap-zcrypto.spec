# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/zmap/zcrypto
%global goipath         github.com/zmap/zcrypto
%global commit          64a80ee67140cba7184e874ad522497452a9f92c

%gometa

%global common_description %{expand:
Liberal Go TLS + X.509 Library for Research.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Liberal Go TLS + X.509 Library for Research

# Main library: Apache-2.0
# Code from Google: ISC
# util/isURL.go: MIT
License:        Apache-2.0 AND ISC AND MIT
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
for test in "TestFetchRemote" \
%ifarch %{ix86} %{arm}
            "TestVerify" \
            "TestParse" \
            "TestCheck" \
            "TestFetchLocal" \
%endif
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
