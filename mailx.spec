%global use_nss 0
%global mailrc %{_sysconfdir}/mail.rc

Summary: Enhanced implementation of the mailx command
Name: mailx
Version: 12.5
Release: 44%{?dist}
# MPLv1.1 .. nss.c, nsserr.c
License: BSD with advertising and MPLv1.1
URL: http://heirloom.sourceforge.net/mailx.html
# Mailx's upstream provides only the CVS method of downloading source code.
# Use get-upstream-tarball.sh script to download current version of mailx.
Source0: mailx-%{version}.tar.xz
Source1: get-upstream-tarball.sh

Patch0: nail-11.25-config.patch
Patch1: mailx-12.3-pager.patch
Patch2: mailx-12.5-lzw.patch
# resolves: #805410
Patch3: mailx-12.5-fname-null.patch
# resolves: #857120
Patch4: mailx-12.5-collect.patch
# resolves: #948869
Patch5: mailx-12.5-usage.patch
# resolves: #1099275 and #979460
Patch6: mailx-12.5-man-page-fixes.patch

Patch7: mailx-12.5-outof-Introduce-expandaddr-flag.patch
Patch8: mailx-12.5-fio.c-Unconditionally-require-wordexp-support.patch
Patch9: mailx-12.5-globname-Invoke-wordexp-with-WRDE_NOCMD-CVE-2004-277.patch
Patch10: mailx-12.5-unpack-Disable-option-processing-for-email-addresses.patch

# resolves: #1113617
Patch11: mailx-12.5-empty-from.patch
# resolves: #1296536
Patch12: mailx-12.5-nss-hostname-matching.patch
# resolves: #1494559
Patch13: mailx-12.5-encsplit.patch
# fix issues with openssl >= 1.1.0
Patch14: mailx-12.5-openssl.patch
# handle missing SSLv3 support
Patch15: mailx-12.5-no-SSLv3.patch

BuildRequires: make
BuildRequires: gcc

%if %{use_nss}
BuildRequires: nss-devel, pkgconfig, krb5-devel
%else
BuildRequires: openssl-devel
%endif

Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

Obsoletes: nail < %{version}
Provides: nail = %{version}

# For backwards compatibility:
Provides: /bin/mail
Provides: /bin/mailx

%description
Mailx is an enhanced mail command, which provides the functionality
of the POSIX mailx command, as well as SysV mail and Berkeley Mail
(from which it is derived).

Additionally to the POSIX features, mailx can work with Maildir/ e-mail
storage format (as well as mailboxes), supports IMAP, POP3 and SMTP
protocols (including over SSL) to operate with remote hosts, handles mime
types and different charsets. There are a lot of other useful features,
see mailx(1).

And as its ancient analogues, mailx can be used as a mail script language,
both for sending and receiving mail.

Besides the "mailx" command, this package provides "mail" and "Mail"
(which should be compatible with its predecessors from the mailx-8.x source),
as well as "nail" (the initial name of this project).


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
sed -i 's,/etc/nail.rc,%{mailrc},g' mailx.1


%build
%if %{use_nss}
INCLUDES="$INCLUDES `pkg-config --cflags-only-I nss`"
export INCLUDES
%endif

export LDFLAGS="%{build_ldflags}"

echo    PREFIX=%{_prefix} \
    BINDIR=%{_bindir} \
    MANDIR=%{_mandir} \
    SYSCONFDIR=%{_sysconfdir} \
    MAILRC=%{mailrc} \
    MAILSPOOL=%{_localstatedir}/mail \
    SENDMAIL=%{_sbindir}/sendmail \
    UCBINSTALL=install \
> makeflags

#  %{?_smp_mflags} cannot be used here
make `cat makeflags` \
    CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64" \
    IPv6=-DHAVE_IPv6_FUNCS


%install
make DESTDIR=$RPM_BUILD_ROOT STRIP=: `cat makeflags` install

# rename files for alternative usage
mv %{buildroot}%{_bindir}/mailx %{buildroot}%{_bindir}/mailx.%{name}
touch %{buildroot}%{_bindir}/{Mail,mail,mailx,nail}
mv %{buildroot}%{_mandir}/man1/mailx.1 %{buildroot}%{_mandir}/man1/mailx.%{name}.1
touch %{buildroot}%{_mandir}/man1/{Mail,mail,mailx,nail}.1


