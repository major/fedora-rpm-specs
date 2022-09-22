Name:		git-crypt
Version:	0.6.0
Release:	14%{?dist}
Summary:	Transparent file encryption in git

# MIT/X11 (BSD like): fhstream.{hpp|cpp} and parse_options.{hpp|cpp}
# GPLv3+: all other source files
License:	GPLv3+ and MIT
URL:		https://www.agwa.name/projects/git-crypt
Source0:	%{URL}/downloads/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	openssl-devel
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
BuildRequires: make
Requires:	git

%description
git-crypt enables transparent encryption and decryption of files in a
git repository. Files which you choose to protect are encrypted when
committed, and decrypted when checked out. git-crypt lets you freely
share a repository containing a mix of public and private
content. git-crypt gracefully degrades, so developers without the
secret key can still clone and commit to a repository with encrypted
files. This lets you store your secret material (such as keys or
passwords) in the same repository as your code, without requiring you
to lock down your entire repository.

%prep
%autosetup
sed -i "s|^\tinstall -|\t\$(INSTALL) -|" Makefile

%build
export DOCBOOK_XSL=%{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl
export ENABLE_MAN=yes
export CXXFLAGS="%{optflags} -DOPENSSL_API_COMPAT=0x30000000L"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
%make_install ENABLE_MAN=yes PREFIX=%{_prefix}

%files
%license COPYING
%doc README README.md
%{_bindir}/%{name}
%{_mandir}/man1/git-crypt.1*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.6.0-12
- Applied openssl3 compat compile flag

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.6.0-12
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr  1 2018 Christian Kellner <ckellner@redhat.com> - 0.6.0-3
- More review comments: License corrections, LDFLAGS,
  patch Makefile to preserve timestamps for install and
  fix add gcc-c++ as build requirement.

* Sat Mar 31 2018 Christian Kellner <ckellner@redhat.com> - 0.6.0-2
- Address review comments: Fix Summary, use macros for paths.

* Sat Mar 31 2018 Christian Kellner <ckellner@redhat.com> - 0.6.0-1
- Drop gpg-from-git-config.patch (included upstream)
- Drop openssl11.patch (fixed upstream)
- Setup CXXFLAGS so we get the correct compiler flags;
  this is also needed for debuginfo extraction to work.

* Fri Jun  9 2017 Christian Kellner <ckellner@redhat.com> - 0.5.0-4
- Add patch to read gpg excutable from .git/config

* Fri Mar 31 2017 Christian Kellner <ckellner@redhat.com> - 0.5.0-3
- Only apply the patch on fedora versions > 25

* Thu Mar 30 2017 Christian Kellner <ckellner@redhat.com> - 0.5.0-2
- Add patch for openssl 1.1 changes

* Tue Mar 28 2017 Christian Kellner <ckellner@redhat.com> - 0.5.0-1
- Initial revision
