%global qt_module qtspeech

%global examples 1

Summary: Qt6 - Speech component
Name:    qt6-%{qt_module}
Version: 6.5.1
Release: 3%{?dist}

# Code can be either LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only
# See e.g. src/plugins/speechdispatcher or src/tts
# Examples are under BSD-3-Clause
License: (GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-3-Clause
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtmultimedia-devel >= %{version}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: speech-dispatcher-devel >= 0.8
%if 0%{?fedora} || 0%{?rhel} < 10
BuildRequires: flite-devel
%endif

BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
The module enables a Qt application to support accessibility features
such as text-to-speech, which is useful for end-users who are visually
challenged or cannot access the application for whatever reason. The
most common use case where text-to-speech comes in handy is when the
end-user is driving and cannot attend the incoming messages on the phone.
In such a scenario, the messaging application can read out the incoming
message. Qt Serial Port provides the basic functionality, which includes
configuring, I/O operations, getting and setting the control signals of
the RS-232 pinouts.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%cmake_qt6 -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%files
%license LICENSES/GPL* LICENSES/LGPL* LICENSES/BSD*
%{_qt6_libdir}/libQt6TextToSpeech.so.6{,.*}
%dir %{_qt6_plugindir}/texttospeech
%{_qt6_plugindir}/texttospeech/*.so
%dir %{_qt6_qmldir}/QtTextToSpeech
%{_qt6_qmldir}/QtTextToSpeech/*

%files devel
%dir %{_qt6_headerdir}/QtTextToSpeech
%{_qt6_headerdir}/QtTextToSpeech/*
%{_qt6_libdir}/libQt6TextToSpeech.so
%{_qt6_libdir}/libQt6TextToSpeech.prl
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6TextToSpeech
%{_qt6_libdir}/cmake/Qt6TextToSpeech/*.cmake
%{_qt6_libdir}/pkgconfig/Qt6TextToSpeech.pc
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_texttospeech*.pri
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/*.json

%files examples
%{_qt6_examplesdir}/


%changelog
* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-3
- Rebuild for qtbase private API version change

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-2
- Rebuild for qtbase private API version change

* Mon May 22 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-1
- 6.5.1

* Tue Apr 04 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.0-1
- 6.5.0

* Thu Mar 23 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.3-1
- 6.4.3

* Mon Feb 27 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.2-1
- Initial package
