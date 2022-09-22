# data-only package
%global debug_package %{nil}

# NOTE: this package is not noarch because LibreOffice has no
# arch-independent extension location

Name: libreoffice-gallery-vrt-network-equipment
Version: 1.2.0
Release: 18%{?dist}
Summary: A network equipment shape gallery for LibreOffice

License: CC-BY-SA
URL: http://www.vrt.com.au/downloads/vrt-network-equipment
Source0: http://www.vrt.com.au/sites/default/files/download/VRTnetworkequipment_%{version}-lo.oxt
Source1: libreoffice-gallery-vrt-network-equipment.metainfo.xml

Requires: libreoffice-core%{?_isa}

%description
A network equipment shape gallery for LibreOffice.

The gallery includes
* Clients & Displays: desktop, thin client, laptop, tablets, phones,
  industrial panel PCs, wide-screen TV and projector systems.
* Peripherals: Just printers and fax for now.
* Servers: a range of tower, rack and industrial PCs with emblems for a
  range of server roles - mix-n-match to suit (the tower can also be
  used with the thin client to create a desktop tower).
* Network & Power: Infrastructure for your network, including industrial
  fibre/Ethernet/serial components and odds and ends for wireless and
  mesh networking, solar systems and UPS.
* Sensors & Controllers: PLCs & remote I/O, RTUs, data loggers,
  electricity, water and gas meters, CCTV.

%prep
%setup -q -c -n %{name}-%{version}
find . -type f -print0 | xargs -0 chmod -x
mv Release-notes release-notes

%build

%install
install -d -m 0755 %{buildroot}%{_libdir}/libreoffice/share/extensions/vrt-network-equipment
cp -pr * %{buildroot}%{_libdir}/libreoffice/share/extensions/vrt-network-equipment
install -d -m 0755 %{buildroot}%{_datadir}/appdata
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

%files
%{_datadir}/appdata/%{name}.metainfo.xml
%{_libdir}/libreoffice/share/extensions/vrt-network-equipment

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 David Tardon <dtardon@redhat.com> - 1.2.0-4
- add appdata addon metadata

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 David Tardon <dtardon@redhat.com> - 1.2.0-1
- new upstream release

* Sat Jul 19 2014 David Tardon <dtardon@redhat.com> - 1.1.1-1
- new upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 David Tardon <dtardon@redhat.com> - 1.0.4-1
- new release

* Tue Sep 10 2013 David Tardon <dtardon@redhat.com> - 1.0.3-1
- initial import
