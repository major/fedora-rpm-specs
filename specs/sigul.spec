Summary: A signing server and related software client
Name: sigul

Version: 1.2
Release: 6%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only

URL: https://pagure.io/sigul/
Source0: https://pagure.io/sigul/archive/v%{version}/sigul-v%{version}.tar.gz
Source1: sigul_bridge.service
Source2: sigul_server.service
Source3: sigul.logrotate
# Upstream patch to avoid error with older python-cryptography in epel9
Patch0: https://github.com/sigul-project/sigul/commit/2b5cc2054417a3deaea8bc2c4fa7cbcad1a27dc7.patch
# Upstream patch to fix the constraints on the ca certs
Patch1: https://github.com/sigul-project/sigul/commit/ff4f3aa2cad9ce9699c44c9a78a82b09ab40e999.patch
# Always add AuthorityKeyIdentifier on certicates
Patch2: https://github.com/sigul-project/sigul/commit/23f65929474dce5ff060ec929ed9aa92174f644b.patch

BuildRequires: make
BuildRequires: nss-tools
BuildRequires: python3-pycodestyle
Requires: python3
Requires: python3-nss >= 0.11
BuildRequires: python3-nss, gnupg, koji, python3-pexpect, python3-gpg, python3, python3-fedora
BuildRequires: rpm-sign python3-urlgrabber git
BuildRequires: python3-sqlalchemy
BuildRequires: systemd-rpm-macros autoconf automake
BuildRequires: python3-cryptography

Requires: logrotate
Requires: koji
# For sigul_setup_client
Requires: coreutils nss-tools
Requires(pre): shadow-utils
BuildRequires:  gcc
# To detect the path correctly in configure
BuildRequires: gnupg
# To run the test suite
BuildRequires: systemd
BuildRequires: ostree
BuildRequires: ostree-devel
BuildRequires: skopeo

%if 0%{?rhel}
# There is no ostree package for RHEL other than x86_64, as that's in Atomic Host
ExclusiveArch: x86_64
%elif 0%{?fedora}
ExcludeArch: %{ix86}
%endif

%description
A signing server, which lets authorized users sign data without having any
access to the necessary private key, a client for the server, and a "bridge"
that connects the two.


%package server
Summary: Sigul server component
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnupg

Requires: python3-cryptography
Requires: python3-gpg
Requires: python3-pexpect
Requires: python3-sqlalchemy >= 0.5
Requires: python3-sqlalchemy

Requires: ostree
Requires: rpm-sign
# For systemd unit macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description server
The server part of sigul that keeps the keys and performs the actual signing.


%package bridge
Summary: Sigul bridge
Requires: %{name}%{?_isa} = %{version}-%{release}

Requires: python3-fedora
Requires: python3-urlgrabber

# For systemd unit macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description bridge
The bridge part of sigul that facilitates connection between the client and server.


%prep
%autosetup -p1 -n sigul-v%{version}

%build
autoreconf -i
%configure
make %{?_smp_mflags}

