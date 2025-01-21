Name:          tnftp
Version:       20230507
Release:       6%{?dist}
Summary:       FTP (File Transfer Protocol) client from NetBSD

License:       0BSD AND BSD-2-Clause AND BSD-3-Clause AND ISC

# From the README:
# `tnftp' is a `port' of the NetBSD FTP client to other systems.
# See http://www.NetBSD.org/ for more details about NetBSD.
URL:           http://www.NetBSD.org/
Source0:       http://ftp.netbsd.org/pub/NetBSD/misc/%{name}/%{name}-%{version}.tar.gz
Source1:       http://ftp.netbsd.org/pub/NetBSD/misc/%{name}/%{name}-%{version}.tar.gz.asc
Source2:       gpgkey-2A8E22EDB07B5414548D8507A4186D9A7F332472.gpg

BuildRequires: make
BuildRequires: libedit-devel
BuildRequires: openssl-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gnupg2

%description
%{name} is the FTP (File Transfer Protocol) client from NetBSD.  FTP
is a widely used protocol for transferring files over the Internet and
for archiving files.  %{name} provides some advanced features beyond
the Linux netkit ftp client, but maintains a similar user interface to
the traditional ftp client.  It was formerly called lukemftp.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
export CFLAGS="%{optflags}"
%configure --enable-editcomplete \
           --without-local-libedit \
           --enable-ipv6 \
           --enable-ssl
%make_build

%install
%make_install

%files
%doc ChangeLog INSTALL NEWS README THANKS todo
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20230507-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230507-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 David Cantrell <dcantrell@redhat.com> - 20230507-4
- Use %%autosetup in %%prep

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230507-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230507-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 David Cantrell <dcantrell@redhat.com> - 20230507-1
- Upgrade to tnftp-20230507 (#2203899)
- Change License tag to SPDX expression
- Add signature verification before unpacking source archive

* Mon Apr 10 2023 David Cantrell <dcantrell@redhat.com> - 20230409-1
- Upgrade to tnftp-20230409

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20210827-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210827-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210827-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 20210827-2
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 30 2021 David Cantrell <dcantrell@redhat.com> - 20210827-1
- Upgrade to tnftp-20210827 (#1998401)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200705-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 23 2021 David Cantrell <dcantrell@redhat.com> - 20200705-1
- Upgrade to tnftp-20200705 (#1853905)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 06 2015 David Cantrell <dcantrell@redhat.com> - 20151004-1
- Upgrade to tnftp-20151004 (#1268664)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 David Cantrell <dcantrell@redhat.com> - 20141104-1
- Upgrade to tnftp-20141104 (#1160314)

* Fri Oct 31 2014 David Cantrell <dcantrell@redhat.com> - 20141031-1
- Upgrade to tnftp-20141031 to fix CVE-2014-8517 (#1158287)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130505-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 David Cantrell <dcantrell@redhat.com> - 20130505-7
- Link with system libedit rather than using internal one (#1079639)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130505-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130505-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 David Cantrell <dcantrell@redhat.com> - 20130505-4
- Add missing %%changelog lines and increment release number

* Thu May 30 2013 David Cantrell <dcantrell@redhat.com> - 20130505-3
- Remove the remaining unnecessary 'rm -rf %%{buildroot}'
- Include ChangeLog on the %%doc line
- Change License field to 'BSD and ISC'

* Wed May 29 2013 David Cantrell <dcantrell@redhat.com> - 20130505-2
- Remove unnecessary %%clean section
- Remove unnecessary %%defattr line in %%files section
- Use the %%{name} macro in the %%description and %%files sections
- Change URL to 'http://www.NetBSD.org/'

* Thu May 16 2013 David Cantrell <dcantrell@redhat.com> - 20130505-1
- Initial package
