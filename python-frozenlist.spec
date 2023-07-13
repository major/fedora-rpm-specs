# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:           python-frozenlist
Version:        1.3.3
Release:        %autorelease
Summary:        List-like structure which can be made immutable

License:        Apache-2.0
URL:            https://github.com/aio-libs/frozenlist
Source:         %{pypi_source frozenlist}

BuildRequires:  python3-devel

BuildRequires:  gcc
BuildRequires:  python3dist(cython)

BuildRequires:  python3dist(pytest)

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
FrozenList is a list-like structure which implements
collections.abc.MutableSequence, and which can be made immutable.}

%description %{common_description}


%package -n python3-frozenlist
Summary:        %{summary}

%description -n python3-frozenlist %{common_description}


%if %{with doc}
%package        doc
Summary:        Documentation for python-frozenlist

BuildArch:      noarch

%description    doc %{common_description}
%endif


%prep
%autosetup -n frozenlist-%{version}

# Remove Cython-generated sources; we must ensure they are regenerated.
find . -type f -name '*.c' -print -delete

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py


%generate_buildrequires
%pyproject_buildrequires


%build
# Re-generate C sources with Cython. Imitates Makefile on GitHub.
%{python3} -m cython -3 frozenlist/*.pyx -I frozenlist

%pyproject_wheel

%if %{with doc}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files frozenlist


%check
%pytest


%files -n python3-frozenlist -f %{pyproject_files}
%if %{without doc}
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%endif


%if %{with doc}
%files doc
%license LICENSE
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%doc docs/_build/latex/frozenlist.pdf
%endif


%changelog
%autochangelog
