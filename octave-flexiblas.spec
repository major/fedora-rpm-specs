%global octpkg flexiblas
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$

Name:           octave-%{octpkg}
Version:        3.2.1
Release:        2%{?dist}
Summary:        FlexiBLAS API Interface for Octave
License:        GPLv3+
URL:            https://www.mpi-magdeburg.mpg.de/projects/%{octpkg}
Source0:        https://github.com/mpimd-csc/%{octpkg}/releases/download/v%{version}/%{octpkg}-octave-%{version}.tar.gz

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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Fri Jun 03 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.0-2
- Rebuild for octave 7.1

* Sat May 21 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Fri Feb 25 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Wed Jan 19 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2

* Wed Aug 18 2021 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-6
- Rebuilt for new octave API

* Mon Aug 16 2021 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-5
- Rebuilt for new octave API

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Iñaki Úcar <iucar@fedoraproject.org> 3.0.0-2
- https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot

* Sat Sep 19 2020 Iñaki Úcar <iucar@fedoraproject.org> 3.0.0-1
- Initial Fedora package
