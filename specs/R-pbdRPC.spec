%global packname  pbdRPC
%global packvers  0.2-1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2.1
Release:          24%{?dist}
Summary:          Programming with Big Data -- Remote Procedure Call

# NOTE: There is a bundled copy of putty which is MIT, but we disable its usage
# in favor of ssh.
License:          MPL-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packvers}.tar.gz
# https://github.com/snoweye/pbdRPC/pull/7
Patch0001:        fix-configure.patch

# Here's the R view of the dependencies world:
# Depends:   R-tools
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         openssh-clients
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-tools
BuildRequires:    openssh-clients

%description
A very light implementation yet secure for remote procedure calls with
unified interface via ssh (OpenSSH).


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1

# Remove all arch-requiring bits, as they are unnecessary.
sed -i '/NeedsCompilation/s/yes/no/' DESCRIPTION
rm -r configure* src
sed -i '/src/d' MD5
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# Remove unused license (it's installed even if option is disabled.)
rm %{buildroot}%{rlibdir}/%{packname}/putty_LICENCE


%check
%{_bindir}/R CMD check %{packname}


%files
%license %{packname}/COPYING
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.1-22
- R-maint-sig mass rebuild

* Sat Apr 13 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.1-21
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.1-17
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 03 2022 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.1-15
- R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.1-11
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.2.1-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-2
- Fix package's no-arch-ness

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Wed Mar 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-1
- Update to latest release.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-7
- Fix path to license file.

* Tue Aug 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-6
- Add license file to rpm.

* Tue Aug 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-5
- Add R-core Require for noarch package.

* Fri Aug 25 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-4
- Install to correct noarch directory, but simpler.

* Fri Aug 25 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-3
- Install into correct noarch directory.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-2
- Fix configuration options.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-1
- initial package for Fedora
