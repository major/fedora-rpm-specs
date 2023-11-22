%global pypi_name plotnine

# Use forge macros to pull from GitHub
%global forgeurl https://github.com/has2k1/plotnine

# Run selected tests
%bcond tests 1

# Run all tests
%bcond all_tests 0

Name:           python-%{pypi_name}
Version:        0.12.4
Release:        %{autorelease}
Summary:        Implementation of a grammar of graphics in Python, based on ggplot2
%forgemeta
BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# BSD-3-Clause applies to plotnine/themes/seaborn_rcmod.py
# GPL-2.0-only applies to plotnine/themes/theme_tufte.py
License:        MIT AND BSD-3-Clause AND GPL-2.0-only
URL:            https://plotnine.readthedocs.io/en/stable
Source0:        %forgesource

%global _description %{expand:
Implementation of a grammar of graphics in Python, based on ggplot2.

The grammar allows users to compose plots by explicitly mapping data to
the visual objects that make up the plot.

Plotting with a grammar is powerful, it makes custom (and otherwise complex)
plots easy to think about and then create, while the simple plots remain
simple.

Welcome to Plot 9 from Outerspace 🪐 🦇}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-geopandas
BuildRequires:  python3-adjustText
BuildRequires:  comic-neue-fonts
BuildRequires:  git-core
%if %{with tests}
BuildRequires:  python3-pytest
# Below packages are from extra extra, which we provide, but it looks
# like it's not being installed, but needed for test
BuildRequires:  python3-adjustText
BuildRequires:  python3-scikit-misc
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-geopandas
# Test dependencies
BuildRequires:  python3-shapely
BuildRequires:  python3-statsmodels
%endif

%description -n python3-%{pypi_name} %_description


%pyproject_extras_subpkg -n python3-%{pypi_name} extra


%prep
%forgeautosetup -p1 -S git
# Disable coverage in pytest
sed -i -e 's/--cov=plotnine --cov-report=xml //' pyproject.toml
git add --all
git commit -m '[Fedora]: Disable linters'
git tag v%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%if %{with tests}
%if %{without all_tests}
# For a a more readable input to %%pytest
k="${k-}${k+ and }not logticks"
k="${k-}${k+ and }not facet"
k="${k-}${k+ and }not label"
k="${k-}${k+ and }not ribbon"
k="${k-}${k+ and }not arrow"
k="${k-}${k+ and }not adjust_text"
k="${k-}${k+ and }not caption_simple"
k="${k-}${k+ and }not theme"
k="${k-}${k+ and }not scale"
k="${k-}${k+ and }not coords"
k="${k-}${k+ and }not geom_bar_col_histogram"
k="${k-}${k+ and }not geom_bin_2d"
k="${k-}${k+ and }not geom_boxplot"
k="${k-}${k+ and }not geom_density"
k="${k-}${k+ and }not geom_dotplot"
k="${k-}${k+ and }not geom_map"
k="${k-}${k+ and }not geom_point"
k="${k-}${k+ and }not geom_raster"
k="${k-}${k+ and }not geom_violin"
k="${k-}${k+ and }not lint_and_format"
k="${k-}${k+ and }not position"
k="${k-}${k+ and }not qplot"
k="${k-}${k+ and }not stat_ecdf"
k="${k-}${k+ and }not stat_summary"
%endif
%pytest -v ${k+-k }"${k-}"
%else
%pyproject_check_import
%endif


%files -n python3-plotnine -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
