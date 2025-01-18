%global perl_vendorlib %(eval $(perl -V:vendorlib); echo $vendorlib)
# RHEL uses %%{_prefix}/com for %%{_sharedstatedir} instead of /var/lib
%if 0%{?rhel}
%global gitolite_homedir /var/lib/%{name}
%else
%global gitolite_homedir %{_sharedstatedir}/%{name}
%endif

Name:           gitolite3
Epoch:          1
Version:        3.6.13
Release:        6%{?dist}
Summary:        Highly flexible server for git directory version tracker

License:        GPL-2.0-only AND CC-BY-SA-1.0
URL:            http://github.com/sitaramc/gitolite
Source0:        https://github.com/sitaramc/gitolite/archive/v%{version}.tar.gz
Source1:        gitolite3-README-fedora
# Upstream: https://github.com/sitaramc/gitolite/commit/c656af01b73a5cc4f80512
Source2:        compile-1


BuildArch:      noarch
BuildRequires:      perl-generators
Provides:       perl(%{name}) = %{version}-%{release}
Requires:       git
Requires:       openssh-clients
Requires(pre):  shadow-utils
Recommends:       subversion

%description
Gitolite allows a server to host many git repositories and provide access
to many developers, without having to give them real userids on the server.
The essential magic in doing this is ssh's pubkey access and the authorized
keys file, and the inspiration was an older program called gitosis.

Gitolite can restrict who can read from (clone/fetch) or write to (push) a
repository. It can also restrict who can push to what branch or tag, which
is very important in a corporate environment. Gitolite can be installed
without requiring root permissions, and with no additional software than git
itself and perl. It also has several other neat features described below and
elsewhere in the doc/ directory.


%prep
%setup -qn gitolite-%{version}
cp %{SOURCE1} .


%build
#This page intentionally left blank.

%install
rm -rf $RPM_BUILD_ROOT

# Directory structure
install -d $RPM_BUILD_ROOT%{gitolite_homedir}
install -d $RPM_BUILD_ROOT%{gitolite_homedir}/.ssh
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

# Code
cp -pr src/lib/Gitolite $RPM_BUILD_ROOT%{perl_vendorlib}
echo "%{version}-%{release}" >src/VERSION
cp -a src/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/commands/
ln -s %{_datadir}/%{name}/gitolite $RPM_BUILD_ROOT%{_bindir}/gitolite

# empty authorized_keys file
touch $RPM_BUILD_ROOT%{gitolite_homedir}/.ssh/authorized_keys


%pre
# Add "gitolite" user per https://fedoraproject.org/wiki/Packaging:UsersAndGroups
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{gitolite_homedir} -s /bin/sh \
        -c "git repository hosting" %{name}
exit 0


