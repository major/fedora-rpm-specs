# disable kdeplasma component since plasma5 porting is not finished
# https://github.com/a-rodin/qstardict/issues/14
%global with_kdeplasma 0

Name:       qstardict
Version:    1.3
Release:    27%{?dist}
Summary:    StarDict clone written using Qt
License:    GPLv2+
URL:        http://qstardict.ylsoftware.com/
Source0:    https://github.com/a-rodin/qstardict/archive/qstardict-%{version}.tar.gz


BuildRequires: make
BuildRequires:  glib2-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-knotifications-devel
%if %with_kdeplasma
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5ConfigWidgets)
%endif

# This project is using private headers
BuildRequires:  qt5-qtbase-private-devel

# exclude provate provides
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*\.so$

%description
QStarDict is a StarDict clone written using Qt. The user interface
is similar to StarDict.

Main features:
* Full support of StarDict dictionaries
* Working from the system tray
* Scanning mouse selection and showing pop-up windows with translation of
selected words
* Translations reformatting
* Pronouncing of the translated words
* Plugins support

%if %with_kdeplasma
%package -n kde-plasma-%{name}
Summary:    Plasma applet of qstardict
Requires:   %{name} = %{version}-%{release}
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

%description -n kde-plasma-%{name}
This package contains KDE plasma applet of qstardict.

%endif

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%qmake_qt5 PLUGINS_DIR=%{_libdir}/%{name}/plugins QMAKE_LRELEASE=lrelease-qt5
make %{?_smp_mflags}

%if %with_kdeplasma
# Build plasma applet
cd kdeplasma
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake_kf5 .. -DCMAKE_INCLUDE_CURRENT_DIR=ON
popd
make %{?_smp_mflags} -C %{_target_platform}
%endif

%install
make install INSTALL_ROOT=%{buildroot}

%if %with_kdeplasma
pushd kdeplasma
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
popd
%endif

desktop-file-install --vendor="" \
    --dir=%{buildroot}%{_datadir}/applications              \
     %{buildroot}%{_datadir}/applications/%{name}.desktop

rm -fr %{buildroot}%{_docdir}

%files
%doc AUTHORS ChangeLog README THANKS
%license COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%if %with_kdeplasma
%files -n kde-plasma-%{name}
%{_kde4_libdir}/kde4/*.so
%{_kde4_datadir}/kde4/services/*.desktop
%endif


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.3-26
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.3-25
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.3-24
- Rebuild (qt5)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3-20
- drop hard-coded Qt runtime dep (apparently not needed)

* Mon Nov 23 07:54:51 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1.3-19
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.3-18
- rebuild (qt5)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3-16
- rebuild (qt5)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.3-14
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.3-13
- rebuild (qt5)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.3-11
- rebuild (qt5)

* Mon Mar 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.3-10
- rebuild (qt5)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3-8
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 1.3-7
- rebuild (qt5)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3-5
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3-4
- rebuild (qt5)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 1.3-3
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.3-1
- Update to 1.3 (#1538071)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-9
- Remove obsolete scriptlets

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 1.2-8
- rebuild (qt5)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.2-7
- rebuild (qt5)

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.2-6
- BR: qt5-qtbase-private-devel

* Wed Oct 11 2017 Jan Grulich <jgrulich@redhat.com> - 1.2-5
- rebuild (qt5)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Robin Lee <cheeselee@fedoraproject.org> - 1.2-2
- rebuild (qt5)

* Fri May 12 2017 Robin Lee <cheeselee@fedoraproject.org> - 1.2-1
- Update to 1.2
- Build with qt5, and don't build kde plasma component

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1-2
- use %%qmake_qt4 macro to ensure proper build flags

* Mon Jan 25 2016 Robin Lee <cheeselee@fedoraproject.org> - 1.1-1
- Update to 1.1
- Dropped qstardict-1.0.1-glib-2.31.patch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan  6 2012 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-2
- Rebuild against GCC 4.7
- Incorporate a patch to solve GLib 2.31 compatibility

* Mon Dec  5 2011 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sun Oct  9 2011 Robin Lee <cheeselee@fedoraproject.org> - 1.0-2
- Popup window saves settings (#743715)
- Filter the private so provides

* Sun Jul 31 2011 Robin Lee <cheeselee@fedoraproject.org> - 1.0-1
- Update to 1.0
- Other specfile cleanups

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Mar 12 2010 Cheese Lee <cheeselee@126.com> - 0.13.1-3
- Included a manpage from Debian
- Updated summary and description
- Initial import to Fedora repositories

* Mon Mar  1 2010 Cheese Lee <cheeselee@126.com> - 0.13.1-2
- License chagned to GPLv2+
- BR: qt-devel, cmake removed, kdelibs-devel changed to kdelibs4-devel
- Removed the explicit claim for certain plugins
- Explicitly link to libX11.so for the change of DSO linking of F13

* Sun Feb 14 2010 Cheese Lee <cheeselee@126.com> - 0.13.1-1
- Initial packaging for Fedora based on the spec file from Mandriva
