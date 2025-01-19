%global libo %{_libdir}/libreoffice
# The location of the installed extension. Apparently the directory name must
# end with .uno.pkg or unopkg will fail.
%global voikkoext %{libo}/share/extensions/voikko.uno.pkg
# The python code in this package is clearly noarch, but LibreOffice is
# arch-specific. Keeping this package arch-specific as well, for now.
%global debug_package %{nil}

# Manually byte-compile the extension files later
%global _python_bytecompile_extra 0

Name:           libreoffice-voikko
Version:        5.0
Release:        19%{?dist}
Summary:        Finnish spellchecker and hyphenator extension for LibreOffice

License:        GPL-3.0-or-later
URL:            http://voikko.puimula.org/
# The usual format of stable release URLs
Source0:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
# The usual format of test release URLs
#Source0:        http://www.puimula.org/htp/testing/%{name}-%{version}rc2.tar.gz
# https://github.com/voikko/libreoffice-voikko/pull/12
Patch0:         0001-make-install-unpacked-flattens-the-python-hierarchy-.patch

BuildRequires:    python3-devel
BuildRequires: make
Requires:         python3-libvoikko
Requires:         libreoffice-core%{?_isa}
Requires:         libreoffice-pyuno%{?_isa}

%description
This package contains a Finnish spell-checking and hyphenation component for
LibreOffice. The actual spell-checking and hyphenation functionality is
provided by the Voikko library.


%prep
%setup -q
%patch -P0 -p1 -b .fix.install-unpacked

%build
make extension-files %{?_smp_mflags}

%install
make install-unpacked DESTDIR=$RPM_BUILD_ROOT%{voikkoext}
%py_byte_compile %{__python3} %{buildroot}%{voikkoext}


%files
%{voikkoext}
%doc ChangeLog COPYING README

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 02 2023 Stephan Bergmann <sbergman@redhat.cm> - 5.0-14
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Stephan Bergmann <sbergman@redhat.com> - 5.0-10
- Fix description.xml

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Caolán McNamara <caolanm@redhat.com> - 5.0-5
- Resolves: rhbz#1676830 fix make install-unpacked to keep hierarchy

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 5 2018 Ville-Pekka Vainio <vpvainio AT iki.fi> - 5.0-2
- Fix dependencies

* Fri Aug 3 2018 Ville-Pekka Vainio <vpvainio AT iki.fi> - 5.0-1
- New upstream release, migrated to python
- Turn off automatic python byte-compilation and use py_byte_compile for the
  extension files

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 16 2016 Ville-Pekka Vainio <vpvainio@iki.fi> - 4.1-5
- The F24 mass rebuild failed, build again, this time it should succeed

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Oct 26 2014 Ville-Pekka Vainio <vpvainio AT iki.fi> - 4.1-1
- New upstream release, bump LibreOffice dependency to 4.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 19 2013 Ville-Pekka Vainio <vpvainio AT iki.fi> - 3.4.1-1
- New upstream release
- Update upstream URLs

* Wed Aug 07 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 3.4-3
- Don't use Arched BR: as written in Guidelines
- fix build failure as cpumaker dropped -BURC option

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Ville-Pekka Vainio <vpvainio AT iki.fi> - 3.4-1
- New upstream release
- Rebuilt for LibreOffice 4.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 04 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 3.3-1
- New upstream release for LibreOffice 3.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 3.2-4
- Specify CC_FLAGS and COMP_LINK_FLAGS so that an extra -O switch and setting an
  rpath are avoided.

* Sun Sep 25 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 3.2-3
- Remove the versioned dependency on libvoikko
- Bump the obsoleted openoffice.org-voikko version

* Sun Sep 18 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 3.2-2
- Build in the build section, install in the install section
- Add the _isa macro to the libreoffice dependencies

* Sun Aug 28 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 3.2-1
- Package renamed from openoffice.org-voikko to libreoffice-voikko
- First upstream libreoffice-voikko release

