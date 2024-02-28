%global octpkg dicom

Name:           octave-%{octpkg}
Version:        0.6.0
Release:        %autorelease
Summary:        Dicom processing for Octave
License:        GPL-3.0-or-later
URL:            https://gnu-octave.github.io/packages/dicom/
Source0:        https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  octave-devel
BuildRequires:  gdcm-devel
BuildRequires:  libappstream-glib

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
The Octave-forge Image package provides functions for processing 
Digital communications in medicine (DICOM) files.

%prep
%autosetup -n %{octpkg}-%{version}

%build
# Tell it where gdcm headers are
export GDCM_CXXFLAGS="-I%{_includedir}/gdcm/"
%octave_pkg_build

%install
%octave_pkg_install
# Remove unneeded files that depends on python
rm %{buildroot}%{octpkgdir}/doc/mk*.py

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%{octpkgdir}/
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
