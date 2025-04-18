# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/gohugoio/hugo-goldmark-extensions
%global goipath         github.com/gohugoio/hugo-goldmark-extensions
Version:                0.3.0
%global tag             passthrough/v0.3.0
%global distprefix      %{nil}

%gometa -L -f

%global common_description %{expand:
A collection of Goldmark extensions created by the Hugo community.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-gohugoio-hugo-goldmark-extensions
Release:        %autorelease
Summary:        A collection of Goldmark extensions created by the Hugo community

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
# passthrough: fails on Rawhide.
%gocheck \
	-d passthrough
%endif

%gopkgfiles

%changelog
%autochangelog
