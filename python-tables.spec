#global commit 16191801a53eddae8ca9380a28988c3b5b263c5e
%{?gitcommit:%global gitcommitshort %(c=%{gitcommit}; echo ${c:0:7})}

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Summary:        HDF5 support in Python
Name:           python-tables
Version:        3.8.0
Release:        %autorelease
#Source0:        https://github.com/PyTables/PyTables/archive/%{commit}/PyTables-%{commit}.tar.gz
Source0:        https://github.com/PyTables/PyTables/archive/v%{version}/python-tables-%{version}.tar.gz

# sometimes it doesn't get updated
%global manual_version 3.3.0

%bcond tests 1

Source1:        https://github.com/PyTables/PyTables/releases/download/v%{manual_version}/pytablesmanual-%{manual_version}.pdf
Patch1:         0001-Skip-tests-that-fail-on-s390x.patch
Patch2:         0002-Relax-dependency-on-blosc2.patch
Patch3:         0003-Fix-build-errors-when-compiled-using-cython-3.0.0b1.patch
Patch4:         0004-Fix-compatibility-with-numpu-v1.25.patch
Patch5:         0005-python3.12-cython-fix-slice-indexing.patch
Patch6:         0006-Add-workaround-for-staticmethod-invocation-error.patch
Patch7:         0007-Drop-misguided-check.patch

License:        BSD
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
%setup -n PyTables-%{version} -q

# https://github.com/PyTables/PyTables/issues/735
%ifarch s390x
%patch 1 -p1
%endif

%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1

cp -a %{SOURCE1} pytablesmanual.pdf

# Make sure we are not using anything from the bundled blosc by mistake
find c-blosc -mindepth 1 -maxdepth 1 -name hdf5 -prune -o -exec rm -r {} +

# circumvent the broken attempt to detect library location
sed -r -i \
  '/def get_blosc2_directories\(\):/a \ \ \ \ return "%{_includedir}","%{_libdir}"' \
  setup.py

%build
%py3_build

%install
chmod -x examples/check_examples.sh
sed -i 's|bin/env |bin/|' utils/*

%py3_install

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

%files -n python%{python3_pkgversion}-tables
%license LICENSE.txt LICENSES
%{_bindir}/ptdump
%{_bindir}/ptrepack
%{_bindir}/pt2to3
%{_bindir}/pttree
%{python3_sitearch}/tables/
%{python3_sitearch}/tables-%{version}*.egg-info/

%files doc
%license LICENSE.txt LICENSES
%doc pytablesmanual.pdf
%doc [A-KM-Za-z]*.txt
%doc examples/

%changelog
%autochangelog
