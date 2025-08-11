%global octpkg image

Name:           octave-%{octpkg}
Version:        2.16.1
Release:        %autorelease
Summary:        Image processing for Octave
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://octave.sourceforge.net/image/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 6:4.0.0

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave


%description
The Octave-forge Image package provides functions for processing images.
The package also provides functions for feature extraction, image
statistics, spatial and geometric transformations, morphological
operations, linear filtering, and much more.

%prep
%setup -qcT

%build
#export CXXFLAGS="%{optflags} -fPIC"
export XTRA_CXXFLAGS="-fPIC"
%octave_pkg_build -T

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%{octpkgdir}/private/
%{octpkgdir}/@imref2d/
%{octpkgdir}/@imref3d/
%{octpkgdir}/@strel/
%{_metainfodir}/io.sourceforge.octave.%{octpkg}.metainfo.xml


%changelog
%autochangelog
