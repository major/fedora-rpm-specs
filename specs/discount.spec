# FTBFS with GCC 14 -Werror=incompatible-pointer-types
# https://bugzilla.redhat.com/show_bug.cgi?id=2261063
%global build_type_safety_c 2

Name:           discount
Version:        2.2.7
Release:        12%{?dist}
Summary:        A command-line utility for converting Markdown files into HTML
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.pell.portland.or.us/~orc/Code/%{name}
Source0:        https://github.com/Orc/%{name}/archive/v%{version}.tar.gz
Patch0:         discount-dont-run-ldconfig.patch
Patch1:         define_destructor.patch
Patch2:         set_deps.patch
Patch3: discount-c99.patch

BuildRequires:  gcc
BuildRequires: make
BuildRequires:  cmake
Requires:       libmarkdown%{?_isa} = %{version}-%{release}

%description
DISCOUNT is an implementation of John Gruber's Markdown language in C.
It includes all of the original Markdown features, along with a few
extensions, and passes the Markdown test suite.


%package -n libmarkdown
Summary: A fast implementation of the Markdown language in C

%description -n libmarkdown
libmarkdown is the library portion of discount, a fast Markdown language
implementation, written in C.


%package -n libmarkdown-devel
Summary: Development headers for the libmarkdown library
Requires: libmarkdown%{?_isa} = %{version}-%{release}

%description -n libmarkdown-devel
This package contains development headers and developer-oriented man pages for
libmarkdown.


%prep
%setup -q

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1


