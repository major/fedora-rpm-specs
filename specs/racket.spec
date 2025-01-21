%global _find_debuginfo_opts --keep-section .rackboot

Name:           racket
Version:        8.15
Release:        3%{?dist}
Summary:        General purpose programming language

# see LICENSE.txt
License:        MIT AND Apache-2.0
URL:            https://racket-lang.org
Source0:        https://download.racket-lang.org/installers/%{version}/%{name}-%{version}-src.tgz
Patch0:         racket-configure-c99.patch

# To compile the program
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

# To fix rpath issue with executables.
BuildRequires:  chrpath

# Racket heavily utilizes the system ffi library.
BuildRequires:  libffi-devel

# For the racket/gui library (via libffi)
# https://github.com/racket/gui/blob/master/gui-lib/mred/private/wx/gtk/gtk3.rkt
BuildRequires:  gtk3

# For the racket/draw library (via libffi)
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/cairo-lib.rkt
BuildRequires:  cairo
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/pango.rkt
BuildRequires:  pango
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/png.rkt
BuildRequires:  libpng
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/jpeg.rkt
BuildRequires:  libjpeg-turbo
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/glib.rkt
BuildRequires:  glib2

# To validate desktop file
BuildRequires:  desktop-file-utils

BuildRequires:  git

# Require the subpackages
Requires:       racket-minimal%{?_isa} = %{version}-%{release}
Requires:       racket-pkgs = %{version}-%{release}
Recommends:     racket-doc = %{version}-%{release}

%description
Racket is a general-purpose programming language as well as
the world's first ecosystem for developing and deploying new
languages. Make your dream language, or use one of the dozens
already available.

# Equivalent to upstream's minimal-racket release
%package        minimal
Summary:        A minimal Racket installation
Requires:       racket-collects = %{version}-%{release}
%description    minimal
Racket's core runtime

%package        collects
Summary:        Racket's core collections libraries
BuildArch:      noarch
%description    collects
Libraries providing Racket's core functionality

# Arch independent source and bytecode files
%package        pkgs
Summary:        Racket package collections
# See BuildRequires section for details on dependencies
Requires:       gtk3
Requires:       cairo
Requires:       pango
Requires:       libpng
Requires:       glib2
Requires:       libjpeg-turbo
Requires:       racket-minimal = %{version}-%{release}
BuildArch:      noarch
%description    pkgs
Additional packages and libraries for Racket

# Development headers and links
%package        devel
Summary:        Development files for Racket
Requires:       racket-minimal%{?_isa} = %{version}-%{release}
%description    devel
Files needed to link against Racket.

# HTML documentation
%package        doc
Summary:        Documentation files for Racket
BuildArch:      noarch
%description    doc
A local installation of the Racket documentation system.

%prep
%autosetup -p1

# Remove bundled libffi
rm -r src/bc/foreign/libffi

%build
cd src

# https://github.com/racket/racket/issues/5183
CFLAGS="$CFLAGS -std=gnu17"
%configure \
        --enable-pthread \
        --enable-shared \
        --enable-libffi \
        --disable-libs \
%ifarch ppc64le s390x
        --enable-pb \
%endif
%ifarch ppc64le
        --enable-mach=tpb64l \
%endif
%ifarch s390x
        --enable-mach=tpb64b \
%endif
        --enable-lt="%{_bindir}/libtool" \
        --disable-strip

%make_build

%install
%make_install -C src

# Delete mred binaries and replace them with links.
rm %{buildroot}%{_bindir}/mred
rm %{buildroot}%{_bindir}/mred-text
ln -s gracket %{buildroot}%{_bindir}/mred
ln -s gracket-text %{buildroot}%{_bindir}/mred-text

# Fix the rpath error.
chrpath --delete %{buildroot}%{_bindir}/racket
chrpath --delete %{buildroot}%{_libdir}/racket/gracket

