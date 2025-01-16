Name:    qt5-doc
Summary: Qt5 - Complete documentation
Version: 5.15.16
Release: 1%{?dist}
BuildArch: noarch

# Automatically converted from old format: GFDL - review is highly recommended.
License: LicenseRef-Callaway-GFDL
# The tarball for this docs are self generated through provided script on SOURCES generate-qt-doc.sh
Url: http://qt-project.org/
Source0: qt-doc-opensource-src-%{version}.tar.xz
Source1: generate-qt-doc.sh

# optimize build, skip unecessary steps
%global debug_package   %{nil}
%global __spec_install_post %{nil}

BuildRequires: qt5-rpm-macros >= 5.5.0

Obsoletes: qt5-qtcanvas3d-doc < 5.13

Requires: qt5-qtbase-doc >= %{version}
Requires: qt5-qt3d-doc >= %{version}
Requires: qt5-qtcharts-doc >= %{version}
Requires: qt5-qtconnectivity-doc >= %{version}
Requires: qt5-qtdeclarative-doc >= %{version}
Requires: qt5-qtgraphicaleffects-doc >= %{version}
Requires: qt5-qtimageformats-doc >= %{version}
Requires: qt5-qtlocation-doc >= %{version}
Requires: qt5-qtmultimedia-doc >= %{version}
Requires: qt5-qtquickcontrols2-doc >= %{version}
Requires: qt5-qtquickcontrols-doc >= %{version}
Requires: qt5-qtscript-doc >= %{version}
Requires: qt5-qtscxml-doc >= %{version}
Requires: qt5-qtsensors-doc >= %{version}
Requires: qt5-qtserialbus-doc >= %{version}
Requires: qt5-qtserialport-doc >= %{version}
Requires: qt5-qtsvg-doc >= %{version}
Requires: qt5-qttools-doc >= %{version}
Requires: qt5-qtvirtualkeyboard-doc >= %{version}
Requires: qt5-qtwebchannel-doc >= %{version}
Requires: qt5-qtwebsockets-doc >= %{version}
Requires: qt5-qtx11extras-doc >= %{version}
Requires: qt5-qtxmlpatterns-doc >= %{version}
Requires: qt5-qtdatavis3d-doc >= %{version}
Requires: qt5-qtgamepad-doc >= %{version}
Requires: qt5-qtlocation-doc >= %{version}
Requires: qt5-qtwayland-doc >= %{version}
Requires: qt5-qtwebview-doc >= %{version}
Requires: qt5-qtspeech-doc >= %{version}
Requires: qt5-qtremoteobjects-doc >= %{version}
Requires: qt5-qtcharts-doc >= %{version}
Requires: qt5-qtpurchasing-doc >= %{version}

%description
This is the meta package for all Qt library documentation

# Empty files to produce qt5-doc package for easier installation of complete documentation
%files

%package -n qt5-qtbase-doc
Summary: Documentation for qtbase

%description -n qt5-qtbase-doc
%{summary}.

%files -n qt5-qtbase-doc
%{_qt5_docdir}/qmake*
%{_qt5_docdir}/qtconcurrent*
%{_qt5_docdir}/qtcore*
%{_qt5_docdir}/qtdbus*
%{_qt5_docdir}/qtgui*
%{_qt5_docdir}/qtnetwork*
%{_qt5_docdir}/qtopengl*
%{_qt5_docdir}/qtplatformheaders*
%{_qt5_docdir}/qtprintsupport*
%{_qt5_docdir}/qtsql*
%{_qt5_docdir}/qtwidgets*
%{_qt5_docdir}/qtxml*
%{_qt5_docdir}/qttestlib*

%package -n qt5-qt3d-doc
Summary: Documentation for qt3d

%description -n qt5-qt3d-doc
%{summary}.

%files -n qt5-qt3d-doc
%{_qt5_docdir}/qt3d*

%package -n qt5-qtcharts-doc
Summary: Documentation for qtcharts

%description -n qt5-qtcharts-doc
%{summary}.

%files -n qt5-qtcharts-doc
%{_qt5_docdir}/qtcharts*
%{_qt5_docdir}/qtlabs*

%package -n qt5-qtconnectivity-doc
Summary: Documentation for qtconnectivity

%description -n qt5-qtconnectivity-doc
%{summary}.

%files -n qt5-qtconnectivity-doc
%{_qt5_docdir}/qtbluetooth*
%{_qt5_docdir}/qtnfc*

