%global packname Rhtslib
%global rlibdir %{_libdir}/R/library

Name:		R-%{packname}
Version:	2.4.1
Release:	3%{dist}
Summary:	HTSlib high-throughput sequencing library as an R package
License:	LGPL-2.0-or-later
URL:		http://www.bioconductor.org/packages/release/bioc/html/Rhtslib.html
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Patch0:		R-Rhtslib-zlibbioc.patch
Patch1:		R-Rhtslib-buildroot-fix.patch
BuildRequires:	R-devel >= 3.0.0 bzip2-devel zlib-devel xz-devel libcurl-devel

%description
This package provides version 1.7 of the 'HTSlib' C library for
high-throughput sequence analysis. The package is primarily useful to
developers of other R packages who wish to make use of HTSlib. Motivation and
instructions for use of this package are in the vignette,
vignette(package="Rhtslib", "Rhtslib").

%package devel
Summary:	Development files for R-Rhtslib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}

%description devel
Development files for R-Rhtslib.

%prep
%setup -q -c -n %{packname}
pushd %{packname}
%patch -P0 -p1
%patch -P1 -p1
popd

%build

%install
mkdir -p %{buildroot}%{rlibdir}
R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
# Missing R-BiocStyle
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{rlibdir}/%{packname}/
%doc %{rlibdir}/%{packname}/doc/
%doc %{rlibdir}/%{packname}/html/
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/testdata/
%{rlibdir}/%{packname}/libs/
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/usrlib/
%{rlibdir}/%{packname}/usrlib/*.so*

%files devel
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/usrlib/*.a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.1-1
- Update to latest version

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.28.0-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.28.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.28.0-1
- update to 1.28.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 1.24.0-1
- update to 1.24.0
- rebuild for R 4.1.0

* Thu Feb  4 2021 Tom Callaway <spot@fedoraproject.org> - 1.22.0-1
- update to 1.22.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.20.0-1
- update to 1.20.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Tom Callaway <spot@fedoraproject.org> - 1.18.0-1
- update to 1.18.0

* Wed Oct 30 2019 Tom Callaway <spot@fedoraproject.org> - 1.16.3-1
- initial package
