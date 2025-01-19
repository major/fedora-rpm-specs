%global svn_rev 1200

Name:           lcd4linux
Version:        0.11
# We package an svn snapshot of what will become 0.11 since upstream has
# neglected to do a new release for ages
Release:        0.35.svn%{svn_rev}%{?dist}
Summary:        Display system state on an external LCD display
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ssl.bulix.org/projects/lcd4linux/
# This is the non rpmbuild parsable url:
# http://ssl.bulix.org/projects/lcd4linux/changeset/1200/trunk?old_path=%2F&format=zip
# Note replace 1200 with svn_rev!
Source0:        lcd4linux-trunk-1200.zip
# Courtesey of Debain
Source1:        lcd4linux.8
Source2:        lcd4X11.sh
Source3:        lcd4X11.desktop
Source4:        README.fedora
Patch0:         lcd4linux-XWindow-conf.patch
BuildRequires:  gd-devel ncurses-devel libX11-devel libICE-devel sqlite-devel
BuildRequires:  serdisplib-devel libftdi-devel libjpeg-devel libst2205-devel
BuildRequires:  libvncserver-devel gettext-devel dbus-devel
BuildRequires:  libtool desktop-file-utils make
# Most drivers require the old libusb-0.1 API; and
# the MDM166A driver requires the new libusb-1.0
BuildRequires:  libusb-compat-0.1-devel libusb1-devel
ExcludeArch:    s390 s390x

%description
LCD4Linux is a small program that grabs information from the kernel
and some subsystems and displays it on an external liquid crystal display.


%prep
%setup -q -n trunk
%patch -P0 -p1
chmod +x bootstrap configure
./bootstrap
cp -a %{SOURCE4} .


%build
%configure
make %{?_smp_mflags}
sed -e "s@#Display 'XWindow'@Display 'XWindow'@" \
    -e "s@Display 'ACool'@#Display 'ACool'@" \
    -e "s@Layout 'TestLayer'@#Layout 'TestLayer'@" \
    -e "s@#Layout 'Default'@Layout 'Default'@" \
    lcd4linux.conf.sample > lcd4X11.conf
touch -r lcd4linux.conf.sample lcd4X11.conf


%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 lcd4X11.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 lcd4linux.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/lcd4X11
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}


%files
%doc COPYING ChangeLog README.fedora lcd4linux.conf.sample
%config(noreplace) %{_sysconfdir}/lcd4X11.conf
%{_bindir}/%{name}
%{_bindir}/lcd4X11
%{_mandir}/man8/%{name}.8*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/lcd4X11.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.35.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.11-0.34.svn1200
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.33.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.32.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.31.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.30.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.29.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Hans de Goede <hdegoede@redhat.com> - 0.11-0.28.svn1200
- Fix FTBFS (rhbz#2113475)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.27.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.26.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.25.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.24.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.23.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.22.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.21.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.20.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.19.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.18.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.17.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.16.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.11-0.15.svn1200
- rebuild (libvncserver)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.14.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.13.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.12.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.11.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.10.svn1200
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Hans de Goede <hdegoede@redhat.com> - 0.11-0.9.svn1200
- Update to svn revision 1200
- Drop all our patches (these are all upstream now)
- Rebuild for new libftdi
- Fix FTBFS (rhbz#1037152)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.8.svn1143
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 0.11-0.7.svn1143
- rebuild for new GD 2.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.6.svn1143
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.5.svn1143
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.4.svn1143
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar  4 2011 Dan Horák <dan[at]danny.cz> - 0.11-0.3.svn1143
- add ExcludeArch: s390(x)

* Tue Feb 22 2011 Hans de Goede <hdegoede@redhat.com> - 0.11-0.2.svn1143
- Add missing BuildRequires: gettext-devel dbus-devel libvncserver-devel
- Drop BuildRequires: libmpdclient-devel, the mpd plugin does not work
  with recent versions of libmpdclient

* Sat Feb 19 2011 Hans de Goede <hdegoede@redhat.com> - 0.11-0.1.svn1143
- Initial Fedora package
