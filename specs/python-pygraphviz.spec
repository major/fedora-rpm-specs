%bcond doc %{undefined el10}

Name:           python-pygraphviz
Version:        1.14
Release:        %autorelease
Summary:        Create and Manipulate Graphs and Networks
License:        BSD-3-Clause
URL:            https://pygraphviz.github.io/
VCS:            https://github.com/pygraphviz/pygraphviz
Source0:        %{vcs}/archive/pygraphviz-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  graphviz-devel
BuildRequires:  swig

%global _description %{expand:
PyGraphviz is a Python interface to the Graphviz graph layout and
visualization package. With PyGraphviz you can create, edit, read,
write, and draw graphs using Python to access the Graphviz graph data
structure and layout algorithms. PyGraphviz is independent from
NetworkX but provides a similar programming interface.}

%description %_description

%package -n python3-pygraphviz
Summary:        %{summary}

%description -n python3-pygraphviz %_description

%if %{with doc}
%package doc
# The content is BSD-3-Clause.  Other licenses are due to Sphinx files.
# _static/basic.css: BSD-2-Clause
# _static/binder_badge_logo.svg: BSD-3-Clause
# _static/broken_example.png: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jupyterlite_badge_logo.svg: BSD-3-Clause
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/no_image.png: BSD-3-Clause
# _static/opensearch.xml: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/pygments.css: BDS-3-Clause
# _static/scripts/bootstrap*: MIT
# _static/scripts/pydata-sphinx-theme*: BSD-3-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sg_gallery*.css: BSD-3-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# _static/styles/bootstrap*: MIT
# _static/styles/pydata-sphinx-theme*: BSD-3-Clause
# _static/styles/theme.css: BSD-2-Clause
# _static/version_switcher.json: BSD-3-Clause
# _static/webpack-macros.html: BSD-3-Clause
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause AND MIT
Summary:        Documentation for pygraphviz
Provides:       bundled(js-bootstrap)
BuildArch:      noarch

%description doc
Documentation for PyGraphViz.
%endif

%prep
%autosetup -p1 -n pygraphviz-pygraphviz-%{version}

# Regenerate the swig-generated files
swig -python pygraphviz/graphviz.i

# Fix the shebangs in the examples
%py3_shebang_fix examples

# Skip the code coverage tests
sed -i -e '/codecov/d' -e '/pytest-cov/d' requirements/test.txt

# Downgrade the sphinx dependency. Docs seems to be build fine with 7.x.
sed -i 's/sphinx>=8\.0/sphinx/' requirements/doc.txt

%generate_buildrequires
%pyproject_buildrequires requirements/test.txt %{?with_doc:requirements/doc.txt}

%build
%pyproject_wheel

%if %{with doc}
# Point to the local switcher instead of the inaccessible one on the web
sed -i "s,https://pygraphviz\.github\.io/documentation/latest,$PWD/doc/source," doc/source/conf.py

# docs
%make_build -C doc html PYTHONPATH=$(echo $PWD/build/lib.%{python3_platform}-*)
# or $PWD/build/lib.%%{python3_platform}-%%(%%python3 -c 'import sys; print(sys.implementation.cache_tag)'
%endif

%install
%pyproject_install
%pyproject_save_files pygraphviz
%if %{with doc}
rm doc/build/html/.buildinfo
%endif
chmod g-w %{buildroot}%{python3_sitearch}/pygraphviz/_graphviz.*.so

%global _docdir_fmt %{name}

%check
%pytest -v %{buildroot}%{python3_sitearch}/pygraphviz/tests/

%files -n python3-pygraphviz -f %{pyproject_files}
%exclude %{python3_sitearch}/pygraphviz/graphviz_wrap.c
%doc README.rst

%if %{with doc}
%files doc
%doc doc/build/html
%doc examples
%license LICENSE
%endif

%changelog
%autochangelog
