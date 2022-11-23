# data-only package
%global debug_package %{nil}

# NOTE: this package is not noarch because LibreOffice has no
# arch-independent extension location

Name: libreoffice-gallery-vrt-network-equipment
Version: 1.2.0
Release: %autorelease
Summary: A network equipment shape gallery for LibreOffice

License: CC-BY-SA-3.0
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
%autochangelog
