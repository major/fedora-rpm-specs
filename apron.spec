Name:           apron
Version:        0.9.14
Summary:        Numerical abstract domain library
Release:        7%{?dist}

# The entire package is LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
# except newpolka/mf_qsort.c and ppl/*, all of which are GPL-2.0-or-later.
# This means that libpolkaMPQ.so.*, libpolkaRll.so.*, and libap_ppl.so.* are
# GPL-2.0-or-later, and the other libraries are all LGPL-2.1-or-later WITH
# OCaml-LGPL-linking-exception.
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND GPL-2.0-or-later
URL:            https://antoinemine.github.io/Apron/doc/
VCS:            https://github.com/antoinemine/apron
Source0:        %{vcs}/archive/v%{version}/%{name}-%{version}.tar.gz
# This patch has not been sent upstream as it is GCC-specific.  Certain
# symbols are defined in both libpolkaMPQ and libpolkaRll, with different
# implementations.  This patch makes references to those symbols in
# libap_pkgrid be weak references, since that library can be combined with
# either of the 2 implementations.
Patch0:         %{name}-weak.patch
# Fix the OCaml build on bytecode-only architectures
Patch1:         %{name}-ocaml-bytecode.patch
# Update CSDP support for CSDP 6.2.0
Patch2:         %{name}-csdp.patch
# Since the jgmp library is not installed in a normal search path, add an rpath
# to the japron library so it can find jgmp
Patch3:         %{name}-japron-link.patch
# Fix a japron hasVar bug
# https://github.com/antoinemine/apron/issues/94
# https://github.com/antoinemine/apron/pull/95
Patch4:         %{name}-hasvar.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  csdp-devel
BuildRequires:  doxygen-latex
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  glpk-devel
%ifarch %{java_arches}
BuildRequires:  java-devel
BuildRequires:  javapackages-local
%endif
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ppl-devel
BuildRequires:  pplite-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-mlgmpidl-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  perl-interpreter
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(etoc.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(listofitems.sty)
BuildRequires:  tex(newunicodechar.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  texinfo-tex

%global sover %(cut -d. -f 1 <<< %{version})

# Do not Require symbols we do not Provide
%global __ocaml_requires_opts -i Coeff -i Dim -i Interval -i Lincons0 -i Linexpr0 -i Scalar -i Tcons0 -i Texpr0

# This can be removed when F40 reaches EOL
%ifnarch %{java_arches}
Obsoletes:      japron < 0.9.13-12
%endif

%description
The APRON library is dedicated to the static analysis of the numerical
variables of a program by Abstract Interpretation.  The aim of such an
analysis is to infer invariants about these variables, like 1<=x+y<=z,
which holds during any execution of the program.

The APRON library is intended to be a common interface to various
underlying libraries/abstract domains and to provide additional services
that can be implemented independently from the underlying
library/abstract domain.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glpk-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Provides:       bundled(js-jquery)

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n     ocaml-%{name}
Summary:        Ocaml interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}
Ocaml interface to the APRON library.

%package -n     ocaml-%{name}-devel
Summary:        Development files for the Ocaml interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}-devel
Development files for the Ocaml interface to the APRON library.

%ifarch %{java_arches}
%package -n     japron
Summary:        Java interface to APRON
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       javapackages-filesystem

%description -n japron
Java interface to the APRON library.
%endif

%prep
%autosetup -N -n %{name}-%{version}
%patch -P0 -p0
%ifnarch %{ocaml_native_compiler}
%patch -P1 -p0
%endif
%autopatch -m2 -p0

# Fix library path for 64-bit installs
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's,\${apron_prefix}/lib,&64,' configure
  sed -i 's,/lib,&64,' vars.mk
fi

# Fix encodings
iconv -f iso8859-1 -t utf-8 Changes > Changes.utf8
touch -r Changes Changes.utf8
mv -f Changes.utf8 Changes

# Preserve timestamps when copying
sed -i 's/^\([[:blank:]]*cp[[:blank:]]\)/\1-p /' Makefile */Makefile

# Build with debuginfo
sed -i 's/^OCAMLOPTFLAGS =/& -g/' configure
sed -i "s|\$(OCAMLMKLIB) -L.*|& -g|" vars.mk

