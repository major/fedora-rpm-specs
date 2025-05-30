# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/rsc/qr
%global goipath         rsc.io/qr
%global forgeurl        https://github.com/rsc/qr
Version:                0.2.0
%global commit          b6857d426aa506d5bf7efb8f73928d72bcf4e73d

%gometa

%global common_description %{expand:
Golang generator of QR codes.}

%global godocs        README.md
%global golicenses    LICENSE

%global godevelheader %{expand:
Requires:       pkgconfig(libqrencode)
}

Name:           %{goname}
Release:        %autorelease
Summary:        Golang generator of QR codes

License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  pkgconfig(libqrencode)

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
# https://github.com/rsc/qr/issues/5
# Release Note:
# The internal representation of the output code has been slightly changed - the
# second bit from LSB side now represents; 1:ECC bit / 0:data bit. This change is
# only for debug purposes and does not affect user applications.
rm -rfv coding/qr_test.go
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog