%bcond_with tests

%global forgeurl https://github.com/wmayner/pyphi

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-pyphi
Version:        1.2.1
Release:        %autorelease
Summary:        A toolbox for integrated information theory
%forgemeta
# The entire source is GPL-3.0-or-later, except:
#
#   - docs/_themes/ contains “krTheme Sphinx Style,” which is BSD-3-Clause; but
#     we remove it in %%prep and do not use it.
License:        GPL-3.0-or-later
URL:            %forgeurl
Source0:        %forgesource

# https://github.com/wmayner/pyphi/pull/50
Patch:          0001-fix-py3.10-correct-collections-import.patch
# Remove sphinx-contrib-napoleon
# https://github.com/wmayner/pyphi/pull/22
Patch:          %{url}/pull/22.patch

# Tests fails on s390x: https://github.com/wmayner/pyphi/issues/41
# https://bugzilla.redhat.com/show_bug.cgi?id=2010104
ExcludeArch:    s390x

# The base package is arched so we can easily detect arch-dependent build
# issues, but there is no compiled code.
%global debug_package %{nil}

BuildRequires:  python3-devel

%if %{with doc_pdf}
# Documentation
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
BuildRequires:  /usr/bin/xindy
# HTML theme module is imported even when building LaTeX:
BuildRequires:  %{py3_dist sphinx_rtd_theme}
%endif

%global _description %{expand:
PyPhi is a Python library for computing integrated information (𝚽), and the
associated quantities and objects.

If you use this code, please cite the paper:

  Mayner WGP, Marshall W, Albantakis L, Findlay G, Marchman R, Tononi G. (2018)
  PyPhi: A toolbox for integrated information theory. PLOS Computational
  Biology 14(7): e1006343. https://doi.org/10.1371/journal.pcbi.1006343}

%description %_description

%package -n python3-pyphi
Summary:        %{summary}

BuildArch:      noarch

%description -n python3-pyphi %_description

%package doc
Summary:        %{summary}

BuildArch:      noarch

%description doc
Documentation for %{name}

%prep
%autosetup -n pyphi-%{version} -p1

# Strip unnecessary shebangs from non-script files
find . -type f -name '*.py' -execdir sed -r -i '1{/^#!/d}' '{}' '+'

# Remove a bundled copy of gprof2dot (packaged in Fedora, upstream at
# https://github.com/jrfonseca/gprof2dot); we do not need to do profiling and
# will not ship it in the binary RPMs.
rm -v profiling/gprof2dot
# Remove a bundled copy of “krTheme Sphinx Style”
rm -rvf docs/_themes/*

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r '/^(coverage|asv|virtualenv)\b/d' test_requirements.txt |
  tee test_requirements.filtered.txt

# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:test_requirements.filtered.txt}

%build
%pyproject_wheel
%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files pyphi

%check
%if %{with tests}
  %pytest
%else
  %pyproject_check_import
%endif

%files -n python3-pyphi -f %{pyproject_files}
%doc README.md CHANGELOG.md CACHING.rst redis.conf

%files doc
%license LICENSE.md
%if %{with doc_pdf}
%doc docs/_build/latex/PyPhi.pdf
%endif

%changelog
%autochangelog
