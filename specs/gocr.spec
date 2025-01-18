Name:           gocr
Version:        0.52
Release:        16%{?dist}
Summary:        GNU Optical Character Recognition program

License:        GPL-2.0-or-later
URL:            http://jocr.sourceforge.net/
Source0:        http://www-e.uni-magdeburg.de/jschulen/ocr/gocr-%{version}.tar.gz
Patch0:         gocr-0.46-perms.patch

BuildRequires:  gcc
BuildRequires:  netpbm-devel
BuildRequires: make
# Needed for conversion programs
Requires:       gzip, bzip2, /usr/bin/djpeg, netpbm-progs, transfig
Obsoletes:      %{name}-devel <= 0.45-4

%description
GOCR is an OCR (Optical Character Recognition) program, developed under the
GNU Public License. It converts scanned images of text back to text files.
Joerg Schulenburg started the program, and now leads a team of developers.

GOCR can be used with different front-ends, which makes it very easy to port
to different OSes and architectures. It can open many different image
formats, and its quality have been improving in a daily basis.

%prep
%setup -q
%patch -P0 -p1 -b .perms


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
# Don't ship static library
rm -rf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}
# Don't ship buggy Tcl/Tk frontend
rm $RPM_BUILD_ROOT/%{_bindir}/gocr.tcl

%files
%doc AUTHORS BUGS CREDITS doc/gocr.html gpl.html HISTORY README
%doc REMARK.txt REVIEW TODO
%lang(de) %doc READMEde.txt
%{_bindir}/gocr
%{_mandir}/man1/gocr.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Tomas Smetana <tsmetana@redhat.com> - 0.52-11
- Use SPDX license tag

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Tomas Smetana <tsmetana@redhat.com> - 0.52-1
- new upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Tomas Smetana <tsmetana@redhat.com> - 0.50-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Tomas Smetana <tsmetana@redhat.com> - 0.49-2
- rebuild because of libnetpbm

* Tue Nov 15 2011 Tomas Smetana <tsmetana@redhat.com> - 0.49-1
- new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 02 2010 Adam Tkac <atkac redhat com> - 0.48-2
- require /usr/bin/djpeg instead of libjpeg to be compatible with both
  libjpeg and libjpeg-turbo

* Tue Jan 19 2010 Tomas Smetana <tsmetana@redhat.com> - 0.48-1
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Tomas Smetana <tsmetana@redhat.com> - 0.46-1
- new upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 04 2008 Tomas Smetana <tsmetana@redhat.com> - 0.45-4
- and obsolete the devel package

* Thu Sep 04 2008 Tomas Smetana <tsmetana@redhat.com> - 0.45-3
- remove the unusable devel package again (related #344721)

* Wed Feb 13 2008 Tomas Smetana <tsmetana@redhat.com> - 0.45-2
- rebuild (gcc-4.3)

* Mon Jan 28 2008 Patrice Dumas <pertusus@free.fr> - 0.45-1
- update to 0.45
- rename gocr-0.44-man.patch to gocr-0.45-perms.patch and
  fix library and header permissions

* Mon Jan 14 2008 Tomas Smetana <tsmetana@redhat.com> - 0.44-4
- build devel package (with static library)

* Tue Aug 21 2007 - Orion Poplawski <orion@cora.nwra.com> - 0.44-3
- Update license tag to GPLv2+
- Rebuild for BuildID

* Wed Mar 21 2007 - Orion Poplawski <orion@cora.nwra.com> - 0.44-2
- Bump release to fix import tag issue

* Fri Mar 02 2007 - Orion Poplawski <orion@cora.nwra.com> - 0.44-1
- Update to 0.44

* Mon Dec 18 2006 - Orion Poplawski <orion@cora.nwra.com> - 0.43-1
- Update to 0.43
- Don't ship frontends

* Wed Nov 22 2006 - Orion Poplawski <orion@cora.nwra.com> - 0.41-3
- Add more requires

* Tue Nov 21 2006 - Orion Poplawski <orion@cora.nwra.com> - 0.41-2
- Split TCL/Tk GUI into -tk sub-package
- Ship GTK+ GUI

* Mon Nov 20 2006 - Orion Poplawski <orion@cora.nwra.com> - 0.41-1
- Initial Fedora Extras Version
