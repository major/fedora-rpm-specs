%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-pyscaffold
Version:        4.4.1
Release:        %autorelease
Summary:        Template tool for putting up the scaffold of a Python project

# The entire source is MIT, except for the template files under
# pyscaffold.templates, which are 0BSD.
License:        MIT and 0BSD
URL:            https://pyscaffold.org/
Source0:        %{pypi_source PyScaffold}
# Man page written by hand in groff_man(7) format for Fedora based on --help
# output. Note that help2man(1) could autogenerate a decent man page if needed:
#   help2man --no-info --output=putup.1 putup
# but the hand-written one is better-formatted and contains better
# cross-references.
Source1:        putup.1

# Downstream-only: do not run coverage analysis
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          PyScaffold-4.2.1-no-coverage.patch
# Downstream-only: remove animated demo from docs since this cannot be included
# in a PDF
Patch:          PyScaffold-4.1-no-animated-doc-demo.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  git-core
# Needs vim (vim-enhanced) or vi (vim-minimal); we choose the lighter-weight BR
BuildRequires:  vim-minimal
BuildRequires:  python-unversioned-command
%endif

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  /usr/bin/xindy
BuildRequires:  tex-xetex-bin
BuildRequires:  /usr/bin/rsvg-convert
%endif

%global common_description %{expand: \
PyScaffold is a project generator for bootstrapping high quality Python
packages, ready to be shared on PyPI and installable via pip. It is easy to use
and encourages the adoption of the best tools and practices of the Python
ecosystem, helping you and your team to stay sane, happy and productive. The
best part? It is stable and has been used by thousands of developers for over
half a decade!}

%description
%{common_description}


%package -n python3-pyscaffold
Summary:        %{summary}

%description -n python3-pyscaffold
%{common_description}


%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.


# We do not package the “all” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-markdown) >= 0.4
#   python3dist(pyscaffoldext-custom-extension) >= 0.6
#   python3dist(pyscaffoldext-dsproject) >= 0.5
#   python3dist(pyscaffoldext-django) >= 0.1.1
#   python3dist(pyscaffoldext-cookiecutter) >= 0.1
#   python3dist(pyscaffoldext-travis) >= 0.3
#
# We do not package the “md” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-markdown) >= 0.4
#
# We do not package the “ds” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-dsproject) >= 0.5


%prep
%autosetup -n PyScaffold-%{version} -p1

# Correct all shebangs in tests and templates
%py3_shebang_fix tests

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py
# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py
# Cannot use SVG images when building PDF documentation; rewrite to use PDFs,
# which we will generate in %%build
find docs -type f -exec \
    gawk '/\.svg/ { print FILENAME; nextfile }' '{}' '+' |
  xargs -r -t sed -r -i 's/\.svg/\.pdf/g'
# Drop “furo” HTML theme dependency, since we build PDF, and furo is not
# packaged anyway (RHBZ#1910798)
sed -r -i '/\bfuro\b/d' docs/requirements.txt

# Cannot install “all” extra for testing
sed -r -i 's/^([[:blank:]]*)(all)\b/\1# \2/' tox.ini

# Relax version constraint to allow newer platformdirs
# https://github.com/pyscaffold/pyscaffold/pull/721
sed -i -e 's/platformdirs>=2,<3/\platformdirs>=2,<4/' setup.cfg


%generate_buildrequires
# Missing dependencies for “all”, “md”, and “ds” extras
%pyproject_buildrequires %{?with_tests:-t} %{?with_doc_pdf:docs/requirements.txt}


%build
%pyproject_wheel

%if %{with doc_pdf}
# Cannot use SVG images when building PDF documentation; convert to PDFs
find docs -type f -name '*.svg' |
  while read -r fn
  do
    rsvg-convert --format=pdf \
        --output="$(dirname "${fn}")/$(basename "${fn}" .svg).pdf" "${fn}"
  done

PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
# setup.py does not install the template files
install -p -m 0644 \
    -t '%{buildroot}/%{python3_sitelib}/pyscaffold/templates' \
    src/pyscaffold/templates/*.template
%pyproject_save_files pyscaffold
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check
%if %{with tests}
# Hopefully keep from overwriting user’s git config if building locally
TEST_HOME="$(mktemp -d)"
trap "rm -vrf '${TEST_HOME}'" INT TERM EXIT
export HOME="${TEST_HOME}"
# Required for a test
git config --global user.email 'jane@doe.com'
git config --global user.name 'jane doe'

# skip tests that need network access
k="${k-}${k+ and }not test_inplace_update"
k="${k-}${k+ and }not test_piptools_works_with_pyscaffold"
k="${k-}${k+ and }not test_update_version_3_0_to_3_1"
k="${k-}${k+ and }not test_update_version_3_0_to_3_1_pretend"
k="${k-}${k+ and }not test_install_packages"
k="${k-}${k+ and }not test_api_with_venv"
k="${k-}${k+ and }not test_cli_with_venv"
k="${k-}${k+ and }not test_pipenv_works_with_pyscaffold"
# We should be able to write:
#   %%tox -- -- -k "${k-}" …
# but for some reason this does not successfully collect any tests.
%pytest -k "${k-}" \
    --ignore=tests/test_install.py \
    --ignore=tests/system/test_common.py
%endif


%files -n python3-pyscaffold -f %{pyproject_files}
%doc AUTHORS.rst
%doc CHANGELOG.rst
%doc CONTRIBUTING.rst
%doc README.rst

%{_bindir}/putup
%{_mandir}/man1/putup.1*


%files doc
%license LICENSE.txt
%if %{with doc_pdf}
%doc docs/_build/latex/user_guide.pdf
%endif


%changelog
%autochangelog
