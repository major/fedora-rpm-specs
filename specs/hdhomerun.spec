# This is the correct folder for firewalld service files, even on x86_64
# It is not used for shared objects
%global fw_services %{_prefix}/lib/firewalld/services

# Use if gtk2 is not available
%bcond_without gui

%if %{with gui}
%global make_subfolder hdhomerun_config_gui
%else
%global make_subfolder libhdhomerun
%endif

Name:           hdhomerun
Version:        20231214
Release:        5%{?dist}
Summary:        Silicon Dust HDHomeRun configuration utility

License:        LGPL-2.1-or-later
URL:            http://www.silicondust.com/
Source0:        http://download.silicondust.com/hdhomerun/libhdhomerun_%{version}.tgz
Source1:        http://download.silicondust.com/hdhomerun/hdhomerun_config_gui_%{version}.tgz
Source2:        hdhomerun_config_gui.desktop
Source3:        %{name}.xml

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed

%if %{with gui}
BuildRequires:  gtk2-devel
BuildRequires:  libicns-utils
BuildRequires:  desktop-file-utils
%endif

%description
The configuration and firmware upgrade utility for Silicon Dust's
networked HDTV dual-tuner HDHomeRun device.

%package devel
Summary: Developer tools for the hdhomerun library
Requires: hdhomerun%{?_isa} = %{version}-%{release}

%description devel
The hdhumerun-devel package provides developer tools for the hdhomerun library.


%prep
%autosetup -c -a 1

# Fix up linefeeds, drop execute bit and don't strip binaries
#sed -i 's/\r//' libhdhomerun/*
sed -i -e '/$(STRIP).*/d' -e 's/C\(PP\)\?FLAGS .=/C\1FLAGS ?=/' libhdhomerun/Makefile

# Convert files to utf8
for f in libhdhomerun/*; do
  /usr/bin/iconv -f iso-8859-1 -t utf-8 --output $f.new $f && mv $f.new $f
done

%build
pushd %{make_subfolder}
%{?with_gui:%configure}
%{?without_gui:%{set_build_flags}}
%make_build
popd

cat << __EOF__ > README.firmware
The HDHomeRun Firmwares are not redistributable, but the latest versions of
both the US ATSC and European DVB-T firmwares can always be obtained from
the Silicon Dust web site:

https://www.silicondust.com/support/linux/

__EOF__

%if %{with gui}
pushd %{make_subfolder}/OSX
icns2png -x hdhr.icns
popd
%endif

%install
%if %{with gui}
%make_install -C %{make_subfolder}

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}

for size in 16x16 32x32 128x128 256x256 512x512; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
    install -m0755 hdhomerun_config_gui/OSX/hdhr_${size}x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/hdhr.png
done

%else
# SiliconDust puts the install target for libhdhomerun in
# hdhomerun_config_gui, so we do it manually when not including the gui
mkdir -p %{buildroot}%{_libdir}
install -m0755 libhdhomerun/libhdhomerun.so %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_bindir}/
 install -m0755 libhdhomerun/hdhomerun_config %{buildroot}%{_bindir}/
%endif

mkdir include
cp -a libhdhomerun/*.h include
sed -r 's|(^#include +["])(.*)(["] *$)|#include <hdhomerun/\2>|' \
    libhdhomerun/hdhomerun.h > include/hdhomerun.h
mkdir -p %{buildroot}%{_includedir}/hdhomerun
install -p include/*.h %{buildroot}%{_includedir}/hdhomerun/

# Install firewalld config
mkdir -p %{buildroot}%{fw_services}
install -pm 0644 %{SOURCE3} %{buildroot}%{fw_services}/

%files
%license libhdhomerun/LICENSE
%doc libhdhomerun/README.md README.firmware

# lib and cli are LGPLv3
%{_libdir}/libhdhomerun.so
%{_bindir}/hdhomerun_config
%{fw_services}/%{name}.xml

%if %{with gui}
%license hdhomerun_config_gui/COPYING
%doc hdhomerun_config_gui/AUTHORS hdhomerun_config_gui/README

# gui is GPLv3
%{_bindir}/hdhomerun_config_gui
%{_datadir}/applications/hdhomerun_config_gui.desktop
%{_datadir}/icons/hicolor/*/apps/hdhr.png
%endif

