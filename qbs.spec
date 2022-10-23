#global commit 40746dae36452398649481fecad9cdc5f25cc80f
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{name}-%{commit}
%else
%global source_folder %{name}-src-%{version}
%endif

Name:           qbs
# qbs was previously packaged as part of qt-creator, using the qt-creator version, hence the epoch bump
Epoch:          1
Version:        1.23.2
Release:        1%{?dist}
Summary:        Cross platform build tool

# See LGPL_EXCEPTION.txt
License:        LGPLv2 with exceptions and LGPLv3 with exceptions
URL:            https://wiki.qt.io/qbs
%if 0%{?commit:1}
Source0:        https://code.qt.io/cgit/qbs/qbs.git/snapshot/qbs-%{commit}.tar.xz
%else
Source0:        https://download.qt.io/official_releases/%{name}/%{version}/%{name}-src-%{version}.tar.gz
%endif

# Attempt to filter qbs debug output from stderr
Patch1:         qbs_tst_blackbox_stderr.patch
# Fix qmake detection
Patch2:         qbs_qmake.patch


BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-lxml
BuildRequires:  python3-beautifulsoup4
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qdoc
BuildRequires:  qt5-qhelpgenerator
BuildRequires:  qt5-qtscript-devel

# Needed for tests
BuildRequires:  glibc-static
%ifarch x86_64
BuildRequires:  libasan
BuildRequires:  libtsan
%endif
BuildRequires:  libstdc++-static
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel


%description
Qbs is a tool that helps simplify the build process for developing projects
across multiple platforms. Qbs can be used for any software project, regardless
of programming language, toolkit, or libraries used.

Qbs is an all-in-one tool that generates a build graph from a high-level
project description (like qmake or CMake) and additionally undertakes the task
of executing the commands in the low-level build graph (like make).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        examples
Summary:        Example projects using %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description    examples
The %{name}-examples package contains example files for using %{name}.

%package        doc
Summary:        Documentation for %{name}
License:        GFDL
BuildArch:      noarch

%description    doc
HTML documentation for %{name}.


%prep
%autosetup -p1 -n %{source_folder}


%build
%cmake \
    -DQBS_LIB_INSTALL_DIR=%{_libdir} \
    -DQBS_PLUGINS_INSTALL_BASE=%{_lib} \
    -DWITH_UNIT_TESTS=ON \
    -DQBS_ENABLE_RPATH=OFF \
    -DQBS_INSTALL_HTML_DOCS=ON
%cmake_build


%install
%cmake_install
install -Dpm 0644 doc/man/qbs.1 %{buildroot}%{_mandir}/man1/qbs.1

# Remove python dmgbuild code, it only works on macOS (#1559529)
rm -rf %{buildroot}%{_datadir}/qbs/python/mac_alias/
rm -rf %{buildroot}%{_datadir}/qbs/python/ds_store/
rm -rf %{buildroot}%{_datadir}/qbs/python/dmgbuild/
rm -rf %{buildroot}%{_datadir}/qbs/python/biplist/
rmdir %{buildroot}%{_datadir}/qbs/python/
rm -f %{buildroot}%{_libexecdir}/qbs/dmgbuild

# Don't package tests
rm %{buildroot}%{_bindir}/tst_*


%check
%ctest || :


%files
%license LICENSE.LGPLv21 LICENSE.LGPLv3 LGPL_EXCEPTION.txt
%doc README.md
%{_bindir}/%{name}*
%{_libdir}/%{name}/
%{_libdir}/libqbs*.so.1.23*
%{_libexecdir}/qbs/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%exclude %{_datadir}/%{name}/examples

%files devel
%{_includedir}/%{name}/
%{_libdir}/libqbs*.so

%files examples
%{_datadir}/%{name}/examples/

%files doc
%doc %{_defaultdocdir}/%{name}


%changelog
* Fri Oct 21 2022 Sandro Mani <manisandro@gmail.com> - 1:1.23.2-1
- Update to 1.23.2

* Wed Aug 17 2022 Sandro Mani <manisandro@gmail.com> - 1:1.23.1-1
- Update to 1.23.1

