Name:		gdigi
Version:	0.4.0
Release:	20140229gitcada964d%{?dist}
Summary:	Utility to control DigiTech effect pedals
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		http://desowin.org/gdigi/
Source0:	http://downloads.sourceforge.net/project/gdigi/gdigi/%{version}/%{name}-%{version}.tar.bz2
Source1:	gdigi.png
Source2:	icon.png
Patch0:		gdigi-0.4.0-git.patch
Patch1:		gdigi-define_var_as_extern.patch
BuildRequires:  gcc
BuildRequires:	expat-devel gtk3-devel alsa-lib-devel libxml2-devel desktop-file-utils
BuildRequires: make

%description
%{name} is a tool aimed to provide X-Edit functionality to Linux users.

Supported devices: RP150, RP155, RP250, RP255, RP355, RP500, RP1000,
		   GNX3000, GNX4K.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
mkdir -p $RPM_BUILD_DIR/%{name}-%{version}/images
install -m 644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_DIR/%{name}-%{version}/images/

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/%{_datadir}/applications/
mkdir -p %{buildroot}/%{_datadir}/icons/
mkdir -p %{buildroot}/%{_mandir}/man1/
make install DESTDIR=%{buildroot}
install -p -m 644 gdigi.1 %{buildroot}/%{_mandir}/man1/gdigi.1
desktop-file-validate %{buildroot}/%{_datadir}/applications/gdigi.desktop

%files
%doc AUTHORS COPYING HACKING README TODO
%{_bindir}/gdigi
%{_mandir}/man1/gdigi.1.gz
%{_datadir}/applications/gdigi.desktop
%{_datadir}/icons/gdigi.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140229gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-20140228gitcada964d
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140227gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140226gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140225gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140224gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140223gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140222gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140221gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140220gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140219gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140218gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140217gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140216gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140215gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140214gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140213gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140212gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140211gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140210gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20140209gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-20140208gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-20140207gitcada964d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Mauro Carvalho Chehab <mchehab@redhat.com> - 0.4.0-20140206gitcada964d
- Update to the latest version, with adds some fixes for RP500 and RP1000

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.4.0-.1.fc19
- Update to version 0.4.0 with effect pedal support

* Mon Dec 03 2012 Mauro Carvalho Chehab <mchehab@redhat.com> 0.3.0-20121203git.2.fc19
- Update changelog

* Mon Dec 03 2012 Mauro Carvalho Chehab <mchehab@redhat.com> 0.3.0-20121203git.1.fc19
- Update to today's git, with fixes FSF addresses

* Sun Dec 02 2012 Mauro Carvalho Chehab <mchehab@redhat.com> 0.3.0-20121202git.2.fc19
- fix rpmlint compliants, removed requires, validate .desktop, drop obsoleted tags

* Sun Dec 02 2012 Mauro Carvalho Chehab <mchehab@redhat.com> 0.3.0-20121202git.1.fc19
- Package created

