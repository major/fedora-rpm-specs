%bcond_without tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-llvmlite
Version:        0.40.0
Release:        %{autorelease}
Summary:        Lightweight LLVM Python binding for writing JIT compilers

# The entire source is BSD-2-Clause, except:
#   - The bundled versioneer.py, and the _version.py it generates (which is
#     packaged) is LicenseRef-Fedora-Public-Domain. In later versions of
#     versioneer, this becomes CC0-1.0 and then Unlicense.
#     Public-domain text added to fedora-license-data in commit
#     830d88d4d89ee5596839de5b2c1f48426488841f:
#     https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/210
# Additionally, the following does not affect the license of the binary RPMs:
#   - conda-recipes/appveyor/run_with_env.cmd is CC0-1.0; for distribution in
#     the source RPM, it is covered by “Existing uses of CC0-1.0 on code files
#     in Fedora packages prior to 2022-08-01, and subsequent upstream versions
#     of those files in those packages, continue to be allowed. We encourage
#     Fedora package maintainers to ask upstreams to relicense such files.”
#     https://gitlab.com/fedora/legal/fedora-license-data/-/issues/91#note_1151947383
License:        BSD-2-Clause AND LicenseRef-Fedora-Public-Domain

URL:            http://llvmlite.pydata.org/
%global forgeurl https://github.com/numba/llvmlite
Source0:        %{forgeurl}/archive/v%{version}/llvmlite-%{version}.tar.gz

BuildRequires:  python3-devel

# 0.40.0 only supports llvm14
BuildRequires:  llvm14-devel
BuildRequires:  gcc-c++

%global _description %{expand:
llvmlite is a project originally tailored for Numba‘s needs, using the
following approach:

  • A small C wrapper around the parts of the LLVM C++ API we need that are not
    already exposed by the LLVM C API.
  • A ctypes Python wrapper around the C API.
  • A pure Python implementation of the subset of the LLVM IR builder that we
    need for Numba.}

%description %_description

%package -n python3-llvmlite
Summary:        %{summary}


%description -n python3-llvmlite %_description

%package doc
Summary:        %{summary}
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# The HTML theme is imported in conf.py even when not generating HTML
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -n llvmlite-%{version} -p1

# increase verbosity of tests to 2
sed -i 's/\(def run_tests.*verbosity=\)1/\12/' llvmlite/tests/__init__.py

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# No network access
echo 'intersphinx_mapping.clear()' >> docs/source/conf.py

%ifarch ppc64le
# Test failure in 0.40.0 on 64-bit PowerPC: test_get_process_triple
# https://github.com/numba/llvmlite/issues/941
#
# We can skip this failure because upstream considers the discrepancy harmless.
# https://github.com/numba/llvmlite/issues/941#issuecomment-1542381275
sed -r -i \
    's/^([[:blank:]]*)(def test_get_process_triple\()/\1@unittest.skip("Issue #941")\n&/' \
    llvmlite/tests/test_binding.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
export LLVM_CONFIG="%{_libdir}/llvm14/bin/llvm-config"
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files llvmlite

%check
%if %{with tests}
PYTHONPATH='%{buildroot}%{python3_sitearch}' %{python3} runtests.py
%endif

%files -n python3-llvmlite -f %{pyproject_files}
%doc CHANGE_LOG README.rst

%files doc
%license LICENSE
%doc examples/
%if %{with doc_pdf}
%doc docs/_build/latex/llvmlite.pdf
%endif

%changelog
%autochangelog