* Thu Jul 21 2022 Sandro Mani <manisandro@gmail.com> - 1:1.23.0-1
- Update to 1.23.0

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1:1.22.1-3
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1:1.22.1-2
- Rebuild (qt5)

* Fri Apr 29 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1:1.22.1-1
- Update to 1.22.1 (#2080246)

* Tue Mar 29 2022 Sandro Mani <manisandro@gmail.com> - 1:1.22.0-1
- Update to 1.22.0

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1:1.21.0-4
- Rebuild (qt5)

* Thu Feb 24 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1:1.21.0-3
- Fixing plugin path in runtime

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Sandro Mani <manisandro@gmail.com> - 1:1.21.0-1
- Update to 1.21.0

* Fri Oct 08 2021 Sandro Mani <manisandro@gmail.com> - 1:1.20.1-1
- Update to 1.20.1

* Tue Aug 31 2021 Sandro Mani <manisandro@gmail.com> - 1:1.20.0-1
- Update to 1.20.0

* Mon Jul 26 2021 Sandro Mani <manisandro@gmail.com> - 1:1.19.2-1
- Update to 1.19.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Sandro Mani <manisandro@gmail.com> - 1:1.19.1-1
- Update to 1.19.1

* Tue Jun 15 2021 Sandro Mani <manisandro@gmail.com> - 1.1.19.0-2
- Fix qmake detection
- Swiitch to cmake build

* Tue May 11 2021 Sandro Mani <manisandro@gmail.com> - 1.1.19.0-1
- Update to 1.19.0

* Tue May 04 2021 Sandro Mani <manisandro@gmail.com> - 1:1.18.2-1
- Update to 1.18.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Sandro Mani <manisandro@gmail.com> - 1:1.18.0-1
- Update to 1.18.0

* Mon Sep 07 2020 Marie Loise Nolden <loise@kde.org> - 1:1.17.0-1
- Update to 1.17.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Sandro Mani <manisandro@gmail.com> - 1:1.16.0-1
- Update to 1.16.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Sandro Mani <manisandro@gmail.com> - 1:1.15.0-1
- Update to 1.15.0

* Thu Nov 07 2019 Sandro Mani <manisandro@gmail.com> - 1:1.14.1-1
- Update to 1.14.1

* Thu Oct 10 2019 Sandro Mani <manisandro@gmail.com> - 1:1.14.0-1
- Update to 1.14.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Sandro Mani <manisandro@gmail.com> - 1:1.13.1-1
- Update to 1.13.1

* Tue Apr 16 2019 Sandro Mani <manisandro@gmail.com> - 1:1.13.0-1
- Update to 1.13.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.2-1
- Update to 1.12.2

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.1-1
- Update to 1.12.1

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.0-1
- Update to 1.12.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.0-0.3.git40746da
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.0-0.2.git40746da
- Add qbs_installheader.patch

* Thu Jun 07 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.0-0.1.git40746da
- Update to git 40746da

* Mon May 07 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.1-1
- Update to 1.11.1

* Wed Mar 28 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-1
- Update to 1.11.0

* Sun Mar 25 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.5.git8e39638
- Also remove %%{_libexecdir}/qbs/dmgbuild

* Fri Mar 23 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.4.git8e39638
- Remove python dmgbuild code, it only works on macOS (#1559529)

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.3.git8e39638
- Add missing BR: gcc-c++, make

* Thu Feb 08 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.2.git8e39638
- Add patch to install missing header

* Wed Feb 07 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.1.git8e39638
- Update to git 8e39638

* Fri Dec 08 2017 Sandro Mani <manisandro@gmail.com> - 1:1.10.0-1
- Update to 1.10.0

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 1:1.9.1-1
- Update to 1.9.1

* Tue Sep 05 2017 Sandro Mani <manisandro@gmail.com> - 1:1.9.0-1
- Update to 1.9.0

* Mon Jul 31 2017 Sandro Mani <manisandro@gmail.com> - 1:1.9.0-0.1.git998c698
- Update to latest git

* Sat Jul 29 2017 Sandro Mani <manisandro@gmail.com> - 1:1.8.1-2
- Add doc subpackage
- Enable tests

* Wed Jul 26 2017 Sandro Mani <manisandro@gmail.com> - 1:1.8.1-1
- Initial package
