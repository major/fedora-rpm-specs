%bcond_without check

%global _hardened_build 1

%global distprefix %{nil}

# https://github.com/aliyun/aliyun-cli
%global goipath0        github.com/aliyun/aliyun-cli
Version:                3.0.104

# https://github.com/aliyun/aliyun-openapi-meta
%global goipath1        github.com/aliyun/aliyun-openapi-meta
%global version1        0
%global commit1         031f9f2ea5b68c1acf94bfe47c12616ab515b0c5

%gometa -a

%global _docdir_fmt     %{name}

%global godevelsummary0 Alibaba Cloud (Aliyun) CLI
%global godevelsummary1 Alibaba Cloud (Aliyun) OpenAPI Meta Data

%global common_description %{expand:
Alibaba Cloud (Aliyun) CLI.}

%global golicenses0     LICENSE LICENSE-oss
%global godocs0         CHANGELOG.md README-CN.md README.md README-bin.md\\\
                        README-cli.md README-CN-oss.md README-oss.md\\\
                        CHANGELOG-oss.md

%global golicenses1     LICENSE
%global godocs1         README-openapi-meta.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        %{godevelsummary0}

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
URL:            %{gourl}
Source0:        %{gosource0}
Source1:        %{gosource1}

# https://github.com/aliyun/aliyun-cli/issues/303
# https://bugzilla.redhat.com/show_bug.cgi?id=1866529
ExcludeArch:    armv7hl                   # (Bug rhbz#1866529)
# https://bugzilla.redhat.com/show_bug.cgi?id=1956389
ExcludeArch:    i686                      # (Bug rhbz#1956389)

BuildRequires:  golang-github-shulhan-bindata
BuildRequires:  golang(github.com/alibabacloud-go/tea/tea)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/endpoints)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/responses)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/ecs)
BuildRequires:  golang(github.com/aliyun/aliyun-oss-go-sdk/oss)
BuildRequires:  golang(github.com/aliyun/credentials-go/credentials)
BuildRequires:  golang(github.com/alyu/configparser)
BuildRequires:  golang(github.com/droundy/goopt)
BuildRequires:  golang(github.com/jmespath/go-jmespath)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(gopkg.in/ini.v1)
BuildRequires:  help2man

%if %{with check}
# Tests
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  zsh
%endif

%description
%{common_description}

%gopkg

%prep
%goprep -a
cd %{gosourcedir}
mv bin/README.md README-bin.md
mv cli/README.md README-cli.md
mv oss/README.md README-oss.md
mv oss/README-CN.md README-CN-oss.md
mv oss/LICENSE LICENSE-oss
mv oss/CHANGELOG.md CHANGELOG-oss.md
mv %{_builddir}/%{extractdir1}/README.md %{_builddir}/%{extractdir1}/README-openapi-meta.md
rm %{gobuilddir}/src/%{goipath0} %{gobuilddir}/src/%{goipath1}
rmdir ./aliyun-openapi-meta
ln -fs %{_builddir}/%{extractdir1} ./aliyun-openapi-meta
go-bindata.shulhan -o resource/metas.go -pkg resource ./aliyun-openapi-meta/...
ln -fs %{_builddir}/%{extractdir0} %{gobuilddir}/src/%{goipath0}
ln -fs %{_builddir}/%{extractdir1} %{gobuilddir}/src/%{goipath1}

%build
LDFLAGS="-X '%{goipath0}/cli.Version=%{version}'" 
%gobuild -o %{gobuilddir}/bin/aliyun %{goipath0}/main
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{godevelsummary0}" -s 1 -o %{gobuilddir}/share/man/man1/aliyun.1 -N --version-string="%{version}" %{gobuilddir}/bin/aliyun

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
cp -Trv /etc/skel %{getenv:HOME}
# Skip 'openapi' and 'oss/lib' tests due to need for credentials
%gocheck -d 'openapi' -d 'oss/lib'
%endif