%pre
# remove alternativized files if they are not symlinks
for f in Mail mail mailx nail; do
    [ -L %{_bindir}/$f ] || rm -f %{_bindir}/$f >/dev/null 2>&1 || :
    [ -L %{_mandir}/man1/$f.1.gz ] || rm -f %{_mandir}/man1/$f.1.gz >/dev/null 2>&1 || :
done


%preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove mailx %{_bindir}/mailx.%{name} >/dev/null 2>&1 || :
fi


%post
# set up the alternatives files
%{_sbindir}/update-alternatives --install %{_bindir}/mailx mailx %{_bindir}/mailx.%{name} 200 \
    --slave %{_bindir}/Mail Mail %{_bindir}/mailx.%{name} \
    --slave %{_bindir}/mail mail %{_bindir}/mailx.%{name} \
    --slave %{_bindir}/nail nail %{_bindir}/mailx.%{name} \
    --slave %{_mandir}/man1/mailx.1.gz mailx.1.gz %{_mandir}/man1/mailx.%{name}.1.gz \
    --slave %{_mandir}/man1/Mail.1.gz Mail.1.gz %{_mandir}/man1/mailx.%{name}.1.gz \
    --slave %{_mandir}/man1/mail.1.gz mail.1.gz %{_mandir}/man1/mailx.%{name}.1.gz \
    --slave %{_mandir}/man1/nail.1.gz nail.1.gz %{_mandir}/man1/mailx.%{name}.1.gz \
    >/dev/null 2>&1 || :


%postun
if [ $1 -ge 1 ]; then
    if [ "$(readlink %{_sysconfdir}/alternatives/mailx)" == "%{_bindir}/mailx.%{name}" ]; then
        %{_sbindir}/update-alternatives --set mailx %{_bindir}/mailx.%{name} >/dev/null 2>&1 || :
    fi
fi


%triggerpostun -- mailx < 12
[[ -f %{mailrc}.rpmnew ]] && {
    # old config was changed. Merge both together.
    ( echo '# The settings above was inherited from the old mailx-8.x config'
      echo
      cat %{mailrc}.rpmnew
    ) >>%{mailrc}
} || :


%triggerpostun -- nail <= 12.3
[[ -f %{_sysconfdir}/nail.rc.rpmsave ]] && {
    # old config was changed...
    save=%{mailrc}.rpmnew
    [[ -f $save ]] && save=%{mailrc}.rpmsave

    mv -f %{mailrc} $save
    mv -f %{_sysconfdir}/nail.rc.rpmsave %{mailrc}
} || :


%files
%doc COPYING AUTHORS README
%config(noreplace) %{mailrc}
%ghost %{_bindir}/{Mail,mail,mailx,nail}
%{_bindir}/mailx.%{name}
%ghost %{_mandir}/man1/{Mail,mail,mailx,nail}.1*
%{_mandir}/man1/mailx.%{name}.1*


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Nikola Forró <nforro@redhat.com> - 12.5-40
- Handle missing SSLv3 support

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 12.5-39
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 16 2021 Nikola Forró <nforro@redhat.com> - 12.5-37
- Fix alternatives
  resolves: #1897928

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nikola Forró <nforro@redhat.com> - 12.5-34
- Set up alternatives

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 12.5-30
- Install executables to /usr/bin, not /bin
  https://fedoraproject.org/wiki/Features/UsrMove

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Nikola Forró <nforro@redhat.com> - 12.5-28
- switch to OpenSSL

* Tue Feb 20 2018 Nikola Forró <nforro@redhat.com> - 12.5-27
- add missing gcc build dependency

* Fri Feb  9 2018 Florian Weimer <fweimer@redhat.com> - 12.5-26
- Use LDFLAGS from redhat-rpm-config

* Wed Feb 07 2018 Nikola Forró <nforro@redhat.com> - 12.5-25
- fix also quoted-printable encoded words
  related: #1494559, #1515591

* Wed Nov 22 2017 Nikola Forró <nforro@redhat.com> - 12.5-24
- add missing linear whitespace to encsplit patch
  resolves: #1515591

