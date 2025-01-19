Name:           pbuilder
Version:        0.231.1
Release:        4%{?dist}
Summary:        Personal package builder for Debian packages

License:        GPL-2.0-or-later
URL:            http://packages.debian.org/unstable/admin/%{name}
Source0:        http://ftp.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}.tar.xz
Source1:        README.fedora
Source2:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-config
Source3:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-debian-stable
Source4:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-ubuntu-old
Source5:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-ubuntu-old2
Source6:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilder-ubuntu-stable
Source7:        https://bitbucket.org/amidevous/fedora-rpm/raw/master/pbuilder/debian/pbuilderrc
# Don't hardcode pbuilder user id, add a ccache section
Patch0:         pbuilder_pbuilderrc.patch
# Don't build HTML docs since it requires TLDP stylesheets which are not packaged for Fedora
Patch1:         pbuilder_no-html-docs.patch

BuildArch:      noarch

BuildRequires:  dblatex
BuildRequires:  dpkg-dev
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  python3
BuildRequires:  tex(fancybox.sty)
BuildRequires:  tex(pdflscape.sty)

#From https://salsa.debian.org/pbuilder-team/pbuilder/-/blob/master/debian/control
#Depends:
# debootstrap (>= 1.0.97) | cdebootstrap,
# dpkg-dev (>= 1.17.0),
# mount,
# ${misc:Depends},
#Recommends:
# devscripts,
# eatmydata,
# fakeroot,
# net-tools | iproute2,
# sudo,

Requires:       debootstrap
Requires:       dpkg-dev
Requires:       util-linux-core
Recommends:     devscripts
Recommends:     fakeroot
Recommends:     iproute
Recommends:     sudo
Requires:       gcc
Requires:       gnupg
Requires:       debconf
Requires:       debhelper
Requires:       wget
Requires:       debian-keyring
Requires:       ubu-keyring

%description
pbuilder constructs a chroot system, and builds a package inside the chroot.
It is an ideal system to use to check that a package has correct build-
dependencies.


%prep
%autosetup -p1

# Adjust ccache path
sed -i 's|/usr/lib/ccache|%{_libdir}/ccache|g' pbuilderrc


%build
%make_build


%install
%make_install

# Man pages
install -Dpm 0644 debuild-pbuilder.1 %{buildroot}%{_mandir}/man1/debuild-pbuilder.1
install -Dpm 0644 pdebuild.1 %{buildroot}%{_mandir}/man1/pdebuild.1
install -Dpm 0644 pbuilderrc.5 %{buildroot}%{_mandir}/man5/pbuilderrc.5
install -Dpm 0644 pbuilder.8 %{buildroot}%{_mandir}/man8/pbuilder.8

# Install directories
install -d %{buildroot}%{_localstatedir}/cache/%{name}
install -d %{buildroot}%{_localstatedir}/cache/%{name}/build
install -d %{buildroot}%{_localstatedir}/cache/%{name}/ccache
install -Dpm 0777 %{SOURCE2} %{buildroot}%{_bindir}/pbuilder-config
install -Dpm 0777 %{SOURCE3} %{buildroot}%{_bindir}/debian-stable
install -Dpm 0777 %{SOURCE4} %{buildroot}%{_bindir}/pbuilder-ubuntu-old
install -Dpm 0777 %{SOURCE5} %{buildroot}%{_bindir}/pbuilder-ubuntu-old2
install -Dpm 0777 %{SOURCE6} %{buildroot}%{_bindir}/pbuilder-ubuntu-stable

# Configuration file
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/pbuilderrc

# Copy README.fedora to root
cp -a %{SOURCE1} README.fedora


%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || \
  useradd -r -g %{name} -d %{_localstatedir}/run/%{name} -s /sbin/nologin \
    -c "%{name}" %{name}
exit 0


%check
%ifarch %arm
# Some tests fail on arm because ubuntu mirrors are unavailable for that arch
make check || :
%else
make check
%endif


