Summary: An Optical Character Recognition program
Name: ocrad
Version: 0.29
Release: 4%{?dist}
License: GPL-3.0-or-later
Source: ftp://ftp.gnu.org/gnu/ocrad/%{name}-%{version}.tar.lz
Patch0: ocrad-0.25-nostatic.patch
URL: http://www.gnu.org/software/ocrad/ocrad.html
BuildRequires: make
BuildRequires: lzip gcc-c++
BuildRequires: libpng-devel

%description
GNU Ocrad is an OCR (Optical Character Recognition) program based on a feature
extraction method. It reads images in pbm (bitmap), pgm (greyscale) or ppm
(color) formats and produces text in byte (8-bit) or UTF-8 formats.
Also includes a layout analyser able to separate the columns or blocks of text
normally found on printed pages.
Ocrad can be used as a stand-alone console application, or as a backend to
other programs.

%prep
%setup -q
%patch 0 -p1 -b .nostatic

%build
%configure
make CXXFLAGS="$RPM_OPT_FLAGS" %{?_smp_flags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p doc/ocrad.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/ocrad
%attr(0644,root,root) %{_mandir}/man1/*
%attr(0644,root,root) %{_infodir}/ocrad.info.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Tomas Smetana <tsmetana@redhat.com> - 0.29-1
- New upstream version

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Tomas Smetana <tsmetana@redhat.com> - 0.28-4
- Use SPDX license tag

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Tomas Smetana <tsmetana@redhat.com> - 0.28-1
- New upstream version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Tomas Smetana <tsmetana@redhat.com> - 0.26-4
- Add C++ compiler to BuildRequires, fixes: rhbz#1605290

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Tomas Smetana <tsmetana@redhat.com> - 0.26-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Tomas Smetana <tsmetana@redhat.com> - 0.25-1
- new upstream version

* Thu Oct 09 2014 Tomas Smetana <tsmetana@redhat.com> - 0.24-1
- new upstream version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Tomas Smetana <tsmetana@redhat.com> - 0.23-1
- new upstream version

* Fri Jul 26 2013 Tomas Smetana <tsmetana@redhat.com> - 0.22-1
- new upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 16 2011 Tomas Smetana <tsmetana@redhat.com> - 0.21-1
- new upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Tomas Smetana <tsmetana@redhat.com> 0.20-1
- new upstream version

* Tue Apr 27 2010 Tomas Smetana <tsmetana@redhat.com> 0.19-2
- build requires lzip

* Tue Apr 27 2010 Tomas Smetana <tsmetana@redhat.com> 0.19-1
- new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Tomas Smetana <tsmetana@redhat.com> 0.18-1
- new upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 03 2008 Tomas Smetana <tsmetana@redhat.com> 0.17-3
- remove unpackaged file

* Fri Feb 29 2008 Tomas Smetana <tsmetana@redhat.com> 0.17-2
- fix spec file
- fix compilation issues with gcc-4.3

* Fri Feb 29 2008 Tomas Smetana <tsmetana@redhat.com> 0.17-1
- Spec file created
