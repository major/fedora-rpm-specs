Name:           nekovm
Version:        2.3.0
Release:        18%{?dist}
Summary:        Neko embedded scripting language and virtual machine

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://nekovm.org/
Source0:        https://github.com/HaxeFoundation/neko/archive/v2-3-0/neko-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  git
BuildRequires:  gc-devel
BuildRequires:  pcre-devel
BuildRequires:  gtk2-devel
BuildRequires:  mariadb-connector-c-devel openssl-devel
BuildRequires:  sqlite-devel >= 3
BuildRequires:  httpd-devel
BuildRequires:  mbedtls-devel


%description
Neko is a high-level dynamically typed programming language which can
also be used as an embedded scripting language. It has been designed
to provide a common run-time for several different languages. Neko is
not only very easy to learn and use, but also has the flexibility of
being able to extend the language with C libraries. You can even write
generators from your own language to Neko and then use the Neko
run-time to compile, run, and access existing libraries.

If you need to add a scripting language to your application, Neko
provides one of the best trade-offs available between simplicity,
extensibility and speed.

Neko allows the language designer to focus on design whilst reusing a
fast and well constructed run-time, as well as existing libraries for
accessing file system, network, databases, XML...

Neko has a compiler and virtual machine. The Virtual Machine is both
very lightweight and extremely well optimized so that it can run very
quickly. The VM can be easily embedded into any application and your
libraries are directly accessible using the C foreign function
interface.

The compiler converts a source .neko file into a byte-code .n file that
can be executed with the Virtual Machine. Although the compiler is
written in Neko itself, it is still very fast. You can use the
compiler as standalone command-line executable separated from the VM,
or as a Neko library to perform compile-and-run for interactive
languages.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n neko-2-3-0


%build
# Avoid a compiler stack-overflow when building on 64 bit.
ulimit -s unlimited

%cmake . \
    -G Ninja \
    -DRELOCATABLE=OFF \
    -DRUN_LDCONFIG=OFF \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}
%cmake_build


%check
%ninja_test -C "%{_vpath_builddir}"


%install
%ninja_install -C "%{_vpath_builddir}"


%files
%doc README.md
%license LICENSE
%{_bindir}/neko
%{_bindir}/nekoc
%{_bindir}/nekoml
%{_bindir}/nekotools
%{_libdir}/libneko.so.*
%{_libdir}/neko/


%files devel
%doc CHANGES
%{_includedir}/*.h
%{_libdir}/libneko.so
%{_libdir}/cmake/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> - 2.3.0-17
- Rebuilt for mbedTLS 3.6.1

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Morten Stevens <mstevens@fedoraproject.org> - 2.3.0-9
- Rebuilt for mbedTLS 2.28.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Andy Li <andy@onthewings.net> - 2.3.0-5
- Rebuilt to dodge build-id conflict (RHBZ#1896901)

* Thu Jul 30 2020 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-4
- Use updated cmake macros
  https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 Andy Li <andy@onthewings.net> - 2.3.0-1
- New upstream version 2.3.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Andy Li <andy@onthewings.net> - 2.2.0-9
- Rebuilt for mbed TLS 2.16.0.

* Thu Sep 27 2018 Morten Stevens <mstevens@fedoraproject.org> - 2.2.0-8
- Rebuilt for mbed TLS 2.13.0

* Thu Sep 27 2018 Morten Stevens <mstevens@fedoraproject.org> - 2.2.0-7
- Rebuilt for mbed TLS 2.13.0

* Fri Jul 13 2018 Andy Li <andy@onthewings.net> - 2.2.0-6
- Add BuildRequires on gcc.
- Rebuilt for mbed TLS 2.11.0.

* Thu Jul 05 2018 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-5
- Remove ldconfig
  https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/SU3LJVDZ7LUSJGZR5MS72BMRAFP3PQQL/

* Mon May 21 2018 Robert Scheck <robert@fedoraproject.org> - 2.2.0-4
- Rebuilt for mbed TLS 2.9.0 (libmbedcrypto.so.2)

* Mon Feb 19 2018 Robert Scheck <robert@fedoraproject.org> - 2.2.0-3
- Rebuilt for mbed TLS 2.7.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Andy Li <andy@onthewings.net> - 2.2.0-1
- New upstream version 2.2.0.
- Remove patches applied in upstream.

* Thu Oct 12 2017 Andy Li <andy@onthewings.net> - 2.1.0-9
- Add nekotools test.
- Use Ninja to build.
- Add upstream patch of avoiding recompile nekoc/nekoml.

* Mon Sep 25 2017 Andy Li <andy@onthewings.net> - 2.1.0-8
- Use mariadb-connector-c-devel instead of mariadb-devel.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Richard W.M. Jones <rjones@redhat.com> - 2.1.0-5
- Rebuild against latest mariadb.

* Thu Jul 13 2017 Andy Li <andy@onthewings.net> - 2.1.0-4
- Added upstream fix (nekovm-xlocale.patch).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 08 2016 Andy Li <andy@onthewings.net> - 2.1.0-2
- Disabled parallel make.
- Added upstream fix (nekovm-mincoming-stack-boundary.patch).

* Tue Jun 07 2016 Andy Li <andy@onthewings.net> - 2.1.0-1
- New upstream version 2.1.0.
- Use the new upstream CMake build config.
- Depend on MariaDB instead of MySQL.
- Put libneko.so to devel package.
- Fixed spelling warnings in description.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Richard Jones <rjones@redhat.com> - 2.0.0-7
- Remove useless defattr in files section.

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 2.0.0-6
- Use global instead of define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  1 2013 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-1
- New upstream version 2.0.0 (RHBZ#979806).
- Rebase patches.
- Unset MAKEFLAGS before build.
- Make libneko.so be a symlink to libneko.so.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.2-3
- Only build SSE on x86_64 to fix FTBFS

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.8.2-2
- Rebuild against PCRE 8.30

* Mon Jan 16 2012 Richard W.M. Jones <rjones@redhat.com> - 1.8.2-1
- New upstream version 1.8.2.
- Rebase and fix soname patch.
- Run 'make test'.
- A cleaner way to rewrite CFLAGS.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Richard W.M. Jones <rjones@redhat.com> - 1.8.1-5
- Rebuild for updated libpng 1.5.

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.8.1-4
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Richard W.M. Jones <rjones@redhat.com> - 1.8.1-2
- Bump and rebuild.

* Thu Jan 14 2010 Richard W.M. Jones <rjones@redhat.com> - 1.8.1-1
- New upstream version 1.8.1.
- Rebase nekovm-library-paths.patch.
- Recheck package with rpmlint.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.8.0-6
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-3
- Rebuild to get updated mysql dep.

* Tue Dec 16 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-2
- New upstream release 1.8.0.
- Use dos2unix --keepdate.
- Use scriptlets to run ldconfig.
- Use _libdir instead of _prefix/lib.
- Set the soname correctly and include libneko.so.1.

* Wed Sep  3 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-7
- prelink conf file DOESN'T use prefixes, need to use a glob instead.

* Tue Sep  2 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-6
- BR sqlite-devel
- Remove DOS line-endings and executable bits from the source.
- Add RPM CFLAGS.
- *.ndll files are always installed in /usr/lib/neko (even on 64 bit).
- Search /usr/lib64 directory for libraries when building.
- When building, link against libmysqlclient.so (not .a).
- Avoid a compiler stack overflow when building on 64 bit.
- Stop prelink from stripping the binaries.

* Mon Sep  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-3
- Better way to strip the binaries.

* Sun Aug 31 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-2
- Initial RPM release.