%files devel
%dir %{_includedir}/hdhomerun
%{_includedir}/hdhomerun/*.h


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20231214-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Andrew Bauer <zonexpoertconsulting@outlook.com> - 20231214-4
- Gtk2 is now built and managed in epel, refactor to accomodate this change

* Thu Sep 05 2024 Andrew Bauer <zonexpoertconsulting@outlook.com> - 20231214-3
- refactor specfile to accomodate no gtk2 in el10

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231214-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Richard Shaw <hobbes1069@gmail.com> - 20231214-1
- Update to 20231214.
- Migrate to SPDX license identifier.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230719-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230719-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 23 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 20230719-1
- 20230719 release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230323-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 03 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 20230323-1
- 20230323 release
- add hdhomerun firewalld config

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200907-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200907-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200907-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200907-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200907-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Richard Shaw <hobbes1069@gmail.com> - 20200907-1
- Update to 20200907.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190621-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190621-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Richard Shaw <hobbes1069@gmail.com> - 20190621-1
- Update to 20190621.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180817-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180817-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Richard Shaw <hobbes1069@gmail.com> - 20180817-1
- Update to 20180817.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.35.20161117
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.34.20161117
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.33.20161117
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.32.20161117
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 19 2017 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.0-0.31.20161117
- Update to 20161117

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.30.20150615
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.29.20150615
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 28 2015 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.0-0.28.20150615
- Update to 20150615

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.27.20140604
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0-0.26.20140604
- Rebuilt for GCC 5 C++11 ABI change

* Tue Sep 23 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.0-0.26.20140604
- Remove duplicate description section

* Tue Sep 23 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.0-0.25.20140604
- Extract icons from OSX icon set
- Add desktop file for GUI

* Tue Sep 23 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.0-0.24.20140604
- Update to 20140604

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.23.20130328
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.22.20130328
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.21.20130328
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Paul Wouters <pwouters@redhat.com> - 0.0-0.20.20130328
- Update to 20130328 (rhbz#964210)
- Removed DESTDIR patch, got merged in at upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.19.20120405
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 27 2012 Jeffrey Ollie <jeff@ocjtech.us> - 0.0-0.18.20120405
- Update to 20120405

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.17.20100213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.16.20100213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.0-0.15.20100213
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.14.20100213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 09 2010 Jarod Wilson <jarod@redhat.com> - 0.0-0.13.20100213
- Update to 20100213 release
- Add a devel sub-package so other software can be built against
  the system libhdhomerun (Rolf Fokkens, fixes rhbz#571139)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.12.20090415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Jarod Wilson <jarod@redhat.com> 0.0-0.11.20090415
- Add README.firmware, pointing folks to firmware downloads

* Tue Jun 23 2009 Jarod Wilson <jarod@redhat.com> 0.0-0.10.20090415
- Update to 20090415 release
- Add new GTK2 config GUI

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.9.20081002
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Jarod Wilson <jarod@redhat.com> 0.0-0.8.20081002
- Update to 20081002 release

* Tue Aug 19 2008 Jarod Wilson <jarod@redhat.com> 0.0-0.7.20080727
- Update to 20080727 release

* Thu Feb 14 2008 Jarod Wilson <jwilson@redhat.com> 0.0-0.6.20080212
- Update to 20080212 release

* Fri Oct 19 2007 Jarod Wilson <jwilson@redhat.com> - 0.0-0.5.20071015
- Update to 20071015 release
- Update license field

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0-0.4.20070716
- Rebuild for selinux ppc32 issue.

* Tue Jul 17 2007 Jarod Wilson <jwilson@redhat.com> 0.0-0.3.20070716
- Update to 20070716 release

* Thu Jul 12 2007 Jarod Wilson <jwilson@redhat.com> 0.0-0.2.20070616
- Use sed instead of perl, drop perl BR: (jeff@ocjtech.us)
- Convert source files to utf8 (jeff@ocjtech.us)

* Mon Jun 18 2007 Jarod Wilson <jwilson@redhat.com> 0.0-0.1.20070616
- Update to 20070616 release
- Don't install any of the header files and drop lib from the package
  name, since this really isn't a library

* Fri May 18 2007 Jarod Wilson <jwilson@redhat.com> 0.0-0.1.20070512
- Initial packaging for Fedora
