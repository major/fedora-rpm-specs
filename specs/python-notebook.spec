# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

Name:           python-notebook
Version:        7.3.2
Release:        %autorelease
Summary:        A web-based notebook environment for interactive computing
# SPDX
License:        BSD-3-Clause
URL:            https://jupyter.org
Source:         %{pypi_source notebook}

BuildArch:      noarch

BuildRequires:  python3-devel
# For validating desktop entry
BuildRequires:  desktop-file-utils

%global _description \
The Jupyter Notebook is a web application that allows you to create and \
share documents that contain live code, equations, visualizations, and \
explanatory text. The Notebook has support for multiple programming \
languages, sharing, and interactive widgets.

%description %_description

%package -n     python3-notebook
Summary:        %{summary}
Requires:       python-jupyter-filesystem
%py_provides    python3-jupyter-notebook
%py_provides    python3-ipython-notebook
%py_provides    notebook
%py_provides    jupyter-notebook
# We stopped shipping doc a long time ago, but there are possible conflicts.
# For details, see https://bugzilla.redhat.com/2254087
# (Keep this around at least until Fedora 41.)
Obsoletes:      python-notebook-doc < 7

%description -n python3-notebook %_description


%prep
%autosetup -p1 -n notebook-%{version}

# The nbval package is used for validation of notebooks.
# It's sedded out because it isn't yet packaged in Fedora.
# Selenium tests are skipped because the version in Fedora is too old.
# We don't test coverage.
# pytest-tornasync is unmaintained upstream and will be
# replaced by pytest-jupyter.
for pkg in nbval "selenium==.*" coverage pytest-cov pytest-tornasync; do
  sed -Ei "/\"$pkg\",?/d" pyproject.toml
done

# Remove all backup files
find ./ -name "*.json.orig" -delete

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files notebook

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/notebook.json

%check
%pytest -W ignore::DeprecationWarning --ignore notebook/tests/selenium

desktop-file-validate %{buildroot}%{_datadir}/applications/jupyter-notebook.desktop


%files -n python3-notebook -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jupyter-notebook
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/notebook.json
%{_datadir}/jupyter/lab/schemas/@jupyter-notebook/
%{_datadir}/jupyter/labextensions/@jupyter-notebook/
%{_datadir}/applications/jupyter-notebook.desktop
%{_datadir}/icons/hicolor/scalable/apps/notebook.svg

%changelog
%autochangelog
