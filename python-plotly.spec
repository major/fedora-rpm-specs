# XXX 1: that they bundle one file in _plotly_utils: png.py, which is in the
# pypng module. However, it is unclear if they're actively tracking the
# upstream code so we just use their bundled copy.

# XXX 2: There are empty files in the _plotly_future directory but they are
# required and cannot be removed

# They do not include tests in the pypi tar, and they don't make GitHub
# releases only for the Python package---the GitHub tar also includes their JS
# etc. bits which we don't need here.
# Leave this here in case they do start including tests in their PyPi tar.
%bcond_with tests

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
Version:    5.9.0
Release:    %autorelease
Summary:    An open-source, interactive data visualization library

# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
License:    MIT
URL:        https://plotly.com/python/
Source0:    %{pypi_source plotly}

BuildArch:  noarch

%description %_description

%package -n python%{python3_pkgversion}-plotly
Summary:    %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pip}
# not automatically pulled in
BuildRequires:  %{py3_dist ipywidgets}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist matplotlib}

# For jupyter configs etc.
Requires:   python-jupyter-filesystem
Recommends: %{py3_dist notebook}

# For tests, but see note at top of spec
# https://github.com/plotly/plotly.py/blob/master/.circleci/config.yml
# https://github.com/plotly/plotly.py/blob/6c463ee500960000341cc735b2d95680ac48e3ad/packages/python/plotly/tox.ini

# also required for import check
BuildRequires:  %{py3_dist pytest}

%description -n python%{python3_pkgversion}-plotly %_description


%prep
%autosetup -p1 -n plotly-%{version}

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
%{pytest}
%endif

# exclude deprecated modules
%pyproject_check_import -e plotly.config -e plotly.dashboard_objs -e plotly.grid_objs -e plotly.plotly* -e plotly.presentation_objs -e plotly.session -e plotly.widgets

%files -n python%{python3_pkgversion}-plotly -f %{pyproject_files}
%doc README.md
%{_datadir}/jupyter/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/jupyterlab-plotly.json


%changelog
%autochangelog
