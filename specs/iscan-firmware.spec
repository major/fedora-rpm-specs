Summary:	Firmware for Epson flatbed scanners
Name:		iscan-firmware
Version:	20241112
Release:	%autorelease
# AVASYSPL.en.txt and LICENSE.EPSON.en.txt are LicenseRef-Fedora-Firmware:
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/608
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/610
License:	LicenseRef-Fedora-Firmware
URL:		http://download.ebz.epson.net/dsc/search/01/search/
BuildArch:	noarch

# All firmware files can be downloaded individually, by searching per model, at:
# http://download.ebz.epson.net/dsc/search/01/search/

# The tarball contains a random version of the software, libraries and a firmware
# package (a "plugin"). The plugin package contains the firmware file.

# GT-F500, GT-F550, Perfection 2480 Photo, Perfection 2580 Photo
Source0:    iscan-plugin-gt-f500-1.0.0-1.c2.i386.rpm
# GT-9400UF, Perfection 3170 Photo
Source1:    iscan-plugin-gt-9400-1.0.0-1.c2.i386.rpm
# GT-F520, GT-F570, Perfection 3490 Photo, Perfection 3590 Photo
Source2:    iscan-plugin-gt-f520-1.0.0-1.c2.i386.rpm
# GT-F600, Perfection 4180 Photo
Source3:    iscan-plugin-gt-f600-1.0.0-1.c2.i386.rpm
# GT-X750, Perfection 4490 Photo
Source4:    iscan-plugin-gt-x750-2.1.2-1.x86_64.rpm
# GT-F650, GT-S600, Perfection V10, Perfection V100 Photo
Source5:    iscan-plugin-gt-s600-2.1.2-1.x86_64.rpm
# GT-F670, Perfection V200 Photo
Source6:    iscan-plugin-gt-f670-2.1.2-1.x86_64.rpm
# GT-F700, Perfection V350 Photo
Source7:    iscan-plugin-gt-f700-2.1.2-1.x86_64.rpm
# GT-1500, GT-D1000
Source8:    iscan-plugin-gt-1500-2.2.0-1.x86_64.rpm
# GT-F720, GT-S620, Perfection V30, Perfection V300 Photo
Source9:    esci-interpreter-gt-f720-0.1.1-2.x86_64.rpm
# GT-X770, Perfection V500 Photo
Source10:   iscan-plugin-gt-x770-2.1.2-1.i386.rpm

Requires:	linux-firmware

%description
Firmware for the following Epson flatbed scanners:

* esfw32: Perfection 3170 PHOTO / GT-9400
* esfw41: Perfection 2480/2580 PHOTO / GT-F500/F550
* esfw43: Perfection 4180 PHOTO / GT-F600
* esfw52: Perfection 3490/3590 PHOTO / GT-F520/F570
* esfw54: Perfection 4490 PHOTO / GT-X750
* esfw66: Perfection V10/V100 PHOTO / GT-S600 / GT-F650
* esfw68: Perfection V350 PHOTO / GT-F700
* esfw7A: Perfection V200 PHOTO / GT-F670
* esfw7C: Perfection V500 PHOTO / GT-X770
* esfw86: GT-1500 / GT-D1000
* esfw8b: Perfection V30/V300 / GT-F720 / GT-S620

%prep
%setup -c -T
for f in \
    %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
    %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10}; do
    rpm2cpio $f | cpio -idm --no-absolute-filenames
done

find ./%{_docdir} -name "*txt" -exec mv {} . \;

for file in *.txt ; do
    iconv -f euc-jp -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/epson
install -pm644 .%{_datadir}/*/*.bin %{buildroot}%{_prefix}/lib/firmware/epson/

%files
%license AVASYSPL.en.txt EAPL.en.txt LICENSE.EPSON.en.txt
%lang(ja) %license AVASYSPL.ja.txt EAPL.ja.txt LICENSE.EPSON.ja.txt
%dir %{_prefix}/lib/firmware/epson
%{_prefix}/lib/firmware/epson/esfw32.bin
%{_prefix}/lib/firmware/epson/esfw41.bin
%{_prefix}/lib/firmware/epson/esfw43.bin
%{_prefix}/lib/firmware/epson/esfw52.bin
%{_prefix}/lib/firmware/epson/esfw54.bin
%{_prefix}/lib/firmware/epson/esfw66.bin
%{_prefix}/lib/firmware/epson/esfw68.bin
%{_prefix}/lib/firmware/epson/esfw7A.bin
%{_prefix}/lib/firmware/epson/esfw7C.bin
%{_prefix}/lib/firmware/epson/esfw86.bin
%{_prefix}/lib/firmware/epson/esfw8b.bin

%changelog
%autochangelog