%files
%doc README AUTHORS THANKS debian/TODO README.fedora
%config(noreplace) %{_sysconfdir}/pbuilderrc
%config(noreplace) %{_sysconfdir}/pbuilder/
%{_bindir}/debuild-pbuilder
%{_bindir}/pdebuild
%{_bindir}/pbuilder-config
%{_bindir}/debian-stable
%{_bindir}/pbuilder-ubuntu-old
%{_bindir}/pbuilder-ubuntu-old2
%{_bindir}/pbuilder-ubuntu-stable
%{_sbindir}/pbuilder
%{_prefix}/lib/pbuilder/
%{_datadir}/bash-completion/
%{_datadir}/pbuilder/
%{_mandir}/man1/debuild-pbuilder.1*
%{_mandir}/man1/pdebuild.1*
%{_mandir}/man5/pbuilderrc.5*
%{_mandir}/man8/pbuilder.8*
%{_docdir}/pbuilder/*
# The ccache folder needs to be owned by the pbuilder user
%attr(0755,%{name},root) %{_localstatedir}/cache/%{name}/ccache


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.231.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Sérgio Basto <sergio@serjux.com> - 0.231.1-3
- Requires util-linux-core instead mount, which doesn't exist as package on
  Fedora

* Sat Sep 21 2024 Sérgio Basto <sergio@serjux.com> - 0.231.1-2
- Update requires and recommends following upstream
- devscripts is not available on EPEL (yet)

* Sat Sep 07 2024 Sérgio Basto <sergio@serjux.com> - 0.231.1-1
- Update pbuilder to 0.231.1 (#2310546)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Sérgio Basto <sergio@serjux.com> - 0.231-11
- Fix build for epel9

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.231-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Sandro Mani <manisandro@gmail.com> - 0.231-1
- Update to 0.231

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.230.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Petr Viktorin <pviktori@redhat.com> - 0.230.4-4
- Switch BuildRequires to python3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.230.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.230.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 0.230.4-1
- Updateto 0.230.4

* Tue Mar 26 2019 Sandro Mani <manisandro@gmail.com> - 0.230.3-1
- Update to 0.230.3

* Fri Mar 01 2019 Sandro Mani <manisandro@gmail.com> - 0.230.2-1
- Update to 0.230.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.230.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Sandro Mani <manisandro@gmail.com> - 0.230.1-1
- Update to 0.230.1

* Sat Nov 10 2018 Sandro Mani <manisandro@gmail.com> - 0.230-1
- Update to 0.230

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.229.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Sandro Mani <manisandro@gmail.com> - 0.229.3-1
- Update to 0.229.3

* Thu Apr 05 2018 Sandro Mani <manisandro@gmail.com> - 0.229.2-1
- Update to 0.229.2

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.229.1-3
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.229.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Sandro Mani <manisandro@gmail.com> - 0.229.1-1
- Update to 0.229.1

* Mon Oct 30 2017 Sandro Mani <manisandro@gmail.com> - 0.229-1
- Update to 0.229

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 0.228.9-1
- Update to 0.228.9

* Sat Aug 26 2017 Sandro Mani <manisandro@gmail.com> - 0.228.8-1
- Update to 0.228.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.228.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Sandro Mani <manisandro@gmail.com> - 0.228.7-1
- Update to 0.228.7

* Mon Mar 13 2017 Sandro Mani <manisandro@gmail.com> - 0.228.6-1
- Update to 0.228.6

* Sat Mar 04 2017 Sandro Mani <manisandro@gmail.com> - 0.228.5-1
- Update to 0.228.5

* Tue Feb 07 2017 Sandro Mani <manisandro@gmail.com> - 0.228.4-1
- Update to 0.228.4

* Tue Feb 07 2017 Sérgio Basto <sergio@serjux.com> - 0.228.3-2
- Fix epel7 build

* Wed Jan 25 2017 Sandro Mani <manisandro@gmail.com> - 0.228.3-1
- Update to 0.228.3

* Tue Jan 24 2017 Sandro Mani <manisandro@gmail.com> - 0.228.2-1
- Update to 0.228.2

* Sun Jan 22 2017 Sandro Mani <manisandro@gmail.com> - 0.228.1-1
- Update to 0.228.1

* Mon Jan 16 2017 Sandro Mani <manisandro@gmail.com> - 0.228-1
- Update to 0.228

* Tue Nov 29 2016 Sandro Mani <manisandro@gmail.com> - 0.227-1
- Update to 0.227

* Thu Sep 15 2016 Sandro Mani <manisandro@gmail.com> - 0.226.1-1
- Update to 0.226.1

* Mon Sep 05 2016 Sandro Mani <manisandro@gmail.com> - 0.226-1
- Update to 0.226

* Thu Jul 21 2016 Sandro Mani <manisandro@gmail.com> - 0.225.2-1
- Update to 0.225.2

* Wed Jul 20 2016 Sandro Mani <manisandro@gmail.com> - 0.225.1-2
- Backport upstream patch: Don't trash CHROOTEXEC when using eatmydata (#1358337)
- Modernize spec

* Tue Jun 28 2016 Sandro Mani <manisandro@gmail.com> - 0.225.1-1
- Update to 0.225.1

* Mon Jun 13 2016 Sandro Mani <manisandro@gmail.com> - 0.225-1
- Update to 0.225

* Sat Apr 30 2016 Sandro Mani <manisandro@gmail.com> - 0.224-1
- Update to 0.224

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.223-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Sandro Mani <manisandro@gmail.com> - 0.223-1
- Update to 0.223

* Thu Jan 14 2016 Sandro Mani <manisandro@gmail.com> - 0.222-1
- Update to 0.222

* Wed Dec 09 2015 Sandro Mani <manisandro@gmail.com> - 0.221.3-1
- Update to 0.221.3

* Wed Dec 09 2015 Sandro Mani <manisandro@gmail.com> - 0.221.2-1
- Update to 0.221.2

* Thu Nov 26 2015 Sandro Mani <manisandro@gmail.com> - 0.221.1-1
- Update to 0.221.1

* Wed Nov 25 2015 Sandro Mani <manisandro@gmail.com> - 0.221-1
- Update to 0.221

* Tue Nov 24 2015 Sandro Mani <manisandro@gmail.com> - 0.220-1
- Update to 0.220

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.215-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 13 2014 Sandro Mani <manisandro@gmail.com> - 0.215-13
- Skip mounting /selinux in chroots

* Sun Dec 07 2014 Sandro Mani <manisandro@gmail.com> - 0.215-12
- Fix pbuilder_selinux-ro.patch

* Sun Dec 07 2014 Sandro Mani <manisandro@gmail.com> - 0.215-11
- Fix pbuilder_selinux-ro.patch

* Sat Dec 06 2014 Sandro Mani <manisandro@gmail.com> - 0.215-10
- Add patch to mount /selinux read-only (see debian bug #734193), fixed failure
  to create trusty, utopic base images
- README.fedora additions

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.215-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Sandro Mani <manisandro@gmail.com> - 0.215-8
- Improve README.fedora, thanks Till Maas, see rhbz#1068727

* Tue Oct 29 2013 Sandro Mani <manisandro@gmail.com> - 0.215-7
- Drop pbuilder_pdebuild-bindmounts.patch (one should use pdebuild -- --bindmounts <dir> instead)
- Fix README.fedora: ubuntu-keyring is called ubu-keyring

* Fri Oct 18 2013 Sandro Mani <manisandro@gmail.com> - 0.215-6
- Add patch to make it possible to pass --bindmounts to pdebuild

* Mon Oct 14 2013 Sandro Mani <manisandro@gmail.com> - 0.215-5
- Package is noarch
- Co-own %%{_sysconfdir}/bash_completion.d/

* Thu Oct 10 2013 Sandro Mani <manisandro@gmail.com> - 0.215-4
- Improve README.fedora
- Add some missing requires

* Tue Oct 08 2013 Sandro Mani <manisandro@gmail.com> - 0.215-3
- Don't test non-existing ubuntu arm mirrors

* Thu Sep 19 2013 Sandro Mani <manisandro@gmail.com> - 0.215-2
- Create build and ccache directories in /var/cache/pbuilder
- Don't use hardcoded user id
- Prepare pbuilderrc for ccache usage

* Thu Sep 19 2013 Sandro Mani <manisandro@gmail.com> - 0.215-1
- Initial package