# Fix paths in the desktop files.
sed -i "s#%{buildroot}##g" %{buildroot}/%{_datadir}/applications/*.desktop

# Validate desktop files
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

# Fix buildroot references in html docs
for i in $(find %{buildroot}/%{_datadir}/doc/racket/ -name '*.html'); do
  sed -i "s#%{buildroot}##g" $i
done

# Remove the executable bit on legacy template file
chmod -x %{buildroot}%{_libdir}/racket/starter-sh

# disable check-buildroot
# (see https://github.com/racket/racket/issues/3878 discussion)
%undefine __arch_install_post

%check
%{buildroot}%{_bindir}/%{name} --version

%ldconfig_scriptlets

%files
%license src/LICENSE*.txt
%{_bindir}/drracket
%{_bindir}/gracket
%{_bindir}/gracket-text
%{_bindir}/mred
%{_bindir}/mred-text
%{_bindir}/mzc
%{_bindir}/mzpp
%{_bindir}/mzscheme
%{_bindir}/mztext
%{_bindir}/pdf-slatex
%{_bindir}/plt-games
%{_bindir}/plt-help
%{_bindir}/plt-r5rs
%{_bindir}/plt-r6rs
%{_bindir}/plt-web-server
%{_bindir}/scribble
%{_bindir}/setup-plt
%{_bindir}/slatex
%{_bindir}/slideshow
%{_bindir}/swindle
%{_datadir}/applications/

%files collects
%license src/LICENSE*.txt
%{_datadir}/racket/collects

%files minimal
%license src/LICENSE*.txt
%{_bindir}/racket
%{_bindir}/raco
%{_libdir}/racket
%dir %{_datadir}/racket/
%{_datadir}/racket/links.rktd
%{_datadir}/racket/pkgs/racket-lib
%{_datadir}/man/man1/racket*
%{_datadir}/man/man1/raco*
%dir %{_sysconfdir}/racket/
%config %{_sysconfdir}/racket/config.rktd

%files pkgs
%license src/LICENSE*.txt
%{_datadir}/racket
%{_datadir}/man/man1/drracket*
%{_datadir}/man/man1/gracket*
%{_datadir}/man/man1/mred*
%{_datadir}/man/man1/mzc*
%{_datadir}/man/man1/mzscheme*
%{_datadir}/man/man1/plt-help*
%{_datadir}/man/man1/setup-plt*
%exclude %{_datadir}/racket/links.rktd
%exclude %dir %{_datadir}/racket/pkgs/racket-lib
%exclude %dir %{_datadir}/racket/collects

%files devel
%license src/LICENSE-*.txt
%{_includedir}/racket

%files doc
%license src/LICENSE*.txt
%{_datadir}/doc/racket

%changelog
* Sun Jan 19 2025 Jens Petersen <petersen@redhat.com> - 8.15-3
- build with gcc15 using -std=gnu17

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov  6 2024 Jens Petersen <petersen@redhat.com> - 8.15-1
- Update to 8.15 release
- https://blog.racket-lang.org/2024/11/racket-v8-15.html

* Tue Aug 20 2024 Jens Petersen <petersen@redhat.com> - 8.14-1
- Update to 8.14 release
- https://blog.racket-lang.org/2024/08/racket-v8-14.html

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 20 2024 Jens Petersen <petersen@redhat.com> - 8.13-1
- https://blog.racket-lang.org/2024/05/racket-v8-13.html

* Wed May  1 2024 Jens Petersen <petersen@redhat.com> - 8.12-2
- re-enable ppc64le and s390x with portable bytecode backend (following debian)

* Mon Apr 29 2024 Jens Petersen <petersen@redhat.com> - 8.12-1
- https://blog.racket-lang.org/2024/02/racket-v8-12.html

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 31 2023 Jens Petersen <petersen@redhat.com> - 7.9-2
- re-enable ppc64le for epel

* Mon Aug 28 2023 Jens Petersen <petersen@redhat.com> - 7.9-1
- update to 7.9
- drop the nonfree doc patch

* Sat Aug 26 2023 Jens Petersen <petersen@redhat.com> - 7.4-12
- disable ppc64le (#2226390)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Florian Weimer <fweimer@redhat.com> - 7.4-10
- Port configure script to C99

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 David Benoit <dbenoit@redhat.com> - 7.4.1
- Update package version
- Remove doc-open-url patch (fixed upstream)
- Update remove-nonfree patch

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 David Benoit <dbenoit@redhat.com> 7.0-6
- Fix buildarch

* Sat Sep 22 2018 David Benoit <dbenoit@redhat.com> 7.0-5
- Remove links.rktd scriptlets and instead make docs
  a weak dependency

* Fri Sep 21 2018 David Benoit <dbenoit@redhat.com> 7.0-4
- Add scriptlets to handle updating links.rktd based on
  whether racket-pkgs is installed
- fix owenership of docs dir
- update docs patch

* Thu Sep 6 2018 David Benoit <dbenoit@redhat.com> 7.0-3
- use arm macro instead of armv7hl

* Wed Sep 5 2018 David Benoit <dbenoit@redhat.com> 7.0-2
- Disable SSE math on i686 until issue is fixed upstream
- Exclude ppc due to issue building Racket v7.0 and
  arch being deprecated in next release

* Fri Aug 17 2018 David Benoit <dbenoit@redhat.com> 7.0-1
- Update sources to Racket v7.0
- Remove 6.12 patches and add update remove nonfree
  srfi patch to 7.0

* Mon Jul 30 2018 David Benoit <dbenoit@redhat.com> 6.12-8
- Annotate dependencies with links to source code
- Move dependencies to racket-pkgs, since they are only used
  by that subpackage
- Update mred symbolic links
- Fix ownership of directories
- Remove executable bit from starter-sh

* Thu Jul 12 2018 David Benoit <dbenoit@redhat.com> 6.12-7
- Remove hardened build since it is enabled by default
- Add gcc to BuildRequires
- Remove wildcards from directory listings in files section

* Fri Apr 13 2018 David Benoit <dbenoit@redhat.com> 6.12-6
- Remove license wildcard and add license field to each subpackage

* Fri Apr 6 2018 David Benoit <dbenoit@redhat.com> 6.12-5
- remove update-database post scripts
- move libracket3m.so link into -devel
- add ldconfig_scriptlets after install
- remove disable debug_package and configure
  with --disable-strip instead
- add license to files section and update
  license header field
- validate desktop files
- change ownership of /etc/racket
- update changelog with release info
- use specific man directory man/man1/*
- refactor racket into subpackages
  racket-minimal, racket-collects, and racket-pkgs

* Wed Apr 4 2018 David Benoit <dbenoit@redhat.com> 6.12-4
- noarch -docs subpackage

* Tue Mar 20 2018 David Benoit <dbenoit@redhat.com> 6.12-3
- fix text encoding issue in description section
- remove doc-open-url scriptlets
- add scriptlet to fix paths in html docs
- add patch2 to backport rpaths fix in compiled .zo files
- add patch3 to backport rpaths fix in web-server-lib
- add patch4 to configure doc open url dynamically at runtime
- remove override of __arch_install_post to allow full
  checking of buildroot.

* Thu Feb 1 2018 David Benoit <dbenoit@redhat.com> - 6.12-2
- Fix duplication of object files
- Add version to racket-devel requirements
- Remove base package as a dependency of racket-doc
- Remove Groups tag

* Wed Jan 31 2018 David Benoit <dbenoit@redhat.com> - 6.12-1
- Update to current stable version
- Add patch0 to update SRFIs to latest upstream
- Add patch1 to remove nonfree SRFI components

* Thu Oct 26 2017 David Benoit <dbenoit@redhat.com> - 6.10-1
- Update to current stable version
- Remove libedit readline patch (fixed upstream)
- Break docs into separate package
- Add scriptlets to set doc-open-url based on
  whether docs are installed
- Exclude armv7hl and s390x as target arches
- Update description to match website
- Change URLs to use https instead of http


* Thu Jul 6 2017 David Benoit <dbenoit@redhat.com> - 6.9-1
- Update to current stable version
- Patch libedit readline error
- Remove ExclusiveArch to test all builds in koji

* Fri Jan 22 2016 Brandon Thomas <bthomaszx@gmail.com> - 6.3-1
- Update to current stable version.
- Updated description to match website.
- Removed build requirement "racket-packaging".
- Updated to gtk+3.
- Let Autoprovides determine provides.
- Debuginfo package is empty and preventing the package from building.
- Removed uneeded file copies.
- Remove possible extra static library.

* Sun Dec 14 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.1.6-1
- Update to current snapshot to fix match hash-table expander.

* Mon Dec 01 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.1-1
- Update to current stable version.

* Fri Sep 05 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.5-4
- Use racket-packaging to capture module dependencies.

* Tue Aug 19 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.5-1
- Updated to 6.1.0.5
- Merged the -doc package back in.

* Fri Aug 08 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.4-2
- Do not alter .zo files, prevent check-buildroot from being run instead.

* Thu Aug 07 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.4-1
- Updated to 6.1.0.4
- Split-off -doc package.

* Fri Jul 25 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.3-4
- Updated to 6.1.0.3
- Dropped the unnecessary static library.
- Dropped mred programs to enable debug package.

* Sat Jun 22 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.5-1
- Changed to use 5.3.5 version of Racket.
- Created static package for developers who may need static libraries.
- Added RPM optimization options to CFLAGS for build.
- Added macro to use SMP build options in make.

* Thu May 16 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.4-1
- Changed to use 5.3.4 version of Racket.

* Tue May 14 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.3-3
- Moved documentation to /usr/doc directory.

* Mon May 13 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.3-2
- Remove bundled libffi from racket before building program.

* Thu May  9 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.3-1
- Initial Revision.
