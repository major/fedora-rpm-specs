Name:           btkbdd
Version:        1.5
Release:        17%{?dist}
Summary:        Bluetooth keyboard service

License:        GPL+
URL:            http://v3.sk/~lkundrak/btkbdd/
Source0:        http://v3.sk/~lkundrak/btkbdd/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  bluez-libs-devel /usr/bin/pod2man
BuildRequires:  systemd-units
BuildRequires: make
Requires:       udev systemd

%description
This tool starts a Bluetooth HID Keyboard service, serving keystrokes
obtained via Linux Input subsystem's event device (evdev). In practical
terms, it turns your Linux box with a physical keyboard into a Bluetooth
keyboard, which can be used by various Bluetooth HID capable devices,
including desktop or tablet computers, smart phones, game consoles and so
on.


%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}


%files
%{_sbindir}/btkbdd
%{_sbindir}/evmuxd
%{_mandir}/man8/btkbdd.8.*
%{_mandir}/man8/evmuxd.8.*
%{_unitdir}/btkbdd@.service
%{_unitdir}/evmuxd@.service
%{_udevrulesdir}/90-btkbdd.rules
%{_udevrulesdir}/90-evmuxd.rules
%dir %{_localstatedir}/lib/btkbdd
%doc COPYING README.pod architecture.png


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.5-2
- Drop the postun scriptlet

* Tue Oct 13 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.5-1
- New release with evmuxd

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 29 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.3-5
- Fix source URL, github removed file hosting

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.3-4
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Lubomir Rintel <lkundrak@v3.sk> - 1.3-1
- Support systemd

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 09 2011 Lubomir Rintel <lkundrak@v3.sk> - 1.2-1
- Do not own rules.d (Volker Fröhlich, #772504)
- Change state directory location to match package name

* Tue Jan 04 2011 Lubomir Rintel <lkundrak@v3.sk> - 1.1-1
- Initial packaging
