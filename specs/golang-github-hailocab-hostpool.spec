# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/hailocab/go-hostpool
%global goipath         github.com/hailocab/go-hostpool
%global commit          e80d13ce29ede4452c43dea11e79b9bc8a15b478

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-hailocab-go-hostpool-devel < 0-0.5
Obsoletes:      golang-github-hailocab-go-hostpool-unit-test-devel < 0-0.5
}

%global common_description %{expand:
A Go package to intelligently and flexibly pool among multiple hosts from your
Go application. Host selection can operate in round robin or epsilon greedy
mode, and unresponsive hosts are avoided.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Intelligently and flexibly pool among multiple hosts from your go application

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Fix import path
Patch0:         go-hostpool-test.patch

%if %{with check}
# Tests
BuildRequires:  golang(github.com/bmizerany/assert)
%endif

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