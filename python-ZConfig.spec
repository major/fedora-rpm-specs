# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-ZConfig
Version:        3.6.1
Release:        %autorelease
Summary:        Structured Configuration Library

License:        ZPL-2.1
URL:            https://github.com/zopefoundation/ZConfig/
Source0:        %{pypi_source ZConfig}
# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source1:        zconfig.1
Source2:        zconfig_schema2html.1

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  symlinks

%if %{with doc_pdf}
# Documentation
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
ZConfig is a configuration library intended for general use. It supports a
hierarchical schema-driven configuration model that allows a schema to specify
data conversion routines written in Python. ZConfig’s model is very different
from the model supported by the ConfigParser module found in Python’s standard
library, and is more suitable to configuration-intensive applications.

ZConfig schema are written in an XML-based language and are able to “import”
schema components provided by Python packages. Since components are able to
bind to conversion functions provided by Python code in the package (or
elsewhere), configuration objects can be arbitrarily complex, with values that
have been verified against arbitrary constraints. This makes it easy for
applications to separate configuration support from configuration loading even
with configuration data being defined and consumed by a wide range of separate
packages.}

%description %{common_description}


%package -n python3-ZConfig
Summary:        Structured Configuration Library

%description -n python3-ZConfig %{common_description}


%package -n python3-ZConfig+test
Summary:        Tests and test extras for ZConfig

Requires:       python3-ZConfig = %{version}-%{release}

%description -n python3-ZConfig+test
These are the tests for python3-ZConfig. This package:

• Provides the “ZConfig.tests” package
• Makes sure the “test” extra dependencies are installed


%package doc
Summary:        Documentation for ZConfig

# We have a symlink to a text file in the installed package.
Requires:       python3-ZConfig = %{version}-%{release}

%description doc %{common_description}

This package contains the documentation for ZConfig.


%prep
%autosetup -n ZConfig-%{version} -p1

# We can’t cross-reference Internet documentation.
echo 'intersphinx_mapping.clear()' >> docs/conf.py


%generate_buildrequires
%pyproject_buildrequires -x test%{?with_doc_pdf:,docs}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ZConfig

install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE1}' '%{SOURCE2}'

%if %{with doc_pdf}
# Building documentation in the install section is “weird,” but the
# documentation needs to incorporate the --help output from the command-line
# tools (via sphinxcontrib-programoutput), and those entry points are not
# generated until the wheel is installed, so this is the “least-worst”
# workaround.
PYTHONPATH='%{buildroot}%{python3_sitelib}' PATH="${PATH}:%{buildroot}%{_bindir}" \
    %make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

# We can’t move the file ZConfig/schemaless.txt out of the package because
# there is a test that actually checks for its presence. We can at least mark
# it as documentation in-place.
sed -r -i 's/^.*schemaless.txt/%doc &/' '%{pyproject_files}'
# Since we have one documentation file installed with an absolute path, the
# rest need to be that way too.
install -p -m 0644 -t '%{buildroot}%{_pkgdocdir}' -D \
    CHANGES.rst \
    README.rst \
    docs/schema.dtd \
    %{?with_doc_pdf:docs/_build/latex/ZConfig.pdf}
# Make a relative symlink.
ln -s '%{buildroot}%{python3_sitelib}/ZConfig/schemaless.txt' \
    '%{buildroot}%{_pkgdocdir}/schemaless.txt'
symlinks -c '%{buildroot}%{_pkgdocdir}/schemaless.txt'


%check
%{python3} -m zope.testrunner --test-path=.


%files -n python3-ZConfig -f %{pyproject_files}
# pyproject_files handles LICENSE.txt in dist-info, but COPYRIGHT.txt is not
# present there, so we manually install both files to %%{_licensedir}
%license COPYRIGHT.txt
%license LICENSE.txt

# These are installed with the test extra subpackage.
%exclude %{python3_sitelib}/ZConfig/tests/

%{_bindir}/zconfig
%{_bindir}/zconfig_schema2html
%{_mandir}/man1/zconfig.1*
%{_mandir}/man1/zconfig_schema2html.1*


%files -n python3-ZConfig+test
%{python3_sitelib}/ZConfig/tests/
%ghost %{python3_sitelib}/*.dist-info


%files doc
# Depends on python3-ZConfig: separate copies of license files are not needed.
%doc %{_pkgdocdir}/CHANGES.rst
%doc %{_pkgdocdir}/README.rst
%doc %{_pkgdocdir}/schema.dtd
%doc %{_pkgdocdir}/schemaless.txt
%if %{with doc_pdf}
%doc %{_pkgdocdir}/ZConfig.pdf
%endif


%changelog
%autochangelog
