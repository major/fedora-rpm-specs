# Break a circular dependency with sphinx-autodoc-typehints
%bcond bootstrap 0

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:           python-typeguard
Version:        4.1.1
Release:        %autorelease
Summary:        Run-time type checker for Python

# SPDX
License:        MIT
URL:            https://github.com/agronholm/typeguard
Source:         %{pypi_source typeguard}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
This library provides run-time type checking for functions defined with PEP 484
argument (and return) type annotations.}

%description %{common_description}


%package -n python3-typeguard
Summary:        %{summary}

%description -n python3-typeguard %{common_description}


%if %{with doc}
%package doc
Summary:        Documentation for typeguard

%description doc %{common_description}
%endif


%prep
%autosetup -n typeguard-%{version}

# Because we do not build Sphinx-generated HTML documentation, and conf.py does
# not import the HTML theme package, we do not need to require it at build
# time.
sed -r -i 's/^([[:blank:]]*)(.(sphinx_rtd_theme))\b/\1# \2/' pyproject.toml
# We can’t respect an upper-bound on the Sphinx version; let’s remove it and do
# our best.
sed -r -i 's/("Sphinx)[[:blank:]]*[<=][^"]*/\1/' pyproject.toml

%if %{with bootstrap}
sed -r -i 's/^([[:blank:]]*)(.(sphinx-autodoc-typehints))\b/\1# \2/' \
    pyproject.toml
sed -r -i 's/^([[:blank:]]*)(.(sphinx_autodoc_typehints))\b/\1# \2/' \
    docs/conf.py
%endif

# In docs/conf.py, packaging is used to access the version from the typeguard
# package distribution. This works for upstream, but it doesn’t work when we
# haven’t installed the package with proper dist-info metadata yet.
sed -r -i 's/get_version\("typeguard"\)/"%{version}"/' docs/conf.py

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x test%{?with_doc:,doc}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%if %{with doc}
PYTHONPATH="${PWD}/src" sphinx-build -b latex -j%{?_smp_build_ncpus} \
    docs %{_vpath_builddir}/_latex
%make_build -C %{_vpath_builddir}/_latex LATEXMKOPTS='-quiet'
%endif


%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_install
%pyproject_save_files typeguard


%check
%pytest


%files -n python3-typeguard -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%if %{without doc}
%doc README.rst
%endif


%if %{with doc}
%files doc
%license LICENSE
%doc README.rst
%doc %{_vpath_builddir}/_latex/typeguard.pdf
%endif


%changelog
%autochangelog
