# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-aiosignal
Version:        1.3.1
Release:        %autorelease
Summary:        List of registered asynchronous callbacks

License:        Apache-2.0
URL:            https://github.com/aio-libs/aiosignal
Source0:        %{pypi_source aiosignal}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-asyncio)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
A project to manage callbacks in asyncio projects.}

%description %{common_description}


%package -n python3-aiosignal
Summary:        %{summary}

%description -n python3-aiosignal %{common_description}


%package        doc
Summary:        Documentation for python-aiosignal

BuildArch:      noarch

%description    doc %{common_description}


%prep
%autosetup -n aiosignal-%{version} -p1

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

# Patch out coverage options
sed -r -i 's/--cov[^[:blank:]]*//g' setup.cfg


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXBUILD='sphinx-build' SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files aiosignal


%check
%pytest


%files -n python3-aiosignal -f %{pyproject_files}
# pyproject-rpm-macros marks LICENSE in dist-info; verify with “rpm -qL -p …”
%doc README.rst


%files doc
%license LICENSE
%doc CHANGES.rst
%doc CONTRIBUTORS.txt
%doc README.rst
%if %{with doc_pdf}
%doc docs/_build/latex/aiosignal.pdf
%endif


%changelog
%autochangelog