%files
%license ../%{extractdir0}/LICENSE      ../%{extractdir0}/LICENSE-oss
%doc ../%{extractdir0}/CHANGELOG.md     ../%{extractdir0}/CHANGELOG-oss.md
%doc ../%{extractdir0}/README-CN.md     ../%{extractdir0}/README.md
%doc ../%{extractdir0}/README-bin.md    ../%{extractdir0}/README-cli.md
%doc ../%{extractdir0}/README-CN-oss.md ../%{extractdir0}/README-oss.md
%doc ../%{extractdir1}/README-openapi-meta.md
%{_mandir}/man1/aliyun.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.104-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 3.0.104-5
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.104-4
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Wed Jan 26 2022 Brandon Perkins <bperkins@redhat.com> - 3.0.104-3
- remove 'unset LDFLAGS' with fix to redhat-rpm-config

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Brandon Perkins <bperkins@redhat.com> - 3.0.104-1
- Update to version 3.0.104 (Fixes rhbz#2032015)
- Update to aliyun-openapi-meta to commit
  031f9f2ea5b68c1acf94bfe47c12616ab515b0c5

* Mon Dec 06 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.100-1
- Update to version 3.0.100 (Fixes rhbz#2018579)
- Update to aliyun-openapi-meta to commit
  2831265b4655cec94b9088255d40df431cad3be7

* Wed Oct 27 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.96-1
- Update to version 3.0.96 (Fixes rhbz#2017317)
- Update to aliyun-openapi-meta to commit
  3bcecc8e1466a5f5db7c9ae99f9bc518407d0af7

* Thu Oct 07 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.94-1
- Update to version 3.0.94 (Fixes rhbz#2007261)
- Update to aliyun-openapi-meta to commit
  73154c2e3a0a425f80d0b995838165920839f572

* Thu Sep 09 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.90-1
- Update to version 3.0.90 (Fixes rhbz#1995336)
- Update to aliyun-openapi-meta to commit
  f774074df0fcdbaef8a29d205b9dad2efc912c59

* Tue Aug 17 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.87-1
- Update to version 3.0.87 (Fixes rhbz#1984228)
- Update to aliyun-openapi-meta to commit
  f95db2ea1adaf9645e076ecf6d87ff9ca3105c24

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.81-1
- Update to version 3.0.81 (Fixes rhbz#1979541)
- Update to aliyun-openapi-meta to commit
  5cfbc388745706fc683b2402631fcd970edaf980

* Thu Jul 01 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.80-1
- Update to version 3.0.80 (Fixes rhbz#1973850)
- Update to aliyun-openapi-meta to commit
  ce547b4e929164b4cfd81619ae1e919dea811275

* Tue Jun 15 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.79-1
- Update to version 3.0.79 (Fixes rhbz#1966690)
- Update to aliyun-openapi-meta to commit
  8377da2c573aa411015c9d1ffac993cab533e7d2

* Mon Jun 07 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.77-2
- Fix aliyun-openapi-meta generation (Fixes rhbz#1968295)

* Fri May 28 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.77-1
- Update to version 3.0.77 (Fixes rhbz#1965071)
- Update to aliyun-openapi-meta to commit
  92af720880941fb06015c8627ef6004def4e9de3

* Tue May 25 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.75-1
- Update to version 3.0.75 (Fixes rhbz#1964195)
- Update to aliyun-openapi-meta to commit
  0551d8f554c1b062f603f81c490cfb0cfc51d3d6

* Mon May 03 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.74-2
- ExcludeArch i686 due to build failing from running out of memory (Fixes rhbz#1956389)

* Mon May 03 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.74-1
- Update to version 3.0.74 (Fixes rhbz#1955892)
- Update to aliyun-openapi-meta to commit
  95a090031d4d5b4dd8d2d29104f33769b3ea66b4
- Addition of oss LICENSE and CHANGELOG
- Addition of MIT upstream license
- Removal of patch for building against credentials-go-1.1.0
  https://github.com/aliyun/aliyun-cli/pull/300
- Addition of alibabacloud-go/tea/tea and
  golang.org/x/crypto/ssh/terminal BuildRequires

* Mon Feb 22 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.73-1
- Update to version 3.0.73 (Fixes rhbz#1930798)
- Update to aliyun-openapi-meta to commit
  1e468f0cf8af08594022c94d3d6ff2ba40c574dd

* Wed Feb 10 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.72-1
- Update to version 3.0.72 (Fixes rhbz#1926904)
- Update to aliyun-openapi-meta to commit
  2d5d1aa75ba1fcc3648fb6d168c9b4868ee3d0b6

* Mon Feb 08 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.71-1
- Update to version 3.0.71 (Fixes rhbz#1925882)
- Update to aliyun-openapi-meta to commit
  d45282a09bd3a5f18617f3bf08d496ac65a529ac

* Tue Jan 26 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.69-1
- Update to version 3.0.69 (Fixes rhbz#1920075)
- Update to aliyun-openapi-meta to commit
  7dbfaea94291b4015874f4078a33c5c295dec1f5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.66-1
- Update to version 3.0.66 (Fixes rhbz#1915742)
- Update to aliyun-openapi-meta to commit
  2f79975a97bab92d67e3e0e67305c4fd52195820

* Tue Jan  5 2021 Brandon Perkins <bperkins@redhat.com> - 3.0.65-1
- Update to version 3.0.65 (Fixes rhbz#1910758)
- Update to aliyun-openapi-meta to commit
  1d9ccda91f5c61b5989968c5ca6d4dc50606c542

* Thu Dec  3 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.64-1
- Update to version 3.0.64 (Fixes rhbz#1903194)
- Update to aliyun-openapi-meta to commit
  9ce1f8ae486d76f0fc92a33082b764e73d5bf955

* Mon Nov 30 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.63-1
- Update to version 3.0.63 (Fixes rhbz#1900480)
- Update to aliyun-openapi-meta to commit
  f7af21e461bf01f16535990a996de78b866c6c3e

* Tue Oct 13 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.60-1
- Update to version 3.0.60 (Fixes rhbz#1887004)
- Update to aliyun-openapi-meta to commit
  af98eafaf38bb8dca2d0b205de88e9b1e7e7bb29

* Mon Sep 21 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.59-1
- Update to version 3.0.59 (Fixes rhbz#1880672)
- Update to aliyun-openapi-meta to commit
  944de0a2cc8e892728004bfa63a2d2964a49469b

* Wed Sep 16 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.58-1
- Update to version 3.0.58 (Fixes rhbz#1879465)
- Update to aliyun-openapi-meta to commit
  67c5e4302ba6c8207e4176e57145df677af30976

* Thu Aug 06 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.56-1
- Update to version 3.0.56 (Fixes rhbz#1866826)
- Update to aliyun-openapi-meta to commit
  e7acae2e91780bc24a4b71c17803dec5dbb0989f
- Copy skeleton dot files to HOME directory for TestCompletionInstallers

* Wed Aug 05 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-6
- ExcludeArch armv7hl due to build failing from running out of memory (Fixes rhbz#1866529)
- Explicitly include zsh BuildRequires for tests on s390x

* Mon Aug 03 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-5
- Use go-bindata.shulhan instead of go-bindata
  https://github.com/aliyun/aliyun-cli/issues/262

* Mon Aug 03 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-4
- Set distprefix to nil
- Clean up unneeded globals
- Rename openapi-meta README.md for proper inclusion
- Requre new go-bindata
- Use standard goprep
- Prevent symbolic link infinite loops
- New aliyun-openapi-meta paths
- Added paths to license and doc in main package

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-3
- Update summary and description for clarity and consistency

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-2
- Reenable check stage
- Disable 'openapi' tests due to only being used by meta
- Disable 'oss/lib' tests due to need for credentials

* Sat Aug 01 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-1
- Update to version 3.0.55 (Fixes rhbz#1811183)
- Disable check stage temporarily
- Update to aliyun-openapi-meta to commit
  fb1de10319cf130af8945963ef6659707b5f04b7
- Add godevelsummary, golicenses, and godocs for all sources
- Reorder goprep and patch operations
- Remove goenv before gobuild
- Explicitly set man page summary
- Use standard gopkginstall and gopkgfiles
- Properly generate debugsourcefiles.list

* Fri Jul 31 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-3
- Patch to build against golang-github-aliyun-credentials-1.1.0

* Wed Jul 29 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-2
- Enable check stage
- Rename godocs in subdirectories
- Remove explicit gzip of man page
- Change gometaabs from define to global

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-1
- Update to version 3.0.54 (Fixes rhbz#1811183)
- Explicitly harden package
- Update to aliyun-openapi-meta to commit
  73a3ade39a109bda00ae3a80585fac98b3f3dd70
- Remove golang(github.com/satori/go.uuid)
  (commit=b2ce2384e17bbe0c6d34077efa39dbab3e09123b) BuildRequires
- Fix man page generation
- Clean changelog

* Fri Mar 06 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.36-2
- Add man page

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.36-1
- Update to aliyun-cli to version 3.0.36
- Update to aliyun-openapi-meta to commit
  3e9d6a741c5029c92f6447e4137a6531f037a931

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 3.0.30-1
- Initial package

