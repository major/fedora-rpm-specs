# https://github.com/i-nex/I-Nex/commit/0c10102578e7c762674eaf9460b0903d76f151db
%global commit0 0c10102578e7c762674eaf9460b0903d76f151db
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .%{gitdate}git%{shortcommit0}
%global gitdate 20170703

Name:           i-nex
Version:        7.6.1
#Release:        1%%{gver}%%{?dist}
Release:        14%{?dist}
Summary:        System information tool like hardinfo, sysinfo
License:        GPLv3 and LGPLv3
URL:            https://github.com/eloaders/I-Nex
#Source0:        https://github.com/i-nex/I-Nex/archive/%%{commit0}.tar.gz#/%%{name}-%%{shortcommit0}.tar.gz
Source0:        https://github.com/i-nex/I-Nex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/i-nex/I-Nex/issues/80
Source1:        %{name}.appdata.xml
# https://github.com/i-nex/I-Nex/issues/81
Patch0:         %{name}-Makefile.patch
# Thanks to AUR Linux https://aur.archlinux.org/packages/i-nex/ for the patches
Patch1:         Adapt-for-new-libcpuid-structure.patch
Patch2:         Fix-error-if-proc-mtrr-doesn-t-exist.patch
Patch3:         Fix-for-gambas-compiler-change.patch
Patch4:         Fix-libcpuid-SOVERSION.patch
Patch5:         Hack-for-weird-json-issue.patch

ExcludeArch:    aarch64 %arm ppc64le ppc64 s390x
 
BuildRequires:  gambas3-devel
BuildRequires:  ImageMagick
BuildRequires:  ImageMagick-devel
BuildRequires:  git
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  redhat-lsb
BuildRequires:  automake
BuildRequires:  libappstream-glib
BuildRequires:  gambas3-gb-image
BuildRequires:  gambas3-gb-qt5
BuildRequires:  gambas3-gb-form
BuildRequires:  gambas3-gb-desktop
BuildRequires:  gambas3-gb-form-dialog >= 3.5.0
BuildRequires:  gambas3-gb-form-stock
BuildRequires:  gambas3-gb-gui >= 3.5.0
BuildRequires:  gambas3-gb-qt5-ext >= 3.5.0
BuildRequires:  gambas3-gb-settings
BuildRequires:  gambas3-gb-desktop-x11
BuildRequires:  pkgconfig
BuildRequires:  libcpuid-devel >= 0.5.0
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pciutils
BuildRequires:  procps
BuildRequires:  desktop-file-utils
Requires:       gambas3-gb-gtk
Requires:       gambas3-gb-desktop
Requires:       gambas3-gb-settings
Requires:       gambas3-gb-form-dialog
Requires:       gambas3-gb-qt5 >= 3.5.0
Requires:       gambas3-gb-qt5-ext >= 3.5.0
Requires:       gambas3-gb-form-mdi
Requires:       gambas3-gb-form-stock
Requires:       gambas3-gb-jit
Requires:       gambas3-gb-desktop-x11
Requires:       redhat-lsb
Requires:       mesa-demos 
Requires:       xdpyinfo xrandr
Requires:       gambas3-gb-dbus
Requires:       gambas3-runtime
Requires:       gambas3-gb-image
Requires:       gambas3-gb-gtk
Requires:       gambas3-gb-form
Requires:       util-linux
Requires:       procps-ng
Requires:       coreutils
Requires:       pciutils
Requires:       libcpuid
Requires:       gambas3-runtime
Requires:       gambas3-gb-gui >= 3.5.0
Requires:       net-tools
Requires:       procps-ng
Requires:       pastebinit
Requires:       procps-ng

%description
i-nex - System information tool like hardinfo, sysinfo.
I-Nex is an application that gathers information for hardware 
components available on your system and displays it using an 
user interface similar to the popular Windows tool CPU-Z.

I-Nex can display information for the following components: CPU, 
GPU, Motherboard, Sound, Hard disks, RAM, Network and USB as well 
as some system info like the hostname, Linux distribution and 
version, Xorg, GCC, GLX versions and Linux Kernel info.


%prep
#%%autosetup -p1 -n I-Nex-%{commit0}
%autosetup -p1 -n I-Nex-%{version}
# make it dynamic
sed -i -e 's|^STATIC.*|STATIC = false|' i-nex.mk
sed -i -e 's|^UDEV_RULES_DIR.*|UDEV_RULES_DIR = /usr/lib/udev/rules.d|' i-nex.mk
 
# A hack to be able to run the program via the name execution. Thanks openSuse!
#+ some info tools are under *sbin
cat > %{name}.sh <<HERE
#!/bin/sh

export LIBOVERLAY_SCROLLBAR=0 PATH=/sbin:/usr/sbin:\$PATH
exec %{_bindir}/%{name}.gambas
HERE

#using system's pastebinit
sed -i \
       '\|/usr/share/i-nex/pastebinit/|s|/usr/share/i-nex/pastebinit/||' \
       I-Nex/i-nex/.src/Reports/MPastebinit.module
