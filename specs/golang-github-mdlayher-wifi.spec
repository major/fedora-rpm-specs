# Generated by go2rpm 1.10.0
# Needs netlink
%bcond_with check
%global debug_package %{nil}

# https://github.com/mdlayher/wifi
%global goipath         github.com/mdlayher/wifi
Version:                0.2.0

%gometa -L -f


%global common_description %{expand:
Package wifi provides access to IEEE 802.11 WiFi device actions and statistics.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           golang-github-mdlayher-wifi
Release:        %autorelease
Summary:        Access to IEEE 802.11 WiFi device actions and statistics

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