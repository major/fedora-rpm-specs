%define         name            efont-unicode-bdf
%define         fontdir         %{_datadir}/fonts/japanese/%{name}
%define         catalogdir      %{_sysconfdir}/X11/fontpath.d
%define         catalogname     %{name}


Name:           %{name}
Version:        0.4.2
Release:        40%{?dist}
Summary:        Unicode font by Electronic Font Open Laboratory

# Automatically converted from old format: BSD and Public Domain and Baekmuk and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Public-Domain AND Baekmuk AND LicenseRef-Callaway-MIT
URL:            http://openlab.jp/efont/unicode/
Source0:        http://openlab.jp/efont/dist/unicode-bdf/efont-unicode-bdf-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  %{_bindir}/bdftopcf
BuildRequires:  %{_bindir}/mkfontdir
BuildRequires:  %{_bindir}/ttmkfdir
BuildRequires:  gzip

%description
This package provides Unicode bitmap fonts provided by
Electronic Font Open Laboratory.

%prep
%setup -q

# convert documents' encoding to UTF8.
# must be done in %%prep
for f in README.{naga10,shinonome} ; do
   mv ${f} ${f}.tmp
   iconv -f EUCJP -t UTF8 ${f}.tmp > ${f} && rm -f ${f}.tmp || \
      mv ${f}.tmp ${f}
done

%build
for f in *bdf ; do
  g=${f%bdf}pcf
  bdftopcf -o $g $f
  gzip -9 $g
done

%install
# 1. install actual fonts
mkdir -p $RPM_BUILD_ROOT%{fontdir}
for g in *pcf.gz ; do
  install -m 644 $g $RPM_BUILD_ROOT%{fontdir}
done

# 2-1. create fonts.scale and fonts.dir in advance
ttmkfdir -d $RPM_BUILD_ROOT%{fontdir} -o $RPM_BUILD_ROOT%{fontdir}/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{fontdir}

# 2-2. create ghost files
touch $RPM_BUILD_ROOT%{fontdir}/encodings.dir
%if 0%{?fedora} < 29
touch $RPM_BUILD_ROOT%{fontdir}/fonts.cache-1
%endif

# 2.3 create libXfont catalogue symlink
mkdir -p $RPM_BUILD_ROOT%{catalogdir}
pushd $RPM_BUILD_ROOT%{catalogdir}
pushd ../../..
if [ x$(pwd) != x$RPM_BUILD_ROOT ] ; then
   echo "Current directory is not $RPM_BUILD_ROOT"
   exit 1
fi
popd
ln -sf ../../..%{fontdir} fonts-%{name}
popd

%files
%license COPYRIGHT
%doc README* ChangeLog List.html

%dir %{fontdir}
%{fontdir}/*pcf.gz
%verify(not md5 size mtime) %{fontdir}/fonts.scale
%verify(not md5 size mtime) %{fontdir}/fonts.dir
%ghost %verify(not md5 size mtime) %{fontdir}/encodings.dir

%{catalogdir}/fonts-%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.2-39
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.2-30
- Use binary name directly for xorg utility deaggregation

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Keep backward compatibility for spec file for sure

* Thu Jul 26 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.2-24
- Drop Group tag.
- No need to clean up buildroot.
- Do not create a ghost file for fonts.cache-1.
- No need to call fc-cache explicitly in scriptlets.
- Correct License tag.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Troy Dawson <tdawson@redhat.com> - 0.4.2-21
- Cleanup conditionals

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-10
- F-12: Mass rebuild

* Fri Mar 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-9
- F-11: Again rebuild for new virtual font Provides (#491958)

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-8
- F-11: Mass rebuild

* Sat Aug 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-7
- Drop X related dependency completely, along with chkfontpath drop
  (related to #252268, #252275)
- Generate fonts.dir at the build time instead of the runtime
  (following fonts-japanese)

* Mon Aug 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-6.1
- Rebuild.

* Fri Aug 18 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-6
- Change %%post.

* Tue Aug 15 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-5
- package again.

* Tue Aug 15 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-4
- Own the original font directory.

* Thu Aug 10 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-3
- Again more treatments.

* Thu Aug 10 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-2
- More neat treatments for post and postun.

* Thu Aug 10 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.2-1
- Initial packaging.
