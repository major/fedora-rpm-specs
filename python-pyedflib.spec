# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as substitute.
%bcond_without doc_pdf

%global _description %{expand:
pyEDFlib is a python library to read/write EDF+/BDF+ files based on EDFlib.
EDF means European Data Format and was firstly published Kemp1992. 
In 2003, an improved version of the file protocol named EDF+ has 
been published and can be found at Kemp2003.}

Name:           python-pyedflib
Version:        0.1.33
Release:        1%{?dist}
Summary:        Python library to read/write EDF+/BDF+ files, based on EDFlib

# The entire source is BSD-3-Clause, except:
#   BSD-2-Clause: pyedflib/_extensions/edf.pxi
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/holgern/pyedflib
Source0:        %{url}/archive/v%{version}/pyedflib-%{version}.tar.gz

Patch0:         0001-Numpy-patch.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2027046
ExcludeArch:    s390x

# Uses a forked copy of EDFlib (https://gitlab.com/Teuniz/EDFlib)
# https://github.com/holgern/pyedflib/issues/149
# Version number: pyedflib/_extensions/c/edflib.c, EDFLIB_VERSION
%global edflib_version 1.17
Provides:       bundled(edflib) = %{edflib_version}

%description %_description

%package -n python3-pyedflib
Summary:        %{summary}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}
BuildRequires:  %{py3_dist pytest}

%description -n python3-pyedflib %_description

%package doc
Summary:        Documentation and examples for pyedflib
BuildArch:      noarch

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpydoc)
%endif

# Required by some demos/examples:
Suggests:       python3dist(matplotlib)
Suggests:       python3dist(scipy)

%description doc
%{summary}.

%prep
%autosetup -p1 -n pyedflib-%{version}
# Avoid “too deeply nested” error generating LaTeX from Sphinx:
# https://github.com/sphinx-doc/sphinx/issues/777
cat >> doc/source/conf.py <<'EOF'
latex_elements = {
  'preamble': r'\usepackage{enumitem}\setlistdepth{99}',
}
EOF

# Remove shebangs from demos. The find-then-modify pattern keeps us from
# discarding mtimes on sources that do not need modification.
find demo -type f -exec \
    gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}" \
    %make_build -C doc latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C doc/build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files pyedflib

%check
%pytest
# Make sure we are still indicating the correct bundled edflib version:
grep -E "^#define[[:blank:]]+EDFLIB_VERSION[[:blank:]]+\($(
  echo '%{edflib_version}' | tr -d '.'
)\)[[:blank:]]*\$" 'pyedflib/_extensions/c/edflib.c'

%files -n python3-pyedflib -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc doc/build/latex/PyEDFlib.pdf
%endif
%doc demo

%changelog
* Tue Jun 27 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.33-1
- Update to 0.1.33 (close RHBZ#2217530)
- Replace deprecated pyproject_build_lib macro
- Update License to SPDX

* Mon Apr 24 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.32-1
- Update to 0.1.32 (close RHBZ#2187954)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.30-1
- Update to 0.1.30 (close RHBZ#2105939)

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.1.29-2
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.29-1
- Update to 0.1.29 (close RHBZ#2092244)

* Tue Feb 22 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.28-1
- Update to the latest release

* Mon Jan 31 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.25-1
- Update to the latest release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
