# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
#
# However, currently we do not have all the necessary dependencies:
#   No matching package to install: 'python3dist(myst-nb) = 0.12.2'
#   No matching package to install: 'python3dist(nbsite) = 0.8~rc2'
#   No matching package to install: 'python3dist(panel)'
#   No matching package to install: 'python3dist(pydata-sphinx-theme) < 0.9~~'
%bcond doc_pdf 0

Name:           python-param
# Update this on every new upstream release.  Consult the file param/.version
# in the PyPI release tarball, or check the commit hash corresponding to the
# release tag on GitHub.
%global shortcommit 782a03c
Version:        1.13.0
Release:        %autorelease
Summary:        Make your Python code clearer and more reliable by declaring Parameters

License:        BSD-3-Clause
# The GitHub tarball contains documentation, examples, and tests; the PyPI
# tarball does not. See:
# https://github.com/holoviz/param/issues/219
# https://github.com/holoviz/param/issues/103
URL:            https://github.com/holoviz/param
Source:         %{url}/archive/v%{version}/param-%{version}.tar.gz

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

BuildRequires:  python3dist(pytest)

%global common_description %{expand:
Param is a library providing Parameters: Python attributes extended to have
features such as type and range checking, dynamically generated values,
documentation strings, default values, etc., each of which is inherited from
parent classes if not specified in a subclass.

Documentation and examples may be found at https://param.holoviz.org.}

%description %{common_description}


%package -n python3-param
Summary:        %{summary}
%py_provides python3-numbergen

# The file param/version.py is derived from a forked copy of
# https://github.com/pyviz-dev/autover. See the comments at the top of the file
# for details. Note that we cannot unbundle this library because it is in the
# public API, so the fork matters.
Provides:       bundled(python3dist(autover)) = 0.2.5

%description -n python3-param %{common_description}


%package doc
Summary:        Documentation and examples for param

%description doc %{common_description}


%prep
%autosetup -n param-%{version}

# Imitate the PyPI release process.
cat > param/.version <<EOF
{"git_describe": "v%{version}-0-g%{shortcommit}", "version_string": "%{version}"}
EOF

# Do not generate test dependencies for linting or coverage:
sed -r -i '/\b(flake8|coverage)\b/d' setup.py


%generate_buildrequires
%pyproject_buildrequires -x tests%{?with_doc_pdf:,doc}


%build
%pyproject_wheel

%if %{with doc_pdf}
sphinx-build -b latex -j%{?_smp_build_ncpus} docs %{_vpath_builddir}/_latex
%make_build -C %{_vpath_builddir}/_latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files param


%check
%pytest


%files -n python3-param -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE.txt; verify with “rpm -qL -p …”
%{python3_sitelib}/numbergen/


%files doc
%license LICENSE.txt
%doc README.md
%doc examples/
%if %{with doc_pdf}
%doc {_vpath_builddir}/_latex/param.pdf
%endif


%changelog
%autochangelog
