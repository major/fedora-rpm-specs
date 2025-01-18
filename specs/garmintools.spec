Name:		garmintools
Version:	0.10
Release:	32%{?dist}
Summary:	Tools for Garmin GPS-devices

License:	GPL-2.0-or-later
URL:		https://%{name}.googlecode.com
Source0:	%{url}/files/%{name}-%{version}.tar.gz

# Fix for gpx_laps_hr_cad
# See: https://code.google.com/p/garmintools/issues/detail?id=15
Patch0:		garmintools-0.10_gpx-laps-hr-cad.patch
# Fix for garmin_save_runs
# See: https://code.google.com/p/garmintools/issues/detail?id=35
Patch1:		garmintools-0.10_fix-gcc-48.patch

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	libusb-compat-0.1-devel
BuildRequires:	perl-generators
BuildRequires:	systemd-rpm-macros

Requires:	systemd-udev


%description
This software provides Linux users with the ability to communicate
with the Garmin Forerunner 305 via the USB interface.  It
implements all of the documented Garmin protocols as of Rev C
(May 19, 2006) over the USB physical link.

This means that if you have a Garmin with a USB connection to a PC,
you ought to be able to use this software to communicate with it.


%package	devel
Summary:	Development-files for %{name}

Requires:	%{name}%{?_isa} == %{version}-%{release}
Requires:	libusb-compat-0.1-devel%{?_isa}

%description	devel
This package contains files for developing application using
lib%{name}.


%prep
%setup -q
%patch -P0 -p1 -b .gpx_laps_hr_cad
%patch -P1 -p1 -b .fix-gcc-48


%build
%configure --disable-static

# Kill rpath.
sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	libtool

%make_build


%install
%make_install

# We intentionally do NOT ship libtool-dumplings.
rm -f %{buildroot}%{_libdir}/*.{,l}a

# Install additional tools.
install -pm 0755 extras/fore2gmn.pl %{buildroot}%{_bindir}/fore2gmn

# Create needed dirs.
install -d -m 0755 \
	%{buildroot}%{_pkgdocdir} \
	%{buildroot}%{_modprobedir} \
	%{buildroot}%{_udevrulesdir}

# Create needed config.
cat >> 51-garmin.rules << EOF
ATTRS{idVendor}=="091e", ATTRS{idProduct}=="0003", MODE="0666"
EOF

cat >> %{name}.conf << EOF
# stop garmin_gps serial from loading for USB garmin devices
blacklist garmin_gps
EOF

install -pm 0644 51-garmin.rules %{buildroot}%{_udevrulesdir}
install -pm 0644 %{name}.conf %{buildroot}%{_modprobedir}

# Install documentation-files.
install -pm 0644 \
	AUTHORS ChangeLog NEWS README TODO \
	%{buildroot}%{_pkgdocdir}
rm -f %{buildroot}%{_pkgdocdir}/COPYING


%post
/sbin/ldconfig
# Remove garmin_gps module if loaded, see README.
/sbin/rmmod garmin_gps &>/dev/null || :

%postun -p /sbin/ldconfig


%files
%license COPYING
%config(noreplace) %{_modprobedir}/%{name}.conf
%config(noreplace) %{_udevrulesdir}/51-garmin.rules
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%{_bindir}/fore2gmn
%{_bindir}/garmin_*
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/*.1*

%files devel
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/NEWS
%doc %{_pkgdocdir}/TODO
%{_includedir}/garmin.h
%{_libdir}/lib%{name}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 12 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.10-31
- Fix build failure due to incompatible variable types (rhbz#2300685)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.10-27
- Fix use of invalid key in 51-garmin.rules
- Convert License tag to SPDX

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.10-24
- Move udev and modprobe rules from /etc to /usr/lib (rhbz#1365584)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-22
- Fix FailsToInstall
- Clean up the spec file

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Björn Esser <bjoern.esser@gmail.com> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 30 2015 Björn Esser <bjoern.esser@gmail.com> - 0.10-7
- added needed stuff for el5

* Mon Jun 29 2015 Björn Esser <bjoern.esser@gmail.com> - 0.10-6
- re-import after unretirement (#1236294)
- added Patch0 and Patch1 as suggested in review

* Sat Jun 27 2015 Björn Esser <bjoern.esser@gmail.com> - 0.10-5.1
- unretire in Fedora (#1236294)

* Fri Feb 18 2011 Fabian Affolter <fabian@bernewireless.net> - 0.10-5
- Fixed build issue with libusb

* Sat Jul 17 2010 Fabian Affolter <fabian@bernewireless.net> - 0.10-4
- Rename garmintools to garmintools.conf to fix #615119

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.10-3
- Explicitly BR libgarmin-static in accordance with the Packaging
  Guidelines (libgarmin-devel is still static-only).

* Tue Sep 22 2009 Fabian Affolter <fabian@bernewireless.net> - 0.10-2
- Fixed ldconfig stuff
- Fixed ownership of files
- Fixed rpath

* Sat May 02 2009 Fabian Affolter <fabian@bernewireless.net> - 0.10-1
- Updated to new upstream version 0.10

* Thu Sep 11 2008 Fabian Affolter <fabian@bernewireless.net> - 0.09-2
- Fix spec file acc. #461849 Comment #1

* Wed Sep 10 2008 Fabian Affolter <fabian@bernewireless.net> - 0.09-1
- Initial spec for Fedora
