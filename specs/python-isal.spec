Name:		python-isal
Version:	1.7.2
Release:	4%{?dist}
Summary:	Faster zlib and gzip compatible (de)compression using the ISA-L library
#		src/isal/crc32_combine.h is Zlib
License:	PSF-2.0 AND Zlib
URL:		https://github.com/pycompression/python-isal
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
#		https://github.com/pycompression/python-isal/pull/227
Patch0:		0001-Add-a-dummy-non-empty-environment-when-using-assert_.patch

ExcludeArch:	%{ix86}

BuildRequires:	gcc
BuildRequires:	isa-l-devel
BuildRequires:	pyproject-rpm-macros
BuildRequires:	python3-devel
BuildRequires:	python3-pip
BuildRequires:	python3-setuptools
BuildRequires:	python3-wheel
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-timeout
BuildRequires:	python3-test

%description
This package provides Python bindings for the ISA-L library.

The Intel(R) Intelligent Storage Acceleration Library (ISA-L)
implements several key algorithms in assembly language.

This includes a variety of functions to provide zlib/gzip compatible
compression and decompression.

%package -n python3-isal
Summary:	%{summary}
%py_provides	python3-isal

%description -n python3-isal
This package provides Python bindings for the ISA-L library.

The Intel(R) Intelligent Storage Acceleration Library (ISA-L)
implements several key algorithms in assembly language.

This includes a variety of functions to provide zlib/gzip compatible
compression and decompression.

%prep
%setup -q
%patch -P0 -p1

# The versioningit module extracts the version from the "version in git".
# We are building from a source archive that doesn't have the git version
# information.
# Make a fake versioningit module that hardcodes the version.
mkdir -p deps/versioningit
cat > deps/versioningit/__init__.py <<EOF
def get_version() -> str:
    return '%{version}'
EOF

# Create the _version.py file otherwise created by the versioningit module.
echo "__version__ = '%{version}'" > src/isal/_version.py

%build
export PYTHON_ISAL_LINK_DYNAMIC=1
export PYTHONPATH=deps
%pyproject_wheel

%install
%pyproject_install

%check
%pytest tests

%files -n  python3-isal
%{python3_sitearch}/isal
%{python3_sitearch}/isal-%{version}.dist-info
%license LICENSE

%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.7.2-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.14

* Sat Mar 15 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.7.2-1
- Initial Fedora package
