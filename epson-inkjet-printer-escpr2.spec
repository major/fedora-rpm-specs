# The lsb release used in the tarball name
%global lsb 1lsb3.2
# Not defined on el6
%{!?_cups_serverbin: %global _cups_serverbin %(/usr/bin/cups-config --serverbin)}

Name:           epson-inkjet-printer-escpr2
Summary:        Drivers for Epson inkjet printers
Version:        1.1.48
Release:        2.%{lsb}%{?dist}
License:        GPLv2+
URL:            http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX
# Download address is garbled on web page, and only .src.rpm is offered.
Source0:        https://download3.ebz.epson.net/dsc/f/03/00/13/52/26/977f2b2c13cc185981479fbd225b802c35c92beb/epson-inkjet-printer-escpr2-1.1.48-1lsb3.2.src.rpm
BuildArch:      noarch

# The escpr2 drivers are binary only blobs, but at least some of the PPD files work with the escpr driver
Requires:       epson-inkjet-printer-escpr

%if 0%{?fedora} >= 21
# For automatic detection of printer drivers
BuildRequires:  python3-cups
%endif
%if 0%{?rhel} == 7
# For automatic detection of printer drivers
BuildRequires:  python-cups
%endif
%if 0%{?rhel} == 6
# For dir ownership
Requires:       cups
%else
# For dir ownership
Requires:       cups-filesystem
# So that automatic printer driver installation works
BuildRequires:  python-cups
%endif

%description
This package contains PPD files for newer Epson Inkjet printers which
are not available in the fully open source epson-inkjet-printer-escpr
driver.

The escpr2 driver relies on a binary blob in the source package, which
has been removed in Fedora. The PPD files have been patched to use the
open source escpr driver, instead.

Although many of the PPD files work with the older, fully open source
driver (e.g. ET-3700 seems to work), it is quite likely that some
don't. This is not a bug in the Fedora package, but a limitation of
the partly closed-source upstream drivers.

%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -ivd
rm lsb-rpm.spec
tar zxvf epson-inkjet-printer-escpr2-%{version}-%{lsb}.tar.gz
mv epson-inkjet-printer-escpr2-%{version} src

find . -name \*.a -delete
find . -name \*.la -delete
find src/ -name \*.h -exec chmod 644 {} \;
find src/ -name \*.c -exec chmod 644 {} \;

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/ppd/Epson/epson-inkjet-printer-escpr
# Hack ppd files so that they use the open source v1 driver instead of
# the v2 binary blob and compress them
for ppd in src/ppd/*.ppd; do
    sed "s|epson-escpr-wrapper2|epson-escpr-wrapper|g" $ppd > %{buildroot}%{_datadir}/ppd/Epson/epson-inkjet-printer-escpr/$(basename $ppd)
    gzip %{buildroot}%{_datadir}/ppd/Epson/epson-inkjet-printer-escpr/$(basename $ppd)
done

%files
%license src/COPYING
%doc src/README src/README.ja src/AUTHORS src/NEWS
%{_datadir}/ppd/Epson/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.48-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.48-1.1lsb3.2
- Update to 1.1.48.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-4.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.24-1.1lsb3.2
- Update to 1.1.24 with review fixes.

* Fri Sep 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.18-1.1lsb3.2
- First release.
