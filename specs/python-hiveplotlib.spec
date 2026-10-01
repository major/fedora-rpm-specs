# TODO: Package dependencies for more backends
# - datashader backend needs datashader and numba
# - holoviews backend needs holoviews and numba
# - plotly backend needs plotly

%global giturl  https://gitlab.com/hiveplotlib/hiveplotlib

Name:           python-hiveplotlib
Version:        0.28.0
Release:        %autorelease
Summary:        Plotting package for generating & visualizing static Hive Plots

License:        BSD-3-Clause
URL:            https://hiveplotlib.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/v%{version}/hiveplotlib-v%{version}.tar.bz2
# Remove unwanted and unavailable dependencies from the pytest setup
Patch:          %{name}-pytest.patch

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x bokeh,networkx,testing
BuildOption(install): -l hiveplotlib

%global _desc %{expand:The hiveplotlib package supports generating and visualizing static Hive Plots
in Python.  By default, visualization is supported with the matplotlib backend
only, but bokeh support is also available.  Beyond the visualization backends,
hiveplotlib integrates with networkx: build a hive plot directly from a
networkx graph and compute graph metrics on it.}

%description
%_desc

%package -n     python3-hiveplotlib
Summary:        Plotting package for generating & visualizing static Hive Plots

%description -n python3-hiveplotlib
%_desc

%pyproject_extras_subpkg -n python3-hiveplotlib bokeh,networkx

%prep
%autosetup -n hiveplotlib-v%{version} -p1

%check
%pytest

%files -n python3-hiveplotlib -f %{pyproject_files}
%doc CHANGELOG.rst README.md

%changelog
%autochangelog
