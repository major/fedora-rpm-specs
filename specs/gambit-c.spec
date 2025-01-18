# Using -O2 on ppc64 triggers ICE with gcc < 4.6.4
# http://www.iro.umontreal.ca/~gambit/bugzilla/show_bug.cgi?id=155
# https://bugzilla.redhat.com/show_bug.cgi?id=808285
# Use --with ppc64opt2 when rebuilding to see if this is fixed
%bcond_with ppc64opt2

%if 0%{?el6}
%ifarch ppc64
%if ! %{with ppc64opt2}
%global disable_c_opt 1
%global optflags %(echo %{optflags} | sed 's/-O2 /-O1 /')
%endif
%endif # ppc64
%endif # el6

Name:           gambit-c
Version:        4.9.3
Release:        15%{?dist}
Summary:        Scheme programming system

# Automatically converted from old format: ASL 2.0 or LGPLv2 - review is highly recommended.
License:        Apache-2.0 OR LicenseRef-Callaway-LGPLv2
URL:            http://gambitscheme.org/
%global _dirname gambit-v%(echo %{version} | sed -e 's/\\./_/g')-devel
Source0:        http://www.iro.umontreal.ca/~gambit/download/gambit/v4.9/source/%{_dirname}.tgz
Source1:        gambit-init.el
Patch0:         gambc-v4_2_8-modtime.patch

BuildRequires:  gcc
BuildRequires:  emacs
BuildRequires: make
Requires:       gcc
Requires:       emacs-filesystem >= %{_emacs_version}


%description
Gambit-C includes a Scheme interpreter and a Scheme compiler which can
be used to build standalone executables.  Because the compiler
generates portable C code it is fairly easy to port to any platform
with a decent C compiler.

The Gambit-C system conforms to the R4RS, R5RS and IEEE Scheme
standards.  The full numeric tower is implemented, including: infinite
precision integers (bignums), rationals, inexact reals (floating point
numbers), and complex numbers.


%package        doc
Summary:        Documentation for %{name}

BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires(post):  info
Requires(preun): info
# switch to noarch
Obsoletes:      gambit-c-doc < %{version}-%{release}

%description    doc
Gambit-C includes a Scheme interpreter and a Scheme compiler which can
be used to build standalone executables.  Because the compiler
generates portable C code it is fairly easy to port to any platform
with a decent C compiler.

This package contains the Gambit-C user manual in HTML and PDF formats.


%prep
%autosetup -n %{_dirname} -p1
# Gambit tries to do a git update-index if a git repo is detected
rm -rf .git

