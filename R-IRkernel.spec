%global packname IRkernel
%global packver  1.3
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Summary:          Native R Kernel for the 'Jupyter Notebook'

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Use-noarch-R-path-in-kernelspec.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-repr >= 0.4.99, R-methods, R-evaluate >= 0.10, R-IRdisplay >= 0.3.0.9999, R-pbdZMQ >= 0.2-1, R-crayon, R-jsonlite >= 0.9.6, R-uuid, R-digest
# Suggests:  R-testthat, R-roxygen2
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         python-jupyter-filesystem
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-repr >= 0.4.99
BuildRequires:    R-methods
BuildRequires:    R-evaluate >= 0.10
BuildRequires:    R-IRdisplay >= 0.3.0.9999
BuildRequires:    R-pbdZMQ >= 0.2.1
BuildRequires:    R-crayon
BuildRequires:    R-jsonlite >= 0.9.6
BuildRequires:    R-uuid
BuildRequires:    R-digest
BuildRequires:    R-testthat
BuildRequires:    R-roxygen2
BuildRequires:    python3dist(jupyter-kernel-test)
BuildRequires:    python3dist(ndjson-testrunner)

%description
The R kernel for the 'Jupyter' environment executes R code which the front-end
('Jupyter Notebook' or other front-ends) submits to the kernel via the network.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1

# Remove bundled Python code
rm -r tests/testthat/jkt
rm -r tests/testthat/njr
rm -r tests/testthat/__pycache__
sed -i -e '/jkt/d' -e '/__pycache__/d' MD5
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Install the kernel spec, too.
R_LIBS_USER=%{buildroot}%{rlibdir} \
    Rscript -e 'IRkernel::installspec(prefix = "%{buildroot}%{_prefix}")'


%check
# lots of test failures (FAIL 16)
%if 0
NOT_CRAN=true \
    %{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{packname}/README.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/kernelspec
%{_datadir}/jupyter/kernels/ir


%changelog
* Sun Sep 04 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.3-1
- R 4.2.1, update to 1.3

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.2-1
- update to 1.2
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-2
- Make path to R in kernelspec truly noarch

* Thu May 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Tue Apr 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.15-1
- initial package for Fedora
