%global packname  argon2
%global rlibdir  %{_libdir}/R/library

# Even if I update libargon2 to 20190702 && hack it to export the symbol for secure_wipe_memory
# this package fails its tests when built against system argon2 and b2.
# Feel free to fix this so we can use the system copies.
# 2022-08-02 spot@fedoraproject.org
%bcond_without bundled

Name:             R-%{packname}
Version:          0.4.0
Release:          10%{?dist}
Summary:          Secure Password Hashing

# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_0.4-0.tar.gz
Patch0001:        0001-Build-against-system-libraries-0.4.0.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel tex(latex)
%if %{with bundled}
Provides:         bundled(libargon2) = 20190702
Provides:         bundled(libb2)
%else
BuildRequires:    libargon2-devel >= 20190702
BuildRequires:    libb2-devel
%endif

%description
Utilities for secure password hashing via the argon2 algorithm. It is a
relatively new hashing algorithm and is believed to be very secure. The
'argon2' implementation included in the package is the reference
implementation.  The package also includes some utilities that should be
useful for digest authentication, including a wrapper of 'blake2b'.  For
similar R packages, see sodium and 'bcrypt'.  See
<https://en.wikipedia.org/wiki/Argon2> or
<https://eprint.iacr.org/2015/430.pdf> for more information.


%prep
%setup -q -c -n %{packname}

# Delete bundled libraries.
%if !%{with bundled}
pushd %{packname}
rm -r src/argon2
%patch -P0001 -p1
popd
%endif


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/COPYRIGHTS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.4.0-7
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.4.0-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Tom Callaway <spot@fedoraproject.org> - 0.4.0-1
- update to 0.4-0
- rebuild for R 4.2.1
- use bundled bits

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.0-12
- rebuild for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.og> - 0.2.0-9
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-7
- rebuilt

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Remi Collet <remi@fedoraproject.org> - 0.2.0-5
- rebuild for libargon2 new soname

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.2.0-2
- rebuild for R 3.5.0

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.2.0-1
- initial package for Fedora
