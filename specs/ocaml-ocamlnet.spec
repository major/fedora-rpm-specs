# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ocamlnet
Version:        4.1.9
Release:        23%{?dist}
Summary:        Network protocols for OCaml
License:        BSD-3-Clause

URL:            http://projects.camlcity.org/projects/ocamlnet.html
VCS:            git:https://gitlab.com/gerdstolpmann/lib-ocamlnet3.git
Source0:        http://download.camlcity.org/download/ocamlnet-%{version}.tar.gz

# Avoid implicit int return types in C code in configure
# https://gitlab.com/gerdstolpmann/lib-ocamlnet3/-/merge_requests/23
Patch0:         ocaml-ocamlnet-configure-c99.patch

# Build ocamlrpcgen as native code.  Sent upstream 2021-01-14.
Patch1:         0001-Build-ocamlrpcgen-as-native-code.patch

# Make library linkage explicit
Patch2:         0002-Make-library-linkage-explicit.patch

# Various fixes for OCaml 5
Patch3:         https://gitlab.com/gerdstolpmann/lib-ocamlnet3/-/merge_requests/24.patch

# More OCaml 5 changes missed by patch 3
Patch4:         %{name}-ocaml5.patch

BuildRequires:  make
BuildRequires:  ocaml >= 4.07.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  ocaml-labltk-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  gnutls-devel
BuildRequires:  krb5-devel
BuildRequires:  ncurses-devel
BuildRequires:  tcl-devel

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings


%description
Ocamlnet is an ongoing effort to collect modules, classes and
functions that are useful to implement network protocols. Since
version 2.2, Ocamlnet incorporates the Equeue, RPC, and Netclient
libraries, so it is now really a big player.

In detail, the following features are available:

 * netstring is about processing strings that occur in network
   contexts. Features: MIME encoding/decoding, Date/time parsing,
   Character encoding conversion, HTML parsing and printing, URL
   parsing and printing, OO-representation of channels, and a lot
   more.

 * netcgi2 focuses on portable web applications.

 * rpc implements ONCRPC (alias SunRPC), the remote procedure call
   technology behind NFS and other Unix services.

 * netplex is a generic server framework. It can be used to build
   stand-alone server programs from individual components like those
   from netcgi2, nethttpd, and rpc.

 * netclient implements clients for HTTP (version 1.1, of course), FTP
   (currently partially), and Telnet.

 * equeue is an event queue used for many protocol implementations. It
   makes it possible to run several clients and/or servers in parallel
   without having to use multi-threading or multi-processing.

 * shell is about calling external commands like a Unix shell does.

 * netshm provides shared memory for IPC purposes.

 * netsys contains bindings for system functions missing in core OCaml.

 * netsmtp and netpop are client implementations of the SMTP and POP3
   protocols.

 * Bindings for GnuTLS and GSSAPI (TLS/HTTPS support).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-lablgtk-devel%{?_isa}
Requires:       ocaml-pcre-devel%{?_isa}
Requires:       ocaml-zip-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package        nethttpd
Summary:        Ocamlnet HTTP daemon
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    nethttpd
Nethttpd is a web server component (HTTP server implementation). It
can be used for web applications without using an extra web server, or
for serving web services.


%package        nethttpd-devel
Summary:        Development files for %{name}-nethttpd
License:        GPL-2.0-or-later
Requires:       %{name}-nethttpd%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}


%description    nethttpd-devel
The %{name}-nethttpd-devel package contains libraries and signature
files for developing applications that use %{name}-nethttpd.


%prep
%autosetup -N -n ocamlnet-%{version}
%autopatch -M 0 -p1
%ifarch %{ocaml_native_compiler}
%patch -P 1 -p2
%endif
%autopatch -m 2 -p2

# Fix the version number
# See https://gitlab.com/gerdstolpmann/lib-ocamlnet3/-/merge_requests/19
sed -i 's/^\(version=\).*/\1"%{version}"/' configure

