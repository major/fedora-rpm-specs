# Generated by go2rpm 1.15.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%global gosupfiles metadecoder_iptc_fields.json

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/bep/imagemeta
%global goipath         github.com/bep/imagemeta
Version:                0.8.3

%gometa -L -f

%global common_description %{expand:
Go library for reading EXIF, IPTC and XMP image meta data.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-bep-imagemeta
Release:        %autorelease
Summary:        Go library for reading EXIF, IPTC and XMP image meta data

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
