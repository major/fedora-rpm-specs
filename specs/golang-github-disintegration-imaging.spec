# Generated by go2rpm
%ifnarch aarch64 ppc64le s390x
%bcond_without check
%endif

%global debug_package %{nil}

# https://github.com/disintegration/imaging
%global goipath         github.com/disintegration/imaging
Version:                1.6.2

%gometa

%global common_description %{expand:
Package imaging provides basic image processing functions (resize, rotate, crop,
brightness/contrast adjustments, etc.).

All the image processing functions provided by the package accept any image type
that implements image.Image interface as an input, and return a new image of
*image.NRGBA type (32bit RGBA colors, non-premultiplied alpha).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Simple image processing package for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/image/bmp)
BuildRequires:  golang(golang.org/x/image/tiff)

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|\r||g' README.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
