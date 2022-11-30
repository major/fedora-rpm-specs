Name:           libsavitar
Version:        4.13.1
Release:        4%{?dist}
Summary:        C++ implementation of 3mf loading with SIP Python bindings
License:        LGPLv3+
URL:            https://github.com/Ultimaker/libSavitar
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         %{name}-no-pugixml.patch

BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pugixml-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sip-devel
BuildRequires:  /usr/bin/sip

# we add a dependency on setuptools to provide the distutils module
# upstream already removed the distutils usage in version 5+
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%description
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

%package        devel

# The cmake scripts are BSD
License:        LGPLv3+ and BSD

Summary:        Development files for libsavitar
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

Development files.

%package -n     python3-savitar
Summary:        Python 3 libSavitar bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-savitar}

%description -n python3-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

The Python bindings.

%prep
%autosetup -n libSavitar-%{version} -p1 -S git

# Wrong end of line encoding
dos2unix README.md

# Bundling
rm pugixml -rf
sed -i 's|"../pugixml/src/pugixml.hpp"|<pugixml.hpp>|g' src/*.cpp src/*.h

# https://github.com/Ultimaker/libSavitar/pull/18
sed -i 's/Python3_SITELIB/Python3_SITEARCH/' cmake/SIPMacros.cmake

%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libSavitar.so.*

%files devel
%license LICENSE cmake/COPYING-CMAKE-SCRIPTS
%{_libdir}/libSavitar.so
%{_includedir}/Savitar
# Own the dir not to depend on cmake:
%{_libdir}/cmake

%files -n python3-savitar
%license LICENSE
%doc README.md
%{python3_sitearch}/Savitar.so

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 4.13.1-3
- Rebuilt for Python 3.11

* Mon Mar 28 2022 Miro Hrončok <mhroncok@redhat.com> - 4.13.1-2
- Fix build failure with cmake 3.23+
- Fixes: rhbz#2069148

* Tue Feb 01 2022 Gabriel Féron <feron.gabriel@gmail.com> - 4.13.1-1
- Update to 4.13.1

* Thu Jan 20 2022 Gabriel Féron <feron.gabriel@gmail.com> - 4.13.0-1
- Update to 4.13.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.12.1-1
- Update to 4.12.1

* Wed Sep 15 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.11.0-1
- Update to 4.11.0

* Mon Aug 16 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.10.0-1
- Update to 4.10.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.9.1-1
- Update to 4.9.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.9.0-2
- Rebuilt for Python 3.10

* Mon Apr 26 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.9.0-1
- Update to 4.9.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Jan Pazdziora <jpazdziora@redhat.com> - 4.8.0-1
- Update to 4.8.0

* Thu Sep 03 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.1-1
- Update to 4.7.1

* Mon Aug 31 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.6.1-2
- Rebuilt for Python 3.9

* Tue May 5 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.1-1
- Update to 4.6.1

* Tue Apr 21 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.4.0-1
- Update to 4.4.0

* Fri Nov 01 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-4
- Make the dependency of python3-savitar on libsavitar strict (#1767762)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Wed Apr 03 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Gabriel Féron <feron.gabriel@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-2
- Use PyQt5.sip (#1601917)

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-1
- Update to 3.5.1 (#1644323)

* Tue Aug 28 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-1
- Update to 3.4.1 (#1599715)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.7

* Wed May 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-1
- Update to 3.3.0 (#1571783)

* Mon Mar 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Fix license tag (AGPLv3+ to LGPLv3+)

* Mon Mar 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-1
- Update to 3.2.1 (#1523886)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-1
- Update to 3.1.0 (#1523886)
- Don't sed lib -> lib64 (not needed now)

* Mon Oct 23 2017 Miro Hrončok <mhroncok@redhat.com> - 3.0.3-1
- Update to 3.0.3 (#1505189)

* Wed Aug 30 2017 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-1
- Update to 2.7.0 (#1486731)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-1
- Updated to 2.6.1 (#1465417)

* Tue Jun 27 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-1
- Updated to 2.6.0 (#1465417)

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 0-0.1.20170501git1ad7ddb
- New package
