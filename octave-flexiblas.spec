%global octpkg flexiblas
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$

Name:           octave-%{octpkg}
Version:        3.4.1
Release:        %autorelease
Summary:        FlexiBLAS API Interface for Octave
License:        GPL-3.0-or-later
URL:            https://www.mpi-magdeburg.mpg.de/projects/%{octpkg}
Source0:        %{octpkg}-octave-%{version}.tar.gz
# Generated using create-oct-package.sh from:
# Source1:        https://github.com/mpimd-csc/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  octave-devel >= 5.1.0
BuildRequires:  flexiblas-devel >= 3.0.0
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
FlexiBLAS is a BLAS wrapper library which allows to change the BLAS
without recompiling the programs.

%prep
%setup -q -n %{octpkg}-octave

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING

%changelog
%autochangelog
