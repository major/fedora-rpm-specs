%global commit0 c48532692f8c5a412da891b3d43bd46a24cd179e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       rbm
Version:    0.4^20220725git%{shortcommit0}
Release:    1%{?dist}
Summary:    Reproducible Build Manager
License:    CC0-1.0
# A bug tracker is at <https://gitlab.torproject.org/tpo/applications/rbm/>.
URL:        https://rbm.torproject.org/
# Latest 0.4 release is very old, use a git snapshot,
# <https://github.com/boklm/rbm/issues/2>.
# Upstream git repository is <https://git.torproject.org/builders/rbm.git>.
Source0:    %{name}-%{shortcommit0}.tar.gz
# Install container script, proposed to an upstream,
# <https://github.com/boklm/rbm/pull/8>.
Patch0:     rbm-c485326-Install-container-script-as-rmbcontainer.patch
BuildArch:  noarch
BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# No tests are executed, run-time depdencies are not needed at build time.
# bash for /bin/sh defined in default configuration
Requires:       bash
Requires:       bzip2
# coreutils for chown, mktemp, rm, uname
Requires:       coreutils
# debuild not yet packaged
# dnf in default configuration,
Requires:       dnf
Requires:       git-core
# gnupg for gpg defined in default configuration
Requires:       gnupg
Requires:       gzip
# hostname for hostname in container tool
Requires:       hostname
Requires:       man-db
Requires:       mercurial
Requires:       perl(Exporter)
# redhat-lsb-core for lsb_release
Requires:       redhat-lsb-core
# rpm in default configuration
Requires:       rpm
# rpm-build for rpmbuild defined in default configuration
Requires:       rpm-build
# shadow-utils for newuidmap, newgidmap in container tool
Requires:       shadow-utils
# sudo in default configuration
Requires:       sudo
# tar in default configuration
Requires:       tar
# util-linux-core for mount in container tool
Requires:       util-linux-core
# wget in default configuration
Requires:       wget
Requires:       xz

%description
Reproducible Build Manager (rbm) is a tool that helps you create and build
packages for multiple Linux distributions, and automate the parts that can be
automated. It includes options to run the build in a defined environment to
allow reproducing the build.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
%{make_build} sysconfigdir=%{_sysconfdir} bindir=%{_bindir} mandir=%{_mandir} \
    perldir=%{perl_vendorlib}

%install
%{make_install} sysconfigdir=%{_sysconfdir} bindir=%{_bindir} mandir=%{_mandir} \
    perldir=%{perl_vendorlib}

%files
%license COPYING
%doc NEWS README.md TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
* Mon Jul 25 2022 Petr Pisar <ppisar@redhat.com> - 0.4^20220725gitc485326-1
- A rebase to a git snapshot taken on 2022-07-25

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24.20190910gite04f03f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.4-23.20190910gite04f03f
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22.20190910gite04f03f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21.20190910gite04f03f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.4-20.20190910gite04f03f
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19.20190910gite04f03f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18.20190910gite04f03f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.4-17.20190910gite04f03f
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.4-16.20190910gite04f03f
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15.20190910gite04f03f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Petr Pisar <ppisar@redhat.com> - 0.4-14.20190910gite04f03f
- Upgraded to a git snapshot from 2019-09-10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13.20151206gitd50b2a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.4-12.20151206gitd50b2a6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11.20151206gitd50b2a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10.20151206gitd50b2a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.4-9.20151206gitd50b2a6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8.20151206gitd50b2a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7.20151206gitd50b2a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.4-6.20151206gitd50b2a6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5.20151206gitd50b2a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Petr Pisar <ppisar@redhat.com> - 0.4-4.20151206gitd50b2a6
- Create a home directory for default user in a Docker container
- Fix error reporting while parsing LSB release string
- Do not create hg directory (upstream bug #4)
- Use dnf instead of yum (upstream bug #3)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.4-3.20151206gitd50b2a6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2.20151206gitd50b2a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Petr Pisar <ppisar@redhat.com> - 0.4-1.20151206gitd50b2a6
- Git snapshot on 2015-12-06 packaged
- Correct typos
