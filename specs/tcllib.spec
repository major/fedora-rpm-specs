%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Summary:    The standard Tcl library
Name:       tcllib
Version:    1.21
Release:    7%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
Source:     https://core.tcl-lang.org/tcllib/uv/%{name}-%{version}.tar.xz
URL:        https://core.tcl-lang.org/tcllib/doc/trunk/embedded/index.md
BuildArch:  noarch

Requires:   tcl(abi) = 8.6

BuildRequires: tcl >= 8.6

%description
Tcllib, the Tcl Standard Library is a collection of Tcl packages
that provide utility functions useful to a large collection of Tcl
programmers.

%prep
%setup -q
chmod -x modules/doctools/mpformats/fr.msg
# Convert a couple of files to UTF-8
for file in modules/struct/pool.html ; do
    iconv --from=ISO-8859-1 --to=UTF-8 ${file} > ${file}.new
    mv -f ${file}.new ${file}
done

%build
# Nothing to build!

%install
echo 'not available' > modules/calendar/calendar.n
%{_bindir}/tclsh installer.tcl -no-gui -no-wait -no-html -no-examples \
    -pkg-path %{buildroot}/%{tcl_sitelib}/%name-%version \
    -app-path %{buildroot}%{_bindir} \
    -nroff-path %{buildroot}%_mandir/mann
# install HTML documentation into specific modules sub-directories:
pushd modules
cp ftp/docs/*.html ftp/
for module in comm exif ftp mime stooop struct textutil; do
    mkdir -p ../$module && cp $module/*.html ../$module/;
done
popd

# Clean up rpmlint warnings
find %{buildroot}/%{_datadir} -name \*.tcl -exec chmod 0644 {} \;

%files
%doc support/releases/PACKAGES README.md support/releases/history/README-1.9.txt ChangeLog
%doc exif/ ftp/ mime/ stooop/ struct/ textutil/
%license license.terms
%{tcl_sitelib}/%{name}-%{version}
%{_mandir}/mann/*
%{_bindir}/dtplite
%{_bindir}/mkdoc
%{_bindir}/nns*
%{_bindir}/page
%{_bindir}/pt
%{_bindir}/tcldocstrip

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.21-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 1.21-1
- Update to new 1.21.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 03 2022 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 1.20-1
- Update to new 1.20.
- Fixed version in log for 1.19-1.
- Fix filename in doc: README -> README.md.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 1.19-1
- Update to new 1.19.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 1.18-1
- Update to new 1.18.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.17-1
- Update to 1.17.
- Drop upstream patch as it was... hm... included in upstream.
- Fix download URL.
- Drop commented code.
- Drop defattr tag.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.16-5
- Add one more binary file to bin dir.

* Tue Mar 03 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.16-4
- Drop man renames as they are renamedin upstream.

* Tue Mar 03 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.16-3
- Update prev. patch.

* Tue Mar 03 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.16-2
- Fix topdir name.

* Tue Mar 03 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.16-1
- Update to 1.16.
- Patch for RHBZ #1197669.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.15-7
- Fixed conflict of zlib manpage with tcl package

* Tue May 27 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.15-6
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Tue Feb 25 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 1.15-4
- Add two more man files to conflict-list. Again.

* Mon Feb 24 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 1.15-3
- Add two more man files to conflict-list.

* Fri Feb 21 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 1.15-2
- Fix man/mann file conflict with tcl package.

* Thu Feb 20 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 1.15-1
- Update for new 1.15.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Wart <wart at kobold.org> - 1.11.1-1
- Update to 1.11.1

* Thu Jan 3 2008 Wart <wart at kobold.org> - 1.10-2
- Rebuild for Tcl 8.5

* Sat Nov 24 2007 Wart <wart at kobold.org> - 1.10-1
- Update to 1.10
- Fix download URL

* Tue Aug 21 2007 Wart <wart at kobold.org> - 1.9-5
- License tag clarification

* Fri May 11 2007 Wart <wart at kobold.org> - 1.9-4
- Include command line applications

* Fri Feb 16 2007 Wart <wart at kobold.org> - 1.9-3
- Rebuild for reversion back to tcl8.4

* Thu Feb 1 2007 Wart <wart at kobold.org> 1.9-2
- Rebuild for tcl8.5 (changes tcllib's install directory)

* Thu Oct 19 2006 Wart <wart at kobold.org> 1.9-1
- Update to 1.9

* Mon Aug 21 2006 Wart <wart at kobold.org> 1.8-5
- Rebuild for Fedora Extras

* Thu Feb 16 2006 Wart <wart at kobold.org> 1.8-4
- Remove executable bits on the library files to clean up rpmlint
  warnings.

* Mon Oct 17 2005 Wart <wart at kobold.org> 1.8-3
- Bumped release number again so to match the release in the FC3/FC4
  branches.

* Sun Oct 16 2005 Wart <wart at kobold.org> 1.8-2
- Bumped release number to fix cvs tagging problem.

* Sun Oct 16 2005 Wart <wart at kobold.org> 1.8-1
- update to 1.8

* Sun Oct 2 2005 Wart <wart at kobold.org> 1.7-3
- Remove generated filelist; other minor spec file improvements.

* Mon Jul 4 2005 Wart <wart at kobold.org> 1.7-2
- Minor spec file changes in an attempt to conform to Fedora Extras
  packaging guidelines.

* Thu Oct 14 2004 Jean-Luc Fontaine <jfontain@free.fr> 1.7-1
- 1.7 version
- new modules: asn, bee, grammar_fa, http, ident, jpeg, ldap,
  png, rc4, ripemd, tar, tie, treeql, uuid
- modules removed: struct1

* Thu Feb 19 2004 Jean-Luc Fontaine <jfontain@free.fr> 1.6-1
- 1.6 version
- leaner and cleaner spec file based on Fedora standards
- install under tcl_library, not hard-coded /usr/lib
