Summary:		A robust log colorizer
Summary(ru):	Мощный коллоризатор логов
Name:		ccze
Version:		0.2.1
Release:		29%{?dist}
# http://web.archive.org/web/20040803024236/bonehunter.rulez.org/CCZE.phtml
URL:			http://bonehunter.rulez.org/CCZE.html
License:		GPLv2+
Source:		ftp://bonehunter.rulez.org/pub/ccze/stable/ccze-%{version}.tar.gz
# Package intended to EL-5 too, so we still need define BuildRoot
BuildRequires:  gcc
BuildRequires:	ncurses-devel >= 5.0, pcre-devel >= 3.1
BuildRequires: make
# Upstream is dead. So, patch himself.
Patch0:		ccze-0.2.1-Wmulticharacter.patch
# Upstream is dead, port Debian patch to correct handle -o switch
Patch1:		ccze-opts.diff

%description
CCZE is a roboust and modular log colorizer, with plugins for apm,
exim, fetchmail, httpd, postfix, procmail, squid, syslog, ulogd,
vsftpd, xferlog and more.

%description -l ru
CCZE это мощный и модульный раскрашиватель логов. Имеются модули-
-плагины для: apm, exim, fetchmail, httpd, postfix, procmail, squid,
syslog, ulogd, vsftpd, xferlog и другие.

%prep
%setup -q
%patch0 -p1 -b .-Wmulticharacter
%patch1 -p1 -b .-Wmulticharacter

%build
%configure --with-builtins=all
# To avoid problem: /usr/include/errno.h:69: error: two or more data types in declaration specifiers
# we add -D__error_t_defined=1 to inform what errno_t already defined.
make %{?_smp_mflags} CFLAGS="%{optflags} -D__error_t_defined=1"

%install
rm -rf %{buildroot}

iconv -f ISO-8859-1 -t UTF-8 THANKS > THANKS.new
touch --reference THANKS THANKS.new
mv -f THANKS.new THANKS

#% makeinstall
make install DESTDIR="%{buildroot}"

install -d %{buildroot}/%{_sysconfdir}
src/ccze-dump > %{buildroot}/%{_sysconfdir}/cczerc

rm %{buildroot}/%{_includedir}/ccze.h

%files
%doc AUTHORS COPYING ChangeLog ChangeLog-0.1 NEWS README THANKS FAQ
%config(noreplace) %{_sysconfdir}/cczerc
%{_bindir}/ccze
%{_bindir}/ccze-cssdump
%{_mandir}/man1/ccze.1*
%{_mandir}/man1/ccze-cssdump.1*
%{_mandir}/man7/ccze-plugin.7*

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.2.1-9
- Rebuild against PCRE 8.30

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 5 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.2.1-6
- Port from Debian Patch1:		ccze-opts.diff. BZ#578958

* Tue Aug 4 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.2.1-5
- Things of Martin Gieseking in informal review:
- Add %%{?_smp_mflags} to make.
- Change BuildRoot.

* Sat Jul 11 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.2.1-4
- %%makeinstall replaced by make install DESTDIR="%%{buildroot}" as pointed by Jussi Lehtola.

* Sat Jul 11 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.2.1-3
- Import form ftp://ftp.pbone.net/mirror/norlug.org/norlug/redhat-7.3/SRPMS/ccze-0.2.1-2.norlug.src.rpm
- Reformat with tabs.
- Remove unneded defines, and replece it by direct values in appropriate tags:
	%%define version 0.2.1, %%define dist stable, %%define release 2.norlug
- Add %%{?dist} part into release
- Add Fedora system optflags to build
- Add Patch0: ccze-0.2.1-Wmulticharacter.patch
- Add -D__error_t_defined=1 into CFLAGS.
- Add clan buildroot in %%install
- License changed from GPL to GPLv2+
- Add noreplace option to %%config file
- Remove devel file %%{_includedir}/ccze.h
- Add COPYING to %%doc files.
- iconv'ed THANKS from ISO-8859-1 (guessed)
- Add Summary and description on Russian.

* Thu Sep 4 2003 Chip Cuccio <chipster@norlug.org> 0.2.1-2
- initial build
