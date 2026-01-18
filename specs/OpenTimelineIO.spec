# NOTE: upstream has not added any SOVERSION to the C++ libraries.
# In order to avoid any possible ambiguity, this has been patched to
# add VERSION but no SOVERSION, so that **each version bump is treated
# as incompatible** and will require dependents to be rebuilt.
# https://github.com/AcademySoftwareFoundation/OpenTimelineIO/issues/1182

# C++ and Python APIs have different build paths,
# not well designed to be built together
%bcond python 0

%global rjcommit 24b5e7a8b27f42fa16b96fc70aade9106cf7102f

Name:           OpenTimelineIO
Version:        0.17.0
Release:        5%{?dist}
Summary:        Editorial timeline information API
# OpenTimelineIO is Apache-2.0, rapidjson is MIT
License:        Apache-2.0 AND MIT
URL:            https://github.com/AcademySoftwareFoundation/OpenTimelineIO
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/Tencent/rapidjson/archive/%{rjcommit}/rapidjson-%{rjcommit}.tar.gz

# Fix destination of libraries and cmake files, add VERSION to shared libraries
Patch0:         cmake-install.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Imath)
%if %{with python}
BuildRequires:  cmake(pybind11)
BuildRequires:  python3-devel
%endif

Provides:       bundled(rapidjson) = %{rjcommit}

%description
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references to
external media. It is not however, a container format for media.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Imath)

%description devel
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references to
external media. It is not however, a container format for media.

%if %{with python}
%package -n python3-%{name}
Summary:        Python interface for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references to
external media. It is not however, a container format for media.

%package tools
Summary:       Additional tools for %{name}
Requires:      python3-%{name} = %{version}-%{release}

%description tools
Additional tools for %{name}.

%endif

%prep
%autosetup -p1 -a1
# Imath: system version used via OTIO_FIND_MATH
# rapidjson: snapshot needed for APIs added since last release
find src/deps/{Imath,rapidjson} -delete
mv rapidjson-%{rjcommit} src/deps/rapidjson


%build
%cmake \
  -DOTIO_CXX_INSTALL=ON \
%if %{with python}
  -DOTIO_PYTHON_INSTALL=ON \
  -DOTIO_PYTHON_INSTALL_DIR=%{python3_sitearch} \
%endif
  -DOTIO_FIND_IMATH=ON \
  -DOTIO_SHARED_LIBS=ON \
  -DOTIO_DEPENDENCIES_INSTALL=OFF
%cmake_build


%install
%cmake_install


%files
%license LICENSE.txt NOTICE.txt
%doc README.md
%{_libdir}/libopentime.so.%{version}
%{_libdir}/libopentimelineio.so.%{version}

%files devel
%{_includedir}/opentime/
%{_includedir}/opentimelineio/
%{_libdir}/libopentime.so
%{_libdir}/libopentimelineio.so
%{_datadir}/cmake/opentime/
%{_datadir}/cmake/opentimelineio/

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/opentimelineio-%{version}.*/
%{python3_sitearch}/opentimelineio/
%{python3_sitearch}/opentimelineview/

%files tools
%{_bindir}/otio*
%endif


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Mar 27 2025 Steve Cossette <farchord@gmail.com> - 0.17.0-2
- Fix dependancy install issue

%autochangelog
