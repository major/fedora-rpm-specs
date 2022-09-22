Name:           python-pygraphviz
Version:        1.10
Release:        %autorelease
Summary:        Create and Manipulate Graphs and Networks
License:        BSD
URL:            http://networkx.lanl.gov/pygraphviz/
Source0:        https://github.com/pygraphviz/pygraphviz/archive/pygraphviz-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-gallery)
BuildRequires:  python3dist(numpydoc)
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
%{?python_provide:%python_provide python3-pygraphviz}

%description -n python3-pygraphviz %_description

%package doc
Summary:        Documentation for pygraphviz
Provides:       bundled(jquery)
BuildArch:      noarch

%description doc
Documentation for PyGraphViz.

%prep
%autosetup -p1 -n pygraphviz-pygraphviz-%{version}

# Regenerate the swig-generated files
swig -python pygraphviz/graphviz.i

# Fix the shebangs in the examples
for fil in examples/*.py; do
  sed -i.orig 's,%{_bindir}/env python,%{__python3},' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
%py3_build

# docs
%make_build -C doc html PYTHONPATH=$(echo $PWD/build/lib.%{python3_platform}-*)
# or $PWD/build/lib.%%{python3_platform}-%%(%%python3 -c 'import sys; print(sys.implementation.cache_tag)'

%install
%py3_install
mv %{buildroot}%{_docdir}/pygraphviz-* %{buildroot}%{_pkgdocdir}
rm %{buildroot}%{_pkgdocdir}/INSTALL.txt
cp -p README.rst %{buildroot}%{_pkgdocdir}
rm doc/build/html/.buildinfo
cp -av doc/build/html %{buildroot}%{_pkgdocdir}/
chmod g-w %{buildroot}%{python3_sitearch}/pygraphviz/_graphviz.*.so

%global _docdir_fmt %{name}

%check
pytest -v %{buildroot}%{python3_sitearch}/pygraphviz/tests/

%files -n python3-pygraphviz
%{python3_sitearch}/pygraphviz*
%exclude %{python3_sitearch}/pygraphviz/graphviz_wrap.c
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.rst
%license LICENSE

%files doc
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/examples
%license LICENSE

%changelog
%autochangelog