# cmxs detection broken with OCaml 5.2
%ifarch %{ocaml_native_compiler}
sed -i 's,ocamlopt -shared -o \.dummy\.cmxs >/dev/null 2>/dev/null,true,' configure
%endif

# safe-string detection broken with OCaml 5.2
sed -i 's,ocamlc -safe-string >/dev/null 2>/dev/null,true,' configure

# opaque detection broken with OCaml 5.2
sed -i 's,ocamlc -opaque >/dev/null 2>/dev/null,true,' configure


%build
# Parallel builds don't work:
unset MAKEFLAGS

./configure \
  -bindir %{_bindir} \
  -datadir %{_datadir}/%{name} \
  -disable-apache \
  -enable-pcre \
  -enable-gtk2 \
  -enable-gnutls \
  -enable-gssapi \
  -enable-nethttpd \
  -enable-tcl \
  -enable-zip

%ifarch %{ocaml_native_compiler}
# This is a hack caused by the ocamlrpcgen patch.  Because "make all"
# no longer builds ocamlrpcgen (it is now built by "make opt") but
# some other parts of the build depend on this program, we have to run
# make opt first and ignore the result.  Hopefully we'll get a better
# result when upstream integrate the patch.  RWMJ 2021-01.
make opt ||:
%endif

make all

%ifarch %{ocaml_native_compiler}
make opt
%endif

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install

# rpc-generator/dummy.mli is empty and according to Gerd Stolpmann can
# be deleted safely.  This avoids an rpmlint warning.
rm -f $RPM_BUILD_ROOT%{_libdir}/ocaml/rpc-generator/dummy.mli

%files
%doc ChangeLog RELNOTES
%{_libdir}/ocaml/equeue
%{_libdir}/ocaml/equeue-gtk2
%{_libdir}/ocaml/equeue-tcl
%{_libdir}/ocaml/netcamlbox
%{_libdir}/ocaml/netcgi2
%{_libdir}/ocaml/netcgi2-plex
%{_libdir}/ocaml/netclient
%{_libdir}/ocaml/netgss-system
%{_libdir}/ocaml/netmulticore
%{_libdir}/ocaml/netplex
%{_libdir}/ocaml/netshm
%{_libdir}/ocaml/netstring
%{_libdir}/ocaml/netstring-pcre
%{_libdir}/ocaml/netsys
%{_libdir}/ocaml/nettls-gnutls
%{_libdir}/ocaml/netunidata
%{_libdir}/ocaml/netzip
%{_libdir}/ocaml/rpc
%{_libdir}/ocaml/rpc-auth-local
%{_libdir}/ocaml/rpc-generator
%{_libdir}/ocaml/shell
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%exclude %{_libdir}/ocaml/*/*.o
%endif
%exclude %{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner
%{_datadir}/%{name}/
%{_bindir}/netplex-admin
%{_bindir}/ocamlrpcgen


%files devel
%doc ChangeLog RELNOTES
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.o
%endif
%{_libdir}/ocaml/*/*.mli


