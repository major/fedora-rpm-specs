%global packname timeSeries
%global packver  4030.106
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((PerformanceAnalytics|fTrading|robustbase|xts)\\)

# Not available yet or heavy dependencies.
%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          7%{?dist}
Summary:          Financial Time Series Objects (Rmetrics)

License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        fix-FSF-address.patch

# Here's the R view of the dependencies world:
# Depends:   R-timeDate >= 2150.95
# Imports:   R-graphics, R-grDevices, R-stats, R-methods, R-utils
# Suggests:  R-RUnit, R-robustbase, R-xts, R-PerformanceAnalytics, R-fTrading
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-timeDate >= 2150.95
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-stats
BuildRequires:    R-methods
BuildRequires:    R-utils
%if %{with_suggests}
BuildRequires:    R-RUnit
BuildRequires:    R-robustbase
BuildRequires:    R-xts
BuildRequires:    R-PerformanceAnalytics
BuildRequires:    R-fTrading
%endif

%description
'S4' classes and various tools for financial time series: Basic functions such
as scaling and sorting, subsetting, mathematical operations and statistical
functions.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1

# Fix line endings.
for file in inst/doc/timeSeriesPlot.R*; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname} --no-vignettes --no-manual
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-vignettes --no-manual
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%license %{rlibdir}/%{packname}/COPYING
%license %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extensionsTests
%{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/*pkgdown.yml
%{rlibdir}/%{packname}/extdata

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4030.106-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4030.106-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 4030.106-5
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4030.106-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4030.106-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4030.106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 26 2023 Tom Callaway <spot@fedoraproject.org> - 4030.106-1
- update to 4030.106

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 4021.105-1
- R-maint-sig mass rebuild
- Update to latest version

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4021.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 4021.104-1
- update to 4021.104
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3062.100-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3062.100-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3062.100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 3062.100-5
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3062.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3062.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 3062.100-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3062.100-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3042.102-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3042.102-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3042.102-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3042.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3042.102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3042.102-2
- Fix some file line endings
- Fix FSF address

* Tue Jun 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3042.102-1
- initial package for Fedora
