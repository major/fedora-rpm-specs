%global octpkg doctest

Name:           octave-%{octpkg}
Version:        0.8.0
Release:        %autorelease
Summary:        Documentation tests for Octave
License:        BSD-3-Clause AND FSFAP
URL:            https://octave.sourceforge.io/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  octave-devel
BuildRequires:  texinfo >= 6.0

Requires:       octave(api) = %{octave_api}
Requires:       texinfo >= 6.0
Requires(post): octave
Requires(postun): octave


%description
The Octave-forge Doctest package finds specially-formatted blocks of
example code within documentation files.  It then executes the code
and confirms the output is correct.  This can be useful as part of a
testing framework or simply to ensure that documentation stays
up-to-date during software development.

%prep
%setup -q -n %{octpkg}-%{version}

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
%dir %{octpkgdir}
%{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/private
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%doc %{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/*.m
%{_metainfodir}/octave-%{octpkg}.metainfo.xml


%changelog
%autochangelog
