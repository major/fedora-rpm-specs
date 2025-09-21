Name:		python-isal
Version:	1.8.0
Release:	2%{?dist}
Summary:	Faster zlib and gzip compatible (de)compression using the ISA-L library
#		src/isal/crc32_combine.h is Zlib
License:	PSF-2.0 AND Zlib
URL:		https://github.com/pycompression/python-isal
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
#		Tweaks for building on EPEL 9
Patch0:		%{name}-old-setuptools-epel9.patch

ExcludeArch:	%{ix86}

BuildRequires:	gcc
BuildRequires:	isa-l-devel
BuildRequires:	pyproject-rpm-macros
BuildRequires:	python3-devel
BuildRequires:	python3-pip
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
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
%if %{?rhel}%{!?rhel:0} == 9
%patch -P0 -p1
%endif

# setuptools versions < 77 don't support PEP 639
# convert license key in pyproject.toml to old format for older versions
setuptoolsver=$(python3 -c "import setuptools; print(setuptools.__version__.split('.')[0])")
if [ $setuptoolsver -lt 77 ] ; then
    sed 's!^\(license\)\s*=\s*\(.*\)$!\1 = { text = \2 }!' -i pyproject.toml
fi

%build
export PYTHON_ISAL_LINK_DYNAMIC=1
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_ISAL=%{version}
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
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.8.0-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Thu Sep 11 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.8.0-1
- Update to version 1.8.0
- Drop patch accepted upstream

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.7.2-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.14

* Sat Mar 15 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.7.2-1
- Initial Fedora package
