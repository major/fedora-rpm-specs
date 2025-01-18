%bcond_without check

%global _hardened_build 1

# https://github.com/aliyun/ossutil
%global goipath         github.com/aliyun/ossutil
Version:                1.7.9

%gometa

%global common_description %{expand:
Alibaba Cloud (Aliyun) Object Storage Service (OSS) CLI.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README-CN.md README.md

Name:           %{goname}
Release:        12%{?dist}
Summary:        Alibaba Cloud (Aliyun) Object Storage Service (OSS) CLI

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aliyun/aliyun-oss-go-sdk/oss)
BuildRequires:  golang(github.com/alyu/configparser)
BuildRequires:  golang(github.com/droundy/goopt)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  help2man

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/ossutil %{goipath}
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{summary}" -s 1 -o %{gobuilddir}/share/man/man1/ossutil.1 -N --version-string="%{version}" %{gobuilddir}/bin/ossutil

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
# Skip 'lib' tests due to need for credentials
%gocheck -d 'lib'
%endif

%files
%license LICENSE
%doc CHANGELOG.md README-CN.md README.md
%{_mandir}/man1/ossutil.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 1.7.9-10
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 1.7.9-4
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.9-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Wed Jan 26 2022 Brandon Perkins <bperkins@redhat.com> - 1.7.9-2
- remove 'unset LDFLAGS' with fix to redhat-rpm-config

* Fri Jan 21 2022 Brandon Perkins <bperkins@redhat.com> - 1.7.9-1
- Update to version 1.7.9 (Fixes rhbz#2043747)
- don't use LDFLAGS='-Wl,-z relro ' from redhat-rpm-config to avoid error:
  "flag provided but not defined: -Wl,-z,relro"

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Brandon Perkins <bperkins@redhat.com> - 1.7.8-1
- Update to version 1.7.8 (Fixes rhbz#2033169)

* Thu Sep 09 2021 Brandon Perkins <bperkins@redhat.com> - 1.7.7-1
- Update to version 1.7.7 (Fixes rhbz#1998123)

* Tue Aug 17 2021 Brandon Perkins <bperkins@redhat.com> - 1.7.6-1
- Update to version 1.7.6 (Fixes rhbz#1990431)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Brandon Perkins <bperkins@redhat.com> - 1.7.5-1
- Update to version 1.7.5 (Fixes rhbz#1980939)

* Thu Jul 01 2021 Brandon Perkins <bperkins@redhat.com> - 1.7.4-1
- Update to version 1.7.4 (Fixes rhbz#1977801)

* Mon Apr 12 2021 Brandon Perkins <bperkins@redhat.com> - 1.7.3-1
- Update to version 1.7.3 (Fixes rhbz#1948055)

* Wed Mar 24 2021 Brandon Perkins <bperkins@redhat.com> - 1.7.2-1
- Update to version 1.7.2 (Fixes rhbz#1942623)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 13:49:47 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.1-1
- Update to 1.7.1
- Close: rhbz#1915743

* Fri Nov 20 2020 Brandon Perkins <bperkins@redhat.com> - 1.7.0-1
- Update to version 1.7.0 (Fixes rhbz#1899568)

* Fri Sep 04 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.19-1
- Update to version 1.6.19 (Fixes rhbz#1875619)

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.18-3
- Update summary and description for clarity and consistency

* Wed Jul 29 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.18-2
- Enable check stage
- Disable 'lib' tests due to need for credentials
- Add version tag
- Remove explicit gzip of man page

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.18-1
- Update to version 1.6.18 (Fixes rhbz#1811182)
- Explicitly harden package
- Remove golang(github.com/satori/go.uuid)
  (commit=b2ce2384e17bbe0c6d34077efa39dbab3e09123b) BuildRequires
- Fix man page generation
- Clean changelog

* Fri Mar 06 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.10-2
- Add man page

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.10-1
- Update to version 1.6.10

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 1.6.9-1
- Initial package

