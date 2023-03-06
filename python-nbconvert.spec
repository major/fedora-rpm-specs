# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

%global pypi_name nbconvert

%bcond_without doc
%bcond_without check

Name:           python-%{pypi_name}
Version:        7.2.5
Release:        %autorelease
Summary:        Converting Jupyter Notebooks

License:        BSD and MIT
URL:            http://jupyter.org
Source0:        %pypi_source
# See
# https://github.com/jupyter/nbconvert/blob/main/hatch_build.py
# https://github.com/jupyter/nbconvert/issues/1896
Source1:        https://cdn.jupyter.org/notebook/5.4.0/style/style.min.css

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
sed -i 's/"mistune>=.*"/"mistune"/' pyproject.toml

mkdir -p share/templates/classic/static/
cp -v %{SOURCE1} share/templates/classic/static/style.css

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
# Some tests need pyppeteer, some fail on unclosed context zmq.asyncio.Context()
# and some run in subprocess and therefore don't have "nbconvert.tests" in PYTHONPATH
%{__python3} -m pytest -W ignore::DeprecationWarning -k "\
    not test_export and \
    not test_webpdf_without_chromium and \
    not test_webpdf_with_chromium and \
    not test_no_input and \
    not test_basic_execution and \
    not test_mixed_markdown_execution and \
    not test_populate_language_info and \
    not test_preprocess_cell and \
    not test_convert_full_qualified_name and \
    not test_post_processor"
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
