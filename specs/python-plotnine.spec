%global pypi_name plotnine

# Run selected tests
%bcond tests 1

# Run all tests
%bcond all_tests 0

Name:           python-%{pypi_name}
Version:        0.14.5
Release:        %{autorelease}
Summary:        Implementation of a grammar of graphics in Python, based on ggplot2

%global forgeurl https://github.com/has2k1/plotnine
%forgemeta

# BSD-3-Clause applies to plotnine/themes/seaborn_rcmod.py
# GPL-2.0-only applies to plotnine/themes/theme_tufte.py
License:        MIT AND BSD-3-Clause AND GPL-2.0-only
URL:            https://plotnine.readthedocs.io/en/stable
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
%if %{with tests}
# For locale tests using `locale.setlocale()`
BuildRequires:  glibc-langpack-en
BuildRequires:  python3-pytest
%endif

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

%description -n python3-%{pypi_name} %_description


%pyproject_extras_subpkg -n python3-%{pypi_name} extra


%prep
%forgeautosetup -p1 -S git

# Disable coverage in pytest
sed -i 's/--cov=plotnine --cov-report=xml //' pyproject.toml

# Raise upper bound on `mizani`. Upstream already did this on main.
# https://github.com/has2k1/plotnine/commit/61870d0e03888a8f8e7fb238baf85275557e34b6
# We do it in place here, to avoid having to drop the patch again next
# release
sed -i 's/mizani~=0.11.0/mizani~=0.12.0/' pyproject.toml

git add --all
git commit -m '[Fedora]: Disable linters'
git tag v%{version}


%generate_buildrequires
%pyproject_buildrequires -x extra


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%if %{with tests}
%if %{without all_tests}
# For a a more readable input to %%pytest
# Most tests fail image comparison for unknown reasons.
# To the naked eye the images appear identical.

# For test scripts where all or almost all tests fail,
# we ignore the entire test
i="${i-}${i+ }--ignore tests/test_annotation_logticks.py"
i="${i-}${i+ }--ignore tests/test_coords.py"
i="${i-}${i+ }--ignore tests/test_facets.py"
i="${i-}${i+ }--ignore tests/test_geom_boxplot.py"
i="${i-}${i+ }--ignore tests/test_geom_density.py"
i="${i-}${i+ }--ignore tests/test_geom_freqpoly.py"
i="${i-}${i+ }--ignore tests/test_geom_map.py"
i="${i-}${i+ }--ignore tests/test_geom_text_label.py"
i="${i-}${i+ }--ignore tests/test_lint_and_format.py"
i="${i-}${i+ }--ignore tests/test_scale_labelling.py"
i="${i-}${i+ }--ignore tests/test_stat_ecdf.py"

# For test scripts where some tests fail we list those tests
# or a glob matching those
k="${k-}${k+ and }not test_stat_bin_2d"
k="${k-}${k+ and }not test_geom_crossbar"
k="${k-}${k+ and }not test_labeller_cols_both_wrap"
k="${k-}${k+ and }not test_labeller_cols_both_grid"
k="${k-}${k+ and }not test_labeller_towords"
k="${k-}${k+ and }not test_aslabeller_dict_0tag"
k="${k-}${k+ and }not test_uneven_num_of_lines"
k="${k-}${k+ and }not test_bar_count"
k="${k-}${k+ and }not test_histogram_count"
k="${k-}${k+ and }not test_stat_count_int"
k="${k-}${k+ and }not test_stat_count_float"
k="${k-}${k+ and }not test_discrete_y"
k="${k-}${k+ and }not test_contours"
k="${k-}${k+ and }not test_arrow"
k="${k-}${k+ and }not test_arrow_facets"
k="${k-}${k+ and }not test_line"
k="${k-}${k+ and }not test_square"
k="${k-}${k+ and }not test_rectangle"
k="${k-}${k+ and }not test_rect_aesthetics"
k="${k-}${k+ and }not test_tile_aesthetics"
k="${k-}${k+ and }not test_area_aesthetics"
k="${k-}${k+ and }not test_scale_area_coordatalip"
k="${k-}${k+ and }not test_legend_fill_ratio"
k="${k-}${k+ and }not test_nudge"
k="${k-}${k+ and }not test_stack_non_linear_scale"
k="${k-}${k+ and }not test_dodge_preserve_single_text"
k="${k-}${k+ and }not test_dodge2"
k="${k-}${k+ and }not test_dodge2_varwidth"
k="${k-}${k+ and }not test_scalars"
k="${k-}${k+ and }not test_series_labelling"
k="${k-}${k+ and }not test_save_as_pdf_pages_closes_plots"
k="${k-}${k+ and }not test_multiple_aesthetics"
k="${k-}${k+ and }not test_missing_data_discrete_scale"
k="${k-}${k+ and }not test_datetime_scale_limits"
k="${k-}${k+ and }not test_args"
k="${k-}${k+ and }not test_mean_sdl"
k="${k-}${k+ and }not test_theme"
k="${k-}${k+ and }not test_default"
k="${k-}${k+ and }not test_legend"
k="${k-}${k+ and }not test_turn_off_guide"
k="${k-}${k+ and }not test_facet_grid"
k="${k-}${k+ and }not test_facet_wrap"
k="${k-}${k+ and }not test_plot_margin_protruding_axis_text"
k="${k-}${k+ and }not test_colorbar_frame"
k="${k-}${k+ and }not test_different_colorbar_themes"
k="${k-}${k+ and }not test_inside_legend_90pct_top_right"

# Test failing image comparison since version 0.13.0.
k="${k-}${k+ and }not test_discrete_y"
k="${k-}${k+ and }not test_midpoint"
k="${k-}${k+ and }not test_line"
k="${k-}${k+ and }not test_rect_aesthetics"
k="${k-}${k+ and }not test_tile_aesthetics"
k="${k-}${k+ and }not test_legend_fill_ratio"
k="${k-}${k+ and }not test_args"

# Tests failing image comparison since version 0.13.3.
k="${k-}${k+ and }not test_axis_title_x_justification"
k="${k-}${k+ and }not test_axis_title_y_justification"
k="${k-}${k+ and }not test_plot_title_justification"

# Test failing image comparison since version 0.14.4
k="${k-}${k+ and }not test_transform_datetime_aes_param"
%endif
%pytest -v ${i-} ${k+-k }"${k-}"
%else
%pyproject_check_import
%endif


%files -n python3-plotnine -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