# Permission fixes
chmod -x lib/*.{c,h}


%build
# disable expensive optimizations on specified platforms
# see INSTALL.txt
%ifarch s390 %{arm}
%global disable_gcc_opts 1
%endif

%if 0%{?rhel}
%if 0%{?rhel} <= 7
%global disable_gcc_opts 1
%endif
%endif

%configure --enable-single-host \
%if 0%{?disable_c_opt:1}
%else
           --enable-c-opt \
%endif
%if 0%{?disable_gcc_opts:1}
%else
           --enable-gcc-opts \
%endif
           --bindir=%{_libdir}/%{name}/bin \
           --libdir=%{_libdir}/%{name}

make %{?_smp_mflags}

# Compile emacs module
(cd misc && %{_emacs_bytecompile} gambit.el)


%check
# tests fail on s390x:
# https://bugzilla.redhat.com/show_bug.cgi?id=1714392
%ifnarch s390x
make check
%endif


%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for i in gsc gsi
do
  ln -sf ../%{_lib}/%{name}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done
cat > $RPM_BUILD_ROOT%{_bindir}/gsix <<EOF
#!/bin/sh
%{_libdir}/%{name}/bin/six $@
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/gsix

# Remove duplicate docs
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

# Emacs mode files
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
cp -p misc/gambit.elc $RPM_BUILD_ROOT%{_emacs_sitelispdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}

# Link static libs
(cd $RPM_BUILD_ROOT%{_libdir} && ln -s %{name}/*.a .)


%files
%license LGPL.txt LICENSE-2.0.txt
%doc README
%{_bindir}/*
%{_includedir}/*.h
%{_mandir}/man1/gsi.*
%{_libdir}/%{name}
%{_libdir}/*.a
%{_emacs_sitelispdir}/*.el
%{_emacs_sitelispdir}/*.elc
%{_emacs_sitestartdir}/gambit-init.el


%files doc
%doc doc/gambit.html doc/gambit.pdf
# don't package examples until makefiles are fixed
# examples
%{_infodir}/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 4.9.3-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.9.3-1
- Update to 4.9.3
- Move license files to /usr/share/licenses

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.8.8-1
- Update to 4.8.8
- Automatically calculate _dirname

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.8.7-1
- Update to 4.8.7

* Mon Jan  9 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.8.6-1
- Update to 4.8.6

* Sun Feb 28 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.8.4-2
- Re-enable ARM build with upstream cast fix

* Sun Feb 21 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.8.4-1
- Update to 4.8.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep  6 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.7.9-1
- Update to 4.7.9
- Update home page link
- Adjust to new Emacs packaging guidelines, no longer shipping separate packages
- Further reduce expensive optimizations on resource-limited arches

* Tue Jul 28 2015 Peter Robinson <pbrobinson@fedoraproject.org> 4.7.7-1
- Update to 4.7.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 4.7.5-1
- Update to 4.7.5

* Tue Nov 04 2014 Jakub Čajka <jcajka@redhat.com> - 4.7.3-2
- Fix build OOM on s390

* Thu Oct 30 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb  7 2014 Michel Salim <salimma@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Tue Nov 05 2013 Kyle McMartin <kyle@fedoraproject.org>
- Fix FTBFS because of dirname macro, use _dirname instead.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun  5 2012 Michel Salim <salimma@fedoraproject.org> - 4.6.6-1
- Update to 4.6.6

* Sat Mar 31 2012 Michel Salim <salimma@fedoraproject.org> - 4.6.5-2
- Reduce optimization level on ppc64 to work around gcc compilation error

* Thu Mar 29 2012 Michel Salim <salimma@fedoraproject.org> - 4.6.5-1
- Update to 4.6.5
- Drop termite subpackages, they have been disabled for many releases
- Disable ppc64 target for now; broken since 4.6.4

* Wed Feb 15 2012 Michel Salim <salimma@fedoraproject.org> - 4.6.4-1
- Update to 4.6.4

* Wed Feb  1 2012 Michel Salim <salimma@fedoraproject.org> - 4.6.3-1
- Update to 4.6.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 27 2011 Michel Salim <salimma@fedoraproject.org> - 4.6.1-1
- Update to 4.6.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 12 2010 Michel Salim <salimma@fedoraproject.org> - 4.6.0-2
- noarch -doc subpackage properly obsoletes older, arched variant

* Mon Jul 12 2010 Michel Salim <salimma@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0
- Bundle license text with independent Emacs subpackage

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Michel Salim <salimma@fedoraproject.org> - 4.3.2-2
- If termite packages are disabled, the corresponding gambit-c packages
  Provides: and Obsoletes: them

* Fri Dec 19 2008 Michel Salim <salimma@fedoraproject.org> - 4.3.2-1
- Update to 4.3.2

* Tue Oct 14 2008 Michel Salim <salimma@fedoraproject.org> - 4.2.9-1
- Update to 4.2.9
- Disable Termite for now; still broken
- When built on EL-5, depend directly on emacs binary rather than emacs(bin)

* Mon Jul 14 2008 Michel Salim <salimma@fedoraproject.org> - 4.2.8-6
- Put include files and libraries in standard paths

* Thu Jun 19 2008 Michel Salim <salimma@fedoraproject.org> - 4.2.8-5
- Package Termite as a module instead of bundling a custom Gambit-C with it

* Thu Jun 19 2008 Michel Salim <salimma@fedoraproject.org> - 4.2.8-4
- Permission fixes for Termite subpackage

* Wed Jun 18 2008 Michel Salim <salimma@fedoraproject.org> - 4.2.8-3
- Bundle Termite as a subpackage

* Sat Jun  7 2008 Michel Salim <salimma@fedoraproject.org> - 4.2.8-2
- Rename six symlink to avoid clash with existing six package

* Mon Jun  2 2008 Michel Salim <salimma@fedoraproject.org> - 4.2.8-1
- Update to 4.2.8
- Rename to gambit-c

* Fri Dec 28 2007 Gerard Milmeister <gemi@bluewin.ch> - 4.1.2-1
- new release 4.1.2

* Sat Apr 14 2007 Gerard Milmeister <gemi@bluewin.ch> - 4.0-1.b22
- new version 4.0b22

* Sun Oct 15 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.0-1.b20
- new version 4.0b20

* Sat Feb  4 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.0-1.b17
- new version 4.0b17

* Mon Nov  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.0-1.b15
- New Version 4.0b15

* Fri Aug 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.0-1.b14
- First Fedora release

