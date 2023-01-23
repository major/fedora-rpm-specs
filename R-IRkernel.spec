%global packname IRkernel
%global packver  1.3.2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
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
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

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
# rm -r tests/testthat/__pycache__
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
NOT_CRAN=true \
    %{_bindir}/R CMD check %{packname}

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
%autochangelog
