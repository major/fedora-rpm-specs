%global octpkg io

Name:           octave-%{octpkg}
Version:        2.7.1
Release:        %autorelease
Summary:        Input/Output in external formats
# inst/pch2mat.m is BSD-2-Clause
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            http://octave.sourceforge.net/%{octpkg}/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 6:4.0
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Input/Output in external formats.

%prep
%setup -qcT

%build
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
%{_metainfodir}/io.sourceforge.octave.io.metainfo.xml
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%doc %{octpkgdir}/doc/
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%{octpkgdir}/private/
%{octpkgdir}/templates/


%changelog
%autochangelog
