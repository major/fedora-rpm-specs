Name:           eblook
Version:        1.6.1
Release:        41%{?dist}
Summary:        Command-line EB and EPWING dictionary search program

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://openlab.ring.gr.jp/edict/eblook/
Source0:        http://openlab.ring.gr.jp/edict/eblook/dist/%{name}-%{version}.tar.gz
Patch0:         eblook-strcpy.patch
Patch1:         eblook-size_t.patch
Patch2:         eblook-ssize_t.patch

BuildRequires:  eb-devel
BuildRequires:	automake, libtool
BuildRequires: make

%description
Command-line EB and EPWING dictionary search program.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p2
%patch -P2 -p1
for i in NEWS README; do
    iconv -f ISO-2022-JP -t UTF-8 $i > ${i}.UTF-8
    mv ${i}.UTF-8 $i
done
autoreconf -fi


%build
%configure --with-eb-conf=%{_libdir}/eb.conf
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# convert info file to utf-8
( cd $RPM_BUILD_ROOT%{_infodir}
  %{_bindir}/iconv -f EUC-JP -t UTF-8 eblook.info > eblook.info.utf8 && mv -f eblook.info{.utf8,} || rm eblook.info.utf8
)

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/eblook
%{_infodir}/eblook.info*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.1-40
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep  3 2013 Daiki Ueno <dueno@redhat.com> - 1.6.1-17
- rebuild against new eb

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Daiki Ueno <dueno@redhat.com> - 1.6.1-15
- pull the latest config.guess and config.sub for ARM64 port

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 18 2010 Daiki Ueno <dueno@redhat.com> - 1.6.1-10
- apply a patch for ssize_t and int confusion, provided by Tatsuya Kinoshita.

* Tue Aug 17 2010 Daiki Ueno <dueno@redhat.com> - 1.6.1-9
- apply a patch for size_t and int confusion, provided by Kazuhiro Ito.

* Fri Apr 16 2010 Daiki Ueno <dueno@redhat.com> - 1.6.1-8
- don't use tabs in this spec.
- change the encoding of Japanese docs to UTF-8.

* Fri Apr 16 2010 Daiki Ueno <dueno@redhat.com> - 1.6.1-7
- fix wrong usage of strcpy (closes #579610).

* Mon Aug 31 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.1-6
- F-12: Rebuild against new eb

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Jens Petersen <petersen@redhat.com> - 1.6.1-3
- rebuild with gcc43

* Fri Aug 10 2007 Jens Petersen <petersen@redhat.com>
- specify license is GPLv2+

* Wed Feb 14 2007 Jens Petersen <petersen@redhat.com> - 1.6.1-2
- convert info file to utf-8
- configure --with-eb-conf

* Mon Feb 12 2007 Jens Petersen <petersen@redhat.com> - 1.6.1-1
- initial packaging for Fedora (#228243)
