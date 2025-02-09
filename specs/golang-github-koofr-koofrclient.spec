# Generated by go2rpm 1.9.0
# Requires KOOFR_APIBASE and tests not updated to code changes
%bcond_with check
%global debug_package %{nil}

# https://github.com/koofr/go-koofrclient
%global goipath         github.com/koofr/go-koofrclient
%global commit          cbd7fc9ad6a6cabae8df569f5d2be0e68e571a45

%gometa -f


%global common_description %{expand:
Go Koofr client.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Go Koofr client

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
