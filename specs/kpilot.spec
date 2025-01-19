Name:    kpilot
Summary: Sync PIM data with PalmOS devices
Version: 5.3.0
Release: 43%{?dist}

# no pilot-link on S/390
ExcludeArch: s390 s390x

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/4.3.4/src/kdepim-4.3.4.tar.bz2
# translations collected from:
# http://websvn.kde.org/branches/stable/l10n-kde4/*/messages/kdepim
# http://websvn.kde.org/branches/stable/l10n-kde4/*/docs/kdepim
Source1: kpilot-translations-20100115.tar.bz2
Patch0:  kdepim-4.3.4-qtcore-includes.patch
# Remove bad debugging statements to fix FTBFS (#1556010, #1604519)
Patch1:  kdepim-4.3.4-kpilot-remove-bad-debug.patch

BuildRequires: kdelibs4-devel >= 4.3.4
BuildRequires: kdepimlibs-devel >= 4.3.4
BuildRequires: akonadi-devel
BuildRequires: boost-devel
BuildRequires: pilot-link-devel >= 0.12
BuildRequires: qca2-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?fedora} < 13
Conflicts: kdepim < 6:4.3.80
Conflicts: kde-l10n < 4.3.90-3
%endif

%description
Utility to synchronize PIM (Personal Information Management) data with
PalmOS devices.


%package libs
Summary: Runtime libraries for %{name}

%description libs
%{summary}.


%prep
%setup -q -n kdepim-4.3.4 -a 1
%patch -P0 -p1
%patch -P1 -p1
echo 'add_subdirectory(../doc/kpilot doc)' >>kpilot/CMakeLists.txt
echo 'add_subdirectory(../kpilot-translations-20100115 l10n)' >>kpilot/CMakeLists.txt
pushd kpilot-translations-20100115/doc
for i in *_kpilot ; do
  if [ -e $i/index.docbook ] ; then
    echo "add_subdirectory($i)" >>CMakeLists.txt
    echo 'kde4_create_handbook(index.docbook INSTALL_DESTINATION ${HTML_INSTALL_DIR}/'${i%_kpilot}'/ SUBDIR kpilot)' >$i/CMakeLists.txt
  fi
done
popd


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../kpilot
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# make symlinks relative
mkdir -p %{buildroot}%{_docdir}/HTML/en/common
pushd %{buildroot}%{_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -nfs ../common $i
   fi
done
popd

# don't package devel files
rm -rf %{buildroot}%{_kde4_includedir}/kpilot/
rm -f %{buildroot}%{_kde4_libdir}/libkpilot.so

%find_lang %{name} --with-kde


%check
for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done


%ldconfig_scriptlets libs


%files -f %{name}.lang
%doc kpilot/COPYING
%doc kpilot/README kpilot/AUTHORS kpilot/ChangeLog kpilot/NEWS kpilot/TODO
%{_kde4_bindir}/kpilot
%{_kde4_bindir}/kpilotDaemon
%{_kde4_datadir}/applications/kde4/kpilot*.desktop
%{_kde4_datadir}/config.kcfg/*.kcfg
%{_kde4_datadir}/kde4/services/*.desktop
%{_kde4_datadir}/kde4/servicetypes/kpilotconduit.desktop
%{_kde4_appsdir}/kconf_update/kpilot.upd
%{_kde4_appsdir}/kpilot/
%{_kde4_iconsdir}/hicolor/*/*/*

%files libs
%{_kde4_libdir}/libkpilot.so.*
%{_kde4_libdir}/libkpilot_*.so
%{_kde4_libdir}/kde4/kcm_kpilot.so
%{_kde4_libdir}/kde4/kpilot_conduit_*.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 5.3.0-42
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 5.3.0-28
- Remove bad debugging statements to fix FTBFS (#1556010, #1604519)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.3.0-25
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 5.3.0-20
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 5.3.0-18
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.3.0-16
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 5.3.0-15
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 5.3.0-13
- Fix FTBFS with recent kdelibs/qt (#1107056)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 5.3.0-11
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Machata <pmachata@redhat.com> - 5.3.0-9
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 5.3.0-4
- Fix the translated documentation to get built
- Don't list the documentation in the file list as find_lang does it for us

* Fri Jan 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 5.3.0-3
- Ship translations collected from branches/stable/l10n-kde4
- BR gettext
- Conflicts: kde-l10n < 4.3.90-3 (F12-)

* Tue Dec 22 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 5.3.0-2
- shorten Summary and add linebreak in %%description
- Conflicts with old versions of kdepim (F12-)
- split out -libs subpackage

* Wed Dec 16 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 5.3.0-1
- new specfile for KPilot, split out of kdepim 4.3.4
