%global octpkg statistics

Name:           octave-%{octpkg}
Version:        1.7.3
Release:        %autorelease
Summary:        Additional statistics functions for Octave
License:        GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/gnu-octave/%{octpkg}
Source0:        https://github.com/gnu-octave/%{octpkg}/archive/refs/tags/release-%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel
BuildRequires:  octave-io
Requires:       octave(api) = %{octave_api}
Requires:       octave-io
Requires(post): octave
Requires(postun): octave

# Built out of boulddir
%undefine _debugsource_packages

%description
Additional statistics functions for Octave.


%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install
chmod a-x %{buildroot}/%{octpkgdir}/*.m

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%doc %{octpkgdir}/doc/
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%{octpkgdir}/*.m
%{octpkgdir}/@cvpartition/
%{octpkgdir}/Classification/
%{octpkgdir}/Clustering/
%{octpkgdir}/datasets/
%{octpkgdir}/dist_fit/
%{octpkgdir}/dist_fun/
%{octpkgdir}/dist_obj/
%{octpkgdir}/dist_stat/
%{octpkgdir}/dist_wrap/
%{octpkgdir}/private/*.m
%{octpkgdir}/packinfo/
%{octpkgdir}/Regression/
%{octpkgdir}/shadow9/
%{octpkglibdir}/


%changelog
%autochangelog