%check
exit 0
%if 0%{?fedora}
    if make check; then
        echo "Tests passed"
    else
        echo "Tests failed. Log output follows"
        cat testsuite.log
        cat testsuite.dir/*/{testsuite.log,bridge/sigul_bridge.log,server/sigul_server.log}
        exit 1
    fi
%endif

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install
mkdir -p $RPM_BUILD_ROOT%{_unitdir} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/sigul_bridge.service
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/sigul_server.service
install -m 0644 -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/sigul

%pre
getent group sigul >/dev/null || groupadd -r sigul
getent passwd sigul >/dev/null || \
useradd -r -g sigul -d %{_localstatedir}/lib/sigul -s /sbin/nologin \
        -c "Signing server or bridge" sigul
exit 0

%post bridge
%systemd_post sigul_bridge.service

%post server
%systemd_post sigul_server.service

%preun bridge
%systemd_preun sigul_bridge.service

%preun server
%systemd_preun sigul_server.service

%postun bridge
%systemd_postun_with_restart sigul_bridge.service

%postun server
%systemd_postun_with_restart sigul_server.service


%files
%doc AUTHORS COPYING NEWS README
%dir %{_sysconfdir}/sigul
%config(noreplace) %{_sysconfdir}/sigul/client.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/sigul
%{_bindir}/sigul
%{_bindir}/sigul_setup_client
%{_mandir}/man1/sigul*.1*
%{_mandir}/man8/sigul*.8*
%dir %{_datadir}/sigul
%{_datadir}/sigul/bind_methods.py*
%{_datadir}/sigul/client.py*
%{_datadir}/sigul/double_tls.py*
%{_datadir}/sigul/errors.py*
%{_datadir}/sigul/settings.py*
%{_datadir}/sigul/utils.py*
%{_datadir}/sigul/__pycache__/bind_methods.*
%{_datadir}/sigul/__pycache__/client.*
%{_datadir}/sigul/__pycache__/double_tls.*
%{_datadir}/sigul/__pycache__/errors.*
%{_datadir}/sigul/__pycache__/settings.*
%{_datadir}/sigul/__pycache__/utils.*

%files bridge
%config(noreplace) %attr(640,root,sigul) %{_sysconfdir}/sigul/bridge.conf
%{_unitdir}/sigul_bridge.service
%{_sbindir}/sigul_bridge
%{_datadir}/sigul/bridge*
%{_datadir}/sigul/__pycache__/bridge.*

%files server
%config(noreplace) %attr(640,root,sigul) %{_sysconfdir}/sigul/server.conf
%{_unitdir}/sigul_server.service
%{_bindir}/sigul-ostree-helper
%{_sbindir}/sigul_server
%{_sbindir}/sigul_server_add_admin
%{_sbindir}/sigul_server_create_db
%dir %attr(700,sigul,sigul) %{_localstatedir}/lib/sigul
%dir %attr(700,sigul,sigul) %{_localstatedir}/lib/sigul/gnupg
%{_datadir}/sigul/server*
%{_datadir}/sigul/__pycache__/server*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Nils Philippsen <nils@tiptoe.de> - 1.2-3
- Revert constraining SQLAlchemy version

* Thu Mar 21 2024 Nils Philippsen <nils@tiptoe.de> - 1.2-2
- Require SQLAlchemy < 2

* Tue Feb 27 2024 Kevin Fenzi <kevin@scrye.com> - 1.2-1
- Update to v1.2
- Fix ftbfs. rhbz#2226426
- Add patch to always set AuthorityKeyIdentifier
- Add patch for constraints on ca cert.
- Add patch for older python-cryptography in rhel9

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.1-1
- Rebase to v1.1

* Sat Dec 05 2020 Kevin Fenzi <kevin@scrye.com> - 1.0a1-5
- Drop no longer needed _python_bytecompile_extra

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0a1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0a1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.0a1-2
- Add server_gpg.py

* Tue Jun 09 2020 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.0a1-1
- Rebase to v1.0a1
- Added support for Python3 (and probably dropped Py3)
- Added support for GPGv2

* Mon Apr 06 2020 Mohan Boddu <mboddu@bhujji.com> - 0.207-10
- Fixing build failures

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.207-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.207-1
- Rebase to 0.207

* Wed May 03 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.206-2
- Koji was broken. Rebuild please

* Tue May 02 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.206-1
- Rebase to 0.206

* Wed Mar 01 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.205-1
- Rebase to upstream 0.205

* Tue Feb 21 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.204-3
- Add PIN reading fix

* Tue Feb 21 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.204-2
- rebuilt

* Mon Feb 20 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.204-1
- Rebase to upstream 0.204

* Mon Feb 13 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.203-1
- Rebase to 0.203

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.202-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.202-4
- Add patch for krb5 support

* Sat Oct 29 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.202-3
- Disable test suite for ppc64, since skopeo failed to build
- Enable test suite on Fedora instead of RHEL

* Wed Oct 19 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.202-2
- Do not run tests on el7

* Tue Oct 11 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.202-1
- Update to 0.202

* Tue Sep 20 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.201-2
- Rebuild with test suite on

* Fri Sep 16 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.201-1
- New upstream release

* Wed Sep 07 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.200-1
- New upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Miloslav Trmač <mitr@redhat.com> - 0.102-2
- Migrate to systemd unit files, based on a patch by Kevin Fenzi
  <kevin@scrye.com>.
  Resolves: #1301297

* Thu Nov 26 2015 Miloslav Trmač <mitr@redhat.com> - 0.102-1
- Update to sigul-0.102.
  Resolves: #1283364
  Related: #1272535

* Wed Nov 18 2015 Miloslav Trmač <mitr@redhat.com> - 0.101-1
- Update to sigul-0.101.
  Related: #1272535

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Miloslav Trmač <mitr@redhat.com> - 0.100-5
- Add Requires: rpm-sign
  Resolves: #1215678

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 17 2012 Miloslav Trmač <mitr@redhat.com> - 0.100-1
- Update to sigul-0.100.

* Wed Feb  8 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.99-3
- Remove the python-sqlite2 dep in Fedora as that package is being retired and
  sigul can use the sqlite3  module from the python stdlib

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun  6 2011 Miloslav Trmač <mitr@redhat.com> - 0.99-1
- Update to sigul-0.99.

* Thu Jun  2 2011 Miloslav Trmač <mitr@redhat.com> - 0.98-2
- Add Requires: gnupg
  Resolves: #664536

* Tue May 31 2011 Miloslav Trmač <mitr@redhat.com> - 0.98-1
- Update to sigul-0.98.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com>
- recompiling .py files against Python 2.7 (rhbz#623359)

- Drop no longer necessary references to BuildRoot:

* Fri Jul 31 2009 Miloslav Trmač <mitr@redhat.com> - 0.97-1
- Update to sigul-0.97.
- Ship NEWS.

* Tue Jul 28 2009 Jesse Keating <jkeating@redhat.com> - 0.96-6
- Fix the patch in -4

* Tue Jul 28 2009 Jesse Keating <jkeating@redhat.com> - 0.96-5
- Add a dist tag

* Tue Jul 28 2009 Jesse Keating <jkeating@redhat.com> - 0.96-4
- Add another patch to temporarily work around a stale koji issue.
- Bump python-nss reqs up now that we have a newer one in EPEL

* Mon Jul 27 2009 Jesse Keating <jkeating@redhat.com> - 0.96-3
- Setup the Requires right for EL5

* Mon Jul 27 2009 Jesse Keating <jkeating@redhat.com> - 0.96-2
- Fix various bugs while testing (release by Mitr)
- Patch from jkeating for srpm signing.

* Sat Jul 18 2009 Miloslav Trmač <mitr@redhat.com> - 0.95-0.mitr.1
- Update to 0.95.
- Add missing Requires: m2crypto.

* Wed Jul  1 2009 Miloslav Trmač <mitr@redhat.com> - 0.94-0.mitr.1
- Update to 0.94.

* Fri Apr 10 2009 Miloslav Trmač <mitr@redhat.com> - 0.93-0.mitr.1
- Update to 0.93.

* Wed Jan 28 2009 Miloslav Trmač <mitr@redhat.com> - 0.92-0.mitr.1
- Update to 0.92.

* Mon Jan 12 2009 Miloslav Trmač <mitr@redhat.com> - 0.91-0.mitr.1
- Update to 0.91.

* Sun Jan 11 2009 Miloslav Trmač <mitr@redhat.com> - 0.90-0.mitr.2
- Requires: koji, python-sqlite2

* Sun Jan 11 2009 Miloslav Trmač <mitr@redhat.com> - 0.90-0.mitr.1
- s/rpmsigner/sigul/g

* Sun Nov 30 2008 Miloslav Trmač <mitr@redhat.com> - 0.90-0.mitr.1
- Initial package.
