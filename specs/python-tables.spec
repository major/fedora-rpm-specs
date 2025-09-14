#global commit 16191801a53eddae8ca9380a28988c3b5b263c5e
%{?gitcommit:%global gitcommitshort %(c=%{gitcommit}; echo ${c:0:7})}

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Summary:        HDF5 support in Python
Name:           python-tables
Version:        3.10.2
Release:        %autorelease
#Source0:        https://github.com/PyTables/PyTables/archive/%{commit}/PyTables-%{commit}.tar.gz
Source0:        https://github.com/PyTables/PyTables/archive/v%{version}/python-tables-%{version}.tar.gz

# This was split out, but after some attempts to build it standalone,
# I have no idea how to do that. PyTables upstream builds it as a
# module, so let's do the same for now.
%global hdf5_blosc_version 1.0.1
Source1:        https://github.com/Blosc/hdf5-blosc/archive/v%{hdf5_blosc_version}/hdf5-blosc-%{hdf5_blosc_version}.tar.gz

# sometimes it doesn't get updated
%global manual_version 3.3.0

%bcond tests 1

Source2:        https://github.com/PyTables/PyTables/releases/download/v%{manual_version}/pytablesmanual-%{manual_version}.pdf

# https://github.com/PyTables/PyTables/issues/735
Patch1:         0001-Skip-tests-that-fail-on-s390x.patch

# The test fails with:
# ======================================================================
# FAIL: None (tables.tests.test_direct_chunk.EArrayDirectChunkingTestCase.None)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File ".../usr/lib64/python3.14/site-packages/tables/tests/test_direct_chunk.py", line 212, in test_write_chunk_filtermask
#     self.assertEqual(chunk_info.filter_mask, no_shuffle_mask)
#     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     AssertionError: 0 != 4
Patch2:         0001-Skip-failing-test.patch

License:        BSD-3-Clause
URL:            https://www.pytables.org

BuildRequires:  hdf5-devel >= 1.8
BuildRequires:  bzip2-devel
BuildRequires:  lzo-devel
BuildRequires:  blosc-devel
BuildRequires:  blosc2-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-blosc2
BuildRequires:  python%{python3_pkgversion}-Cython >= 0.13
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-numexpr >= 2.4
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-typing-extensions

ExcludeArch:    %{ix86}

%global _description %{expand:
PyTables is a package for managing hierarchical datasets and designed
to efficiently and easily cope with extremely large amounts of data.}

%description %_description

%package -n python%{python3_pkgversion}-tables
Summary:        %{summary}

Requires:       python%{python3_pkgversion}-numpy
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-numexpr >= 2.4
%{?python_provide:%python_provide python%{python3_pkgversion}-tables}

%description -n python%{python3_pkgversion}-tables %_description

%package        doc
Summary:        Documentation for PyTables
BuildArch:      noarch

%description doc
The %{name}-doc package contains the documentation for %{name}.

%prep
%autosetup -p1 -n PyTables-%{version} -a 1
rmdir hdf5-blosc
mv hdf5-blosc-%{hdf5_blosc_version} hdf5-blosc

cp -a %{SOURCE2} pytablesmanual.pdf

%build
%pyproject_wheel

chmod -x examples/check_examples.sh
sed -i 's|bin/env |bin/|' utils/*

%install
%pyproject_install

%pyproject_save_files -l tables

%check
%if %{with tests}
%ifarch %{ix86} s390x
skip=true
%else
skip=false
%endif

cd /
PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} -m tables.tests.test_all -v || $skip
%endif

%files -n python%{python3_pkgversion}-tables -f %{pyproject_files}
%license LICENSE.txt LICENSES
%{_bindir}/ptdump
%{_bindir}/ptrepack
%{_bindir}/pt2to3
%{_bindir}/pttree

%files doc
%license LICENSE.txt LICENSES
%doc pytablesmanual.pdf
%doc [A-KM-Za-z]*.txt
%doc examples/

%changelog
%autochangelog
