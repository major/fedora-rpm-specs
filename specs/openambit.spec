#global commit 042e1019d31e89ba4acf8fe08bfdc9089bbace0f
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           openambit
Version:        0.5
Release:        14%{?commit:.git%shortcommit}%{?dist}
Summary:        Open software for the Suunto Ambit(2)

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://openambit.org/
Source0:        https://github.com/openambitproject/openambit/archive/%{?commit:%commit}%{!?commit:%version}/openambit-%{?commit:%shortcommit}%{!?commit:%version}.tar.gz

# Unbundle hidapi (see also %%prep)
Patch0:         openambit_unbundle-hidapi.patch
# Port scripts to python3
Patch1:         openambit_python3.patch
# Add missing extern declarations (GCC10 FTBFS)
Patch2:         openambit_gcc10.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  systemd-devel
BuildRequires:  hidapi-devel
BuildRequires:  python3
BuildRequires:  zlib-devel
%if 0%{?with_wireshark:1}
BuildRequires:  wireshark-devel
%endif


Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description
Openambit is application for downloading moves from the Suunto
Ambit(2) outdoor watches, and synchronizing them with the
movescount website.


%package libs
Summary:        Libraries for %{name}
# For %%{_sysconfdir}/udev/rules.d/ ownership
Requires:       systemd

%description libs
The %{name}-libs package contains libraries for %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if 0%{?with_wireshark:1}
%package        wireshark
Summary:        Wireshark dissector for %{name}
Requires:       wireshark%{?_isa} >= 1.12.6-3
License:        BSD

%description    wireshark
The %{name}-wireshark package contains the Wireshark dissector for %{name},
which parses pcap-files made with usbpcap.
%endif


%prep
%autosetup -p1 -n %{name}-%{?commit:%commit}%{!?commit:%version}

# Remove exec permissions since it is installed as %%doc
chmod -x tools/movescountXmlDiff.pl

# Remove bundled hidapi files
rm -rf src/libambit/hidapi


%build
%cmake \
  -DCMAKE_INSTALL_UDEVRULESDIR=%{_udevrulesdir} \
  -DUSE_QT5=ON \
%if 0%{?with_wireshark}
  -DBUILD_EXTRAS=ON \
  -DCMAKE_INSTALL_WIRESHARKPLUGINSDIR=%{_libdir}/wireshark/plugins/ \
%endif
%cmake_build


%install
%cmake_install
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%ldconfig_scriptlets libs


%files
%license src/openambit/COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%files libs
%license src/libambit/COPYING
%{_libdir}/libambit.so.*
%{_libdir}/libmovescount.so.*
%{_udevrulesdir}/libambit.rules

%files devel
%doc src/example/ambitconsole.c
%doc tools/*
%{_includedir}/libambit.h
%{_includedir}/movescount/
%{_libdir}/libambit.so
%{_libdir}/libmovescount.so

%if 0%{?with_wireshark:1}
%files wireshark
%license wireshark_dissector/COPYING
%{_libdir}/wireshark/plugins/ambit.so
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Sandro Mani <manisandro@gmail.com> - 0.5-1
- Update to 0.5

* Tue Aug 13 2019 Sandro Mani <manisandro@gmail.com> - 0.4-12.git042e101
- Update to git 042e101

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 0.4-7
- Add missing BR: gcc-c++, make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 0.4-2
- Rebuild (wireshark)

* Tue Apr 25 2017 Sandro Mani <manisandro@gmail.com> - 0.4-1
- Update to 0.4

* Wed Feb 15 2017 Sandro Mani <manisandro@gmail.com> - 0.3-15.gitb44a1d0
- BR: python

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14.gitb44a1d0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.3-13.gitb44a1d0
- rebuild (wireshark)

* Wed Jun 15 2016 Sandro Mani <manisandro@gmail.com> - 0.3-12.gitb44a1d0
- Update to latest snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11.git5f2b784
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Sandro Mani <manisandro@gmail.com> - 0.3-10.git5f2b784
- Rebuild (wireshark)

* Wed Jul 01 2015 Sandro Mani <manisandro@gmail.com> - 0.3-9.git5f2b784
- Install the wireshark plugin in %%{_libdir}/wireshark/plugins

* Mon Jun 29 2015 Sandro Mani <manisandro@gmail.com> - 0.3-8.git5f2b784
- Install the wireshark plugin in %%{_libdir}/wireshark/plugins/current

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7.git5f2b784
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Sandro Mani <manisandro@gmail.com> - 0.3-6.git5f2b784
- Fix location where udev rules are installed

* Fri May 15 2015 Sandro Mani <manisandro@gmail.com> - 0.3-5.git5f2b784
- Rebuild (wireshark)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3-4.git5f2b784
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 08 2015 Sandro Mani <manisandro@gmail.com> - 0.3-3.git5f2b784
- Rebuild (wireshark)

* Tue Jan 27 2015 Sandro Mani <manisandro@gmail.com> - 0.3-2.git5f2b784
- Bump wireshark version
- Fix License
- Add openambit_strict-aliasing-fixes.patch
- Add openambit_fix-maybe-uninitialized.patch
- Unbundle hidapi

* Sat Dec 27 2014 Sandro Mani <manisandro@gmail.com> - 0.3-1.git5f2b784
- Initial package
