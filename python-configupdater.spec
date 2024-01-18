%bcond tests 1

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-configupdater
Version:        3.2
Release:        %autorelease
Summary:        Parser like ConfigParser but for updating configuration files

# ConfigUpdater is licensed under the MIT license; see below for details.
#
# ConfigUpdater includes code derived from the Python standard library, which
# is licensed under the Python license, a permissive open source license.
#
# It is not well-documented which portions of the software are covered by
# Python-2.0.1.
License:        MIT AND Python-2.0.1
URL:            https://github.com/pyscaffold/configupdater
Source0:        %{pypi_source ConfigUpdater}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global _description %{expand:
The sole purpose of ConfigUpdater is to easily update an INI config file with
no changes to the original file except the intended ones. This means comments,
the ordering of sections and key/value-pairs as well as their cases are kept as
in the original file. Thus ConfigUpdater provides complementary functionality
to Python’s ConfigParser which is primarily meant for reading config files and
writing new ones.

Features:

The key differences to ConfigParser are:

  • minimal invasive changes in the update configuration file,
  • proper handling of comments,
  • only a single config file can be updated at a time,
  • the original case of sections and keys are kept,
  • control over the position of a new section/key

The following features are deliberately not implemented:

  • interpolation of values,
  • propagation of parameters from the default section,
  • conversions of values,
  • passing key/value-pairs with default argument,
  • non-strict mode allowing duplicate sections and keys.}

%description %_description


%package -n python3-ConfigUpdater
Summary:        %{summary}

%description -n python3-ConfigUpdater %_description


%package doc
Summary:        Documentation for %{name}

%description doc
This package provides generated documentation for %{name}.


%prep
%autosetup -n ConfigUpdater-%{version}

# Remove coverage and linter bits
sed -i -r '/(--cov|pytest-cov|flake8)/d' setup.cfg

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py


%generate_buildrequires
%{pyproject_buildrequires \
    %{?with_tests:-x testing} %{?with_doc_pdf:docs/requirements.txt}}


%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l configupdater


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-ConfigUpdater -f %{pyproject_files}
%doc AUTHORS.rst
%doc CHANGELOG.rst
%doc CONTRIBUTING.rst
%doc README.rst


%files doc
%license LICENSE.txt
%if %{with doc_pdf}
%doc docs/_build/latex/user_guide.pdf
%endif


%changelog
%autochangelog
