%if 0%{?rhel}
%global apxs /usr/sbin/apxs
%endif
%if 0%{?fedora}
%global apxs /usr/bin/apxs
%endif
%global apache apache
%global apache_libexecdir %(%{apxs} -q LIBEXECDIR)
%global apache_sysconfdir %(%{apxs} -q SYSCONFDIR)
%global apache_includedir %(%{apxs} -q INCLUDEDIR)
%global apache_serverroot %(%{apxs} -q PREFIX)
%global apache_localstatedir %(%{apxs} -q LOCALSTATEDIR)
%global apache_mmn        %(MMN=$(%{apxs} -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)

Name:           mod_form
Version:        0.2
Release:        15%{?dist}
# The tarball's contents were downloaded from:
# http://apache.webthing.com/svn/apache/forms/mod_form.c
# http://apache.webthing.com/svn/apache/forms/mod_form.h
# the version number 0.2 is arbitrary, because no release
# version was ever defined.
License:        GPLv2+
Summary:        Apache module that decodes data submitted from Web forms
Source0:        mod_form-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  httpd-devel
Requires:       httpd
URL:            http://apache.webthing.com/mod_form

%description
Utility to decode data submitted from Web forms. It deals with both GET
and POST methods where the data are encoded using the default content type
application/x-www-form-urlencoded. It does not decode multipart/form-data
(file upload) forms: for those you should use mod_upload.

%package devel
License:	GPLv2+
Summary:	Apache module that decodes data submitted from Web forms
Requires:	httpd
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Utility to decode data submitted from Web forms. It deals with both GET
and POST methods where the data are encoded using the default content type
application/x-www-form-urlencoded. It does not decode multipart/form-data
(file upload) forms: for those you should use mod_upload.

Development package.

%prep
%setup -q -n mod_form-%{version}

%build
%{apxs} -c mod_form.c

%install
mkdir -p %{buildroot}/%{apache_libexecdir}
mkdir -p %{buildroot}/%{apache_includedir}
cp -p .libs/mod_form.so %{buildroot}/%{apache_libexecdir}
cp -p mod_form.h %{buildroot}/%{apache_includedir}

%files
%{apache_libexecdir}/mod_form.so

%files devel
%{apache_includedir}/mod_form.h

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Andrea Veri <averi@fedoraproject.org> - 0.2-1
- Include latest upstream changes, it being the 
  mod_form.c.preserve_args.patch we were previously applying.
- Adjust versioning to remove SVN bits
- .so files should be installed on the main package, headers are
  expected on the -devel package instead

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5.20131204svn145
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.20131204svn145
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3.20131204svn145
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2.20131204svn145
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Andrea Veri <averi@fedoraproject.org> 0.1-1.20131204svn145
- Adjusted the versioning.
- Fixed the license to be GPLv2+.

* Thu Nov 28 2013 Andrea Veri <averi@fedoraproject.org> 0.1-1
- First package release.