%build
CFLAGS='%{optflags}' ./configure.sh \
    --shared \
    --prefix=%{_prefix} \
    --execdir=%{_bindir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --enable-all-features \
    --with-fenced-code \
    --pkg-config
#make
%make_build %{?_smp_flags}


%install
%make_install install.man install.samples DESTDIR=%{buildroot}
install -D -m 644 libmarkdown.pc %{buildroot}%{_libdir}/pkgconfig/
cp -pav libmarkdown.pc %{buildroot}%{_libdir}/pkgconfig/
# Rename sample programs (names are too generic) and matching man1 pages
mv %{buildroot}%{_bindir}/makepage %{buildroot}%{_bindir}/discount-makepage
mv %{buildroot}%{_bindir}/mkd2html %{buildroot}%{_bindir}/discount-mkd2html
mv %{buildroot}%{_bindir}/theme %{buildroot}%{_bindir}/discount-theme
mv %{buildroot}%{_mandir}/man1/makepage.1 %{buildroot}%{_mandir}/man1/discount-makepage.1
mv %{buildroot}%{_mandir}/man1/mkd2html.1 %{buildroot}%{_mandir}/man1/discount-mkd2html.1
mv %{buildroot}%{_mandir}/man1/theme.1 %{buildroot}%{_mandir}/man1/discount-theme.1

%ldconfig_scriptlets -n libmarkdown


%check
for x in tests/*.t; do
	LD_LIBRARY_PATH=$(pwd) sh "${x}" || exit 1;
done


%files
%{_bindir}/markdown
%{_bindir}/discount-makepage
%{_bindir}/discount-mkd2html
%{_bindir}/discount-theme
%{_mandir}/man1/discount-*.1*
%{_mandir}/man1/markdown.1.gz
%{_mandir}/man3/markdown.3.gz
%{_mandir}/man3/mkd*
%{_mandir}/man7/markdown.7.gz
%{_mandir}/man7/mkd-extensions.7.gz


%files -n libmarkdown
%doc README COPYRIGHT CREDITS
%{_libdir}/libmarkdown.so.*


%files -n libmarkdown-devel
%{_libdir}/libmarkdown.so
%{_libdir}/pkgconfig/libmarkdown.pc
%{_includedir}/mkdio.h


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.7-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Greg Hellings <greg.hellings@gmail.com> - 2.2.7-6
- Use upstream manpage install command
- Rename man pages whose names are bad

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 2.2.7-3
- Fix building in C99 mode

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 18 2022 Greg Hellings - 2.2.7-1
- Upstream version 2.2.7
- Add two patches

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Greg Hellings <greg.hellings@gmail.com> - 2.2.4-1
- Upstream version 2.2.4
- Addresses multiple serious bugs

* Wed Jul 25 2018 Greg Hellings <greg.hellings@gmail.com> - 2.2.3-1
- Upstream version 2.2.3
- Added BR for gcc to build with F29

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-4
- Enable building and installing pkg-config file.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Greg Hellings <greg.hellings@gmail.com> - 2.2.2-1
- Upstream version 2.2.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild


* Mon Feb 02 2015 Craig Barnes <cbgnome@gmail.com> - 2.1.8-1
- Update to latest release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Craig Barnes <cbgnome@gmail.com> - 2.1.7-2
- Add "--with-fenced-code" to configuration flags

* Tue Dec 03 2013 Craig Barnes <cbgnome@gmail.com> - 2.1.7-1
- Update to latest release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Craig Barnes <cbgnome@gmail.com> - 2.1.6-1
- Update to latest release

* Sun Feb 10 2013 Craig Barnes <cbgnome@gmail.com> - 2.1.5a-1
- Update to latest release

* Wed Jul 25 2012 Craig Barnes <cbgnome@gmail.com> - 2.1.3-6
- Add optflags to CFLAGS instead of appending to CC

* Wed Jul 04 2012 Craig Barnes <cbgnome@gmail.com> - 2.1.3-5
- Remove spurious autoconf dependency
- Remove unnecessary manual buildroot cleaning
- Use gcc as CC instead of "cc"
- Fix typo in comment

* Thu Mar 08 2012 Craig Barnes <cr@igbarn.es> - 2.1.3-4
- Pass optflags to configure script

* Tue Jan 24 2012 Craig Barnes <cr@igbarn.es> - 2.1.3-3
- Remove duplicate docs from base package (already included in libmarkdown)
- Add --enable-all-features flag to "turn on all stable, optional features"
- Specify single include file (mkdio.h) instead of using glob matching
- Make man3 and man7 file matching more accurate (specify the "mkd" prefix)

* Tue Jan 24 2012 Craig Barnes <cr@igbarn.es> - 2.1.3-2
- Change renamed "discount" binary back to the upstream default "markdown"
  (the conflict with "python-markdown" was already resolved in rawhide)
- Change renamed "discount.1" man page back to "markdown.1"
- Remove some now unnecessary comments

* Sun Jan 22 2012 Craig Barnes <cr@igbarn.es> - 2.1.3-1
- Rename "markdown" binary to "discount" (clashed with python-markdown)
- Prefix all other binaries with "discount-" (names were too generic)
- Rename man1 pages to match their renamed binaries
- Amend patterns in files section to match renamed binaries and man1 pages
- Remove unnecessary, duplicate paragraph from libmarkdown-devel description
- Remove unnecessary "defattr" macros (default behaviour since RPM 4.4)
- Minor formatting clean-ups
- Update to latest upstream release
- Re-generate patch to reflect upstream changes

* Mon Dec 12 2011 Craig Barnes <cr@igbarn.es> - 2.1.2-4
- Split configure script flags across multiple lines for readability
- Add previously missing "--execdir" flag to configure script
- Use make install.everything target instead of specifying 3 separate targets

* Sun Oct 16 2011 Craig Barnes <cr@igbarn.es> - 2.1.2-3
- Get sources from author's website instead of GitHub

* Sat Oct 01 2011 Craig Barnes <cr@igbarn.es> - 2.1.2-2
- Remove unnecessary post/postun sections for base package
- Make base package explicitly depend on libmarkdown

* Wed Sep 28 2011 Craig Barnes <cr@igbarn.es> - 2.1.2-1
- New upstream version
- Add sample programs to the installation

* Mon Sep 26 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-5
- Move man3 pages from libmarkdown to libmarkdown-devel
- Add license document and other basic documentation to libmarkdown

* Sun Sep 25 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-4
- Make libmarkdown-devel explicitly depend on libmarkdown
- Remove unnecessary clean section
- Make pattern matching in file selections more specific
- Move unversioned shared library to libmarkdown-devel package
- Add post and postun sections for running ldconfig
- Add patch to prevent bundled script from running ldconfig itself

* Sun Sep 25 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-3
- Use seperate "libmarkdown" package for shared library
- Move development headers from discount-devel to libmarkdown-devel
- Add clean directive
- Add check directive for running the bundled test suite

* Thu Sep 22 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-2
- Packaged man pages
- Split development files into separate -devel package
- Fixed various rpmlint warnings

* Thu Sep 22 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-1
- Initial package.

