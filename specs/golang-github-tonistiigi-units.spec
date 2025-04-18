# Generated by go2rpm 1.8.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/tonistiigi/units
%global goipath         github.com/tonistiigi/units
%global commit          6950e57a87eaf136bbe44ef2ec8e75b9e3569de2

%gometa

%global common_description %{expand:
This package implements types that can be used in stdlib formatting functions
like fmt.Printf to control the output of the expected printed string.

Floating point flags %f and %g print the value in using the correct unit suffix.
Decimal units are default, # switches to binary units. If a value is best
represented as full bytes, integer bytes are printed instead.}

%global golicenses      LICENSE
%global godocs          readme.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        None

License:        MIT
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
