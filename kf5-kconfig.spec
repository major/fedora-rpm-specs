%global framework kconfig

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
#global docs 1
#global python_bindings 1
%global tests 1

%endif

%if 0%{?flatpak}
%global docs 0
%endif

# use ninja instead of make
%global ninja 1

Name:    kf5-%{framework}
Version: 5.105.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with advanced configuration system

License: GPLv2+ and LGPLv2+ and MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

## upstreamable patches

%if 0%{?ninja}
BuildRequires:  ninja-build
%endif

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}

BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Xml)

%if 0%{?python_bindings}
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  python3-clang
BuildRequires:  python3-PyQt5-devel
%else
Obsoletes: python3-pykf5-%{framework} < %{version}-%{release}
Obsoletes: pykf5-%{framework}-devel < %{version}-%{release}
%endif
Obsoletes: python2-pykf5-%{framework} < %{version}

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:       kf5-filesystem >= %{majmin}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

%description
KDE Frameworks 5 Tier 1 addon with advanced configuration system made of two
parts: KConfigCore and KConfigGui.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt5Xml)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        core
Summary:        Non-GUI part of KConfig framework
Requires:       kde-settings
%description    core
KConfigCore provides access to the configuration files themselves. It features
centralized definition and lock-down (kiosk) support.

%package        gui
Summary:        GUI part of KConfig framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    gui
KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.

%if 0%{?docs}
%package doc
Summary: API documentation for %{name}
BuildRequires: doxygen
BuildRequires: qt5-qdoc
BuildRequires: qt5-qhelpgenerator
BuildRequires: qt5-qtbase-doc
BuildRequires: make
Requires: kf5-filesystem
BuildArch: noarch
%description doc
%{summary}.
%endif

%if 0%{?python_bindings}
%package -n python3-pykf5-%{framework}
Summary: Python3 bindings for %{framework}
Requires: %{name} = %{version}-%{release}
%description -n python3-pykf5-%{framework}
%{summary}.

%package -n pykf5-%{framework}-devel
Summary: SIP files for %{framework} Python bindings
BuildArch: noarch
%description -n pykf5-%{framework}-devel
%{summary}.
%endif


%prep
%autosetup -n %{framework}-%{version} -p1


%build

%if 0%{?python_bindings:1}
PYTHONPATH=%{_datadir}/ECM/python
export PYTHONPATH
%endif

%cmake_kf5 \
  %if 0%{?flatpak}
  %{?docs:-DBUILD_QCH:BOOL=OFF} \
  %else
  %{?docs:-DBUILD_QCH:BOOL=ON} \
  %endif
  %{?ninja:-G Ninja} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build || \
cat %{__cmake_builddir}/autotests/kconfig_compiler/test5.cpp


%install
%cmake_install

%find_lang_kf5 kconfig5_qt


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
## cant use %%ninja_test here for some reason, doesn't inherit env vars from xvfb or dbus -- rex
xvfb-run -a \
%if 0%{?ninja}
ninja test %{?_smp_mflags} -v -C redhat-linux-build ||:
%else
make test %{?_smp_mflags} -C redhat-linux-build ARGS="--output-on-failure --timeout 300" ||:
%endif
%endif


