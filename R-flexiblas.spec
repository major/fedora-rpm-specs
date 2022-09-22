%global packname flexiblas
%global rlibdir %{_libdir}/R/library

Name:           R-%{packname}
Version:        3.1.0
Release:        3%{?dist}
Summary:        FlexiBLAS API Interface for R

License:        GPLv3+
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel
BuildRequires:  flexiblas-devel >= 3.0.0
BuildRequires:  R-tinytest

%description
Provides functions to switch the BLAS/LAPACK optimized backend and
change the number of threads without leaving the R session, which needs
to be linked against the FlexiBLAS wrapper library
<https://www.mpi-magdeburg.mpg.de/projects/flexiblas>.

%prep
%setup -q -c -n %{packname}
# use system-provided headers and libraries
rm -f %{packname}/src/flexiblas*
sed -i 's/"flexiblas_api.h"/<flexiblas_api.h>/' %{packname}/src/wrapper.c
%global flags PKG_LIBS=$(pkg-config --libs flexiblas_api) \\\
              PKG_CFLAGS=$(pkg-config --cflags flexiblas_api)

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{flags} %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export LANG=C.UTF-8
%{flags} %{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/tinytest

%changelog
* Thu Aug  4 2022 Tom Callaway <spot@fedoraproject.org> - 3.1.0-3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 26 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-5
- Fix test

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 3.0.0-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.0-1
- Initial Fedora package
