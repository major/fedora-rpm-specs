Name:           httrack
Version:        3.49.2
Release:        16%{?dist}
Summary:        Website copier and offline browser
License:        GPLv2+
URL:            http://www.httrack.com
Source0:        http://mirror.httrack.com/historical/%{name}-%{version}.tar.gz
Patch0: httrack-configure-c99.patch
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires: make
Requires:       hicolor-icon-theme
Requires:       xdg-utils

%description
HTTrack is a free and easy-to-use offline browser utility. It allows the user 
to download a World Wide Web site from the Internet to a local directory, 
building recursively all directories, getting HTML, images, and other files 
from the server to your computer. HTTrack arranges the original site's 
relative link-structure. HTTrack can also update an existing mirrored site, 
and resume interrupted downloads. HTTrack is fully configurable, and has an 
integrated help system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
# Do not try to re-run autoconf after patching generated files.
touch -r aclocal.m4 m4/*.m4 configure

# Suppress rpmlint error.
iconv --from-code ISO8859-1 --to-code UTF-8 ./html/contact.html \
  --output contact.utf-8 && mv contact.utf-8 ./html/contact.html

%build
 %{!?_pkgdocdir: %global _pkgdocdir /usr/share/doc/httrack}
%configure  --disable-static \
            --disable-online-unit-tests \
            --htmldir=%{_pkgdocdir}/html \
            --docdir=%{_pkgdocdir}

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
%make_install

# Remove static libraries.
find %{buildroot} -type f -name "*.*a" -delete -print

# Remove unnecessary dynamic libraries from %%{_libdir}/httrack. These come
# from libtest, just a sample project from upstream.
rm -frv %{buildroot}%{_libdir}/%{name}

# Move libtest and templates from %%{_datadir}/httrack into %%{_pkgdocdir}.
mv %{buildroot}%{_datadir}/%{name}/libtest %{buildroot}%{_pkgdocdir}/libtest
mv %{buildroot}%{_datadir}/%{name}/templates %{buildroot}%{_pkgdocdir}/templates

# Now packaged in %%license
rm %{buildroot}%{_pkgdocdir}/html/license.txt

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/WebHTTrack.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/WebHTTrack-Websites.desktop

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check -C tests

%pretrans -p <lua>
--[[Script below fixes some crufts introduced in httrack < 3.47.26-1, to
cleanup wrong symlinks in old httrack packages.
In the past it's a shell script, it worked but another problem came in,
as if users are installing a fresh Fedora then they will fail at here.
This is because coreutils is not installed in pretrans stage although
fresh Fedora doesn't contain directory we want to remove.

https://fedoraproject.org/wiki/Packaging:Directory_Replacement
]]
require "os"
require "posix"

local path1 = "%{_datadir}/httrack/html"
local st1 = posix.stat(path1)
if st1 and st1.type == "directory" then
  local status1 = os.rename(path1, path1..".rpmmoved")
  if not status1 then
    local suffix1 = 0
    while not status1 do
      suffix1 = suffix1 + 1
      status1 = os.rename(path1..".rpmmoved", path1..".rpmmoved."..suffix1)
    end
    os.rename(path1, path1..".rpmmoved")
  end
end

local path2 = "%{_pkgdocdir}/html"
local st2 = posix.stat(path2)
if st2 and st2.type == "link" then
  os.remove(path2)
end

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %doc}
%{_pkgdocdir}
%exclude %{_pkgdocdir}/libtest
%license COPYING license.txt
%{_bindir}/htsserver
%{_bindir}/%{name}
%{_bindir}/proxytrack
%{_bindir}/webhttrack
%{_datadir}/applications/*WebHTTrack.desktop
%{_datadir}/applications/*WebHTTrack-Websites.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}*x*.xpm
%{_datadir}/%{name}/
%{_libdir}/libhtsjava.so.*
%{_libdir}/libhttrack.so.*
%{_mandir}/man1/htsserver.1*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/proxytrack.1*
%{_mandir}/man1/webhttrack.1*

%files devel
%{_pkgdocdir}/libtest/
%{_includedir}/%{name}/
%{_libdir}/libhtsjava.so
%{_libdir}/libhttrack.so

%changelog
* Tue Apr 25 2023 Florian Weimer <fweimer@redhat.com> - 3.49.2-16
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.49.2-12
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.49.2-8
- Do not rely on incidental default values

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.49.2-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.49.2-1
- Bump to 3.49.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.48.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.48.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.48.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.48.22-1
- Bump to 3.48.22

* Sat Mar 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.48.21-1
- Bump to 3.48.21

* Wed Mar 09 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.48.20-5
- Don't use relative %%doc, install into %%{_pkgdocdir} directly
  (Fix F24FTBFS, RHBZ#1307626).
- Rework libtool/rpath handling.
- Reflect Source0-URL having changed.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.48.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.48.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Christopher Meng <rpm@cicku.me> - 3.48.20-2
- Fix %%pretrans scriptlet bug again.

* Tue Feb 24 2015 Christopher Meng <rpm@cicku.me> - 3.48.20-1
- Update to 3.48.20
- Fix %%pretrans scriptlet bug.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.48.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Christopher Meng <rpm@cicku.me> - 3.48.19-2
- Fix -devel package dependency(missing openssl-devel)

* Sun Aug 03 2014 Christopher Meng <rpm@cicku.me> - 3.48.19-1
- Update to 3.48.19
- Fix a rare over-optimization bug.

* Mon Jul 21 2014 Christopher Meng <rpm@cicku.me> - 3.48.18-1
- Update to 3.48.18
- Add missing config.h back

* Fri Jul 11 2014 Christopher Meng <rpm@cicku.me> - 3.48.17-1
- Update to 3.48.17

* Fri Jun 13 2014 Christopher Meng <rpm@cicku.me> - 3.48.13-1
- Update to 3.48.13

* Fri May 23 2014 Christopher Meng <rpm@cicku.me> - 3.48.9-1
- Update to 3.48.9

* Wed Apr 16 2014 Christopher Meng <rpm@cicku.me> - 3.48.3-1
- Update to 3.48.3

* Tue Sep 24 2013 Christopher Meng <rpm@cicku.me> - 3.47.27-1
- Update to 3.47.27(BZ#1008374).
- Fix bug due to symlinks and dirs conflicts bug of RPM.

* Fri Sep 13 2013 Christopher Meng <rpm@cicku.me> - 3.47.26-2
- Fix dlopen requires.
- Cleanup scriptlets.

* Thu Sep 12 2013 Christopher Meng <rpm@cicku.me> - 3.47.26-1
- Update to 3.47.26

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.43.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 3.43.9-7
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.43.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.43.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.43.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.43.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun  7 2010 Tomas Mraz <tmraz@redhat.com> - 3.43.9-2
- Use libssl soname for openssl dlopen and dependency

* Mon Mar 22 2010 Debarshi Ray <rishi@fedoraproject.org> - 3.43.9-1
- Version bump to 3.42.93. (Red Hat Bugzilla #512420)
  * Fixed: application/xhtml+xml not seen as "html"
  * Fixed: URL encoding bugs with filenames containing '%%' characters
  * Fixed: Flash link extraction has been improved
  * Fixed: "Open error when decompressing" errors due to temporary file
    generation problems
  * Fixed: code tag handling bug in certain cases leading to produce invalid
    links
  * Fixed: horrible SSL slowdowns due to bogus select() calls
  * Fixed: Konqueror fixes
  * Updated: Portugues-Brasil language file
- Updated the openssl patch to consume newer sonames.

* Tue Sep 01 2009 Jesse Keating <jkeating@redhat.com> - 3.43.2-5
- Bumped to consume new openssl soname.

* Fri Jul 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 3.43.2-4
- Autorebuild for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.43.2-3
- Updated 'Requires: openssl = 0.9.8k'

* Tue Feb 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 3.43.2-2
- Autorebuild for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Debarshi Ray <rishi@fedoraproject.org> - 3.43.2-1
- Version bump to 3.43.2. (Red Hat Bugzilla #476110)
- Updated 'Requires: openssl = 0.9.8j' and fixed the sources for Rawhide.

* Tue Sep 09 2008 Debarshi Ray <rishi@fedoraproject.org> - 3.42.93-1
- Version bump to 3.42.93. (Red Hat Bugzilla #457523 (CVE-2008-3429), #460529)
- Use of generic macros in the publicly exposed API fixed by upstream.
- Use of xdg-open now added by upstream.
- OpenSSL version updated by upstream.
- Linkage issues in libhtsjava.so fixed by upstream.

* Thu Feb 21 2008 Debarshi Ray <rishi@fedoraproject.org> - 3.42-10
- Fixed runtime problems with --excludedocs.
- Omitted unused direct shared library dependencies.

* Tue Feb 19 2008 Release Engineering <rel-eng@fedoraproject.org> - 3.42-9
- Autorebuild for gcc-4.3.

* Thu Dec 13 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.42-8
- Added 'BuildRequires: chrpath' for removing rpaths.

* Sun Dec 09 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.42-7
- Updated 'Requires: openssl = 0.9.8g' and fixed the sources for Rawhide.

* Fri Dec 07 2007 Release Engineering <rel-eng@fedoraproject.org> - 3.42-6
- Rebuild for deps.

* Tue Nov 27 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.42-4
- Removed Encoding from Desktop Entry for all distributions, except Fedora 7.

* Fri Nov 23 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.42-3
- Mentioned openssl version explicitly as 0.9.8b.

* Fri Nov 23 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.42-2
- Fixed undefined non-weak symbols and unused direct shared library
  dependencies in libhtsjava.so.2.
- Fixed location of some documentation files.

* Sun Nov 18 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.42-1
- Version bump to 3.42.
- Fixed header files to not use generic headers and macros in the publicly
  exposed API.
- Removed Encoding from Desktop Entry.

* Mon Nov 12 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.41.3-2
- Added 'Requires: openssl' and fixed the sources.
- Added 'Requires: xdg-utils' and fixed the sources.
- Removed 'Requires: openssl-devel' from -devel.
- Removed unnecessary dynamic libraries.

* Mon Oct 29 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.41.3-1
- Initial build. Imported SPEC written by Yves Cluckers.
- Disabled parallel make to prevent failure with -j3.
- Changed character encodings from ISO8859-1 to UTF-8.
- Fixed .desktop files to comply with http://www.freedesktop.org/standards/.
