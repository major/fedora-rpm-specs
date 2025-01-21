%global appdefaultsdir /usr/share/X11/app-defaults

Name:               x11-ssh-askpass
Version:            1.2.4.1
Release:            42%{?dist}
Summary:            A passphrase dialog for X and not only for OpenSSH
License:            LicenseRef-Fedora-Public-Domain

# The original site has disappeared, but the source itself has
# reappeared on github.  The original site was:
#
# http://www.jmknoble.net/software/x11-ssh-askpass/
#
# We will use the github mirror of the original source from now on.
%global forgeurl    https://github.com/sigmavirus24/x11-ssh-askpass/
%global tag         %{version}
%global archivename %{name}-%{tag}
%global archiveext  tar.gz
%global archiveurl  %{forgeurl}/archive/refs/tags/%{tag}.%{archiveext}
%forgemeta

URL:                %{forgeurl}
Source0:            %{forgesource}
Source1:            x11-ssh-askpass.csh
Source2:            x11-ssh-askpass.sh
Patch0:             x11-ssh-askpass-1.2.4-random.patch
Patch1:             x11-ssh-askpass-1.2.4.1-gcc-14.x-warnings.patch

Provides:           openssh-askpass-x11

BuildRequires:      make
BuildRequires:      gcc
BuildRequires:      imake
BuildRequires:      libXt-devel
BuildRequires:      coreutils
BuildRequires:      sed

%description
x11-ssh-askpass is a lightweight passphrase dialog for OpenSSH or
other open variants of SSH. In particular, x11-ssh-askpass is useful
with the Unix port of OpenSSH by Damien Miller and others, and Damien
includes it in his RPM packages of OpenSSH.

x11-ssh-askpass uses only the stock X11 libraries (libX11, libXt) for
its user interface. This reduces its dependencies on external libraries
(such as GNOME or Perl/Tk). See the README for further information.

%prep
%forgeautosetup

%build
env LDFLAGS='-Wl,--as-needed' %configure --libexecdir=%{_libexecdir}/openssh --with-app-defaults-dir=%{appdefaultsdir}
xmkmf
# Modernize the features.h macros
sed -i -e 's|-D_XOPEN_SOURCE||g' Makefile
sed -i -e 's|-D_BSD_SOURCE|-D_DEFAULT_SOURCE|g' Makefile
make includes
%make_build

%install
%make_install install.man DESTDIR=%{buildroot}

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/%(basename %{SOURCE1})
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/%(basename %{SOURCE2})

rm -f %{buildroot}%{_libexecdir}/openssh/ssh-askpass
rm -f %{buildroot}%{_mandir}/man1/ssh-askpass.1x*

%files
%doc ChangeLog README TODO *.ad
%config(noreplace) %{_sysconfdir}/profile.d/x11-ssh-askpass.csh
%config(noreplace) %{_sysconfdir}/profile.d/x11-ssh-askpass.sh
%{appdefaultsdir}/SshAskpass
%dir %{_libexecdir}/openssh
%{_libexecdir}/openssh/x11-ssh-askpass
%{_mandir}/man1/x11-ssh-askpass.1x.gz

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 03 2024 David Cantrell <dcantrell@redhat.com> - 1.2.4.1-40
- Modernize the spec file with newer macros
- Pull source from github using forge macros since the original site
  has disappeared
- Patched for latest glibc and gcc to handle warnings
- Use SPDX license expression for the License tag

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 David Cantrell <dcantrell@redhat.com> - 1.2.4.1-34
- Reformatting of the spec file and rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.2.4.1-29
- install profile scriptlets as non-executable to avoid explicit csh/sh dep

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.2.4.1-27
- Remove obsolete requirements for %%postun/%%pre scriptlets

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.2.4.1-25
- Rebuild with fixed binutils

* Fri Jul 27 2018 David Cantrell <dcantrell@redhat.com> - 1.2.4.1-24
- Make nothing but cosmetic changes to the spec file and other source
  files to appease the build system and fix what I suspect is a bogus
  FTBFS (#1606816)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.2.4.1-22
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 09 2009 Adam Jackson <ajax@redhat.com> 1.2.4.1-8
- Requires: libXt for pre and postun, not the file path, since libXt will
  always provide it.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 30 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-6
- use lower-cased name for profile files and simplified them

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4.1-4
- Autorebuild for GCC 4.3

* Sun Feb  4 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-3
- rebuilt with -Wl,--as-needed

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-2
- rebuilt

* Tue Jul 25 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-1
- initial Fedora Extras package (review #176580)

* Sat May 20 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-0.2
- removed '%%config' from the app-defaultsdir
- do not own the app-defaultsdir anymore
- added some tricks to the -random patch to avoid removal of the
  clear-the-passphrase-memset() during optimization

* Sun Mar 26 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-0.1
- fixed path of app-defaults dir

* Wed Dec 21 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-0
- initial build
