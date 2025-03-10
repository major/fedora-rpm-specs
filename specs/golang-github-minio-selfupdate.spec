# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/minio/selfupdate
%global goipath         github.com/minio/selfupdate
Version:                0.6.0

%gometa -f


%global common_description %{expand:
Build self-updating Go programs.}

%global golicenses      NOTICE LICENSE.minisig LICENSE\\\
                        LICENSE-binarydist LICENSE-osext
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Build self-updating Go programs

# Main library: Apache-2.0
# internal/binarydist: MIT
# internal/osext: BSD-3-Clause
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  bsdiff

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
mv internal/binarydist/License LICENSE-binarydist
mv internal/osext/LICENSE LICENSE-osext

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
