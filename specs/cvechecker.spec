# commit
# Use a commit newer than 3.8 release for pulling in some bugfixes
#%%global _commit 0f1ae263b8279e8cca103cf28ae37ab20340ec04
#%%global _shortcommit %%(c=%%{_commit}; echo ${c:0:7})

Name:           cvechecker
Version:        4.0
Release:        14%{?dist}
Summary:        Tool for compare packages installed in your system with CVE database
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/sjvermeu/cvechecker
#Source0:       %%{url}/archive/%%{_commit}/%%{_commit}.tar.gz
#Source0:        %%{name}/archive/%%{version}/%%{name}-%%{version}.tar.gz
# The developer marked the version "cvechecker-4.0" instead of 4.0, so we need to hack the URL
Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         cvechecker-c99.patch
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconf
BuildRequires:  libconfig-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libbsd)
BuildRequires: make
Requires:       jq

%description
The goal of cvechecker is to report about possible vulnerabilities on your
system, by scanning a list of installed software and matching results with the
CVE database.
This is not a bullet-proof method and you will have many false positives
(i.e.: vulnerability is fixed with a revision-release, but the tool isn't able
to detect the revision itself).

%prep
# The developer marked the version "cvechecker-4.0" instead of 4.0, so we need to specify the folder name
# https://github.com/sjvermeu/cvechecker/issues/49
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
autoreconf --force --install
%configure --enable-sqlite3 --enable-mysql --localstatedir=%{_sharedstatedir}
sed -i 's/\/mysql/\/mariadb/g;s/-lmysqlclient/-lmariadb/g' Makefile

%make_build

%install
%make_install PREFIX="%{_prefix}"  CONFDIR="%{buildroot}%{_sysconfdir}"
xmlto --skip-validation html-nochunks %{buildroot}%{_docdir}/cvechecker/acknowledgements.xml 
xmlto --skip-validation html-nochunks %{buildroot}%{_docdir}/cvechecker/userguide.xml
#/usr/share/doc/cvechecker/
install -Dm644 userguide.html  %{buildroot}%{_docdir}/cvechecker/userguide.html
install -Dm644 acknowledgements.html  %{buildroot}%{_docdir}/cvechecker/acknowledgements.html
rm -f %{buildroot}%{_docdir}/cvechecker/acknowledgements.xml %{buildroot}%{_docdir}/cvechecker/userguide.xml

%check
make check

%files
%doc README.md
%doc ChangeLog
%{_docdir}/cvechecker/acknowledgements.html
%{_docdir}/cvechecker/userguide.html
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cvechecker.conf
%{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*
%{_datadir}/cvechecker
%{_sharedstatedir}/cvechecker/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Florian Weimer <fweimer@redhat.com> - 4.0-7
- Apply upstream patch to fix C99 compatibility issue

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Zamir SUN <sztsian@gmail.com> - 4.0-2
- Add jq to requires

* Sat Sep 26 2020 Zamir SUN <sztsian@gmail.com> - 4.0-1
- Update to 4.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 3.8-5
- Rebuild for new libconfig

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Zamir SUN <sztsian@gmail.com> 3.8-2
- Change BuildRequires mariadb-devel to mariadb-connector-c-devel and openssl-devel
- Fixes BZ1494225

* Sat Aug 05 2017 Zamir SUN <sztsian@gmail.com> 3.8-1
- Update to upstream 3.8.
- Modify for mariadb-devel soname change.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Zamir SUN <sztsian@gmail.com> 3.7-3
- Remove Group tag from spec file

* Tue Jul 04 2017 Zamir SUN <sztsian@gmail.com> 3.7-2
- Add debuginfo package and fix some warning

* Tue Mar 14 2017 Zamir SUN <sztsian@gmail.com> 3.7-1
- initial package
