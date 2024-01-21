%global packname rjson
%global packver 0.2.21

Name:             R-%{packname}
Version:          %{packver}
Release:          5%{?dist}
Source0:          %{url}&version=%{version}#/%{packname}_%{packver}.tar.gz
License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Summary:          JSON for R
BuildRequires:    R-devel >= 3.1.0, tex(latex)

%description
Converts R object into JSON objects and vice-versa.

%prep
%setup -q -c -n %{packname}

# come on osx developer
sed -i 's|/usr/bin/r|/usr/bin/Rscript|g' %{packname}/inst/rpc_server/server.r

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

chmod +x %{buildroot}%{_libdir}/R/library/rjson/rpc_server/server.r
chmod +x %{buildroot}%{_libdir}/R/library/rjson/rpc_server/start_server

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/changelog.txt
%doc %{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/rpc_server
%{_libdir}/R/library/%{packname}/unittests

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.2.21-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraproject.org> 0.2.21-1
- update to 0.2.21
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.20-2
- use buildroot macro
- fix url and source0
- use Rscript for the script
- drop unnecessary gcc-c++ Requires, pulled in by R-devel

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.2.20-1
- initial package
