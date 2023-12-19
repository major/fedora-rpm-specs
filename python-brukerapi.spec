# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-brukerapi
Version:        0.1.9
Release:        %autorelease
Summary:        Python package providing I/O interface for Bruker data sets

# SPDX
License:        MIT
URL:            https://github.com/isi-nmr/brukerapi-python
# The PyPI sdist lacks the documentation, examples, and CHANGELOG.rst.
Source0:        %{url}/archive/v%{version}/brukerapi-python-%{version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
# output; see:
#
# Interest in man pages?
# https://github.com/isi-nmr/brukerapi-python/issues/19
Source10:       bruker.1
Source11:       bruker-filter.1
Source12:       bruker-report.1
Source13:       bruker-split.1

# Change description-file to description_file in setup.cfg
# https://github.com/isi-nmr/brukerapi-python/pull/16
Patch:          %{url}/pull/16.patch

# Fix invalid and unintended regex escape sequences
# https://github.com/isi-nmr/brukerapi-python/pull/18
Patch:          %{url}/pull/18.patch

# Fix a few typos in comments and in documentation and help text
# https://github.com/isi-nmr/brukerapi-python/pull/20
Patch:          %{url}/pull/20.patch

# Fix misspelled SchemaRawdata.seralize method
#
# Add a compatibility alias for the old misspelled name.
#
# https://github.com/isi-nmr/brukerapi-python/pull/21
Patch:          %{url}/pull/21.patch

# Explicitly distribute brukerapi.config
#
# Fixes a warning from setuptools about ambiguous configuration
#
# https://github.com/isi-nmr/brukerapi-python/pull/22
Patch:          %{url}/pull/22.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
A Python package providing I/O interface for Bruker data sets.}

%description %{common_description}


%package -n python3-brukerapi
Summary:        %{summary}

%description -n python3-brukerapi %{common_description}


%package        doc
Summary:        Documentation and examples for python-brukerapi

%description    doc %{common_description}


%prep
%autosetup -n brukerapi-python-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires %{?with_doc_pdf:docs/requirements.txt}


%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l brukerapi

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'


%check
# Since tests are described as “minimal”:
%pyproject_check_import

# Two test errors due to request fixture issues
# https://github.com/isi-nmr/brukerapi-python/issues/17
k="${k-}${k+ and }not test_data_load"
k="${k-}${k+ and }not test_data_save"

%pytest -v -k "${k-}"


%files -n python3-brukerapi -f %{pyproject_files}
%{_bindir}/bruker
%{_mandir}/man1/bruker*.1*


%files doc
%license LICENSE

%doc CHANGELOG.rst
%doc README.rst

%doc examples/

%if %{with doc_pdf}
%doc docs/build/latex/brukerapi.pdf
%endif


%changelog
%autochangelog