cp I-Nex/i-nex/logo/i-nex.0.4.x.png %{name}.png
sed -e 's|env LIBOVERLAY_SCROLLBAR=0 /usr/bin/i-nex.gambas|i-nex|' \
         -e '/^Icon=/s|=.*|=%{name}|' debian/%{name}.desktop > %{name}.desktop

#remove empty line
sed -i -e '1,1d' debian/i-nex-library.desktop

#Set QT_QPA_PLATFORM=xcb in desktop file to help with wayland issues
sed -i -e 's|Exec=/usr/bin/i-nex.gambas|Exec=env QT_QPA_PLATFORM=xcb /usr/bin/i-nex.gambas|' %{name}.desktop
sed -i -e 's|Exec=/usr/bin/i-nex.gambas|Exec=env QT_QPA_PLATFORM=xcb /usr/bin/i-nex.gambas|' debian/i-nex.desktop
sed -i -e 's|Exec=/usr/bin/i-nex.gambas --library|Exec=env QT_QPA_PLATFORM=xcb /usr/bin/i-nex.gambas --library|' debian/i-nex-library.desktop

%build
cd I-Nex
autoreconf -fiv
%configure
cd ..
%make_build

%install
%make_install

# A hack to be able to run the program via the name execution.
install -D -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}

# Let's use %%doc macro.
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Let's use system's `pastebinit`.
rm -rf %{buildroot}%{_datadir}/%{name}/pastebinit

chmod 0644 %{buildroot}/%{_udevrulesdir}/i2c_smbus.rules 
mv %{buildroot}/%{_udevrulesdir}/i2c_smbus.rules %{buildroot}/%{_udevrulesdir}/50-i2c_smbus.rules

install -Dm644 %{S:1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README.md
%license debian/copyright
%{_bindir}/i-nex
%{_bindir}/i-nex.gambas
%{_bindir}/i-nex-edid
%{_datadir}/applications/i-nex.desktop
%{_udevrulesdir}/50-i2c_smbus.rules
%{_datadir}/applications/i-nex-library.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/i-nex.1.*
%{_mandir}/man1/i-nex.gambas.1.*
%{_mandir}/man1/i-nex-edid.1.*
%{_datadir}/pixmaps/i-nex-16.png
%{_datadir}/pixmaps/i-nex-32.png
%{_datadir}/pixmaps/i-nex-128.png
%{_datadir}/pixmaps/i-nex.png

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 29 2022 Martin Gansser <martinkg@fedoraproject.org> - 7.6.1-12
- Add Fix-for-gambas-compiler-change.patch
- Add Hack-for-weird-json-issue.patch

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Martin Gansser <martinkg@fedoraproject.org> - 7.6.1-9
- Add BR gambas3-gb-desktop-x11
- Add RR gambas3-gb-desktop-x11

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 7.6.1-6
- Add Adapt-for-new-libcpuid-structure.patch
- Add Fix-error-if-proc-mtrr-doesn-t-exist.patch
- Add Fix-libcpuid-SOVERSION.patch

* Tue Dec 22 2020 Martin Gansser <martinkg@fedoraproject.org> - 7.6.1-5
- Rebuilt for new libcpuid-0.5.0
- Set QT_QPA_PLATFORM=xcb in desktop file to help with wayland issues
- Fix libcpuid library version

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 7.6.1-4
- Require xdpyinfo xrandr, not xorg-x11-server-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 7.6.1-1
- Update to 7.6.1

* Sat Oct 19 2019 Martin Gansser <martinkg@fedoraproject.org> - 7.6.0-10.20170703git0c10102
- Add %%{name}-fix-compilation.patch
- Add RR gambas3-gb-jit

* Tue Oct 08 2019 Petr Viktorin <pviktori@redhat.com> - 7.6.0-9.20170703git0c10102
- Remove unused dependency python2-configobj

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.0-8.20170703git0c10102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.0-7.20170703git0c10102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.0-6.20170703git0c10102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Martin Gansser <martinkg@fedoraproject.org> - 7.6.0-5.20170703git0c10102
- Update Python 2 dependency declarations to new packaging standard

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.0-4.20170703git0c10102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 7.6.0-3.20170703git0c10102
- Delete BR hicolor-icon-theme not needed
- Use udev macro %%{_udevrulesdir}
- Add BR libappstream-glib
- Add %%{name}-Makefile.patch to fix install pixmap
- Add ExcludeArch: aarch64 %%arm ppc64le ppc64 s390x

* Mon Oct 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 7.6.0-2.20170703git0c10102
- Use udev macro %%{_udevrulesdir}
- RR hicolor-icon-theme not needed
- Add an AppData file. See https://fedoraproject.org/wiki/Packaging:AppData
- Add gitdate for snapshot release

* Wed Sep 27 2017 Martin Gansser <martinkg@fedoraproject.org> - 7.6.0-1.20170703git0c10102 
-Initial build
