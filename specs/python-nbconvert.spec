# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

%global pypi_name nbconvert

%bcond bootstrap 0
%bcond check %{without bootstrap}

# Don't build the documentation on EPEL as it would require
# too many dependencies.
%bcond doc %{undefined rhel}

Name:           python-%{pypi_name}
Version:        7.16.4
Release:        %autorelease
Summary:        Converting Jupyter Notebooks

License:        BSD-3-Clause
URL:            http://jupyter.org
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
# Deps not covered by upstream metadata
%if %{with doc}
BuildRequires:  python3-ipython-sphinx
BuildRequires:  pandoc
%endif

%description
The nbconvert tool, jupyter nbconvert, converts notebooks to various other 
formats via Jinja templates. The nbconvert tool allows you to convert an 
.ipynb notebook file into various static formats including HTML, LaTeX, 
PDF, Reveal JS, Markdown (md), ReStructured Text (rst) and executable script.

%package -n     python3-%{pypi_name}
Summary:        Converting Jupyter Notebooks

Recommends:     inkscape
Recommends:     pandoc

%description -n python3-%{pypi_name}

The nbconvert tool, jupyter nbconvert, converts notebooks to various other 
formats via Jinja templates. The nbconvert tool allows you to convert an 
.ipynb notebook file into various static formats including HTML, LaTeX, 
PDF, Reveal JS, Markdown (md), ReStructured Text (rst) and executable script.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for nbconvert
%description -n python-%{pypi_name}-doc
Documentation for nbconvert

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
echo "nbsphinx_allow_errors = True" >> docs/source/conf.py
# Remove coverage testing
sed -i '/"pytest-cov",/d' pyproject.toml
# Packages not available in Fedora
sed -i '/"pytest-dependency",/d' pyproject.toml
sed -i '/pyppeteer/d' pyproject.toml
sed -i 's/"sphinx==.*"/"sphinx"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-x test} %{?with_doc:-x docs}


%build
%pyproject_wheel

%if %{with doc}
export PYTHONPATH=$(pwd)
sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# fix permissions and shebangs
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{pypi_name}/nbconvertapp.py
chmod 755 %{buildroot}%{python3_sitelib}/%{pypi_name}/nbconvertapp.py

%if %{with check}
%check
# Some tests are using templates provided by the previous
# version of nbconvert.
%pytest -W ignore::DeprecationWarning -k "\
    not test_convert_full_qualified_name and \
    not test_post_processor and \
    not test_language_code_error and \
    not test_language_code_not_set and \
    not test_mermaid_output and \
    not test_set_language_code"
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc docs/README.md
%{_bindir}/jupyter-nbconvert
%{_bindir}/jupyter-dejavu
%{_datadir}/jupyter/%{pypi_name}/templates/

%if %{with doc}
%files -n python-%{pypi_name}-doc
%doc html
%endif

%changelog
%autochangelog
