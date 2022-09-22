Name:           newlisp
Version:        10.7.5
Release:        6%{?dist}
Summary:        Lisp-like general purpose scripting

License:        GPLv3+
URL:            http://www.newlisp.org
Source0:        http://www.newlisp.org/downloads/%{name}-%{version}.tgz
Patch0:         %{name}-0000-Support-64bit.patch
Patch1:         %{name}-0003-Don-t-strip-the-resulting-binary.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  readline-devel  
BuildRequires:  libffi-devel     
# This is required for the modules for newLisp
Requires:       openssl-devel%{?_isa} gmp-devel%{_isa} gsl-devel%{_isa}
Requires:       mariadb-connector-c-devel%{?_isa} libpq-devel
Requires:       sqlite-devel%{?_isa} zlib-devel%{?_isa}

%description
Lisp-like general purpose scripting language. %{name} is well suited for 
applications in AI, web search. It also can be used for embedded systems
applications.

%prep
%setup -q
%patch0 -p0 -b .64bit-support
%patch1 -p1 -b .stop-binary-strip

# Remove it from the general build and specify it on supported platforms below
sed -i.m32 's/\-m32 //' makefile_linux
sed -i.m64 's/\-m64 //' makefile_linuxLP64
sed -i.m32 's/\-m32 //' makefile_linux_utf8
sed -i.m64 's/\-m64 //' makefile_linuxLP64_utf8

%build
%configure

%if "%{_lib}" == "lib64"
CFLAGS="%{optflags} -c -DREADLINE -DSUPPORT_UTF8 -DLINUX -DNEWLISP64" \
        make -f makefile_linuxLP64_utf8 %{?_smp_mflags}
%else
CFLAGS="%{optflags} -c -DREADLINE -DSUPPORT_UTF8 -DLINUX" \
        make -f makefile_linux_utf8 %{?_smp_mflags}
%endif

%install
make install_home HOME=%{buildroot}/usr/


%files
%doc %{_datadir}/doc/*
%{_bindir}/%{name}
%{_bindir}/newlispdoc
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/util/%{name}.vim
%{_datadir}/%{name}/modules/*
%attr(0755,-,-) %{_datadir}/%{name}/util/syntax.cgi


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 19 2020 Filipe Rosset <rosset.filipe@gmail.com> - 10.7.5-1
- Update to 10.7.5 fixes rhbz#1709040 and rhbz#1494229

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 10.7.1-11
- Fix string quoting for rpm >= 4.16

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10.7.1-8
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10.7.1-5
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 22 2017 Filipe Rosset <rosset.filipe@gmail.com> - 10.7.1-1
- Rebuilt for new upstream release 10.7.1 fixes rhbz #1184803

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 10.6.0-6
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Nathan Owens <ndowens at fedoraproject.org> 10.6.0-1
- Updated to latest stable release
- Updated 64Bit patch
  -- Most of the patch is upstream, except one part.
 
* Mon Mar 31 2014 Nathan Owens <ndowens at fedoraproject.org> 10.5.4-3
- Added required fields needed by %%{name} modules

* Sun Mar 30 2014 Nathan Owens <ndowens at fedoraproject.org> 10.5.4-2
- Minor cosmetic update

* Sun Mar 30 2014 Nathan Owens <ndowens at fedoraproject.org> 10.5.4-1
- Updated to newest version (bug #857702, #1010619)
- Added newlisp-0001-Support-64bit.patch to fix modules not found  
   -- Added required deps for modules
     ---Fixes broken modules (bug #1063097)
- Removed CFLAGS-Override patch
- Removed a few no longer needed %%datadir lines
 
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 08 2012 Peter Robinson <pbrobinson@fedoraproject.org> 10.4.3-6
- Fix utf8 build on non x86 arches

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Nathan Owens <ndowens[at]fedoraproject.org> 10.4.3-4
- Left out the 8 in utf8 for 32-bit makefile

* Sat Jun 02 2012 Nathan Owens <ndowens[at]fedoraproject.org> 10.4.3-3
- Re-attempt to fix missing rpm_opt_flags

* Tue May 29 2012 Dan Horák <dan[at]danny.cz> 10.4.3-2
- allow build on all arches

* Fri May 11 2012 Nathan Owe <ndowens at fedoraproject.org> 10.4.3-1
- Removed a file in %%files that doesn't exist anymore
- Updated to latest version

* Fri May 04 2012 Nathan Owe <ndowens at fedoraproject.org> 10.4.2-1
- Fixes missing RPM_OPT_FLAGS (bug #815529)
- Updated version (bug #818145)

* Tue Apr 17 2012 Nathan Owe <ndowens at fedoraproject.org> 10.4.0-4
- Rebuild with updated Allow-override-CFLAGS patch

* Tue Apr 17 2012 Nathan Owe <ndowens at fedoraproject.org> 10.4.0-3
- Fixed mixed-tabs-and-spaces warning

* Mon Apr 16 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 10.4.0-2
- Fix building from ARM

* Sat Apr 07 2012 Nathan Owe <ndowens at fedoraproject.org> 10.4.0-1
- Updated version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Nathan Owe <ndowens at fedoraproject dot org> 10.3.5-2
- Fixed %%files listing

* Tue Oct 11 2011 Nathan Owe <ndowens at fedoraproject dot org> 10.3.5-1
- Updated version

* Thu Sep 22 2011 Nathan Owe <ndowens at fedoraproject dot org> 10.3.3-3
- Re-added patches, didn't think they were no longer needed

* Thu Sep 22 2011 Nathan Owe <ndowens at fedoraproject dot org> 10.3.3-2
- Removed patches

* Thu Sep 22 2011 Nathan Owe <ndowens at fedoraproject dot org> 10.3.3-1
- Updated version
- Updated email address

* Sun Jul 24 2011 Nathan Owe <ndowens04 at yahoo.com> 10.3.2-3
- Updated License field to the correct license

* Sun Jul 24 2011 Nathan Owe <ndowens04 at yahoo.com> 10.3.2-2
- Added fixed Man page from SCM 

* Thu Jul 21 2011 Nathan Owe <ndowens04 at yahoo.com> 10.3.2-1
- Initial package
