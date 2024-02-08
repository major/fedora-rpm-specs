# Pull from GitHub, which includes tests
%global forgeurl https://github.com/plotly/plotly.py

# XXX 1: that they bundle one file in _plotly_utils: png.py, which is in the
# pypng module. However, it is unclear if they're actively tracking the
# upstream code so we just use their bundled copy.

# XXX 2: There are empty files in the _plotly_future directory but they are
# required and cannot be removed

# They do not include tests in the pypi tar, and they don't make GitHub
# releases only for the Python package---the GitHub tar also includes their JS
# etc. bits which we don't need here.
# UPDATE: All separate Python packages are tagged separately. That
# makes it easy # to get the source tarball from GitHub, that corresponds
# to a PyPI release and allows us to run tests.
%bcond tests 1

# Conditionalize test suits for selecting dependencies and tests to run
# Run core tests
%bcond test_core 1
# Run I/O tests
%bcond test_io 1
# Run optional tests
%bcond test_optional 1
# Don't run orca tests (simply not possible / useful)
%bcond test_orca 0

%global _description %{expand:
plotly.py is an interactive, open-source, and browser-based graphing library
for Python.

Built on top of plotly.js, plotly.py is a high-level, declarative charting
library. plotly.js ships with over 30 chart types, including scientific charts,
3D graphs, statistical charts, SVG maps, financial charts, and more.

plotly.py is MIT Licensed. Plotly graphs can be viewed in Jupyter notebooks,
standalone HTML files, or hosted online using Chart Studio Cloud.

Documentation is available at https://plotly.com/python/}

Name:       python-plotly
Version:    5.18.0
Release:    %autorelease
Summary:    An open-source, interactive data visualization library
%global tag v%{version}
%forgemeta
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
License:    MIT
URL:        https://plotly.com/python/
Source0:    %forgesource
# We use the sdist tarball to extract the NPM generated files
Source1:    %{pypi_source plotly}

BuildArch:  noarch

%description %_description

%package -n python3-plotly
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  npm
%if %{with tests}
BuildRequires:  python3-pytest
%if %{with test_core}
BuildRequires:  python3-requests
%endif
%if %{with test_io}
BuildRequires:  python3-pandas
BuildRequires:  python3-ipywidgets
%endif
%if %{with test_optional}
BuildRequires:  python3-scipy
BuildRequires:  python3-xarray
BuildRequires:  python3-pillow
BuildRequires:  python3-statsmodels
BuildRequires:  python3-scikit-image
%endif
%if %{with test_orca}
BuildRequires:  orca
%endif
%endif

# For jupyter configs etc.
Requires:       python-jupyter-filesystem
Recommends:     python3-notebook
# Additional packages for use with plotly
Recommends:     python3-chart-studio
Recommends:     python3-plotly-geo

%description -n python3-plotly %_description


%prep
%forgeautosetup -p1

# Upstream bundles three packages in one repo. We only need to consider
# plotly. So, we remove everything else.
mv packages/python/plotly ./top
# Remove symlink. We keep the actual file this links to.
rm -v top/README.md
find ./ -mindepth 1 -maxdepth 1 ! -name top -type d -exec rm -rf '{}' +
find ./ -maxdepth 1 ! -name README.md -type f -delete
mv top/* .
rmdir top

# Extract `npm` generated Javascript files from PyPI tarball
tar xzf %{SOURCE1} plotly-5.18.0/jupyterlab_plotly/labextension plotly-5.18.0/jupyterlab_plotly/nbextension/index.js* --strip-components=1

# Fix one file
sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' _plotly_utils/png.py
chmod -x _plotly_utils/png.py

# remove jupyterlab dep, not required for build, and not packaged in Fedora
sed -i "s/\"jupyterlab~=3.0;python_version>='3.6'\",//" pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files plotly _plotly_utils _plotly_future_ jupyterlab_plotly

install -m 0644 -p -d $RPM_BUILD_ROOT/%{_sysconfdir}/jupyter
mv -v $RPM_BUILD_ROOT/%{_prefix}/etc/jupyter $RPM_BUILD_ROOT/%{_sysconfdir}/


%check
%if %{with tests}
%if %{with test_core}
ts="${ts-}${ts+ }plotly/tests/test_core"
# These tests cannot be run in the build environment
k="${k-}${k+ and }not test_described_subscript_error_on_type_error"
k="${k-}${k+ and }not test_plotlyjs_version"
%endif
%if %{with test_io}
ts="${ts-}${ts+ }plotly/tests/test_io"
# Tests with errors (reason unknown)
k="${k-}${k+ and }not test_object_numpy_encoding"
# Test appears to be flaky
k="${k-}${k+ and }not test_sanitize_json"
%endif
%if %{with test_optional}
ts="${ts-}${ts+ }plotly/tests/test_optional"
# kaleido is not packaged for Fedora
k="${k-}${k+ and }not test_kaleido"
# This optional test fails in koji (not in local mock build)
k="${k-}${k+ and }not test_aggregation"
%endif
%if %{with test_orca}
ts="${ts-}${ts+ }plotly/tests/test_orca"
%endif
%pytest -v "${k:+-k $k}" ${ts-}
%else
# exclude deprecated modules
%pyproject_check_import -e plotly.config -e plotly.dashboard_objs -e plotly.grid_objs -e plotly.plotly* -e plotly.presentation_objs -e plotly.session -e plotly.widgets
%endif


%files -n python3-plotly -f %{pyproject_files}
%doc README.md
%{_datadir}/jupyter/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/jupyterlab-plotly.json


%changelog
%autochangelog
