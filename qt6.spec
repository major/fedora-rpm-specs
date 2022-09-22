
Name: qt6
Version: 6.3.1
Release: 2%{?dist}
Summary: Qt6 meta package
License: GPLv3
URL: https://getfedora.org/
Source0: macros.qt6
Source1: macros.qt6-srpm
Source2: qmake-qt6.sh
BuildArch: noarch

Requires: qt6-qt3d
Requires: qt6-qt5compat
Requires: qt6-qtbase
Requires: qt6-qtbase-gui
Requires: qt6-qtbase-mysql
Requires: qt6-qtbase-postgresql
Requires: qt6-qtcharts
Requires: qt6-qtconnectivity
Requires: qt6-qtdatavis3d
Requires: qt6-qtdeclarative
Requires: qt6-qtdoc
Requires: qt6-qtimageformats
Requires: qt6-qtlocation
Requires: qt6-qtlottie
Requires: qt6-qtmultimedia
Requires: qt6-qtnetworkauth
Requires: qt6-qtquick3d
Requires: qt6-qtquicktimeline
Requires: qt6-qtremoteobjects
Requires: qt6-qtscxml
Requires: qt6-qtsensors
Requires: qt6-qtserialbus
Requires: qt6-qtserialport
Requires: qt6-qtshadertools
Requires: qt6-qtsvg
Requires: qt6-qttools
Requires: qt6-qtvirtualkeyboard
Requires: qt6-qtwayland
Requires: qt6-qtwebchannel
Requires: qt6-qtwebsockets


%description
%{summary}.

%package devel
Summary: Qt6 meta devel package
Requires: qt6-designer
Requires: qt6-linguist
Requires: qt6-qdoc
Requires: qt6-qhelpgenerator
Requires: qt6-qt3d-devel
Requires: qt6-qt5compat-devel
Requires: qt6-qtbase-devel
Requires: qt6-qtbase-static
Requires: qt6-qtcharts-devel
Requires: qt6-qtconnectivity-devel
Requires: qt6-qtdatavis3d-devel
Requires: qt6-qtdeclarative-devel
Requires: qt6-qtdeclarative-static
Requires: qt6-qtimageformats-devel
Requires: qt6-qtlocation-devel
Requires: qt6-qtlottie-devel
Requires: qt6-qtmultimedia-devel
Requires: qt6-qtnetworkauth-devel
Requires: qt6-qtquick3d-devel
Requires: qt6-qtquicktimeline-devel
Requires: qt6-qtremoteobjects-devel
Requires: qt6-qtscxml-devel
Requires: qt6-qtsensors-devel
Requires: qt6-qtserialbus-devel
Requires: qt6-qtserialport-devel
Requires: qt6-qtshadertools-devel
Requires: qt6-qtsvg-devel
Requires: qt6-qttools-devel
Requires: qt6-qttools-static
Requires: qt6-qtvirtualkeyboard-devel
Requires: qt6-qtwayland-devel
Requires: qt6-qtwebchannel-devel
Requires: qt6-qtwebsockets-devel
Requires: qt6-rpm-macros

%description devel
%{summary}.

%package rpm-macros
Summary: RPM macros for building Qt6 and KDE Frameworks 5 packages
Requires: cmake >= 3
Requires: gcc-c++
%description rpm-macros
%{summary}.

%package srpm-macros
Summary: RPM macros for source Qt6 packages
%description srpm-macros
%{summary}.


%install
install -Dpm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt6
install -Dpm644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt6-srpm
install -Dpm755 %{SOURCE2} %{buildroot}%{_bindir}/qmake-qt6.sh
mkdir -p %{buildroot}%{_datadir}/qt6/wrappers
ln -s %{_bindir}/qmake-qt6.sh %{buildroot}%{_datadir}/qt6/wrappers/qmake-qt6
ln -s %{_bindir}/qmake-qt6.sh %{buildroot}%{_datadir}/qt6/wrappers/qmake

# substitute custom flags, and the path to binaries: binaries referenced from
# macros should not change if an application is built with a different prefix.
# %_libdir is left as /usr/%{_lib} (e.g.) so that the resulting macros are
# architecture independent, and don't hardcode /usr/lib or /usr/lib64.
sed -i \
  -e "s|@@QT6_CFLAGS@@|%{?qt6_cflags}|g" \
  -e "s|@@QT6_CXXFLAGS@@|%{?qt6_cxxflags}|g" \
  -e "s|@@QT6_RPM_LD_FLAGS@@|%{?qt6_rpm_ld_flags}|g" \
  -e "s|@@QT6_RPM_OPT_FLAGS@@|%{?qt6_rpm_opt_flags}|g" \
  -e "s|@@QMAKE@@|%{_prefix}/%%{_lib}/qt6/bin/qmake|g" \
  -e "s|@@QMAKE_QT6_WRAPPER@@|%{_bindir}/qmake-qt6.sh|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt6

%if 0%{?metapackage}
mkdir -p %{buildroot}%{_docdir}/qt6
mkdir -p %{buildroot}%{_docdir}/qt6-devel
echo "- Qt6 meta package" > %{buildroot}%{_docdir}/qt6/README
echo "- Qt6 devel meta package" > %{buildroot}%{_docdir}/qt6-devel/README

%files
%{_docdir}/qt6/README

%files devel
%{_docdir}/qt6-devel/README
%endif

%files rpm-macros
%{_rpmmacrodir}/macros.qt6
%{_bindir}/qmake-qt6.sh
%{_datadir}/qt6/wrappers/

%files srpm-macros
%{_rpmmacrodir}/macros.qt6-srpm


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.1-1
- 6.3.1

* Wed Apr 13 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.0-1
- 6.3.0

* Mon Jan 31 2022 Jan Grulich <jgrulich@redhat.com> - 6.2.3-1
- 6.2.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.2-1
- 6.2.2

* Fri Oct 29 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.1-1
- 6.2.1

* Fri Oct 29 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0-2
- 6.2.1

* Thu Sep 30 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0-1
- 6.2.0

* Mon Sep 27 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc2-1
- 6.2.0 - rc2

* Tue Sep 21 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc-2
- Drop qt6-qtquickcontrols2 from required packages

* Sat Sep 18 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc-1
- 6.2.0 - rc

* Mon Sep 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~beta4-3
- Drop qt6_exclude_arch macro

* Mon Sep 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~beta4-2
- Add qt6_exclude_arch macro

* Fri Sep 10 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~beta4-1
- 6.2.0 - beta4

* Mon Aug 30 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~beta3-1
- 6.2.0 - beta3

* Thu Aug 12 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.2-1
- 6.1.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.1-1
- 6.1.1

* Mon May 24 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.0-2
- Fix path to libexecdir

* Thu May 06 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.0-1
- 6.1.0

* Mon Apr 05 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.3-1
- 6.0.3

* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0-1
- 6.0.0
