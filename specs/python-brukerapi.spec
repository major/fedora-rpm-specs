# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
#
# For simplicity, starting with F44, we merged the examples into the library
# package and stopped building the PDF documentation.
%bcond doc %[ %{defined fc43} || %{defined fc42} || %{defined el10} || %{defined el9} ]

Name:           python-brukerapi
Version:        0.1.10
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

BuildSystem:            pyproject
%if %{with doc}
BuildOption(generate_buildrequires): docs/requirements.txt
%endif
BuildOption(install):   -l brukerapi

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}

%if %{with doc}
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

%if %{without doc}
Obsoletes:      python-brukerapi-doc < 0.1.10-1
%endif

%description -n python3-brukerapi %{common_description}


%if %{with doc}
%package        doc
Summary:        Documentation and examples for python-brukerapi

%description    doc %{common_description}


%build -a
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'


%check -a
# Two test errors due to request fixture issues
# https://github.com/isi-nmr/brukerapi-python/issues/17
k="${k-}${k+ and }not test_data_load"
k="${k-}${k+ and }not test_data_save"

%pytest -v -k "${k-}"


%files -n python3-brukerapi -f %{pyproject_files}
%if %{without doc}
%doc CHANGELOG.rst
%doc README.rst
%doc examples/
%endif

%{_bindir}/bruker
%{_mandir}/man1/bruker*.1*


%if %{with doc}
%files doc
%license LICENSE

%doc CHANGELOG.rst
%doc README.rst

%doc examples/

%doc docs/build/latex/brukerapi.pdf
%endif


%changelog
%autochangelog
