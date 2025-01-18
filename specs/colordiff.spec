Name:           colordiff
Version:        1.0.21
Release:        8%{?dist}
Summary:        Color terminal highlighter for diff files

License:        GPL-2.0-or-later
URL:            http://www.colordiff.org/
Source0:        http://www.colordiff.org/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  make
Requires:       diffutils
Requires:       less
Recommends:     bzip2
Recommends:     gzip
Recommends:     xz
Suggests:       curl
Provides:       cdiff

%description
Colordiff is a wrapper for diff and produces the same output but with
pretty syntax highlighting.  Color schemes can be customized.


%prep
%setup -q


%build


%install
%make_install INSTALL_DIR=%{_bindir} \
    ETC_DIR=%{_sysconfdir} MAN_DIR=%{_mandir}/man1


%files
%license COPYING
%doc BUGS CHANGES colordiffrc colordiffrc-gitdiff colordiffrc-lightbg README
%config(noreplace) %{_sysconfdir}/colordiffrc
%{_bindir}/cdiff
%{_bindir}/colordiff
%{_mandir}/man1/cdiff.1*
%{_mandir}/man1/colordiff.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Richard Fearn <richardfearn@gmail.com> - 1.0.21-2
- Use SPDX license identifier

* Thu Dec 22 2022 Richard Fearn <richardfearn@gmail.com> - 1.0.21-1
- Update to 1.0.21 (#2155860)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 13 2022 Richard Fearn <richardfearn@gmail.com> - 1.0.20-1
- Update to 1.0.20 (#2053847)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 19 2020 Richard Fearn <richardfearn@gmail.com> - 1.0.19-1
- Update to 1.0.19

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.0.18-1
- Update to 1.0.18

* Wed May 31 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.0.17-1
- Update to 1.0.17

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.0.16-1
- Update to 1.0.16

* Wed Jun 24 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.0.15-1
- Update to 1.0.15
- Patch to get rid of dependency on which

* Tue Jun 23 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.0.14-1
- Update to 1.0.14
- Use upstream default color scheme
- Soften some dependencies

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.0.13-6
- Ship COPYING as %%license where available

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.13-3
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 14 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.13-1
- Update to 1.0.13.

* Tue Oct 16 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.12-1
- Update to 1.0.12.

* Sun Oct  7 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.11-1
- Update to 1.0.11.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun  4 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.10-1
- Update to 1.0.10.
- Clean up specfile constructs no longer needed with Fedora or EL6+.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 29 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.9-3
- Update cdiff xz patch to use xz also for lzma files.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.9-1
- Update to 1.0.9; wget 1.11, lzma and destdir patches applied upstream.
- Patch cdiff for xz support.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.8a-2
- Fix man page permissions.

* Mon Jan 26 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.8a-1
- 1.0.8a.
- Patch Makefile for DESTDIR support.
- Patch cdiff for lzma support, man page improvements.

* Thu Apr 10 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.0.7-3
- Patch to work around wget 1.11 regression, prefer curl over wget (#441862).
- Drop disttag.

* Tue Nov  6 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.0.7-2
- Upstream brown paper bag 1.0.7 re-release.

* Tue Nov  6 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.0.7-1
- 1.0.7.

* Sat Sep 29 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.0.6a-4
- Requires: which

* Mon Aug 13 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.0.6a-3
- License: GPLv2+

* Sat Jul  7 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.0.6a-2
- Convert docs to UTF-8.

* Sat May 12 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.0.6a-1
- 1.0.6a.

* Wed Apr  4 2007 Ville Skyttä <ville.skytta@iki.fi> - 1.0.6-2
- 1.0.6.

* Wed Aug 30 2006 Ville Skyttä <ville.skytta@iki.fi> - 1.0.5-2
- Drop no longer needed Obsoletes.

* Sat May 21 2005 Ville Skyttä <ville.skytta@iki.fi> - 1.0.5-1
- Add version to cdiff Obsoletes (Matthias Saou).
- Require diffutils (Matthias Saou, Matthew Miller).

* Mon Mar 28 2005 Ville Skyttä <ville.skytta@iki.fi> - 1.0.5-0.1
- 1.0.5.

* Thu Mar 17 2005 Ville Skyttä <ville.skytta@iki.fi> - 1.0.4-0.1
- Disable banner display in default configs.
- Drop unnecessary Epochs.

* Fri Aug 13 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:1.0.4-0.fdr.3
- Apply upstream fix for context diff detection.

* Thu Aug 12 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:1.0.4-0.fdr.2
- Use lightbg as the default scheme and make it work better with dark
  backgrounds too.

* Sat Jul 17 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:1.0.4-0.fdr.1
- First build.
- Include cdiff wrapper.
