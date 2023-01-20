%global packname  scatterplot3d
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.41
Release:          17%{?dist}
Summary:          3D Scatter Plot

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_0.3-41.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grDevices R-graphics R-stats
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch

BuildRequires:    R-devel tex(latex)
BuildRequires:    R-grDevices R-graphics R-stats

%description
Plots a three dimensional (3D) point cloud.


%prep
%setup -q -c -n %{packname}

# Fix encoding.
iconv --from=latin1 --to=UTF-8 %{packname}/inst/CITATION > CITATION.new && \
touch -r %{packname}/inst/CITATION CITATION.new && \
mv CITATION.new %{packname}/inst/CITATION
sed -i 's/latin1/UTF-8/g' %{packname}/DESCRIPTION


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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/po
%lang(en) %{rlibdir}/%{packname}/po/en/
%lang(de) %{rlibdir}/%{packname}/po/de/


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> - 0.3.41-16
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 0.3.41-12
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.41-9
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.41-7
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.41-3
- Fix unowned directory

* Sun Mar 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.41-2
- Correct encoding of citation file
- Install language files correctly

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.41-1
- initial package for Fedora
