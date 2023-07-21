Name:		b43-openfwwf
Version:	5.2
Release:	31%{?dist}
Summary:	Open firmware for some Broadcom 43xx series WLAN chips
License:	GPLv2
URL:		http://www.ing.unibs.it/openfwwf/
Source0:	http://www.ing.unibs.it/openfwwf/firmware/openfwwf-%{version}.tar.gz
Source1:	README.openfwwf
Source2:	openfwwf.conf
BuildArch:	noarch
BuildRequires:	b43-tools, gcc-c++
BuildRequires: make
Requires:	udev
Requires:	module-init-tools


%description
Open firmware for some Broadcom 43xx series WLAN chips.
Currently supported models are 4306, 4311(rev1), 4318 and 4320.


%prep
%setup -q -n openfwwf-%{version}
sed -i s/"-o 0 -g 0"// Makefile
install -p -m 0644 %{SOURCE1} .
install -p -m 0644 %{SOURCE2} .

%build
%make_build


%install
make install PREFIX=%{buildroot}/lib/firmware/b43-open
install -p -D -m 0644 openfwwf.conf %{buildroot}%{_prefix}/lib/modprobe.d/openfwwf.conf


%files
%license COPYING LICENSE
%doc README.openfwwf
%dir /lib/firmware/b43-open
/lib/firmware/b43-open/b0g0bsinitvals5.fw
/lib/firmware/b43-open/b0g0initvals5.fw
/lib/firmware/b43-open/ucode5.fw
%{_prefix}/lib/modprobe.d/openfwwf.conf


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 5.2-24
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 John W. Linville <linville@redhat.com> - 5.2-20
- Add previously unnecessary BuildRequires for gcc-c++

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Peter Lemenkov <lemenkov@gmail.com> 5.2-13
- Spec-file cleanups.
- Changed directory for storing modprobe config (/usr/lib/modprobe.d is a
  directory for distro-defined defaults for modprobe).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 11 2010 Peter Lemenkov <lemenkov@gmail.com> 5.2-5
- Changed directory for storing firmware (rhbz #651350)

* Tue Mar 16 2010 John W. Linville <linville@redhat.com> 5.2-4
- Remove erroneous copyright notice from README.openfwwf

* Wed Jan 27 2010 Peter Lemenkov <lemenkov@gmail.com> 5.2-3
- Fixed typo in summary.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Peter Lemenkov <lemenkov@gmail.com> 5.2-1
- Ver. 5.2

* Mon Jun 29 2009 Peter Lemenkov <lemenkov@gmail.com> 5.1-3
- Changed README a lot
- Changed description

* Fri Jun  5 2009 Peter Lemenkov <lemenkov@gmail.com> 5.1-2
- Added config-file for modprobe

* Wed Mar 18 2009 Peter Lemenkov <lemenkov@gmail.com> 5.1-1
- Initial package for Fedora