%package -n qt5-qtdeclarative-doc
Summary: Documentation for qtdeclarative

%description -n qt5-qtdeclarative-doc
%{summary}.

%files -n qt5-qtdeclarative-doc
%{_qt5_docdir}/qtqml*
%{_qt5_docdir}/qtquick*

%package -n qt5-qtgraphicaleffects-doc
Summary: Documentation for qtgraphicaleffects

%description -n qt5-qtgraphicaleffects-doc
%{summary}.

%files -n qt5-qtgraphicaleffects-doc
%{_qt5_docdir}/qtgraphicaleffects*

%package -n qt5-qtimageformats-doc
Summary: Documentation for qtimageformats

%description -n qt5-qtimageformats-doc
%{summary}.

%files -n qt5-qtimageformats-doc
%{_qt5_docdir}/qtimageformats*

%package -n qt5-qtmultimedia-doc
Summary: Documentation for qtmultimedia

%description -n qt5-qtmultimedia-doc
%{summary}.

%files -n qt5-qtmultimedia-doc
%{_qt5_docdir}/qtmultimedia*

%package -n qt5-qtquickcontrols2-doc
Summary: Documentation for qtquickcontrols2

%description -n qt5-qtquickcontrols2-doc
%{summary}.

%files -n qt5-qtquickcontrols2-doc
%{_qt5_docdir}/qtquickcontrols/

%package -n qt5-qtquickcontrols-doc
Summary: Documentation for qtquickcontrols

%description -n qt5-qtquickcontrols-doc
%{summary}.

%files -n qt5-qtquickcontrols-doc
%{_qt5_docdir}/qtquickcontrols1/

%package -n qt5-qtscript-doc
Summary: Documentation for qtscript

%description -n qt5-qtscript-doc
%{summary}.

%files -n qt5-qtscript-doc
%{_qt5_docdir}/qtscript*

%package -n qt5-qtscxml-doc
Summary: Documentation for qtscxml

%description -n qt5-qtscxml-doc
%{summary}.

%files -n qt5-qtscxml-doc
%{_qt5_docdir}/qtscxml*

%package -n qt5-qtsensors-doc
Summary: Documentation for qtsensors

%description -n qt5-qtsensors-doc
%{summary}.

%files -n qt5-qtsensors-doc
%{_qt5_docdir}/qtsensors*

%package -n qt5-qtserialbus-doc
Summary: Documentation for qtserialbus

%description -n qt5-qtserialbus-doc
%{summary}.

%files -n qt5-qtserialbus-doc
%{_qt5_docdir}/qtserialbus*

%package -n qt5-qtserialport-doc
Summary: Documentation for qtserialport

%description -n qt5-qtserialport-doc
%{summary}.

%files -n qt5-qtserialport-doc
%{_qt5_docdir}/qtserialport*

%package -n qt5-qtsvg-doc
Summary: Documentation for qtsvg

%description -n qt5-qtsvg-doc
%{summary}.

%files -n qt5-qtsvg-doc
%{_qt5_docdir}/qtsvg*

%package -n qt5-qttools-doc
Summary: Documentation for qttools

%description -n qt5-qttools-doc
%{summary}.

%files -n qt5-qttools-doc
#{_qt5_docdir}/qdoc*
%{_qt5_docdir}/qtassistant*
%{_qt5_docdir}/qtdesigner*
%{_qt5_docdir}/qthelp*
%{_qt5_docdir}/qtlinguist*
%{_qt5_docdir}/qtuitools*

%package -n qt5-qtvirtualkeyboard-doc
Summary: Documentation for qtvirtualkeyboard

%description -n qt5-qtvirtualkeyboard-doc
%{summary}.

%files -n qt5-qtvirtualkeyboard-doc
%{_qt5_docdir}/qtvirtualkeyboard*

%package -n qt5-qtwebchannel-doc
Summary: Documentation for qtwebchannel

%description -n qt5-qtwebchannel-doc
%{summary}.

%files -n qt5-qtwebchannel-doc
%{_qt5_docdir}/qtwebchannel*

%package -n qt5-qtwebsockets-doc
Summary: Documentation for qtwebsockets

%description -n qt5-qtwebsockets-doc
%{summary}.

%files -n qt5-qtwebsockets-doc
%{_qt5_docdir}/qtwebsockets*

