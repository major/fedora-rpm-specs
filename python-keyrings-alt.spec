# Owns: /usr/lib/python3.10/site-packages/keyrings/__init__.py
# So keep an eye out for any other packages that may also want to owns it.

%bcond tests 1

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 0
# Currently disabled, something missing:
# Could not import extension jaraco.packaging.sphinx (exception: No module named 'domdf_python_tools')

%global _description %{expand:
Alternate keyring backend implementations for use with the keyring package.

Keyrings in this package may have security risks or other implications. These
backends were extracted from the main keyring project to make them available
for those who wish to employ them, but are discouraged for general production
use. Include this module and use its backends at your own risk.

For example, the PlaintextKeyring stores passwords in plain text on the file
system, defeating the intended purpose of this library to encourage best
practices for security.}

%global forgeurl  https://github.com/jaraco/keyrings.alt

Name:           python-keyrings-alt
Version:        5.0.0
Release:        %{autorelease}
Summary:        Alternate keyring implementations

%forgemeta

# SPDX
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

%description %_description

%package -n python3-keyrings-alt
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  gnome-keyring
%endif
# Not included in install_requires
Requires:       %{py3_dist keyring}
%if %{without doc}
Provides:       python-keyrings-alt-doc = %{version}-%{release}
Obsoletes:      python-keyrings-alt-doc < %{version}-2
%endif

%description -n python3-keyrings-alt %_description

%if %{with doc}
%package doc
Summary:        Documentation for %{name}

BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-jaraco-packaging
BuildRequires:  python3-jaraco-context
BuildRequires:  latexmk

%description doc
This package provides documentation for %{name}.
%endif

%prep
%forgesetup

# Remove backports, used for Py <=3.2
sed -r -i '/backports\.unittest_mock/ d' setup.cfg
# Remove linters and coverage from BR
sed -r -i \
    -e '/pytest-(black|cov|checkdocs|mypy|enabler|ruff)/ d' \
    -e '/python_implementation != "PyPy"/ d' \
    -e '/sphinx-lint/ d' \
    setup.cfg
# We cannot have a pycryptodome test dependency, since there is no
# python-pycryptodome package (it would conflict with python-crypto/pycrypto).
# However, the tests intended for pycryptodome will pass with pycrypto
# installed, so we simply adjust the dependency.
sed -r -i 's/(pycrypto)dome$/\1/' setup.cfg

%if %{with doc}
# The 'jaraco.packaging.sphinx' extension means sphinx-build attempts to
# download things from PyPI. Obviously, we can’t have this.
sed -r -i 's/, .jaraco\.packaging\.sphinx.//' docs/conf.py
# The 'rst.linker' extension doesn’t seem to work for us. Maybe this is because
# we patched out 'jaraco.packaging.sphinx' (or maybe it isn’t).
sed -r -i 's/, .rst\.linker.//' docs/conf.py
# This isn’t packaged; it seems to be used only for the Tidelift referral
# banner in the documentation.
sed -r -i "s/(, )?'jaraco\\.tidelift'//g" docs/conf.py
sed -i -e '/jaraco\.tidelift/ d' setup.cfg
%endif

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r %{?with_tests:-x testing} %{?with_doc:-x docs}

# gdata, keyczar are Py2 only
# pyfs is included as python-fs but tests are still skipped
# Also skipped upstream though: https://github.com/jaraco/keyrings.alt/runs/3082737541?check_suite_focus=true

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%if %{with doc}
PYTHONPATH="${PWD}" sphinx-build-3 docs docs/_latex -b latex %{?_smp_mflags}
%make_build -C docs/_latex LATEXMKOPTS='-quiet'
mv docs/_latex/python.pdf docs/_latex/keyringsalt.pdf
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l keyrings

%check
%if %{with tests}
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{pytest}
%endif

%files -n python3-keyrings-alt -f %{pyproject_files}
%doc README.rst

%if %{with doc}
%files doc
%license LICENSE
%doc docs/_latex/keyringsalt.pdf
%endif

%changelog
%autochangelog