* Tue Jul 19 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 3.1.2-4
- Fix FTBFS (rhbz #716053)
- Update required LibreOffice version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 30 2010 Caolán McNamara <caolanm@redhat.com> - 3.1.2-2
- rebuild for LibreOffice

* Thu Aug 05 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.1.2-1
- New upstream release
- Remove both patches, upstreamed

* Tue Jul 27 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.1-5
- Fix for rhbz #618151, switch group elements to node elements in config.xcu,
  patch by David Tardon

* Wed Jul 14 2010 Caolán McNamara <caolanm@redhat.com> - 3.1-4
- Rebuild for OpenOffice.org 3.3

* Fri Jan 22 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.1-3
- Add patch from SVN to partly fix broken configuration handling, which
  may lead to an OO.o crash (rhbz#549289)

* Thu Nov 19 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.1-2
- Update for OpenOffice.org 3.2

* Mon Aug 10 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.1-1
- Update source URL to "official" upstream and bump version accordingly.
- The tarball is the same as in RC2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.1-0.2.rc2
- New release candidate

* Mon Apr 06 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.1-0.1.rc1
- New release candidate
- Grammar checking enabled

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.0.1-2
- Rebuild for OOO310_m1
- No need to use a define for unopkg anymore

* Wed Jan 21 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.0.1-1
- openoffice.org-voikko 3.0.1
- Drop integrated OOO 3.0.1 compatibility patch
- Require OOO 3.0.1

* Sun Dec 28 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.0-5
- Add patch from upstream to fix FTBFS with OOO300_m14, the grammar
  checking framework was changed

* Wed Nov 19 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.0-4
- Add Epoch 1 to all openoffice.org-core pre-/post-Requires to avoid bugs such
  as rhbz #472093 (incorrect openoffice.org-core dependency)

* Mon Oct 13 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.0-3
- Remove unneeded openoffice.org-core Requires, rpmbuild should detect that
  automatically. Keep libvoikko >= 2.0 Requires as instructed by upstream
  release notes, rpmbuild can't detected that automatically.

* Mon Oct 06 2008 Caolán McNamara <caolanm@redhat.com> - 3.0-2
- add --force to protect against installing by rpm an extension which was
  previously installed manually

* Thu Aug 28 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.0-1
- openoffice.org-voikko 3.0

* Wed Jul 30 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.0-0.2.rc1
- New release candidate:
  - Require libvoikko >= 2.0
  - Don't build with SHOW_UGLY_WARNINGS anymore

* Fri Jul 25 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 3.0-0.1.pre4
- New pre-release
- License changed to GPLv3+
- Require openoffice.org >= 3.0.0
- Drop unneeded 3 layer patch
- Build with new SHOW_UGLY_WARNINGS=1 option as this is a test release

* Tue Jun 03 2008 Caolán McNamara <caolan@redhat.com> - 2.2-5
- add openoffice.org-voikko-2.2-3layer.patch to build against 3 layer OOo

* Sat Apr 26 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-4
- Build with RPM_OPT_FLAGS, adds FORTIFY_SOURCE etc.

* Thu Apr 03 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-3
- Update the package to match the newest extension guidelines:
  - Change location
  - Update openoffice.org-* Requires

* Sun Feb 17 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-2
- Upstream released 2.2
- Remove the "temporary $HOME hack" and all -env options, since unopkg has 
  been patched to take care of all that

* Tue Feb 12 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-0.2.rc1
- Use the package name, not a Debian leftover environment variable as an mktemp
  template

* Mon Feb 11 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-0.1.rc1
- 2.2rc1
- Use new install-unpacked make target, no need to unzip the extension
  anymore
- This target both compiles and installs, so do everything in install and
  leave build empty
- Set $HOME to be a temporary directory while using unopkg. Otherwise unopkg
  causes problems if the package is installed with sudo
- Rebuild for GCC 4.3

* Wed Jan 23 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.1-1
- Bump release for the initial Fedora build

* Mon Jan 21 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.1-0.2
- Make one define a bit cleaner
- Changes by Caolán McNamara:
  - Unpack the component at install time
  - Make a non-empty debuginfo package
  - Install the extension to /usr/lib/

* Mon Jan 21 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.1-0.1
- Initial package
