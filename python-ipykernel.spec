%global modname ipykernel

# When we bootstrap new Python, we need to avoid a build dependnecy loop
%bcond_without tests
%bcond_without doc

Name:           python-%{modname}
Version:        6.25.1
Release:        %autorelease
Summary:        IPython Kernel for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/%{modname}
Source0:        https://github.com/ipython/%{modname}/releases/download/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description \
This package provides the IPython kernel for Jupyter.

%description %{_description}

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
Requires:       python-jupyter-filesystem

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinxcontrib-github-alt
BuildRequires:  python3-myst-parser
BuildRequires:  python3-pydata-sphinx-theme
# for intersphinx:
BuildRequires:  python%{python3_pkgversion}-docs
BuildRequires:  python%{python3_pkgversion}-ipython-doc
BuildRequires:  python-jupyter-client-doc
%endif

Recommends:     python%{python3_pkgversion}-matplotlib
Recommends:     python%{python3_pkgversion}-numpy
Recommends:     python%{python3_pkgversion}-pandas
Recommends:     python%{python3_pkgversion}-scipy
Recommends:     python%{python3_pkgversion}-pillow

%description -n python%{python3_pkgversion}-%{modname} %{_description}

%if %{with doc}
%package doc
Summary:        Documentation for %{name}
Requires:       python%{python3_pkgversion}-docs
Requires:       python%{python3_pkgversion}-ipython-doc
Requires:       python-jupyter-client-doc

%description    doc
This package contains the documentation of %{name}.
%endif

%prep
%autosetup -p1 -n %{modname}-%{version}

# Remove the dependency on debugpy.
# See https://github.com/ipython/ipykernel/pull/767
sed -i '/"debugpy/d' pyproject.toml

%if %{with doc}
# Use local objects.inv for intersphinx:
sed -e "s|\(('https://docs.python.org/3/', \)None)|\1'/usr/share/doc/python3-docs/html/objects.inv')|" \
    -e "s|\(('https://ipython.readthedocs.io/en/latest', \)None)|\1'/usr/share/doc/python3-ipython-doc/html/objects.inv')|" \
    -e "s|\(('https://jupyter.readthedocs.io/en/latest', \)None)|\1'/usr/share/doc/python-jupyter-client/html/objects.inv')|" \
    -i docs/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}

%build
%pyproject_wheel

%if %{with doc}
%make_build -C docs html
%endif

%install
%pyproject_install
%pyproject_save_files %{modname} %{modname}_launcher
%if %{with doc}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -fpavr docs/_build/html %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/html/.buildinfo
%endif

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

%if %{with doc}
%files doc
%doc %{_docdir}/%{name}/html
%endif


%changelog
%autochangelog
