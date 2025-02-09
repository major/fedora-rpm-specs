# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/ghemawat/stream
%global goipath         github.com/ghemawat/stream
%global commit          696b145b53b9611fe9c9f189122f990171e391a0

%gometa

%global common_description %{expand:
Package stream provides filters that can be chained together in a manner
similar to Unix pipelines.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Filters that can be chained together similar to Unix pipelines

License:        Apache-2.0
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
rm -rfv stream_test.go
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog