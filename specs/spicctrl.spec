Name:           spicctrl
Version:        1.9
Release:        37%{?dist}
Summary:        Sony Vaio laptop SPIC control program

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://popies.net/sonypi/
Source0:        http://popies.net/sonypi/spicctrl-%{version}.tar.bz2

ExclusiveArch:	%{ix86} x86_64

BuildRequires: make
BuildRequires:  gcc
%description
spicctrl queries and sets a variety of parameters on Sony Vaio laptop
computers, including AC Power status, battery status, screen brightness,
and bluetooth device power status


%prep
%setup -q
%{__sed} -i 's/ -O2 / $(RPM_OPT_FLAGS) /' Makefile


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m755 spicctrl $RPM_BUILD_ROOT%{_sbindir}
install -p -m644 spicctrl.1 $RPM_BUILD_ROOT%{_mandir}/man1



%post
if [ ! -c /dev/sonypi ]; then
	rm -f /dev/sonypi
	mknod /dev/sonypi c 10 250
fi
if [ -e /etc/modprobe.conf ]; then
	grep 'alias char-major-10-250 sonypi' /etc/modprobe.conf > /dev/null
	RETVAL=$?
	if [ $RETVAL -ne 0 ]; then
		echo 'alias char-major-10-250 sonypi' >> /etc/modprobe.conf
		echo 'options sonypi minor=250' >> /etc/modprobe.conf
	fi
fi


%files
%doc AUTHORS CHANGES LICENSE
%{_sbindir}/spicctrl
%{_mandir}/man1/spicctrl.1.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9-36
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Michel Salim <salimma@fedoraproject.org> - 1.9-7
- Enable x86_64 build

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9-7
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9-6
- Autorebuild for GCC 4.3

* Mon Nov 13 2006 Michel Salim <michel.salim@gmail.com> 1.9-5
- Rebuild for Fedora Extras 6

* Sat May 20 2006 Roozbeh Pournader <roozbeh@farsiweb.info> 1.9-4
- Respect $RPM_OPT_FLAGS (also fixes debuginfo), use correct
  man page permissions (Ville Skyttä)

* Tue Feb 14 2006 Roozbeh Pournader <roozbeh@farsiweb.info> 1.9-3
- Rebuild for Fedora Extras 5

* Tue Jan 31 2006 Roozbeh Pournader <roozbeh@farsiweb.info> 1.9-2
- Bumped release to a proper integer

* Sun Jan 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> 1.9-1.4
- Add %%{?dist} tag

* Mon Dec 26 2005 Roozbeh Pournader <roozbeh@farsiweb.info> 1.9-1.3
- Change ExclusiveArch to %%{ix86}

* Mon Dec 26 2005 Roozbeh Pournader <roozbeh@farsiweb.info> 1.9-1.2
- Add ExclusiveArch

* Thu Dec 22 2005 Roozbeh Pournader <roozbeh@farsiweb.info> 1.9-1.1
- First revision, based on upstream spec file
