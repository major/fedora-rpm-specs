# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/apparentlymart/go-textseg
%global goipath         github.com/apparentlymart/go-textseg/v15
Version:                15.0.0

%gometa -f


%global common_description %{expand:
Go implementation of Unicode Text Segmentation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-apparentlymart-textseg-15
Release:        %autorelease
Summary:        Go implementation of Unicode Text Segmentation

License:        Apache-2.0 AND MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

rm -rfv autoversion

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
