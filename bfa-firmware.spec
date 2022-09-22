Name:		bfa-firmware
Summary:	Brocade Fibre Channel HBA Firmware
Version:	3.2.21.1
Release:	18%{?dist}
License:	Redistributable, no modification permitted
Source0:	LICENSE
# These files were taken from:
# http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
# No direct link is available.
Source1:	bfa_firmware_linux-3.0.0.0-0.tgz
Source2:	bfa_firmware_linux-3.0.3.1-0.tgz
Source3:	bfa_fw_update_to_v3.1.2.1.tgz
Source4:	bfa_fw_update_to_v3.2.21.1.tgz
URL:		http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
BuildArch:	noarch
# Needed for /lib/firmware
Requires:	udev

%description
Brocade Fibre Channel HBA Firmware.

%prep
%setup -c -T
unpack_bfa_firmware() {
	filename=$1
	version=$2
	dir=$3
	installversion=${4:-$version}

	tar xvf $RPM_SOURCE_DIR/$1
	pushd $3
	for i in cbfw ctfw ct2fw; do
		if [ -f $i.bin ]; then
			mv $i.bin $i-$installversion.bin;
		elif [ "$installversion" != "$version" ]; then
			mv $i-$version.bin $i-$installversion.bin
		fi
	done
	popd
}

unpack_bfa_firmware bfa_fw_update_to_v3.2.21.1.tgz 3.2.1.0 bfa_fw_update_to_v3.2.21.1
unpack_bfa_firmware bfa_fw_update_to_v3.1.2.1.tgz 3.1.0.0 bfa_fw_v3.1.2.1
unpack_bfa_firmware bfa_firmware_linux-3.0.3.1-0.tgz 3.0.3.1 .
unpack_bfa_firmware bfa_firmware_linux-3.0.0.0-0.tgz 3.0.0.0 3.0_GA_firwmare_image

if [ ! -f ./LICENSE ]; then
   cp %{SOURCE0} ./
fi

%build
# Firmware, do nothing.

%install
install_bfa_firmware() {
	ver=$1
	dir=$2

	pushd $dir
	install -m0644 cbfw-$ver.bin ct2fw-$ver.bin ctfw-$ver.bin %{buildroot}/lib/firmware/
	popd
}

link_bfa_firmware() {
	dstver=$2
	srcver=$1

	pushd %{buildroot}/lib/firmware/
		ln -s cbfw$srcver.bin cbfw$dstver.bin
		ln -s ct2fw$srcver.bin ct2fw$dstver.bin
		ln -s ctfw$srcver.bin ctfw$dstver.bin
	popd
}

mkdir -p %{buildroot}/lib/firmware/

install_bfa_firmware 3.2.1.0 bfa_fw_update_to_v3.2.21.1
install_bfa_firmware 3.1.0.0 bfa_fw_v3.1.2.1
install_bfa_firmware 3.0.3.1 .

# RHEL 6.3 uses unversioned filenames
# RHEL 6.4 starting with 3.0.3.1 uses versioned filenames
%if 0%{?rhel}
	install_bfa_firmware 3.0.0.0 3.0_GA_firwmare_image
	link_bfa_firmware "-3.0.0.0"
%else
# Upstream starting with 3.1.0.0 uses versioned filenames
#  so link the old version to the old names as expected
	link_bfa_firmware "-3.0.3.1"
%endif

%files
%doc LICENSE
/lib/firmware/cbfw.bin
/lib/firmware/ctfw.bin
/lib/firmware/ct2fw.bin
/lib/firmware/cbfw-3.2.1.0.bin
/lib/firmware/ctfw-3.2.1.0.bin
/lib/firmware/ct2fw-3.2.1.0.bin
/lib/firmware/cbfw-3.1.0.0.bin
/lib/firmware/ctfw-3.1.0.0.bin
/lib/firmware/ct2fw-3.1.0.0.bin
/lib/firmware/cbfw-3.0.3.1.bin
/lib/firmware/ctfw-3.0.3.1.bin
/lib/firmware/ct2fw-3.0.3.1.bin
%if 0%{?rhel}
/lib/firmware/cbfw-3.0.0.0.bin
/lib/firmware/ctfw-3.0.0.0.bin
/lib/firmware/ct2fw-3.0.0.0.bin
%endif

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.21.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.21.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.21.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Tom Callaway <spot@fedoraproject.org> - 3.2.21.1-3
- do not copy LICENSE over itself (fixed FTBFS)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Kyle McMartin <kmcmarti@redhat.com> - 3.2.21.1-1
- update to 3.2.21.1, linked to 3.2.1.0 based on Brocade's submission
  for 3.11 ( http://marc.info/?l=linux-scsi&m=136843872927453&w=2 )

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Kyle McMartin <kmcmarti@redhat.com> 3.1.2.1-1
- update to 3.1.2.1
- add some shell functions to make life easier for multi-versioned firmware
  filenames that are now upstream

* Thu Sep  6 2012 Tom Callaway <spot@fedoraproject.org> 3.0.3.1-1
- update to 3.0.3.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 07 2011 Tom Callaway <spot@fedoraproject.org> 3.0.0.0-1
- update to 3.0.0.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Tom Callaway <spot@fedoraproject.org> 2.3.2.3-1
- update to 2.3.2.3

* Mon Mar  8 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.2.1-2
- Add missing Requires: udev

* Fri Jan 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.2.1-1
- Initial package for Fedora
