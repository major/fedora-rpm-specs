# https://github.com/restic/restic
%global goipath         github.com/restic/restic
Version:                0.12.1

%gometa

%global common_description %{expand:
A backup program that is easy, fast, verifiable, secure, efficient and free.

Backup destinations can be:
*Local
*SFTP
*REST Server
*Amazon S3
*Minio Server
*OpenStack Swift
*Backblaze B2
*Microsoft Azure Blob Storage
*Google Cloud Storage
*Other Services via rclone}

%global golicenses    LICENSE


Name:    restic
Release: 5%{?dist}
Summary: Fast, secure, efficient backup program
URL:     %{gourl}
License: BSD
Source0: %{gosource}
#Patch0: 0001-Fix-running-tests-on-a-SELinux-enabled-system.patch
#Patch1: backport-2652.patch
#Move internal/fs.TestChdir to internal/test.Chdir
#Patch1:  0001-Move-internal-fs.TestChdir-to-internal-test.Chdir.patch
Patch0:  f1cfb97.patch

#Restic does not compile for the following archs
ExcludeArch: s390x

BuildRequires: golang(bazil.org/fuse)
BuildRequires: golang(bazil.org/fuse/fs)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/storage)
BuildRequires: golang(github.com/cenkalti/backoff)
BuildRequires: golang(github.com/elithrar/simple-scrypt)
BuildRequires: golang(github.com/juju/ratelimit)
BuildRequires: golang(github.com/kurin/blazer/b2)
BuildRequires: golang(github.com/mattn/go-isatty)
BuildRequires: golang(github.com/ncw/swift)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/pkg/sftp)
BuildRequires: golang(github.com/pkg/xattr)
BuildRequires: golang(github.com/restic/chunker)
BuildRequires: golang(github.com/hashicorp/golang-lru/simplelru)
BuildRequires: golang(golang.org/x/crypto/poly1305)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sync/errgroup)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/text/encoding/unicode)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/storage/v1)
BuildRequires: golang(gopkg.in/tomb.v2)
#Updated for 0.12.0
BuildRequires: golang(github.com/minio/minio-go/v7)
BuildRequires: golang(github.com/minio/minio-go/v7/pkg/credentials)
BuildRequires: golang(cloud.google.com/go/storage)
#Added for 0.10.0
BuildRequires: golang(github.com/cespare/xxhash)
BuildRequires: golang(github.com/dchest/siphash)
#for check/testing
BuildRequires: golang(github.com/google/go-cmp/cmp)
#Soft dependency for mounting , ie: fusemount
#Requires: fuse


%description
%{common_description}

#%%gopkg

%prep
%goprep
%patch0 -p1

%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/restic


%install
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
install -p -m 644 doc/man/* %{buildroot}%{_mandir}/man1/
#zsh completion
install -p -m 644 doc/zsh-completion.zsh %{buildroot}%{_datarootdir}/zsh/site-functions/_restic
#Bash completion
install -p -m 644 doc/bash-completion.sh %{buildroot}%{_datarootdir}/bash-completion/completions/restic
install -m 0755 -vd %{buildroot}%{_bindir}
install -p -m 755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}


%check
#Skip tests using fuse due to root requirement
export RESTIC_TEST_FUSE=0
%gocheck


%files
%license LICENSE
%doc GOVERNANCE.md CONTRIBUTING.md CHANGELOG.md README.md
%{_bindir}/%{name}
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_restic
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/restic
%{_mandir}/man1/restic*.*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0.12.1-4
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.12.1-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 20 2022 Steve Miller (copart) <code@rellims.com> - 0.12.1-1
- Upgrade to upstream 0.12.1
- Added upstream patch to tests (f1cfb97) for Go >= 1.16.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 16 2021 Kevin Anderson <andersonkw2@gmail.com> - 0.12.0-0
- Upgrade to upstream 0.12.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Steve Miller (copart) <code@rellims.com> - 0.10.0-3
- Removed patch 9abef3b, instead disabled tar tests

* Wed Oct 21 2020 Steve Miller (copart) <code@rellims.com> - 0.10.0-2
- Added upstream patch to tests (9abef3b) to resolve failed build

* Wed Oct 21 2020 Steve Miller (copart) <code@rellims.com> - 0.10.0-1
- Bumped to upstream 0.10.0
  Resolves: #1880788

* Sun Aug 30 2020 Steve Miller (copart) <code@rellims.com> - 0.9.6-6
- Added upstream patch for AllowRoot build issue, commit 18fee4806f6a71e951eaee2a3910140c5efb46e3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Steve Miller (copart) <code@rellims.com> - 0.9.6-3
- Added upstream patch for AccessTime test fix, commit 7cacba0394b1336dfee33e81cb1dc0e87f8ba10f

* Tue Mar 17 2020 Steve Miller (copart) <code@rellims.com> - 0.9.6-2
- Added upstream patch for tests in selinux, commit 2828a9c2b09a7e42ca8ca1c6ac506f87280c158b
- Replaced deprecated gochecks and gobuildroot macros

* Mon Mar 16 2020 Steve Miller (copart) <code@rellims.com> - 0.9.6-1
- Bumped to upstream 0.9.6
  Resolves: #1775745 and #1799976

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Steve Miller (copart) <code@rellims.com> - 0.9.5-1
- Bumped to upstream 0.9.5
  Resolves: #1702384

* Fri Feb 15 2019 Steve Miller (copart) <code@rellims.com> - 0.9.4-1
- Bumped to upstream 0.9.4
- Added new upstream dependency 
  golang(github.com/hashicorp/golang-lru/simplelru)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 3 2018 Steve Miller (copart) <code@rellims.com> - 0.9.3-1
- Bumped to upstream 0.9.3
  Resolves: #1645405 and #1642891
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@xxxxxxxxxxxxxxxxxxxxxxx/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Aug 8 2018 Steve Miller (copart) <code@rellims.com> - 0.9.2-1
- Bumped to upstream 0.9.2

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.9.1-3
- Rebuild with fixed binutils

* Wed Jun 13 2018 Steve Miller (copart) <code@rellims.com> - 0.9.1-2
- First package for Fedora
- Rework using More Go packaging

* Sun Jun 10 2018 Steve Miller (copart) <code@rellims.com> - 0.9.1-1
- Bumped restic version

* Sun May 27 2018 Steve Miller (copart) <code@rellims.com> - 0.9.0-1
- Bumped restic version

* Sun Mar 04 2018 Steve Miller (copart) <code@rellims.com> - 0.8.3-1
- Bumped restic version

* Tue Feb 20 2018 Steve Miller (copart) <code@rellims.com> - 0.8.2-1
- Bumped restic version

* Fri Jan 12 2018 Steve Miller (copart) <code@rellims.com> - 0.8.1-2
- Added man pages
- Added bash completion
- Added zsh completion

* Sun Jan 07 2018 Steve Miller (copart) <code@rellims.com> - 0.8.1-1
- New Version

* Sat Sep 16 2017 Philipp Baum <phil@phib.io> - 0.7.2-1
- New Version

* Sun Aug 27 2017 Philipp Baum <phil@phib.io> - 0.7.1-1
- New Version

* Wed Mar 15 2017 Philipp Baum <phil@phib.io> - 0.5.0-1
- Initial package build
