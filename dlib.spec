%global	majorver 24

%global commit 65bce59a1512cf222dec01d3e0f29b612dd181f5
%global commitdate 20220905
%global shortcommit  %(c=%{commit}; echo ${c:0:9})

Name:		dlib
Version:	19.%{majorver}
Release:	%autorelease -s %{commitdate}git%{shortcommit}
Summary:	A modern C++ toolkit containing machine learning algorithms

License:	Boost
URL:		http://dlib.net
%{!?shortcommit:
Source:	http://dlib.net/files/%{name}-%{version}.tar.bz2
}
%{?shortcommit:
Source:		http://github.com/davisking/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
}

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	cmake(pybind11)
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
# BLAS and LAPACK support
BuildRequires:	pkgconfig(flexiblas)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(x11)
BuildRequires:	python3dist(setuptools)

# Failed to build to ppc64le
ExcludeArch:	ppc64le

%description
Dlib is a general purpose cross-platform open source software library written
in the C++ programming language. Its design is heavily influenced by ideas from
design by contract and component-based software engineering. It contains
components for dealing with networking, threads, graphical user interfaces,
data structures, linear algebra, machine learning, image processing, data
mining, XML and text parsing, numerical optimization, Bayesian networks, and
numerous other tasks.


%package devel
Summary:	Development files for dlib
License:	Boost and Public Domain
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Dlib is a general purpose cross-platform open source software library written
in the C++ programming language. This package contains development files for
the library.


%package -n python3-%{name}
Summary:	Python 3 interface to %{name}
License:	Boost and Public Domain
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Dlib is a general purpose cross-platform open source software library written
in the C++ programming language. This package contains Python 3 API for the
library.


%package doc
Summary:	Documentation for dlib
License:	Boost and Public Domain and CC-BY-SA
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Dlib is a general purpose cross-platform open source software library written
in the C++ programming language. This package contains the library
documentation and examples.


%prep
%{!?shortcommit:
%autosetup -p1
}
%{?shortcommit:
%autosetup -n %{name}-%{commit}
}
find docs -type f -exec chmod 644 {} +
find examples -type f -exec chmod 644 {} +

# unbundle pybind11, see https://bugzilla.redhat.com/2098694
rm -r dlib/external/pybind11
sed -i 's@add_subdirectory(../../dlib/external/pybind11 pybind11_build)@find_package(pybind11 CONFIG)@' tools/python/CMakeLists.txt

%build
%cmake
%cmake_build

# this is really needed: in the python tools build it's enabled by
# default and we do not want that. see
# https://github.com/davisking/dlib/commit/fbd117804758bd9174a27ce471acfe21b8bfc208
# and https://github.com/davisking/dlib/issues/111
#%%global py_setup_args --no USE_SSE4_INSTRUCTIONS
%py3_build


%install
%cmake_install

rm -f %{buildroot}/%{_libdir}/*.a
rm -f %{buildroot}/%{_docdir}/%{name}/LICENSE.txt
# Remove Sphinx build leftovers
rm -f %%{buildroot}/%{_docdir}/%{name}-doc/docs/python/.buildinfo

%py3_install
# Some files got ambiguous python shebangs, we fix them after everything else is done
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitearch}/

find %{buildroot} -name '.*' -exec rm -rf {} +

%files
%license dlib/LICENSE.txt
%{_libdir}/libdlib.so.19*

%files devel
%{_libdir}/libdlib.so
%{_includedir}/dlib/
%{_libdir}/cmake/dlib/
%{_libdir}/pkgconfig/*.pc

%files -n python3-%{name}
%license dlib/LICENSE.txt
%license python_examples/LICENSE_FOR_EXAMPLE_PROGRAMS.txt
%{python3_sitearch}/_%{name}_pybind11%{python3_ext_suffix}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-*.egg-info/

%files doc
%license examples/LICENSE_FOR_EXAMPLE_PROGRAMS.txt
%license examples/video_frames/license.txt
#%%doc documentation.html
%doc docs
#%%doc docs/python/_static/{jquery,underscore}.js
%doc examples


%changelog
%autochangelog
