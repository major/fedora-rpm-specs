# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/integrii/flaggy
%global goipath         github.com/integrii/flaggy
Version:                1.5.2

%gometa -f


%global common_description %{expand:
Idiomatic Go input parsing with subcommands, positional values, and flags at
any position. No required project or package layout and no external
dependencies.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Idiomatic Go input parsing library

License:        Unlicense
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
