# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/nightlyone/lockfile
%global goipath         github.com/nightlyone/lockfile
Version:                1.0.0

%gometa

%global common_description %{expand:
Handle locking via pid files.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        %autorelease
Summary:        Handle locking via pid files

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

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
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog