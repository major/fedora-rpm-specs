# All tests run
%bcond_without tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
#
# Currently, there are several issues that still prevent us from successfully
# building the documentation even with a few obvious patches. See:
# https://github.com/nipy/nipy/pull/503#issuecomment-1421508175
%bcond_with doc_pdf

%global commit 9512cd93b7215b4c750be3968a600c06f2bd22f6
%global snapdate 20230206

Name:           python-nipy
Version:        0.5.0^%(echo '%{commit}' | cut -b -7)git%{snapdate}
Release:        %autorelease
Summary:        Neuroimaging in Python FMRI analysis package

License:        BSD-3-Clause
URL:            https://nipy.org/nipy
Source0:        https://github.com/nipy/nipy/archive/%{commit}/nipy-%{commit}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source10:       nipy_3dto4d.1
Source11:       nipy_4d_realign.1
Source12:       nipy_4dto3d.1
Source13:       nipy_diagnose.1
Source14:       nipy_tsdiffana.1

# Ensure numpy is in install_requires, not only setup_requires
# https://github.com/nipy/nipy/pull/500
Patch:          https://github.com/nipy/nipy/pull/500.patch
# Account for nibabel 5.0.0 removal of .py3k shim - use numpy.compat.py3k
# https://github.com/nipy/nipy/pull/498
# https://salsa.debian.org/med-team/nipy/-/blob/12a4fbea8c99c1e5dc07ee81bc3da1a450617050/debian/patches/nibabel5.0.0.patch
# Latest version from Debian rebased on the commit that is packaged.
Patch:          0001-Account-for-nibabel-5.0.0-removal-of-.py3k-shim-use-.patch
# Unbundle six
# https://github.com/nipy/nipy/pull/504
Patch:          https://github.com/nipy/nipy/pull/504/commits/a6de01c7484114aa52847edc400a386743e60c42.patch

BuildRequires:  gcc
BuildRequires:  flexiblas-devel
BuildRequires:  python3-devel

BuildRequires:  python3dist(setuptools)
# Imported in setup.py
BuildRequires:  python3dist(numpy)
#BuildRequires:  python3dist(six)

# For re-generating C code as required by packaging guidelines; see also
# nipy/nipy/info.py
BuildRequires:  python3dist(cython) >= 0.12.1

# A weak dependency; may enable more tests
BuildRequires:  python3dist(matplotlib)

%if %{with tests}
# https://fedoraproject.org/wiki/Changes/DeprecateNose
BuildRequires:  python3dist(nose)
BuildRequires:  nipy-data
# An indirect dependency, via nibabel.testing (for nibabel 5.x)
BuildRequires:  python3dist(pytest)
%endif

%if %{with doc_pdf}
BuildRequires:  graphviz
BuildRequires:  latexmk
BuildRequires:  make
BuildRequires:  python3-ipython-sphinx
BuildRequires:  python3-sphinx-latex
# Optional documentation dependency
BuildRequires:  python3dist(vtk)
%endif

%global _docdir_fmt %{name}

%global common_description %{expand:
Neuroimaging tools for Python.

The aim of NIPY is to produce a platform-independent Python environment for the
analysis of functional brain imaging data using an open development model.

In NIPY we aim to:

• Provide an open source, mixed language scientific programming environment
  suitable for rapid development.
• Create software components in this environment to make it easy to develop
  tools for MRI, EEG, PET and other modalities.
• Create and maintain a wide base of developers to contribute to this platform.
• Maintain and develop this framework as a single, easily installable bundle.}

%description %{common_description}


%package -n python3-nipy
Summary:        %{summary}

# Adds various plotting functionality, but not an “official” dependency
Recommends:     python3dist(matplotlib)

Suggests:       nipy-data

# The nipy.algorithms.statistics.models subpackage was forked from an
# undetermined version of scipy.stats.models in commit 55a9162 on 2011-09-13;
# before this, the upstream version was monkey-patched via
# nipy.fixes.scipy.stats.models.
Provides:       bundled(python3dist(scipy))

