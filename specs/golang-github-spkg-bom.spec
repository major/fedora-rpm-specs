# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/spkg/bom
%global goipath         github.com/spkg/bom
Version:                1.0.0

%gometa -f

%global common_description %{expand:
Strip UTF-8 byte order marks.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Strip UTF-8 byte order marks

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

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