* Fri Sep 22 2017 Nikola Forró <nforro@redhat.com> - 12.5-23
- fix multi-byte encoded line-folding
  resolves: #1494559

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 12.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Nikola Forró <nforro@redhat.com> - 12.5-18
- fix nss hostname matching
  resolves: #1296536

* Thu Jul 16 2015 Nikola Forró <nforro@redhat.com> - 12.5-17
- fix SIGSEGV crash in smtp_auth_var()
- add warning message for empty from
  resolves: #1113617

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 12.5-15
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Dec 17 2014 jchaloup <jchaloup@redhat.com> - 12.5-14
- Security fix for CVE-2004-2771, CVE-2014-7844
  resolves: #1174903

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Peter Schiffer <pschiffe@redhat.com> - 12.5-12
- added 2 clarifications to the mailx(1) man page

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Peter Schiffer <pschiffe@redhat.com> - 12.5-9
- related: #912785
  used -D_FILE_OFFSET_BITS=64 flag at the compile time
- return error code when TMPDIR is set to an invalid path while sending email
- added missing -v option to the usage message

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov  5 2012 Peter Schiffer <pschiffe@redhat.com> - 12.5-7
- cleaned .spec file
- resolves: #805410
  fixed SIGSEGV crash in which_protocol() function
- updated get-upstream-tarball.sh script and added it as additional source

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.5-4
- Fix decompress lzw issues (#731342)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.5-2
- rebuild for new krb5-libs

* Tue Oct 26 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.5-1
- update to 12.5
- drop patches applied upstream

* Fri Oct  1 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 12.4-7
- fix the typo in man-page

* Mon Dec 21 2009 Ivana Hutarova Varekova <varekova@redhat.com> - 12.4-6
- fix source tag

* Fri Dec 18 2009 Ivana Hutarova Varekova <varekova@redhat.com> - 12.4-5
- fix license tag

* Sat Dec 12 2009 Robert Scheck <robert@fedoraproject.org> - 12.4-4
- Make OpenSSL support working again if NSS flag is disabled

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.4-1
- update to 12.4

* Tue Jul 29 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.3-1
- Place mailx to /bin/mailx, to avoid extra symlink in redhat-lsb package
- /bin/mailx is now a base binary, another symlinked to it.

* Thu Jun 26 2008 Dmitry Butskoy <Dmitry@Butskoy.name>
- add missed BR for krb5-devel
- activate IPv6 support
- change config to /etc/mail.rc for compatibility
- add triggerpostun scriptlets against previous mailx and nail
  to check and merge (when possible) their user config changes
- use proper config filename in manuals
- use "less" instead of non-provided "pg" for nobsdcompat mode

* Wed Jun 18 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.3-0
- Change the name from "nail" to upstream's "mailx".
  Merge with the ordinary "mailx" cvs tree for Fedora 10.
  Now this stuff supersedes the old ancient mailx-8.x in Fedora.
- Build with nss instead of openssl, for "Security Consolidation" process.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 12.3-4
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 12.3-3
 - Rebuild for deps

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 12.3-2
- Rebuild for selinux ppc32 issue.

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to "BSD with advertising"

* Tue Jul 24 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.3-1
- update to 12.3

* Fri Jan 12 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.2-1
- update to 12.2
- spec file cleanups

* Fri Jun 16 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.1-1
- update to 12.1

* Wed Mar 22 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.0-2
- complete "mailx to nail" changes in the manual and config files
- drop _smp_mflags: it caused make to work incorrectly.

* Tue Mar 21 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 12.0-1
- upgrade to 12.0
- change new upstream name "mailx" to the old name "nail" to avoid
  conflicts with the Core mailx package.
- drop Source1, use package's html file instead.

* Mon Oct 17 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 11.25-4
- don't strip binaries on makeinstall (#170972)

* Mon Oct  3 2005 Dmitry Butskoy <Dmitry@Butskoy.name>
- clear buildroot before install (Michael Schwendt)

* Mon Sep 26 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 11.25-3
- more spec file cleanups
- accepted for Fedora Extra
  (review by Aurelien Bompard <gauret@free.fr>)

* Mon Aug 22 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 11.25-2
- spec file cleanups (#166343)

* Fri Aug 19 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 11.25-1
- initial release
- add "set bsdcompat" to nail.rc as default
- copy nail web page to doc