%files
%doc DESIGN README.md TODO
%license LICENSES/*.txt

%ldconfig_scriptlets core

%files core -f kconfig5_qt.lang
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%{_kf5_bindir}/kreadconfig5
%{_kf5_bindir}/kwriteconfig5
%{_kf5_libdir}/libKF5ConfigCore.so.5*
%{_kf5_libdir}/libKF5ConfigQml.so.5*
%{_kf5_libexecdir}/kconfig_compiler_kf5
%{_kf5_libexecdir}/kconf_update

%ldconfig_scriptlets gui

%files gui
%{_kf5_libdir}/libKF5ConfigGui.so.*

%files devel
%{_kf5_includedir}/KConfig/
%{_kf5_includedir}/KConfigCore/
%{_kf5_includedir}/KConfigGui/
%{_kf5_includedir}/KConfigQml/
%{_kf5_libdir}/libKF5ConfigCore.so
%{_kf5_libdir}/libKF5ConfigGui.so
%{_kf5_libdir}/libKF5ConfigQml.so
%{_kf5_libdir}/cmake/KF5Config/
%{_kf5_archdatadir}/mkspecs/modules/qt_KConfigCore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KConfigGui.pri

%if 0%{?docs}
%files doc
%{_qt5_docdir}/KF5Config.qch
%{_qt5_docdir}/KF5Config.tags
%endif

%if 0%{?python_bindings}
%files -n python3-pykf5-%{framework}
%{python3_sitearch}/PyKF5/

%files -n pykf5-%{framework}-devel
%{_datadir}/sip/PyKF5/
%endif


%changelog
* Sun Apr 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.105.0-1
- 5.105.0

* Sat Mar 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.104.0-1
- 5.104.0

* Sun Feb 05 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.103.0-1
- 5.103.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.102.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.102.0-1
- 5.102.0

* Mon Dec 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.101.0-1
- 5.101.0
- use new macros to simplify code

* Sun Nov 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.100.0-1
- 5.100.0

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.99.0-1
- 5.99.0

* Thu Sep 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.98.0-1
- 5.98.0

* Sat Aug 13 2022 Justin Zobel <justin@1707.io> - 5.97.0-1
- Update to 5.97.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.96.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.96.0-1
- 5.96.0

* Fri May 13 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.94.0-1
- 5.94.0

* Sun Apr 10 2022 Justin Zobel <justin@1707.io> - 5.93-1
- Update to 5.93

* Thu Mar 10 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.92.0-1
- 5.92.0

* Fri Feb 11 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.91.0-1
- 5.91.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.90.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.90.0-2
- include Qml bindings

* Tue Jan 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 5.90.0-1
- 5.90.0

* Wed Dec 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.89.0-1
- 5.89.0

* Mon Nov 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.88.0-1
- 5.88.0

* Tue Oct 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.87.0-1
- 5.87.0

* Tue Sep 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.86.0-1
- 5.86.0

* Thu Aug 12 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.85.0-1
- 5.85.0

* Tue Jul 27 2021 Than Ngo <than@redhat.com> - 5.83.0-3
- Fix FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.83.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.83.0-1
- 5.83.0

* Mon May 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.82.0-1
- 5.82.0

* Tue Apr 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.81.0-1
- 5.81.0

* Sat Mar 20 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.80.0-2
- disabling docs for flatpak packages

* Tue Mar 09 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.80.0-1
- 5.80.0

* Wed Feb 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.79.0-3
- respin

* Sat Feb 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.79.0-2
- respin

* Sat Feb 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.79.0-1
- 5.79.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.78.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 08:41:58 CST 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.78.0-1
- 5.78.0

* Thu Dec 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.77.0-2
- re-enable autotests to highlight possible gcc-11 bug (#1907799)

* Sun Dec 13 14:09:46 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.77.0-1
- 5.77.0
- disable tests FTBFS

* Thu Nov 19 08:57:32 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.76.0-1
- 5.76.0

* Wed Oct 14 09:48:40 CDT 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.75.0-1
- 5.75.0

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.74.0-1
- 5.74.0

* Mon Aug 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.73.0-1
- 5.73.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.72.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.72.0-3
- -doc: Requires: kf5-filesystem

* Tue Jul 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.72.0-2
- use %%cmake macros more
- enable -doc subpkg (qch docs)

* Tue Jul 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.72.0-1
- 5.72.0

* Tue Jun 16 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.71.0-1
- 5.71.0

* Mon May 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.70.0-1
- 5.70.0

* Tue Apr 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.69.0-1
- 5.69.0

* Fri Mar 20 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.68.0-1
- 5.68.0

* Sun Feb 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.67.0-1
- 5.67.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.66.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Rex Dieter <rdieter@fedoraproject.org>
- 5.66.0

* Tue Dec 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.65.0-1
- 5.65.0

* Fri Nov 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.64.0-1
- 5.64.0

* Tue Oct 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.63.0-1
- 5.63.0

* Mon Sep 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.62.0-1
- 5.62.0

* Wed Aug 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.61.0-1
- 5.61.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.60.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.60.0-1
- 5.60.0

* Thu Jun 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.59.0-1
- 5.59.0

* Tue May 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.58.0-1
- 5.58.0

* Tue Apr 09 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.57.0-1
- 5.57.0

* Tue Mar 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.56.0-1
- 5.56.0

* Mon Feb 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.55.0-1
- 5.55.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.54.0-1
- 5.54.0

* Sun Dec 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.53.0-1
- 5.53.0

* Sun Nov 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.52.0-1
- 5.52.0

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.51.0-1
- 5.51.0

* Fri Sep 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.50.0-2
- disable python on f29+

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.50.0-1
- 5.50

* Tue Aug 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.49.0-1
- 5.49.0

* Wed Aug 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.48.0-3
- python: support on f29+ again, add Obsoletes otherwise (like ppc64/s390x) (#1610422)
- macro'ize ninja support
- .spec cosmetics (whitespace mostly)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.48.0-1
- 5.48.0

* Thu Jun 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.47.0-2
- cleanup
- use pkgconfig(Qt5...) style deps
- use %%majmin %%make_build %%find_lang_kf5 %%ldconfig_scriptlets

* Sat Jun 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.47.0-1
- 5.47.0

* Sat May 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.46.0-1
- 5.46.0

* Sun Apr 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.45.0-1
- 5.45.0

* Sat Mar 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.44.0-1
- 5.44.0

* Wed Feb 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.43.0-1
- 5.43.0

* Mon Jan 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.0-1
- 5.42.0

* Mon Dec 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.41.0-1
- 5.41.0

* Fri Nov 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-1
- 5.40.0

* Thu Oct 19 2017 Troy Dawson <tdawson@redhat.com> - 5.39.0-2
- Cleanup spec file conditionals

* Sun Oct 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.39.0-1
- 5.39.0

* Wed Sep 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-5
- (re)enable python, use ninja

* Wed Sep 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-4
- disable python, failing on arm7hl, aarch64, ppc64le archs

* Wed Sep 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-3
- enable python bindings

* Wed Sep 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-2
- cosmetics, support %%bootstrap, autotests
- initial support for python bindings (not ready yet)

* Mon Sep 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-1
- 5.38.0

* Fri Aug 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.37.0-1
- 5.37.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.36.0-1
- 5.36.0

* Sun Jun 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.35.0-1
- 5.35.0

* Mon May 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.34.0-1
- 5.34.0

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.33.0-1
- 5.33.0

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.32.0-1
- 5.32.0

* Mon Feb 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.31.0-1
- 5.31.0

* Fri Dec 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.29.0-1
- 5.29.0

* Fri Dec 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.29.0-1
- 5.29.0

* Mon Oct 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Wed Sep 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.26.0-1
- KDE Frameworks 5.26.0

* Mon Aug 08 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.25.0-1
- KDE Frameworks 5.25.0

* Wed Jul 06 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.24.0-1
- KDE Frameworks 5.24.0

* Tue Jun 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.23.0-1
- KDE Frameworks 5.23.0

* Mon May 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.22.0-1
- KDE Frameworks 5.22.0

* Mon May 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-2
- update URL

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-1
- KDE Frameworks 5.21.0

* Mon Mar 14 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.20.0-1
- KDE Frameworks 5.20.0

* Thu Feb 11 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.19.0-1
- KDE Frameworks 5.19.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Rex Dieter <rdieter@fedoraproject.org> 5.18.0-2
- cosmetics, update URL, use %%license, -BR: cmake

* Sun Jan 03 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.18.0-1
- KDE Frameworks 5.18.0

* Tue Dec 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.17.0-1
- KDE Frameworks 5.17.0

* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.16.0-1
- KDE Frameworks 5.16.0

* Tue Oct 20 2015 Rex Dieter <rdieter@fedoraproject.org> 5.15.0-2
- restore/upstream fullpath patch, BR: cmake, sort BR's

* Thu Oct 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.15.0-1
- KDE Frameworks 5.15.0

* Wed Sep 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.14.0-1
- KDE Frameworks 5.14.0

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Tue Aug 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-0.1
- KDE Frameworks 5.13

* Thu Jul 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.12.0-1
- 5.12.0

* Thu Jul 09 2015 Rex Dieter <rdieter@fedoraproject.org> 5.11.0-3
- update URL, minor cosmetics

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Daniel Vrátil <dvratil@redhat.com> - 5.11.0-1
- KDE Frameworks 5.11.0

* Tue May 12 2015 Rex Dieter <rdieter@fedoraproject.org> 5.10.0-3
- followup fix to sm patch

* Mon May 11 2015 Rex Dieter <rdieter@fedoraproject.org> 5.10.0-2
- pull in reviewed/upstreamed session management fixes (kde#346768)

* Mon May 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.10.0-1
- KDE Frameworks 5.10.0

* Sat May 09 2015 Rex Dieter <rdieter@fedoraproject.org> 5.9.0-3
- Candidate session management fixes (kde#346768)

* Wed Apr 15 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.9.0-2
- -core: Requires: kde-settings
- .spec cosmetics

* Tue Apr 07 2015 Daniel Vrátil <dvratil@redhat.com> - 5.9.0-1
- KDE Frameworks 5.9.0

* Mon Mar 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.8.0-1
- KDE Frameworks 5.8.0

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-2
- Rebuild (GCC 5)

* Mon Feb 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-1
- KDE Frameworks 5.7.0

* Thu Jan 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-1
- KDE Frameworks 5.6.0

* Mon Dec 08 2014 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-1
- KDE Frameworks 5.5.0

* Mon Nov 03 2014 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- KDE Frameworks 5.4.0

* Tue Oct 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- KDE Frameworks 5.3.0

* Thu Sep 11 2014 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- KDE Frameworks 5.2.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- KDE Frameworks 5.1.0

* Wed Jul 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- KDE Frameworks 5.0.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.100.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-1
- KDE Frameworks 4.100.0

* Tue May 20 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-3
- Fix license and description
- Add %%post and %%postun to subpackages

* Tue May 06 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-2
- Rebuild against updated kf5-rpm-macros

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-1
- KDE Frameworks 4.99.0

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140205git
- Update to pre-release snapshot of 4.96.0

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
