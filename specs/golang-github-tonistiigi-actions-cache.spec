# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/tonistiigi/go-actions-cache
%global goipath         github.com/tonistiigi/go-actions-cache
%global commit          0bdeb6e1eac762aa4c57a3e8ccc2fdfb68a3f3c4

%gometa

%global common_description %{expand:
Github Actions Cache service API.}

%global godocs          api.md
%global golicenses          LICENSE

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Github Actions Cache service API

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  openssl

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
