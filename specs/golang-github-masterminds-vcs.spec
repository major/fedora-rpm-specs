# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/Masterminds/vcs
%global goipath         github.com/Masterminds/vcs
Version:                1.13.1

%gometa

%global common_description %{expand:
Package Vcs provides the ability to work with varying version control systems
(VCS), also known as source control systems (SCM) though the same interface.}

%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        %autorelease
Summary:        VCS Repo management through a common interface in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  bzr

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
# .: needs network
%gocheck -d .
%endif

%gopkgfiles

%changelog
%autochangelog