%package -n qt5-qtx11extras-doc
Summary: Documentation for qtx11extras

%description -n qt5-qtx11extras-doc
%{summary}.

%files -n qt5-qtx11extras-doc
%{_qt5_docdir}/qtx11extras*

%package -n qt5-qtspeech-doc
Summary: Documentation for qtspeech

%description -n qt5-qtspeech-doc
%{summary}.

%files -n qt5-qtspeech-doc
%{_qt5_docdir}/qtspeech*

%package -n qt5-qtremoteobjects-doc
Summary: Documentation for qtremoteobjects

%description -n qt5-qtremoteobjects-doc
%{summary}.

%files -n qt5-qtremoteobjects-doc
%{_qt5_docdir}/qtremoteobjects*

%package -n qt5-qtpurchasing-doc
Summary: Documentation for qtpurchasing

%description -n qt5-qtpurchasing-doc
%{summary}.

%files -n qt5-qtpurchasing-doc
%{_qt5_docdir}/qtpurchasing*

%package -n qt5-qtwayland-doc
Summary: Documentation for qtwayland

%description -n qt5-qtwayland-doc
%{summary}.

%files -n qt5-qtwayland-doc
%{_qt5_docdir}/qtwayland*

%package -n qt5-qtwebview-doc
Summary: Documentation for qtwebview

%description -n qt5-qtwebview-doc
%{summary}.

%files -n qt5-qtwebview-doc
%{_qt5_docdir}/qtwebview*

%package -n qt5-qtlocation-doc
Summary: Documentation for qtlocation

%description -n qt5-qtlocation-doc
%{summary}.

%files -n qt5-qtlocation-doc
%{_qt5_docdir}/qtlocation*
%{_qt5_docdir}/qtpositioning*

%package -n qt5-qtxmlpatterns-doc
Summary: Documentation for qtxmlpatterns

%description -n qt5-qtxmlpatterns-doc
%{summary}.

%files -n qt5-qtxmlpatterns-doc
%{_qt5_docdir}/qtxmlpatterns*

%package -n qt5-qtdatavis3d-doc
Summary: Documentation for qtdatavis3d

%description -n qt5-qtdatavis3d-doc
%{summary}.

%files -n qt5-qtdatavis3d-doc
%{_qt5_docdir}/qtdatavis3d*
%{_qt5_docdir}/qtdatavisualization*

%package -n qt5-qtgamepad-doc
Summary: Documentation for qtgamepad

%description -n qt5-qtgamepad-doc
%{summary}.

%files -n qt5-qtgamepad-doc
%{_qt5_docdir}/qtgamepad*


%prep
# intentionally left blank
# though could be used to initially unpack (rex)


%build
# intentionally left blank


%install
mkdir -p %{buildroot}
tar xf %{SOURCE0} -C %{buildroot}

## unpackaged files
pushd %{buildroot}%{_qt5_docdir}
rm -rfv \
  qdoc* \
  qtdistancefieldgenerator* \
  qtdoc* qtcmake* \
  qtlottieanimation* \
  qtpdf* \
  qtwebengine*

popd


%changelog
* Thu Jan 09 2025 Zephyr Lykos <fedora@mochaa.ws> - 5.15.16-1
- 5.15.16

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 5.15.1-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.1-1
- 5.15.1

* Mon Aug 10 2020 Jan Grulich <jgrulich@redhat.com> - 5.14-3
- Produce qt5-doc package for easier installation of complete documentation

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14-1
- 5.14

* Sat Apr 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.13-1
- 5.13
- Obsoletes: qt5-qtcanvas3d-doc

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.3-1
- 5.12.3
- omit qtwebengine, now packaged separately

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.1-1
- 5.11.1

* Wed May 09 2018 Jan Grulich <jgrulich@redhat.com> - 5.10.1-1
- Update to 5.10.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.2-2
- omit -qtdoc-doc bits, conflicts with real qt5-qtdoc (#1520355)
- use %%_qt5_docdir macro (instead of hard-coded %%_docdir/qt5)
- optimize build a bit

* Tue Oct 10 2017 Martin Bříza <mbriza@redhat.com> - 5.9.2-1
- Update to 5.9.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.0-0.beta.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.3
- Individual package plus meta package

* Tue Apr 18 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta1.1
- Add proper provides and obsoletes

* Thu Apr 13 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta1.0
- Full documentation package self generated

