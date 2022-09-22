%global _gitver	ff7641193a
Name:		novacom-client
Version:	1.1.0
Release:	0.26.rc1.git.%{_gitver}%{?dist}
Summary:	Client for utility to connect to WebOS devices
License:	ASL 2.0
URL:		https://github.com/openwebos/novacom
# git clone https://github.com/openwebos/novacom.git
# cd novacom
# git archive --prefix=novacom-git-ff7641193a/ --format tar.gz -o ../novacom-git-ff7641193a.tar.gz ff7641193a
Source0:	novacom-git-%{_gitver}.tar.gz
Source1:	novaterm
# This patch forces the makefile to use our CFLAGS and link properly
Patch0:		novacom-makefile-fixes.patch
Patch1:		novacom-remove-base64.patch

%description
Novacom allows you to connect to WebOS devices that are connected over USB.
You must have novacom-server installed to use it.

%package -n novacom
Summary:	Utility to connect to WebOS devices
BuildRequires: make
BuildRequires:	gcc
Requires:	novacom-client = %{version}-%{release}
Requires:	novacom-server

%description -n novacom
Novacom allows you to connect to WebOS devices that are connected over USB.

This package installs both the client and the server.  To use the client, you
must first start the server using 'systemctl start novacomd.service' as root,
and then run 'novacom' as a regular user.

%prep
%setup -q -n novacom-git-%{_gitver}
%patch0 -p1
%patch1 -p1
# Remove bundled base64 library that's available in libtomcrypt
rm -f src/base64.c src/base64.h

%build
make LDFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 build-novacom/novacom $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}

%files
%doc README.md
%{_bindir}/novacom
%{_bindir}/novaterm

%files -n novacom
%doc README.md

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.26.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.25.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.24.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.23.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.22.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.21.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.20.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.19.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.18.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Jonathan Dieter <jdieter@gmail.com> - 1.1.0-0.17.rc1.git.ff7641193a
- Add BuildRequires: gcc

* Thu Feb 08 2018 Jonathan Dieter <jdieter@gmail.com> - 1.1.0-0.16.rc1.git.ff7641193a
- Remove obsolete Group and Buildroot tags, and stop removing buildroot on build and install

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.15.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.14.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.13.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.12.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.11.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.10.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.9.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.8.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.7.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.6.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.5.rc1.git.ff7641193a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May  7 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.4.rc1.git.ff7641193a
- Fix Requires for novacom

* Thu Apr 26 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.3.rc1.git.ff7641193a
- Remove unused base64 functions
- Use consistent RPM_OPT_FLAGS and RPM_BUILD_ROOT variables
- Change define macro to global
- Remove unnecessary BR: glibc-devel

* Thu Apr 12 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.2.rc1.git.ff7641193a
- Rename to novacom-client and add novacom subpackage that pulls in both
  -client and -server
- Remove unneeded defattr line

* Mon Apr  2 2012 Jonathan Dieter <jdieter@lesbg.com> - 1.1.0-0.1.rc1.git.ff7641193a
- Initial release
