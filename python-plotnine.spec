%global pypi_name plotnine

# Generate HTML documentation
# Currently not possible. Documentation depends on importlib_resources,
# which is not yet available in Fedora
%bcond_with doc

# Provide man pages
%bcond_without man

# Run tests
%bcond_without tests
# For a a more readable input to %%pytest
%global _skip_tests %{expand: -k \\
"not logticks and not backtransforms and not se_false and not facet \\
and not label and not ribbon and not arrow and not adjust_text \\
and not caption_simple and not theme and not scale"}

%global _description %{expand:
Implementation of a grammar of graphics in Python, based on ggplot2.

The grammar allows users to compose plots by explicitly mapping data to
the visual objects that make up the plot.

Plotting with a grammar is powerful, it makes custom (and otherwise complex)
plots easy to think about and then create, while the simple plots remain
simple.

Welcome to Plot 9 from Outerspace 🪐 🦇}

Name:           python-%{pypi_name}
Version:        0.10.1
Release:        %{autorelease}
Summary:        Implementation of a grammar of graphics in Python, based on ggplot2
BuildArch:      noarch

# BSD-3-Clause applies to plotnine/themes/seaborn_rcmod.py
# GPL-2.0-only applies to plotnine/themes/theme_tufte.py
License:        MIT AND BSD-3-Clause AND GPL-2.0-only
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %{pypi_source %{pypi_name}}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core
BuildRequires:  python3-geopandas
BuildRequires:  python3-adjustText
BuildRequires:  comic-neue-fonts
%if %{with tests}
BuildRequires:  python3-pytest
# Below packages are from extra extra, which we provide, but it looks
# like it's not being installed, but needed for test
BuildRequires:  python3-adjustText
BuildRequires:  python3-scikit-misc
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-geopandas
# Test dependencies
BuildRequires:  python3-shapely, python3-statsmodels
%endif
%if %{with doc}
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  python3-sphinx, python3-nbformat, python3-nbsphinx
# python-importlib-resources currently not available in Fedora
# jinja2: https://github.com/sphinx-doc/sphinx/issues/10291
BuildRequires:  python3-importlib-resources python3-jinja2 < 3.1
%endif

%description -n python3-%{pypi_name} %_description

%pyproject_extras_subpkg -n python3-%{pypi_name} extra


%if %{with doc}
%package doc
Summary:        HTML documentation for %{name}
Requires:       python3-%{pypi_name} == %{version}

%description doc
%{summary}
%endif


%prep
%autosetup -p1 -n %{pypi_name}-%{version} -S git
# Disable coverage in pytest
sed -i -e 's/--cov=plotnine --cov-report=xml //' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%if %{with doc}
  pushd doc
  make html
  popd
%endif


%install
%pyproject_install
%if %{with doc}
  mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
  cp -a doc/_build/html ${RPM_BUILD_ROOT}%{_pkgdocdir}
  rm -rf ${RPM_BUILD_ROOT}%{_pkgdocdir}/html/.buildinfo
%endif
%pyproject_save_files %{pypi_name}


%check
%if %{with tests}
  %pytest %_skip_tests
%else
  %pyproject_check_import
%endif


%files -n python3-plotnine -f %{pyproject_files}
%doc README.md
%license LICENSE

%if %{with doc}
  %files doc
  %dir %{_pkgdocdir}
  %doc %{_pkgdocdir}/html
%endif

%changelog
%autochangelog
