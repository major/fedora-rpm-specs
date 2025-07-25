# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/golang/sys
%global goipath         golang.org/x/sys
%global forgeurl        https://github.com/golang/sys
Version:                0.34.0

%gometa

%global common_description %{expand:
Go packages for low-level interactions with the operating system.}

%global golicenses      LICENSE PATENTS
%global godocs          AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md

# Add Windows file to compile Winio
%global gosupfiles ${windows[@]}

Name:           %{goname}
Release:        %autorelease
Summary:        Go packages for low-level interaction with the operating system

License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
# Add Windows file to compile Winio
mapfile -t windows <<< $(find *_windows.go -type f)
%gopkginstall

%if %{with check}
%check
for test in "TestOpenByHandleAt" \
            "TestIoctlFileDedupeRange" \
; do
    awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
