%global modname ipykernel

# When we bootstrap new Python, we need to avoid a build dependnecy loop
%bcond bootstrap 0
%bcond tests %{without bootstrap}

Name:           python-%{modname}
Version:        6.29.3
Release:        %autorelease
Summary:        IPython Kernel for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/%{modname}
Source0:        https://github.com/ipython/%{modname}/releases/download/v%{version}/%{modname}-%{version}.tar.gz

# Compatibility with pytest 8
Patch:          https://github.com/ipython/ipykernel/commit/a7d66a.patch
# Avoid a DeprecationWarning on Python 3.13+
Patch:          https://github.com/ipython/ipykernel/pull/1248.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description \
This package provides the IPython kernel for Jupyter.

%description %{_description}

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
Requires:       python-jupyter-filesystem

# We removed the -doc subpackage for Fedora 42.
Obsoletes:      python-ipykernel-doc < 6.29.3-8

Recommends:     python%{python3_pkgversion}-matplotlib
Recommends:     python%{python3_pkgversion}-numpy
Recommends:     python%{python3_pkgversion}-pandas
Recommends:     python%{python3_pkgversion}-scipy
Recommends:     python%{python3_pkgversion}-pillow

%description -n python%{python3_pkgversion}-%{modname} %{_description}

%prep
%autosetup -p1 -n %{modname}-%{version}

# Remove the dependency on debugpy.
# See https://github.com/ipython/ipykernel/pull/767
sed -i '/"debugpy/d' pyproject.toml

# Remove test dependencies on pre-commit (used for linting) and pytest-cov; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
sed -i -r '/"(pre-commit|pytest-cov)/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname} %{modname}_launcher

# Install the kernel so it can be found
# See https://bugzilla.redhat.com/show_bug.cgi?id=1327979#c19
%{python3} -m ipykernel install --prefix %{buildroot}%{_prefix}
ls %{buildroot}%{_datadir}/jupyter/kernels/python3/
cat %{buildroot}%{_datadir}/jupyter/kernels/python3/kernel.json


%check
%if %{with tests}
%pytest -Wdefault
%else
# datapub, pickleutil, serialize need ipyparallel
# pylab needs matplotlib
# trio needs trio
# debugger needs debugpy
# gui needs gobject
%{pyproject_check_import \
    -e %{modname}.datapub -e %{modname}.pickleutil -e %{modname}.serialize \
    -e '%{modname}.pylab*' \
    -e '%{modname}.trio*' \
    -e %{modname}.debugger \
    -e '%{modname}.gui*' \
    -e '*.test*'}
%endif


%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc CONTRIBUTING.md README.md
%{python3_sitelib}/%{modname}
%pycached %{python3_sitelib}/%{modname}_launcher.py
%{python3_sitelib}/%{modname}*.dist-info/
%{_datadir}/jupyter/kernels/python3


%changelog
%autochangelog
