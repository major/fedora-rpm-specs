Name:           http_ping
Version:        20160309
Release:        18%{?dist}
Summary:        HTTP latency measuring utility

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.acme.com/software/http_ping/
Source0:        http://www.acme.com/software/http_ping/%{name}_09Mar2016.tar.gz

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig
BuildRequires: make

%description
http_ping runs an HTTP fetch every few seconds, timing how long it
takes.


%prep
%setup -q -n %{name}
f=http_ping.1 ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
make %{?_smp_mflags} \
  CFLAGS="$RPM_OPT_FLAGS -DUSE_SSL $(pkg-config openssl --cflags)" \
  LDFLAGS="$(pkg-config openssl --libs)"


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 http_ping $RPM_BUILD_ROOT%{_bindir}/http_ping
install -Dpm 644 http_ping.1 $RPM_BUILD_ROOT%{_mandir}/man1/http_ping.1



%files
%doc README
%{_bindir}/http_ping
%{_mandir}/man1/http_ping.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 20160309-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 20160309-9
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20160309-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 alciregi <alciregi@fedoraproject.org> - 20160309-3
- Minor corrections to spec file

* Fri Dec 13 2019 alciregi <alciregi@fedoraproject.org> - 20160309-2
- Minor corrections to spec file

* Fri Dec 13 2019 alciregi <alciregi@fedoraproject.org> - 20160309-1
- Changed wrong version in spec file

* Wed Dec 11 2019 alciregi <alciregi@fedoraproject.org> - 09Mar2016-0
- Update to 09Mar2016.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20050629-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20050629-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20050629-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20050629-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20050629-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20050629-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20050629-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20050629-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 20050629-11
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050629-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 20050629-8
- rebuild with new openssl

* Sat Feb  9 2008 Ville Skyttä <ville.skytta at iki.fi> - 20050629-7
- Rebuild.

* Tue Dec  4 2007 Ville Skyttä <ville.skytta at iki.fi> - 20050629-6
- Rebuild.

* Tue Aug 21 2007 Ville Skyttä <ville.skytta at iki.fi> - 20050629-5
- Rebuild.

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 20050629-4
- Rebuild.

* Thu Feb 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 20050629-3
- Convert man page to UTF-8.

* Wed Nov  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050629-2
- Rebuild for new OpenSSL.

* Fri Oct 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050629-1
- Update to 29jun2005.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.0-3.20020403
- rebuilt

* Mon May  3 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20020403
- BuildRequires pkgconfig (bug 930).

* Sat Nov  1 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20020403
- First build.