# Give the C++ library an soname
sed -i '/shared/s/\$(CXX)/$(CXX_APRON_DYLIB)/' apronxx/Makefile

# For reproducibility, omit timestamps from generated documentation
sed -i '/HTML_TIMESTAMP/s/YES/NO/' apronxx/doc/Doxyfile

%build
# This is NOT an autoconf-generated script.  Do not use %%configure
export CPPFLAGS='-D_GNU_SOURCE -I%{_includedir}/csdp'
export CFLAGS='%{build_cflags} -fsigned-char'
export CXXFLAGS='%{build_cxxflags} -fsigned-char'
export CSDP_PATH=%{_prefix}
%ifarch %{java_arches}
export JAVA_HOME='%{_jvmdir}/java'
export JAVA_TOOL_OPTIONS='-Dfile.encoding=UTF8'
./configure -prefix %{_prefix} -pplite-prefix %{_prefix} -no-strip -java-prefix %{_jvmdir}/java
%else
./configure -prefix %{_prefix} -pplite-prefix %{_prefix} -no-strip
%endif

# Put back a flag that the configure script strips out
sed -i 's/-Wall/& -Werror=format-security/' Makefile.config

# Generate dependency lists
touch apron/depend
make -C apron depend

# Parallel builds fail intermittently
make
make doc

# for some reason this is no longer built in `make doc`
make -C mlapronidl mlapronidl.pdf

%install
# Install the ocaml bits into the buildroot
sed -i 's, install ,&-destdir %{buildroot}%{ocamldir} -ldconf ignore ,' \
    Makefile

# Install
mkdir -p %{buildroot}%{ocamldir}/stublibs
mkdir -p %{buildroot}%{_jnidir}
%ifarch %{java_arches}
make install INSTALL="install -p" APRON_PREFIX=%{buildroot}%{_prefix} \
  JAVA_PREFIX=%{buildroot}%{_jnidir}

# Move the JNI shared objects
mv %{buildroot}%{_libdir}/libj*.so %{buildroot}%{_jnidir}
%else
make install INSTALL="install -p" APRON_PREFIX=%{buildroot}%{_prefix}
%endif

# We don't really want the test binaries
rm -fr %{buildroot}%{_bindir}

# Move the header files into a subdirectory
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/apronxx \
   %{buildroot}%{_includedir}/oct %{buildroot}%{_includedir}/%{name}

# Remove extraneous executable bits
find %{buildroot}%{_includedir} \( -name \*.h -o -name \*.hh \) \
     -perm /0111 -execdir chmod a-x {} +

