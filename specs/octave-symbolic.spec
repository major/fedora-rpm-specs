%global octpkg symbolic

# Disable automatic compilation of Python files in extra directories
%global _python_bytecompile_extra 0

Name:           octave-%{octpkg}
Version:        3.2.2
Release:        %autorelease
Summary:        Symbolic computations for Octave
License:        GPL-3.0-or-later AND FSFAP
URL:            https://gnu-octave.github.io/packages/%{octpkg}
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  octave-devel
BuildRequires:  octave-doctest >= 0.8.0
BuildRequires:  python3
BuildRequires:  python3-packaging
BuildRequires:  python%{python3_pkgversion}-sympy >= 1.5.1

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       python%{python3_pkgversion}-sympy >= 1.5.1


%description
Adds symbolic calculation features to GNU Octave.
These include common Computer Algebra System tools such as algebraic
operations, calculus, equation solving, Fourier and Laplace transforms,
variable precision arithmetic and other features.

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check

# "octave_pkg_check" macro uses "runtests" which doesn't test classes
pushd %{buildroot}/%{octpkgdir}
%octave_cmd r=octsympy_tests; if r, type fntests.log; end; exit(r)
rm -f fntests.log
%octave_cmd pkg load doctest; syms x; r=doctest("."); exit(~r)
popd

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/*.tst
%{octpkgdir}/@logical
%{octpkgdir}/private
%{octpkgdir}/@sym
%{octpkgdir}/@symfun
%{octpkgdir}/@double
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%doc %{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/*.m
%{_metainfodir}/io.github.gnu_octave.%{octpkg}.metainfo.xml

%changelog
%autochangelog
