%global octpkg datatypes

Name:           octave-%{octpkg}
Version:        1.2.0
Release:        %autorelease
Summary:        Extra data types for GNU Octave

# the package's logo ('doc/datatypes.png') is licensed under a Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0)
# inst/tzdata/leap-seconds.list (Public Domain)
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://gnu-octave.github.io/packages/datatypes/
Source0:        https://github.com/pr0m1th3as/datatypes/releases/download/release-%{version}/datatypes-%{version}.tar.gz
# Use system date-tz library
Patch:          octave-datatypes-tz.patch

BuildRequires:  gcc-c++
BuildRequires:  octave-devel
BuildRequires:  date-devel
Requires(post): octave
Requires(postun): octave

%description
Extra data types for GNU Octave.


%prep
%autosetup -p1 -n %{octpkg}-release-%{version}
rm -r src/date src/tz.cpp

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
export TZ=UTC
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license inst/tzdata/LICENSE
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/@cell/
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%{octpkgdir}/demos/
%{octpkgdir}/patients.mat
%{octpkgdir}/tests/
%{octpkgdir}/tzdata/
%doc %{octpkgdir}/doc-cache
%doc %{octpkgdir}/doc/
%dir %{octpkgdir}/packinfo
%doc %{octpkgdir}/packinfo/doc-cache
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/on_uninstall.m
%{octpkgdir}/private/

%changelog
%autochangelog
