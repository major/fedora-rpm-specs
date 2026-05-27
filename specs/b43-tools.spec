Name:		b43-tools
Version:	020
Release:	%autorelease
Summary:	Tools for the Broadcom 43xx series WLAN chip
# assembler — GPLv2
# debug — GPLv3
# disassembler — GPLv2
# ssb_sprom — GPLv2+
License:	GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
URL:		https://github.com/mbuesch/b43-tools
VCS:		git:%{url}.git
Source:		%{url}/archive/b34-fwcutter-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	flex-static
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	python3-devel


%description
Tools for the Broadcom 43xx series WLAN chip.


%prep
%autosetup -p1 -C
install -p -m 0644 assembler/COPYING COPYING.assembler
install -p -m 0644 assembler/README README.assembler
install -p -m 0644 debug/COPYING COPYING.debug
install -p -m 0644 debug/README README.debug
install -p -m 0644 disassembler/COPYING COPYING.disassembler
install -p -m 0644 ssb_sprom/README README.ssb_sprom
install -p -m 0644 ssb_sprom/COPYING COPYING.ssb_sprom


%build
CFLAGS="%{optflags}" %{make_build} -C assembler
CFLAGS="%{optflags}" %{make_build} -C disassembler
CFLAGS="%{optflags}" %{make_build} -C ssb_sprom


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm.bin %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-dasm %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-fwconv %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 ssb_sprom/ssb-sprom %{buildroot}%{_bindir}
# debug tools (pure Python, manual install)
install -p -m 0755 debug/b43-beautifier %{buildroot}%{_bindir}
install -p -m 0755 debug/b43-fwdump %{buildroot}%{_bindir}
install -d %{buildroot}%{python3_sitelib}
install -p -m 0644 debug/libb43.py %{buildroot}%{python3_sitelib}


%files
%doc README.*
%license COPYING.*
%{_bindir}/b43-asm
%{_bindir}/b43-asm.bin
%{_bindir}/b43-beautifier
%{_bindir}/b43-dasm
%{_bindir}/b43-fwdump
%{_bindir}/b43-ivaldump
%{_bindir}/brcm80211-fwconv
%{_bindir}/brcm80211-ivaldump
%{_bindir}/ssb-sprom
%pycached %{python3_sitelib}/libb43.py


%changelog
%autochangelog
