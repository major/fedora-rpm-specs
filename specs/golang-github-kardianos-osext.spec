# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/kardianos/osext
%global goipath         github.com/kardianos/osext
%global commit          2bc1f35cddc0cc527b4bc3dce8578fc2a6c11384

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-bitbucket-kardianos-osext-devel < 0-0.25
}

%global goaltipaths     bitbucket.org/kardianos/osext

%global common_description %{expand:
Find the current Executable and ExecutableFolder.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Extensions to the standard "os" package

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}
# Disable TestExecutableDelete test
Patch0:         0001-disable-broken-test.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
