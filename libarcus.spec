Name:           libarcus
Version:        4.13.1
Release:        5%{?dist}
Summary:        Communication library between internal components for Ultimaker software
License:        LGPLv3+
URL:            https://github.com/Ultimaker/libArcus
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=1601917
Patch1:         libArcus-3.10.0-PyQt5.sip.patch
Patch2:         https://raw.githubusercontent.com/coryan/vcpkg/f69b85aa403b04e7d442c90db3418d484e44024f/ports/arcus/0001-fix-protobuf-deprecated.patch

BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-protobuf
BuildRequires:  python3-pyqt5-sip
BuildRequires:  python3-sip-devel
BuildRequires:  /usr/bin/sip
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core

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
Arcus library contains C++ code and Python 3 bindings for creating a socket in
a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

%package        devel

# The cmake scripts are BSD
License:        LGPLv3+ and BSD

Summary:        Development files for libarcus
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Arcus library contains C++ code and Python 3 bindings for creating a socket in
a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

Development files.

%package -n     python3-arcus
Summary:        Python 3 libArcus bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%{?python_provide:%python_provide python3-arcus}

%description -n python3-arcus
Arcus Python 3 bindings for creating a socket in a thread and using this
socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

%prep
%autosetup -n libArcus-%{version} -p1 -S git

# https://github.com/Ultimaker/libArcus/pull/94#issuecomment-505376760
sed -i 's/Python3_SITELIB/Python3_SITEARCH/' cmake/SIPMacros.cmake

%build
%cmake -DBUILD_EXAMPLES:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md TODO.md
%{_libdir}/libArcus.so.*

%files devel
%license LICENSE cmake/COPYING-CMAKE-SCRIPTS
%doc examples/example.cpp examples/example.proto
%{_libdir}/libArcus.so
%{_includedir}/Arcus
# Own the dir not to depend on cmake:
%{_libdir}/cmake

%files -n python3-arcus
%license LICENSE
%doc README.md TODO.md
%doc examples/example.py
%{python3_sitearch}/Arcus.so

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 4.13.1-3
- Rebuilt for Python 3.11

* Mon Apr 11 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 4.13.1-2
- Fix build failure with cmake 3.23+

* Tue Feb 01 2022 Gabriel Féron <feron.gabriel@gmail.com> - 4.13.1-1
- Update to 4.13.1

* Thu Jan 20 2022 Gabriel Féron <feron.gabriel@gmail.com> - 4.13.0-1
- Update to 4.13.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.12.1-1
- Update to 4.12.1

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 4.11.0-3
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 4.11.0-2
- Rebuilt for protobuf 3.18.1

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

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 4.8.0-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 09:45:36 CET 2021 Adrian Reber <adrian@lisas.de> - 4.8.0-2
- Rebuilt for protobuf 3.14

* Tue Dec 22 2020 Jan Pazdziora <jpazdziora@redhat.com> - 4.8.0-1
- Update to 4.8.0

* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 4.7.1-2
- Rebuilt for protobuf 3.13

* Thu Sep 03 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.1-1
- Update to 4.7.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 4.6.1-3
- Rebuilt for protobuf 3.12

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.6.1-2
- Rebuilt for Python 3.9

* Tue May 5 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.1

* Tue Apr 21 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 4.4.0-2
- Rebuild for protobuf 3.11

* Thu Nov 21 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.4.0-1
- Update to 4.4.0

* Fri Nov 01 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-5
- Make the dependency of python3-arcus on libarcus strict (#1767762)

* Mon Sep 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.0-4
- use python3-pyqt5-sip (#1748527#c12)

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

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5.1-3
- Rebuild for protobuf 3.6

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com>
- Use PyQt5.sip (#1601917)

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-1
- Update to 3.5.1 (#1644323)

* Tue Aug 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.4.1-2
- use more robust upstreamable sip_flags.patch (#1601917)

* Tue Aug 28 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-1
- Update to 3.4.1 (#1599716)

* Thu Aug 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.3.0-4
- Use PyQt5.sip (#1601917)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.7

* Wed May 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-1
- Update to 3.3.0 (#1571482)

* Mon Mar 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-1
- Update to 3.2.1 (#1523891)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-1
- Update to 3.1.0 (#1523891)
- Don't sed lib -> lib64 (not needed now)

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.0.3-3
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.3-2
- Rebuild for protobuf 3.4

* Fri Oct 20 2017 Charalampos Statakis <cstratak@redhat.com> - 3.0.3-1
- Update to 3.0.3

* Wed Aug 30 2017 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-1
- Update to 2.7.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-1
- Update to 2.6.1

* Tue Jun 27 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Tue Jun 13 2017 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-3
- Rebuilt for new protobuf 3.3.1

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Clarify licensing information on cmake files

* Wed Apr 26 2017 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Sat Mar 25 2017 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-1
- Initial package
