%global octpkg dicom

Name:           octave-%{octpkg}
Version:        0.4.1
Release:        %autorelease
Summary:        Dicom processing for Octave
License:        GPLv3+
URL:            http://octave.sourceforge.net/dicom/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

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

# Remove unneeded file that depends on python2
rm -f doc/mkfuncdocs.py

%build
# Tell it where gdcm headers are
export GDCM_CXXFLAGS="-I%{_includedir}/gdcm/"
%octave_pkg_build

%install
%octave_pkg_install

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
