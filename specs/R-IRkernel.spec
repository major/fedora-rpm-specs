Name:           R-IRkernel
Version:        %R_rpm_version 1.3.2
Release:        %autorelease
Summary:        Native R Kernel for the 'Jupyter Notebook'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  python3dist(jupyter-kernel-test)
BuildRequires:  python3dist(ndjson-testrunner)
Requires:       python-jupyter-filesystem

%description
The R kernel for the 'Jupyter' environment executes R code which the front-end
('Jupyter Notebook' or other front-ends) submits to the kernel via the network.

%prep
%autosetup -c
# Remove bundled Python code
rm -r IRkernel/tests/testthat/{jkt,njr}

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files
# Install the kernel spec, too.
R_LIBS_USER=%{buildroot}%{_R_libdir} \
    Rscript -e 'IRkernel::installspec(prefix = "%{buildroot}%{_prefix}")'

%check
%R_check

%files -f %{R_files}
%{_datadir}/jupyter/kernels/ir

%changelog
%autochangelog
