# Generated by go2rpm 1.8.0
%bcond_without check
%global debug_package %{nil}

# https://gitlab.com/cznic/sortutil
%global goipath         modernc.org/sortutil
%global forgeurl        https://gitlab.com/cznic/sortutil
Version:                1.2.0
%global tag             v%{version}

%gometa

%global common_description %{expand:
Utilities supplemental to the Go standard "sort" package.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README

Name:           %{goname}
Release:        %autorelease
Summary:        Utilities supplemental to the Go standard "sort" package

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

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