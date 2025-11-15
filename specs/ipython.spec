# Documentation is disabled by default
# because of missing dependencies: sphinx-toml
%bcond_with doc

%if 0%{?epel}
# disabled tests for epel because of missing dependencies:
# - python3-ipykernel
# - python3-jupyter-client
# - python3-nbformat
# - python3-testpath
%bcond_with check
%else
%bcond_without check
%endif

Name:           ipython
Version:        9.6.0
Release:        %autorelease
Summary:        An enhanced interactive Python shell

# SPDX
# Source code is licensed under BSD-3-Clause except
# - IPython/testing/plugin/pytest_ipdoctest.py
# - IPython/external/pickleshare.py - bundled with reduced functionalities
# which are MIT licensed
License:        BSD-3-Clause AND MIT
URL:            http://ipython.org/
Source0:        %pypi_source

# Unset -s on python shebang - ensure that packages installed with pip
# to user locations are seen and properly loaded.
%undefine _py3_shebang_s

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel

%if %{with doc}
BuildRequires:  python3-exceptiongroup
BuildRequires:  python3-ipykernel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-toml  # Not available in Fedora yet
BuildRequires:  python3-matplotlib
BuildRequires:  python3-typing-extensions
%endif

%if %{with check}
# for latex
BuildRequires: /usr/bin/dvipng
BuildRequires: tex(amsmath.sty)
BuildRequires: tex(amssymb.sty)
BuildRequires: tex(amsthm.sty)
BuildRequires: tex(bm.sty)
%endif

%global ipython_desc_base \
IPython provides a replacement for the interactive Python interpreter with\
extra functionality.\
\
Main features:\
 * Comprehensive object introspection.\
 * Input history, persistent across sessions.\
 * Caching of output results during a session with automatically generated\
   references.\
 * Readline based name completion.\
 * Extensible system of 'magic' commands for controlling the environment and\
   performing many tasks related either to IPython or the operating system.\
 * Configuration system with easy switching between different setups (simpler\
   than changing $PYTHONSTARTUP environment variables every time).\
 * Session logging and reloading.\
 * Extensible syntax processing for special purpose situations.\
 * Access to the system shell with user-extensible alias system.\
 * Easily embeddable in other Python programs.\
 * Integrated access to the pdb debugger and the Python profiler.

%description
%{ipython_desc_base}


%pyproject_extras_subpkg -n python3-ipython test


%package -n python3-ipython
Summary:        An enhanced interactive Python shell
%py_provides    python3-ipython-console
Provides:       ipython3 = %{version}-%{release}
Provides:       ipython = %{version}-%{release}
Provides:       bundled(python3dist(pickleshare)) = 0.7.5
Obsoletes:      python3-ipython-console < 5.3.0-1
Conflicts:      python2-ipython < 7

Requires:       (tex(amsmath.sty) if /usr/bin/dvipng)
Requires:       (tex(amssymb.sty) if /usr/bin/dvipng)
Requires:       (tex(amsthm.sty)  if /usr/bin/dvipng)
Requires:       (tex(bm.sty)      if /usr/bin/dvipng)

%description -n python3-ipython
%{ipython_desc_base}

This package provides IPython for in a terminal.


%package -n python3-ipython-sphinx
Summary:        Sphinx directive to support embedded IPython code
Requires:       python3-ipython = %{version}-%{release}
BuildRequires:  python3-sphinx
Requires:       python3-sphinx

%description -n python3-ipython-sphinx
%{ipython_desc_base}

This package contains the ipython sphinx extension.


%if %{with doc}
%package -n python3-ipython-doc
Summary:        Documentation for %{name}
%description -n python3-ipython-doc
This package contains the documentation of %{name}.
%endif


%prep
%autosetup -p1

# Remove shebangs
sed -i '1d' $(grep -lr '^#!/usr/' IPython)


%generate_buildrequires
%pyproject_buildrequires %{?with_check:-x test}


%build
%pyproject_wheel


%if %{with doc}
pushd docs
PYTHONPATH=.. make html SPHINXBUILD='sphinx-build-3 -D intersphinx_timeout=1'
mkdir -p build/html/
rm -rf build/html/.buildinfo
popd
%endif


%install
%pyproject_install

# link the manpage to ipython3
mv %{buildroot}%{_mandir}/man1/ipython{,3}.1
ln -s ./ipython3.1 %{buildroot}%{_mandir}/man1/ipython.1


%if %{with check}
%check
# Ensure that the user's .pythonrc.py is not invoked during any tests.
export PYTHONSTARTUP=""
# Koji builders can be slow, especially on arms, we scale timeouts 4 times
export IPYTHON_TESTING_TIMEOUT_SCALE=4
# Switch to a temporary directory to avoid _pytest.pathlib.ImportPathMismatchError
mkdir test_temp_dir
pushd test_temp_dir
# Ignored tests don't work well with out custom paths
%pytest -vv -p no:cacheprovider -k "not test_get_xdg_dir_3 and not test_extension" ../tests
popd
rm -rf test_temp_dir
%endif

%files -n python3-ipython
%{_bindir}/ipython3
%{_bindir}/ipython
%{_mandir}/man1/ipython.*
%{_mandir}/man1/ipython3.*
%{python3_sitelib}/ipython-*.dist-info/
%{python3_sitelib}/IPython
%exclude %{python3_sitelib}/IPython/sphinxext/

%files -n python3-ipython-sphinx
%{python3_sitelib}/IPython/sphinxext/

%if %{with doc}
%files -n python3-ipython-doc
%doc docs/build/html
%endif


%changelog
%autochangelog