%description -n python3-nipy %{common_description}


%package doc
Summary:        Documentation and examples for python-nipy

BuildArch:      noarch

Requires:       nipy-data

%description doc
%{summary}.


%prep
%autosetup -n nipy-%{commit} -p1

# Add dependencies on libraries that are unbundled downstream to the metadata:
line="requirement_kwargs['install_requires'].extend(['transforms3d'])"
sed -r -i "s/^(def main|setup)/# Unbundled:\\n${line}\\n&/" setup.py

# Some bundled pure-Python libraries have been replaced with dependencies:
#   - python3dist(transforms3d)
# Begin by removing the subpackage for bundled dependencies:
rm -vrf nipy/externals/
# Now fix the imports. The find-then-modify pattern keeps us from discarding
# mtimes on any sources that do not need modification.
find . -type f -exec gawk \
    '/(from|import) (\.+|nipy\.)externals/ { print FILENAME }' '{}' '+' |
   xargs -r -t sed -r -i \
       -e 's/(from (nipy|\.*)\.externals )import/import/' \
       -e 's/from ((nipy|\.*)\.externals\.)([^ ]+) import/from \3 import/'
sed -r -i '/config\.add_subpackage\(.externals.\)/d' nipy/setup.py

# Remove bundled lapack
rm -rf lib/lapack_lite/

# Remove pre-generated Cython C sources
grep -FrlI 'Generated by Cython' . | xargs -r rm -vf

%py3_shebang_fix examples

cp -p nipy/algorithms/statistics/models/LICENSE.txt scipy-LICENSE.txt

# Remove doc dependency version pins, which we cannot respect
sed -r -i -e 's/(,<.*)$//' -e 's/==/>=/' doc-requirements.txt
# We don’t have a python-nose3 package (a fork and drop-in replacement for the
# deprecated python-nose). We also shouldn’t depend on the deprecated
# python-mock package if we can help it.
sed -r -i 's/^(nose3|mock)\b/# &/' dev-requirements.txt


%generate_buildrequires
%pyproject_buildrequires %{?with_doc_pdf:doc-requirements.txt}


%build
export NIPY_EXTERNAL_LAPACK=1

# Regenerate the Cython files
%make_build recythonize PYTHON='%{python3}'

%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="%{pyproject_build_lib}" PYTHON='%{python3}' \
   %make_build -C doc latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C doc/dist/latex LATEXMKOPTS='-quiet'
%endif


%install
export NIPY_EXTERNAL_LAPACK=1

%pyproject_install
%pyproject_save_files nipy

install -t '%{buildroot}%{_mandir}/man1' -m 0644 -p -D \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}'


%check
%if %{with tests}
mkdir -p for_testing
cd for_testing
PATH="%{buildroot}%{_bindir}:${PATH}" \
    PYTHONPATH='%{buildroot}%{python3_sitearch}' \
    PYTHONDONTWRITEBYTECODE=1 \
    %{python3} ../tools/nipnost --verbosity=3 nipy
%endif


%files -n python3-nipy -f %{pyproject_files}
%license LICENSE
%license scipy-LICENSE.txt

%{_bindir}/nipy_3dto4d
%{_bindir}/nipy_4d_realign
%{_bindir}/nipy_4dto3d
%{_bindir}/nipy_diagnose
%{_bindir}/nipy_tsdiffana

%{_mandir}/man1/nipy_3dto4d.1*
%{_mandir}/man1/nipy_4d_realign.1*
%{_mandir}/man1/nipy_4dto3d.1*
%{_mandir}/man1/nipy_diagnose.1*
%{_mandir}/man1/nipy_tsdiffana.1*


%files doc
%license LICENSE
%license scipy-LICENSE.txt

%doc AUTHOR
%doc Changelog
%doc README.rst
%doc THANKS

%if %{with doc_pdf}
%doc doc/dist/latex/nipy.pdf
%endif

%doc examples/


%changelog
%autochangelog
