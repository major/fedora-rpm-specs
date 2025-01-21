Name: sloccount
Summary: Measures source lines of code (SLOC) in programs
Version: 2.26
Release: 42%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: http://www.dwheeler.com/sloccount/sloccount-%{version}.tar.gz
URL: https://sourceforge.net/projects/sloccount/
BuildRequires: make
BuildRequires: flex
BuildRequires: perl-generators
BuildRequires: gcc

%description
SLOCCount (pronounced "sloc-count") is a suite of programs for counting
physical source lines of code (SLOC) in potentially large software systems.

SLOCCount can be used to generate reports in different formats for use
by report-generating tools.

%prep
%autosetup

%build
make CC="${CC:-gcc} ${RPM_OPT_FLAGS} ${RPM_LD_FLAGS}"

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
make install_programs PREFIX=${RPM_BUILD_ROOT}%{_prefix}
make install_man PREFIX=${RPM_BUILD_ROOT}%{_prefix}
# the sloccount makefile doesn't -m 644 on install for man page
chmod 644 ${RPM_BUILD_ROOT}%{_mandir}/man1/sloccount.1.gz
# Duplicate files can actually just be symlinks
cmp ${RPM_BUILD_ROOT}%{_bindir}/java_count ${RPM_BUILD_ROOT}%{_bindir}/c_count && rm ${RPM_BUILD_ROOT}%{_bindir}/java_count && ln -s c_count ${RPM_BUILD_ROOT}%{_bindir}/java_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/tcl_count && rm ${RPM_BUILD_ROOT}%{_bindir}/tcl_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/tcl_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/sed_count && rm ${RPM_BUILD_ROOT}%{_bindir}/sed_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/sed_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/ruby_count && rm ${RPM_BUILD_ROOT}%{_bindir}/ruby_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/ruby_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/makefile_count && rm ${RPM_BUILD_ROOT}%{_bindir}/makefile_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/makefile_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/exp_count && rm ${RPM_BUILD_ROOT}%{_bindir}/exp_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/exp_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/csh_count && rm ${RPM_BUILD_ROOT}%{_bindir}/csh_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/csh_count
cmp ${RPM_BUILD_ROOT}%{_bindir}/sh_count ${RPM_BUILD_ROOT}%{_bindir}/awk_count && rm ${RPM_BUILD_ROOT}%{_bindir}/awk_count && ln -s sh_count ${RPM_BUILD_ROOT}%{_bindir}/awk_count

%files
%doc sloccount.html README ChangeLog COPYING TODO
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.26-41
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Stewart Smith <stewart@flamingspork.com> - 2.26-37
- Build with the right LDFLAGS (fixes rpmlint warning about PIE binaries, hardens build)
- Remove executable bit on man page.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 09 2022 Bastien Nocera <bnocera@redhat.com> - 2.26-34
+ sloccount-2.26-34
- Update URL

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Bastien Nocera <bnocera@redhat.com> - 2.26-26
+ sloccount-2.26-26
- Add gcc BR

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.26-15
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.26-8
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.26-7
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 2.26-6
- Rebuild for build ID

* Fri Sep 15 2006 - Bastien Nocera <hadess@hadess.net> - 2.26-6
- Rebuilt

* Mon Jul 24 2006 - Bastien Nocera <hadess@hadess.net> - 2.26-5
- Add flex as a BuildReq, thanks to Matt Domsch

* Wed Apr 05 2006 - Bastien Nocera <hadess@hadess.net> - 2.26-4
- Use the RPM_OPT_FLAGS, spotted by Michael Schwendt <bugs.michael@gmx.net>

* Tue Apr 04 2006 - Bastien Nocera <hadess@hadess.net> - 2.26-3
- shorten description, and quieten setup

* Mon Apr 03 2006 - Bastien Nocera <hadess@hadess.net> - 2.26-2
- Update source to match upstream vanilla
  change BuildRoot to match preferred value

* Thu Nov 10 2005 - Bastien Nocera <hadess@hadess.net> - 2.26-1
- First version for Fedora Extras

