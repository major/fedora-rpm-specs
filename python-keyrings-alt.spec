# Owns: /usr/lib/python3.10/site-packages/keyrings/__init__.py
# So keep an eye out for any other packages that may also want to owns it.

%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%global _description %{expand:
Alternate keyring backend implementations for use with the keyring package.

Keyrings in this package may have security risks or other implications. These
backends were extracted from the main keyring project to make them available
for those who wish to employ them, but are discouraged for general production
use. Include this module and use its backends at your own risk.

For example, the PlaintextKeyring stores passwords in plain text on the file
system, defeating the intended purpose of this library to encourage best
practices for security.}

Name:           python-keyrings-alt
Version:        4.1.2
Release:        %{autorelease}
Summary:        Alternate keyring implementations

License:        MIT
URL:            https://github.com/jaraco/keyrings.alt
Source0:        %{pypi_source keyrings.alt}

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

%description -n python3-keyrings-alt %_description

%package doc
Summary:        Documentation for %{name}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description doc
This package provides documentation for %{name}.

%prep
%autosetup -n keyrings.alt-%{version}

# Remove linters and coverage from BR
# Remove backports, used for Py <=3.2
sed -r -i \
    -e '/flake8/ d' \
    -e '/pytest-(black|cov|checkdocs|flake8|mypy|enabler)/ d' \
    -e '/python_implementation != "PyPy"/ d' \
    -e '/backports\.unittest_mock/ d' \
    setup.cfg

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

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x testing} %{?with_doc_pdf:-x docs}

# gdata, keyczar are Py2 only
# pyfs is included as python-fs but tests are still skipped
# Also skipped upstream though: https://github.com/jaraco/keyrings.alt/runs/3082737541?check_suite_focus=true

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" sphinx-build-3 docs docs/_latex -b latex %{?_smp_mflags}
%make_build -C docs/_latex LATEXMKOPTS='-quiet'
mv docs/_latex/python.pdf docs/_latex/keyringsalt.pdf
%endif

%install
%pyproject_install
# also takes the dist-info folder
%pyproject_save_files keyrings

%check
%if %{with tests}
%{pytest}
%endif

%files -n python3-keyrings-alt -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_latex/keyringsalt.pdf
%endif

%changelog
%autochangelog
