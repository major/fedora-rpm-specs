# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/bmizerany/assert
%global goipath         github.com/bmizerany/assert
%global commit          b7ed37b82869576c289d7d97fb2bbd8b64a0cb28

%gometa

%global common_description %{expand:
Assertions for Go tests.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Assertions for Go tests

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml
Patch0:         add-license.patch

BuildRequires:  golang(github.com/kr/pretty)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1
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