%files nethttpd
%doc ChangeLog RELNOTES
%{_libdir}/ocaml/nethttpd
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%endif
%exclude %{_libdir}/ocaml/*/*.mli


%files nethttpd-devel
%doc ChangeLog RELNOTES
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.mli


%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 4.1.9-23
- OCaml 5.3.0 rebuild for Fedora 42
- Update __ocaml_requires_opts for OCaml 5.3.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-21
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-20
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 4.1.9-19
- Add patches for better OCaml 5.x compatibility
- The netcamlbox and netmulticore modules are built again

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-17
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-16
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-15
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-13
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 4.1.9-12
- OCaml 5.0.0 rebuild
- Convert License tag to SPDX
- Neither netcamlbox nor netmulticore can be built

* Thu Apr 27 2023 Florian Weimer <fweimer@redhat.com> - 4.1.9-11
- Port non-autoconf configure script to C99

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-10
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-7
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-6
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 4.1.9-4
- Rebuild for ocaml-lablgtk 2.18.12, ocaml-pcre 7.5.0 and ocaml-zip 1.11
- Drop prelinking conf file now that prelink is gone from Fedora

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1.9-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 4.1.9-1
- New upstream version 4.1.9

* Mon Mar  1 11:02:44 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1.8-4
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1.8-2
- Build ocamlrpcgen as native code.
- Enable stripping.
- Enable LTO (RHBZ#1915570).

* Wed Jan 13 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1.8-1
- New upstream version 4.1.8.
- Disable LTO (RHBZ#1915570).

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-18
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-17
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-15
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-14
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-13
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-12
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-11
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-9
- OCaml 4.10.0+beta1 rebuild.

* Fri Nov 08 2019 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-8
- Bump and rebuild (RHBZ#1770380).

* Sat Jul 27 2019 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-7
- Remove camlp4 dependency.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-3
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-2
- OCaml 4.07.0-rc1 rebuild.

* Tue May 15 2018 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-1
- New upstream version 4.1.6.
- Remove upstream patch.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.5-1
- New upstream version 4.1.5.

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.4-1
- New upstream version 4.1.4.

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-2
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-1
- New upstream version 4.1.3.
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.2-7
- Bump release and rebuild.

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.2-6
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.2-5
- Bump release and rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.2-4
- Bump release and rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 4.1.2-3
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 4.1.2-1
- New upstream version 4.1.2.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.4-3
- OCaml 4.02.3 rebuild.

* Mon Jul 27 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.4-2
- Remove ExcludeArch since bytecode build should now work.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.4-1
- New upstream version 4.0.4.
- Remove ugly hack for gnutls, since it is fixed properly upstream.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.3-4
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.3-3
- Bump release and rebuild.
- Add a hack to make it compile with latest gnutls 3.4.2.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.3-2
- ocaml-4.02.2 rebuild.

* Fri May 15 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.3-1
- Upgrade to 4.0.3, which also fixes gnutls 3.4 compilation problems.

* Wed May 13 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-4
- Bump and rebuild again for gnutls/nettle soname change.

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.1-3
- Rebuilt for nettle soname bump

* Wed Feb 18 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-2
- Enable more features, readding features disabled in the previous commit.
- Enable PCRE.
- Enable GnuTLS.
- Enable GSSAPI.
- Re-enable Nethttpd.
- Re-add documentation for Netsmtp and Netpop (modules renamed).
- Enable camlzip.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 4.0.1-1
- New upstream version 4.0.1.
- ocaml-4.02.1 rebuild.
- Disable SSL (removed from upstream, apparently?)
- Remove POP and SMTP (removed from upstream?)
- Add netunidata.
- Remove patches which are no longer needed / upstream.

* Mon Nov 03 2014 Richard W.M. Jones <rjones@redhat.com> - 3.7.4-10
- Bump and rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 3.7.4-9
- ocaml-4.02.0 final rebuild.
- Fix for int(32|64) -> int(32|64)_t in latest OCaml upstream.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 3.7.4-7
- Fix for broken configure tests.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 3.7.4-6
- Bump release and rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 3.7.4-5
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 3.7.4-3
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Wed Jul 23 2014 Richard W.M. Jones <rjones@redhat.com> - 3.7.4-2
- New upstream version 3.7.4.
- OCaml 4.02.0 beta rebuild.
- Some spec file modernization.
- Add BR tcl-devel.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 02 2013 Richard W.M. Jones <rjones@redhat.com> - 3.7.3-4
- Rebuild for ocaml-lablgtk 2.18.

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 3.7.3-3
- Unfortunately we have to re-add the anti-stripping code back.  See
  comment at top of spec file.
- Disable debuginfo for the same reason.

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 3.7.3-1
- New upstream version 3.7.3.
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Do not strip binaries, remove anti-prelink protection.
- Missing BR ncurses-devel.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Richard W.M. Jones <rjones@redhat.com> - 3.5.1-4
- Rebuild for OCaml 4.00.1.

* Sat Jul 28 2012 Richard W.M. Jones <rjones@redhat.com> - 3.5.1-3
- Rebuild for OCaml 4.00.0 official.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 3.5.1-1
- New upstream version 3.5.1.
- Rebuild for OCaml 4.00.0, plus small patch.
- Move configure into build (not prep).

* Sat Apr 28 2012 Richard W.M. Jones <rjones@redhat.com> - 3.4.1-3
- Bump and rebuild against new OCaml compiler in ARM.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 3.4.1-2
- Rebuild against PCRE 8.30

* Fri Jan  6 2012 Richard W.M. Jones <rjones@redhat.com> - 3.4.1-1
- New upstream version 3.4.1.
- Rebuild for OCaml 3.12.1.

* Mon Sep 19 2011 Richard W.M. Jones <rjones@redhat.com> - 3.4-1
- Move to new upstream 3.4 version.  Note this is not compatible with
  ocamlnet 2.x.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb  6 2011 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-23
- Rebuild against rpm-4.9.0-0.beta1.6.fc15.  See discussion:
  http://lists.fedoraproject.org/pipermail/devel/2011-February/148398.html

* Sat Feb  5 2011 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-22
- Bump and rebuild because of broken deps on ocaml-lablgtk.

* Wed Jan 05 2011 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-21
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).
- Missing BR ocaml-labltk-devel.

* Tue Jan  5 2010 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-19
- {gtk2,openssl,pcre,tcl}-devel BRs have now been pushed down to the
  corresponding ocaml-X-devel packages, so we don't need those here
  any more.

* Tue Jan  5 2010 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-18
- Use new dependency generator in upstream RPM 4.8.
- Add BR gtk2-devel.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-16
- Rebuild for OCaml 3.11.2.

* Tue Sep 29 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-15
- Force rebuild against newer lablgtk.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-13
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  7 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-11
- Rebuild against updated lablgtk.

* Wed Jan 21 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-10
- Fix prelink configuration file.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-9
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-8
- Rebuild for OCaml 3.11.0

* Tue Sep  2 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-7
- Prevent RPM & prelink from stripping bytecode.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-6
- Rebuild for OCaml 3.10.2

* Mon Apr 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-5
- New upstream URL.

* Mon Mar  3 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-4
- Do not strip binaries (bz 435559).

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-3
- Rebuild for ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-2
- Rebuild for OCaml 3.10.1.

* Wed Nov  7 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.9-1
- New upstream release 2.2.9.
- A more bletcherous, but more working, patch to fix the camlp4
  missing path bug.  Hopefully this is very temporary.
- Fixes for mock build under F8:
  + BR tcl-devel

* Thu Sep 13 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.8.1-1
- New upstream version 2.2.8.1.
- License of the base package is in fact BSD.  Clarified also that
  the license of nethttpd is GPLv2+.
- Removed the camlp4 paths patch as it doesn't seem to be necessary.
- Add BRs for camlp4, ocaml-pcre-devel, ocaml-lablgtk-devel,
  openssl-devel
- Removed explicit requires, they're not needed.
- Strip binaries and libraries.
- Ignore Parsetree module in deps.

* Thu Aug  2 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.7-6
- ExcludeArch ppc64
- BR ocaml-pcre-devel
- Fix for camlp4 missing path

* Mon Jun 11 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.7-5
- Updated to latest packaging guidelines.

* Tue May 29 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.7-4
- Added support for ocaml-lablgtk2

* Tue May 29 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.7-3
- Remove empty file rpc-generator/dummy.mli.

* Sat May 26 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.7-2
- Added support for SSL.

* Sat May 26 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.7-1
- Initial RPM.
