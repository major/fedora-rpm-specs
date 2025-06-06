# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/GoKillers/libsodium-go
%global goipath         github.com/GoKillers/libsodium-go
Version:                0.4~beta
%global tag             v0.4-beta

%gometa -f

%global common_description %{expand:
A complete overhaul of the Golang wrapper for libsodium.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A complete overhaul of the Golang wrapper for libsodium

License:        ISC
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  libsodium-devel

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