# Erase the static libraries
rm -f %{buildroot}%{_libdir}/*.a

# Fix up the shared library names
pushd %{buildroot}%{_libdir}
for f in lib*.so; do
  mv $f $f.%{version}
  ln -s $f.%{sover} $f
  ln -s $f.%{version} $f.%{sover}
done
popd

# Don't have two sets of documentation both named html
mkdir doc
mv apron/html doc/apron
mv apronxx/doc/html doc/apronxx

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make -C test APRON_INCLUDE=%{buildroot}%{_includedir}/%{name} \
  APRON_LIB=%{buildroot}%{ocamldir}/%{name} \
  CAMLIDL_PREFIX=%{buildroot}%{_libdir}
test/ctest1

%files
%doc AUTHORS Changes README.md apron/apron.pdf
%license COPYING
%{_libdir}/lib*.so.0
%{_libdir}/lib*.so.0.*

%files devel
%doc doc/apron doc/apronxx
%{_libdir}/lib*.so
%{_includedir}/%{name}/
%{_includedir}/avo/
%{_includedir}/fpp/

%files -n ocaml-%{name}
%doc mlapronidl/mlapronidl.pdf
%dir %{ocamldir}/%{name}/
%{ocamldir}/%{name}/META
%{ocamldir}/%{name}/*.cma
%{ocamldir}/%{name}/*.cmi
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}/*.cmxs
%endif
%{ocamldir}/stublibs/dll*

%files -n ocaml-%{name}-devel
%doc mlapronidl/html/*
%{ocamldir}/%{name}/*.a
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}/*.cmxa
%{ocamldir}/%{name}/*.cmx
%endif
%{ocamldir}/%{name}/*.h
%{ocamldir}/%{name}/*.idl
%{ocamldir}/%{name}/*.mli

%ifarch %{java_arches}
%files -n japron
%doc japron/README
%license japron/COPYING
%{_jnidir}/*.jar
%{_jnidir}/*.so
%endif

%changelog
* Wed Mar 13 2024 Jerry James <loganjerry@gmail.com> - 0.9.14-7
- Rebuild for flint 3.1.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.9.14-4
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.9.14-3
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.9.14-2
- OCaml 5.1 rebuild for Fedora 40

* Wed Oct  4 2023 Jerry James <loganjerry@gmail.com> - 0.9.14-1
- Add upstream patch for a japron hasVar bug

* Fri Sep 22 2023 Jerry James <loganjerry@gmail.com> - 0.9.14-1
- Version 0.9.14
- Add patch to fix japron linkage
- Omit timestamps from generated documentation

* Sat Aug  5 2023 Jerry James <loganjerry@gmail.com> - 0.9.14-0.6.beta.2
- Fix failure to install (rhbz#2229356)

* Thu Aug  3 2023 Jerry James <loganjerry@gmail.com> - 0.9.14-0.5.beta.2
- Enable pplite support

* Thu Jul 27 2023 Jerry James <loganjerry@gmail.com> - 0.9.14-0.4.beta.2
- Update to 0.9.14-beta2
- Enable csdp support

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.9.14-0.2.beta1
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.9.14-0.1.beta1
- Update to 0.9.14-beta1 for OCaml 5.0 support
- Drop upstreamed mpfr and custom-operations patches
- Enable glpk support
- Add patch to fix builds on bytecode-only architectures

* Thu Mar 23 2023 Jerry James <loganjerry@gmail.com> - 0.9.13-17
- Fix reinsertion of -Werror=format-security (bz 2181282)

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.9.13-16
- Rebuild OCaml packages for F38

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec  6 2022 Jerry James <loganjerry@gmail.com> - 0.9.13-14
- Work around build failure with make 4.4 (rhbz#2150171)

* Thu Aug 11 2022 Jerry James <loganjerry@gmail.com> - 0.9.13-13
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 0.9.13-12
- Do not build japron on i686 (rhbz#2104018)
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.9.13-11
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 0.9.13-10
- Add -custom-operations patch to silence warnings
- Trim Requires
- Build native OCaml objects with debuginfo

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.9.13-10
- Rebuilt for java-17-openjdk as system jdk

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.9.13-9
- OCaml 4.13.1 rebuild to remove package notes

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 0.9.13-7
- Rebuild for ocaml-mlgmpidl 1.2.14

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.9.13-6
- OCaml 4.13.1 build

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 16:57:58 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.9.13-4
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Jerry James <loganjerry@gmail.com> - 0.9.13-2
- Fix install location of OCaml stublibs

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 0.9.13-1
- Version 0.9.13
- Drop upstreamed -texinfo patch

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-10
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-9
- OCaml 4.11.0 rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-6
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-5
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-4
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-3
- OCaml 4.10.0 final.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.9.12-1
- New upstream release 0.9.12

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-33.1104.svn20180624
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-32.1104.svn20180624
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-31.1104.svn20180624
- Bump release and rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-30.1104.svn20180624
- OCaml 4.09.0 (final) rebuild.

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 0.9.11-29.1104.svn20180624
- Add -mpfr4 patch and rebuild for mpfr 4

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-28.1104.svn20180624
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-27.1104.svn20180624
- OCaml 4.08.1 (rc2) rebuild.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-26.1104.svn20180624
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-25.1104.svn20180624
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-24.1104.svn20180624
- OCaml 4.08.0 (beta 3) rebuild.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-23.1104.svn20180624
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-22.1104.svn20180624
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-21.1104.svn20180624
- OCaml 4.07.0 (final) rebuild.

* Sat Jul  7 2018 Jerry James <loganjerry@gmail.com> - 0.9.11-20.1104.svn20180624
- Update to latest subversion commit

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-19.1097.svn20160801
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-18.1097.svn20160801
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-17.1097.svn20160801
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-16.1097.svn20160801
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-15.1097.svn20160801
- OCaml 4.07.0-rc1 rebuild.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-14.1097.svn20160801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec  4 2017 Jerry James <loganjerry@gmail.com> - 0.9.11-13.1097.svn20160801
- Rebuild for mlgmpidl 1.2.6-1

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-12.1097.svn20160801
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-11.1097.svn20160801
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-10.1097.svn20160801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-9.1097.svn20160801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-8.1097.svn20160801
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-7.1097.svn20160801
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 0.9.11-6.1097.svn20160801
- Rebuild for mlgmpidl

* Fri Mar  3 2017 Jerry James <loganjerry@gmail.com> - 0.9.11-5.1097.svn20160801
- Update to latest subversion commit and rebuild for ppl 1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-4.1096.svn20160531
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 0.9.11-3.1096.svn20160531
- rebuild for s390x codegen bug

* Sun Nov 06 2016 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-2.1096.svn20160531
- Rebuild for OCaml 4.04.0.

* Sat Jul 16 2016 Jerry James <loganjerry@gmail.com> - 0.9.11-1.1096.svn20160531
- Update to latest subversion commit

* Sun Mar 06 2016 Than Ngo <than@redhat.com> - 0.9.10-36.svn20160125
- remove wWorkaround bz 1305739; it's fixed in lates doxygen

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 0.9.10-35.1091.svn20160125
- Some ocaml projects need the debug libraries; add them back in

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 0.9.10-34.1091.svn20160125
- Update to latest subversion commit
- Add japron subpackage with the Java interface
- Add %%check script
- Drop upstreamed -format-security, -mlgmpidl12, -test, and -ppl1 patches
- Add -texinfo patch to fix documentation build failure

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-32
- Bump release and rebuild.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-31
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-30
- Fix bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-29
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-28
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.10-26
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-25
- ocaml-4.02.1 rebuild.

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 0.9.10-24
- Use license macro

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-23
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-22
- ocaml-4.02.0+rc1 rebuild.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-20
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Jerry James <loganjerry@gmail.com> - 0.9.10-19
- OCaml 4.02.0 beta rebuild

* Fri Jun 27 2014 Jerry James <loganjerry@gmail.com> - 0.9.10-18
- Build with -fsigned-char to fix FTBFS on aarch64
- Use a better test for installing files into 64-bit libdir

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Jerry James <loganjerry@gmail.com> - 0.9.10-16
- Rebuild for ppl 1.1

* Fri Apr 18 2014 Jerry James <loganjerry@gmail.com> - 0.9.10-15
- Ensure GNU extensions are enabled to fix build failure

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-15
- Remove ocaml_arches macro (RHBZ#1087794).

* Wed Nov 20 2013 Jerry James <loganjerry@gmail.com> - 0.9.10-14
- Add -format-security patch

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-13
- Rebuild for OCaml 4.01.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Jerry James <loganjerry@gmail.com> - 0.9.10-11
- Add -ppl1 patch to adapt to PPL 1.0 + GMP 5.1.0
- Update -mlgmpidl12 patch to fix more problems

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Tom Callaway <spot@fedoraproject.org> - 0.9.10-10
- rebuild for ppl

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 0.9.10-9
- Rebuild for OCaml 4.00.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun  9 2012 Jerry James <loganjerry@gmail.com> - 0.9.10-7
- Rebuild for OCaml 4.00.0

* Wed May  9 2012 Jerry James <loganjerry@gmail.com> - 0.9.10-6
- Rebuild for new ocaml-mlgmpidl

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.9.10-5
- Rebuild for GCC 4.7 and Ocaml 3.12.1

* Tue Nov  8 2011 Jerry James <loganjerry@gmail.com> - 0.9.10-4
- -devel also needs ocaml-camlidl-devel
- Pass --as-needed to the linker to fix unused shared library dependencies

* Fri Nov  4 2011 Jerry James <loganjerry@gmail.com> - 0.9.10-3
- Comment on license situation
- Drop debug libraries altogether

* Wed Aug 24 2011 Jerry James <loganjerry@gmail.com> - 0.9.10-2
- Correct license
- Build C and C++ interfaces even when the ocaml interface cannot be built
- Move debug libraries to separate packages

* Fri Jul  8 2011 Jerry James <loganjerry@gmail.com> - 0.9.10-1
- Initial RPM
