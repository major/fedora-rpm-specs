%global pkg_name libpkgmanifest

%global forgeurl https://github.com/rpm-software-management/%{pkg_name}

%global version_major 0
%global version_minor 6
%global version_patch 0

%bcond_with    docs
%bcond_without python
%bcond_without tests

Name:       %{pkg_name}
Version:    %{version_major}.%{version_minor}.%{version_patch}
Release:    5%{?dist}

%forgemeta

Summary:    Library for working with RPM manifests
License:    LGPL-2.1-or-later
URL:        %{forgeurl}
Source:     %{forgesource}
Patch1:     0001-Bump-a-version-to-0.6.0.patch
Patch2:     0002-spec-Package-COPYING.lib-not-LICENSE.patch
Patch3:     0003-Move-from-automatic-release-numbering-to-manual-one.patch

BuildRequires:  pkgconf-pkg-config
BuildRequires:  cmake >= 3.16
BuildRequires:  pkgconfig(yaml-cpp) >= 0.7.0
BuildRequires:  pkgconfig(rpm)

%if "%{toolchain}" == "clang"
BuildRequires:  clang
%else
BuildRequires:  gcc-c++ >= 10.1
%endif

%if %{with tests}
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
%endif

%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  swig >= 4.2.0
%endif

%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%description
%{name} is a C++ library for parsing and generating RPM manifests.

%files -n %{name}
%{_libdir}/%{name}.so.0
%license COPYING.LIB
%doc README.md

%package -n %{name}-devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
Development files for %{name}.

%files -n %{name}-devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%doc docs/design

%if %{with python}
%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary:        Python 3 bindings for the %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python 3 bindings for the %{name} library.

%files -n python3-%{name}
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-*.dist-info
%endif

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
    -DWITH_DOCS=%{?with_docs:ON}%{!?with_docs:OFF} \
    -DWITH_PYTHON=%{?with_python:ON}%{!?with_python:OFF} \
    -DWITH_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
    -DWITH_CODE_COVERAGE=OFF \
    \
    -DVERSION_MAJOR=%{version_major} \
    -DVERSION_MINOR=%{version_minor} \
    -DVERSION_PATCH=%{version_patch}
%cmake_build

%check
%if %{with tests}
    %ctest
%endif

%install
%cmake_install

%changelog
* Fri Sep 18 2026 Petr Pisar <ppisar@redhat.com> - 0.6.0-5
- Move from automatic release numbering to manual one

* Fri Sep 18 2026 Petr Písař <ppisar@redhat.com> - 0.6.0-4
- Fix dangling symbolic link from a LICENSE file

* Fri Sep 18 2026 Petr Písař <ppisar@redhat.com> - 0.6.0-3
- Fix a pkg-config file version

* Wed Sep 16 2026 Packit <hello@packit.dev> - 0.6.0-1
- Update to 0.6.0 upstream release

* Wed Jul 22 2026 Python Maint <python-maint@redhat.com> - 0.5.9-10
- Rebuilt for Python 3.15.0b4 ABI change

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Wed Jun 03 2026 Python Maint <python-maint@redhat.com> - 0.5.9-8
- Rebuilt for Python 3.15

* Fri Jan 30 2026 Petr Písař <ppisar@redhat.com> - 0.5.9-7
- Fix building with GCC 16 (bug #2434767)

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.5.9-5
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.5.9-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.5.9-2
- Rebuilt for Python 3.14

* Thu Apr 03 2025 Packit <hello@packit.dev> - 0.5.9-1
- Update to 0.5.9 upstream release
