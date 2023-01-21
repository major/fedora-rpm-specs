Name:               irssi-xmpp
Version:            0.54
Release:            13%{?dist}
Summary:            XMPP plugin into irssi
License:            GPLv2
URL:                http://cybione.org/~irssi-xmpp/
Source0:            http://cybione.org/~irssi-xmpp/files/%{name}-%{version}.tar.gz

BuildRequires:	irssi-devel
BuildRequires:	loudmouth-devel
BuildRequires:	gcc
BuildRequires: make

Patch0:             irssi-xmpp-0.52-config.patch

Requires: irssi
Requires: loudmouth

%description
Irssi-xmpp is an irssi plugin to connect to the Jabber network.

%prep
%setup -q
%patch0 -p1 -b .config

%build
%{__make} PREFIX=%{_prefix} %{?_smp_mflags} RH_FLAGS="$RPM_OPT_FLAGS"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} PREFIX=%{_prefix} IRSSI_LIB=%{_libdir}/irssi install DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf $RPM_BUILD_ROOT%{_prefix}/share/doc/
%{__rm} -rf $RPM_BUILD_ROOT%{_prefix}/share/irssi

%files
%doc docs/* help/* README.md NEWS TODO
%license COPYING
%{_libdir}/irssi/modules/libfe_xmpp.so
%{_libdir}/irssi/modules/libtext_xmpp.so
%{_libdir}/irssi/modules/libxmpp_core.so

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.54-4
- Rebuild to fix BZ #1575982

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Marcel Haerry <mh+fedora@scrit.ch> - 0.54-1
- Update to latest upstream release

* Wed Aug 02 2017 Marcel Haerry <mh+fedora@scrit.ch> - 0.53-1
- Update to latest upstream release
- Make it work with irssi 1.0 (#1423746)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.52-4
- remove extra line

* Wed Feb 05 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.52-3
- fix some lines in to the patch

* Wed Feb 05 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.52-2
- change config patch for the new version

* Wed Feb 05 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.52-1
- new upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 06 2010 Matěj Cepl <mcepl@redhat.com> - 0.51-1
- New upstream release

* Sun Mar 28 2010 Nikola Pajkovsky <npajkovs@redhat.com> 0.50-4
- previous commit contain empty patch which fix standard fedora CFLAGS
- fix: 577367 - irssi-xmpp not built with $RPM_OPT_FLAGS

* Sun Mar 21 2010 Nikola Pajkovsky <npajkovs@redhat.com> 0.50-3
- add standard fedora CFLAGS
- COPYING README NEWS TODO as doc files
- fix Source0 url

* Tue Aug 18 2009 Nikola Pajkovsky <npajkovs@redhat.com> 0.50-2
- change install section. No patch is needed.
- resolved compilation on x86_64

* Thu Aug 13 2009 Nikola Pajkovsky <npajkovs@redhat.com> 0.50-1
- initial build



