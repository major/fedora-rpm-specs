Name:           fuse-sshfs
Version:        3.7.3
Release:        11%{?dist}
Summary:        FUSE-Filesystem to access remote filesystems via SSH
License:        GPL-2.0-only
URL:            https://github.com/libfuse/sshfs
Source0:        https://github.com/libfuse/sshfs/releases/download/sshfs-%{version}/sshfs-%{version}.tar.xz
Source1:        https://github.com/libfuse/sshfs/releases/download/sshfs-%{version}/sshfs-%{version}.tar.xz.asc
# Find which key was used for signing the release:
#
# $ LANG=C gpg --verify sshfs-3.7.3.tar.xz.asc sshfs-3.7.3.tar.xz
# gpg: Signature made Thu May 26 15:23:53 2022 CEST
# gpg:                using RSA key ED31791B2C5C1613AF388B8AD113FCAC3C4E599F
# gpg: Can't check signature: No public key
#
# Now export the key required as follows:
#
# gpg --no-default-keyring --keyring ./keyring.gpg --keyserver keyserver.ubuntu.com --recv-key ED31791B2C5C1613AF388B8AD113FCAC3C4E599F
# gpg --no-default-keyring --keyring ./keyring.gpg  --output ED31791B2C5C1613AF388B8AD113FCAC3C4E599F.gpg --export
Source2:	ED31791B2C5C1613AF388B8AD113FCAC3C4E599F.gpg

Patch1:         sshfs-0001-Refer-to-mount.fuse3-instead-of-mount.fuse.patch

Provides:       sshfs = %{version}-%{release}
Requires:       fuse3 >= 3.1.0
Requires:       openssh-clients
Recommends:     openssh-askpass

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  fuse3-devel >= 3.1.0
BuildRequires:  glib2-devel >= 2.0
BuildRequires:  openssh-clients
# for man page
BuildRequires:  python3-docutils
# for tests
BuildRequires:  fuse3
BuildRequires:  python3-pytest


%description
This is a FUSE-filesystem client based on the SSH File Transfer Protocol.
Since most SSH servers already support this protocol it is very easy to set
up: i.e. on the server side there's nothing to do.  On the client side
mounting the filesystem is as easy as logging into the server with ssh.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n sshfs-%{version}
# fix tests
sed -i "s/'fusermount'/'fusermount3'/g" test/util.py


%build
%meson
%meson_build


%install
%meson_install


%check
cd %{_vpath_builddir}
# FIXME requires sshd running? Previously tests were just skipped.
#python3 -m pytest test/


%files
%doc AUTHORS README.rst ChangeLog.rst
%license COPYING
%{_bindir}/sshfs
%{_sbindir}/mount.sshfs
%{_sbindir}/mount.fuse.sshfs
%{_mandir}/man1/sshfs.1.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 27 2024 Dusty Mabe <dusty@dustymabe.com> - 3.7.3-9
- Lower openssh-askpass dep to recommends

* Mon Mar 25 2024 Vasiliy Glazov <vascom2@gmail.com> - 3.7.3-8
- Add requires openssh-askpass

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Peter Lemenkov <lemenkov@gmail.com> - 3.7.3-5
- Check GPG signature

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Vasiliy Glazov <vascom2@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 09 2021 Vasiliy Glazov <vascom2@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Vasiliy Glazov <vascom2@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.7.0-3
- Refer to mount.fuse3 in man-page (rhbz#1808864)

* Tue Feb 25 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.7.0-2
- Fixed wrong sed invocation

* Mon Feb 17 2020 Peter Lemenkov <lemenkov@gmail.com> - 3.7.0-1
- Ver. 3.7.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.6.0-1
- Ver. 3.6.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.5.2-1
- Ver. 3.5.2

* Wed Feb 06 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.5.1-1
- Ver. 3.5.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Michael Cronenworth <mike@cchtml.com> - 3.4.0-1
- Ver. 3.4.0

* Wed Aug 15 2018 Michael Cronenworth <mike@cchtml.com> - 2.10-1
- Ver. 2.10 - last 2.x release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.8-1
- Ver. 2.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 14 2014 Peter Lemenkov <lemenkov@gmail.com> - 2.5-1
- Ver. 2.5
- Removed support for building on EPEL 5 (not sure if it was even possible there)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.4-5
- Build with PIE

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.4-1
- Ver. 2.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.3-1
- Ver. 2.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.2-6
- Fix building on EL-6

* Sun Sep 27 2009 Peter Lemenkov <lemenkov@gmail.com> 2.2-5
- No need for versioning in (Build)Requires for openssh-clients

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> 2.2-4
- Rebuilt with new fuse

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  9 2008 Peter Lemenkov <lemenkov@gmail.com> 2.2-1
- Ver. 2.2

* Sun Sep 28 2008 Peter Lemenkov <lemenkov@gmail.com> 2.1-1
- Ver. 2.1

* Mon May 19 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0-1
- Ver. 2.0

* Sat Feb  9 2008 Peter Lemenkov <lemenkov@gmail.com> 1.9-2
- Rebuild for GCC 4.3

* Wed Jan 23 2008 Peter Lemenkov <lemenkov@gmail.com> 1.9-2
- Added missing Requires and BuildRequires - openssh-clients >= 4.4

* Wed Jan 23 2008 Peter Lemenkov <lemenkov@gmail.com> 1.9-1
- Ver. 1.9
- Added provides: sshfs
- Modified License field according to Fedora policy.

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> 1.7-2
- Rebuild for FC6

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> 1.7-1
- New version
- Rebuild for FC6

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> - 1.6-2
- added missing sshnodelay.so

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> - 1.6-1
- Version 1.6

* Mon Feb 13 2006 Peter Lemenkov <lemenkov@newmail.ru> - 1.4-2
- small cosmetic fixes

* Mon Feb 13 2006 Peter Lemenkov <lemenkov@newmail.ru> - 1.4-1
- Version 1.4

* Wed Nov 23 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.2-3
- Use dist

* Fri Nov 04 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.2-2
- Update deps

* Fri Oct 28 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.2-1
- Initial RPM release.
