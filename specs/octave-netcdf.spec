%global octpkg netcdf

Name:           octave-%{octpkg}
Version:        1.0.19
Release:        %autorelease
Summary:        A MATLAB compatible NetCDF interface for Octave
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gnu-octave.githun.io/packages/%{octpkg}/
Source0:        https://github.com/gnu-octave/octave-%{octpkg}/releases/download/v%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  octave-devel
BuildRequires:  netcdf-devel

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
A MATLAB compatible NetCDF interface for Octave.

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%conf
cd src
# Needed to fix C++ flag detection
autoreconf -f

%build
%octave_pkg_build

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
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc/
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/+netcdf/
%{octpkgdir}/packinfo
%{octpkgdir}/private/
%{_metainfodir}/octave-%{octpkg}.metainfo.xml

%changelog
%autochangelog