%files
%{_bindir}/*
%{perl_vendorlib}/*
%{_datadir}/%{name}
# make homedir non world readable
%attr(750,%{name},%{name}) %dir %{gitolite_homedir}
%attr(750,%{name},%{name}) %dir %{gitolite_homedir}/.ssh
%config(noreplace) %attr(640,%{name},%{name}) %{gitolite_homedir}/.ssh/authorized_keys
%doc gitolite3-README-fedora COPYING README.markdown CHANGELOG


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:3.6.13-1
- 3.6.13

* Wed May 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:3.6.12-10
- Loosened subversion dependency.

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:3.6.12-9
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.12-6
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.12-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:3.6.12-1
- 3.6.12

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.11-7
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.11-6
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.11-3
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Gwyn Ciesla <limburgher@gmail.com> - 1:3.6.11-1
- 3.6.11.

* Thu Oct 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:3.6.10-1
- 3.6.10.

* Tue Sep 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:3.6.9-1
- Latest upstream.

* Tue Jul 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:3.6.8-1
- Latest upstream.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.7-6
- Perl 5.28 rebuild

* Tue Apr 24 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1:3.6.7-5
- Back upstream patch making gitolite respect the ALLOW_ORPHAN_GL_CONF
  configuration variabe
- Include the compile-1 command upstream brought in Fedora in:
  https://github.com/sitaramc/gitolite/commit/afb8afa14a892895dc48664c6526351cb

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 1:3.6.7-3
- Backport upstream patch for dist-git
  Upstream: https://github.com/sitaramc/gitolite/commit/41b7885b77cfe992ad3c96d0b021ece51ce1b3e3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:3.6.7-1
- Latest upstream.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.6-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 09 2016 Jon Ciesla <limburgher@gmail.com> - 1:3.6.6-1
- Latest upstream.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.5-3
- Perl 5.24 rebuild

* Mon Feb 22 2016 Jon Ciesla <limburgher@gmail.com> - 1:3.6.5-1
- Latest upstream.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Jon Ciesla <limburgher@gmail.com> - 1:3.6.4-1
- Latest upstream.

* Thu Oct 8 2015 François Cami <fcami@fedoraproject.org> - 1:3.6.3-4
- Fix instructions in README.fedora:
-  gitolite user => gitolite3 user
-  switch setup from -a to -pk (ssh keys) 

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.3-2
- Perl 5.22 rebuild

* Sun Apr 26 2015 Jon Ciesla <limburgher@gmail.com> - 1:3.6.3-1
- Latest upstream.

* Mon Nov 10 2014 Jon Ciesla <limburgher@gmail.com> - 1:3.6.2-1
- Latest upstream.

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.6.1-2
- Perl 5.20 rebuild

* Mon Jun 23 2014 Jon Ciesla <limburgher@gmail.com> - 1:3.6.1-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Jon Ciesla <limburgher@gmail.com> - 1:3.6-1
- Latest upstream.

* Wed Oct 23 2013 Jon Ciesla <limburgher@gmail.com> - 1:3.5.3.1-1
- Latest upstream.

* Wed Oct 16 2013 Jon Ciesla <limburgher@gmail.com> - 1:3.5.3-1
- Latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:3.5.2-2
- Perl 5.18 rebuild

* Wed Jul 10 2013 Jon Ciesla <limburgher@gmail.com> - 1:3.5.2-1
- Latest upstream.

* Thu Mar 28 2013 Jon Ciesla <limburgher@gmail.com> - 1:3.5.1-1
- Latest upstream.

* Mon Mar 25 2013 Jon Ciesla <limburgher@gmail.com> - 1:3.5-1
- Latest upstream.

* Tue Mar 05 2013 Jon Ciesla <limburgher@gmail.com> - 1:3.4-1
- Latest upstream.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 03 2013 Jon Ciesla <limburgher@gmail.com> - 1:3.3-1
- Latest upstream.

* Mon Nov 19 2012 Jon Ciesla <limburgher@gmail.com> - 1:3.2-1
- Latest upstream.

* Wed Oct 10 2012 Jon Ciesla <limburgher@gmail.com> - 1:3.1-1
- 3.1, rewuiring Epoch bump.

* Tue Oct 09 2012 Jon Ciesla <limburgher@gmail.com> - 3.04-4
- Patch for directory traversal bug.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 3.04-2
- Perl 5.16 rebuild

* Wed Jun 27 2012 Jon Ciesla <limburgher@gmail.com> - 3.04-1
- Latest upstream, docs now includable.

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 3.03-3
- Perl 5.16 rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 3.03-2
- Perl 5.16 rebuild

* Wed May 23 2012 Jon Ciesla <limburgher@gmail.com> - 3.03-1
- Latest upstream.

* Mon May 21 2012 Jon Ciesla <limburgher@gmail.com> - 3.02-1
- Latest upstream.

* Tue May 15 2012 Jon Ciesla <limburgher@gmail.com> - 3.01-2
- Added license file, fixed duplicate files, dropped defattr.
- Dropped clean and buildroot.
- Added script to generate tarball in comments.

* Thu May 03 2012 Jon Ciesla <limburgher@gmail.com> - 3.01-1
- Initial packaging based on gitolite 2.3-2.
