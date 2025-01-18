Summary:   Password cracker
Name:      crack
Version:   5.0a
Release:   48%{?dist}
# Automatically converted from old format: Artistic clarified - review is highly recommended.
License:   ClArtistic
Source:    ftp://ftp.cerias.purdue.edu/pub/tools/unix/pwdutils/crack/%{name}5.0.tar.gz
Patch0:    %{name}-chris.patch
Patch1:    %{name}-FHS.patch
URL:       https://dropsafe.crypticide.com/alecm/software/crack/c50-faq.html
BuildRequires: words, gawk, gcc
BuildRequires: make

%description
Crack is a password guessing program that is designed to quickly locate
insecurities in Unix (or other) password files by scanning the contents of a
password file, looking for users who have misguidedly chosen a weak login
password.

This package creates a group named "crack" and the Crack program puts all
its results in the /var/lib/crack/run directory, which belongs to that group.
Only users in the crack group can use this package.


%prep
%setup -q -n c50a
# Make sure we do not use libdes
rm -rf src/libdes
# select proper crypt routine and related checks
rm -f src/util/elcid.c
ln src/util/elcid.c,bsd src/util/elcid.c
mkdir run bin
# Try not to pollute bin namespace
sed -i -e 's/Reporter/CrackReporter/g' doc/gui.txt manual.html manual.txt
%patch -P0 -p1 -b .chris
sed -i 's|/usr/dict/|/usr/share/dict/|g' conf/dictgrps.conf
# Alter script to use FHS layout
%patch -P1 -p1 -b .FHS

%build
%global build_type_safety_c 0
C5FLAGS="-D_XOPEN_SOURCE -DUSE_STRING_H -DUSE_STDLIB_H -DUSE_SIGNAL_H -DUSE_SYS_TYPES_H -DUSE_UNISTD_H -DUSE_PWD_H"
make XDIR=../../bin XCC=gcc XCFLAGS="$RPM_OPT_FLAGS $C5FLAGS" XLIBS=-lcrypt utils
CRACK_HOME=`pwd` CRACK_BIN_HOME=`pwd` CRACK_STATE_DIR=`pwd` ./Crack -makedict


%install
rm -rf $RPM_BUILD_ROOT
rm -f bin/libc5.a bin/stdlib-cracker
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}
cp -a bin $RPM_BUILD_ROOT%{_libexecdir}/%{name} 
cp -a conf dict scripts $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a run $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}
install -p -m0755 Crack $RPM_BUILD_ROOT%{_bindir}/Crack
install -p -m0755 Reporter $RPM_BUILD_ROOT%{_bindir}/CrackReporter



%pre
if [ $1 -eq 1 ]; then
    groupadd -r crack >/dev/null 2>&1 || :
fi


%files
%doc LICENCE manual.* doc
%attr(00750, root, crack) %{_bindir}/Crack*
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/
%dir %{_sharedstatedir}/%{name}/
%attr(02770, root, crack) %dir %{_sharedstatedir}/%{name}/run/
%attr(02770, root, crack) %dir %{_sharedstatedir}/%{name}/run/dict/
%attr(00640, root, crack) %{_sharedstatedir}/%{name}/run/dict/*
%attr(00640, root, crack) %{_sharedstatedir}/%{name}/run/dict/.dictmade


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0a-47
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 5.0a-43
- Set build_type_safety_c to 0 (#2155212)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Florian Weimer <fweimer@redhat.com> - 5.0a-40
- Build in C89 mode due to many C99 incompatibilities (#2155212)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Christian Iseli <Christian.Iseli@unil.ch> - 5.0a-32
- Fix URL (#1699019)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 5.0a-30
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Jul 23 2018 Christian Iseli <Christian.Iseli@unil.ch> - 5.0a-29
- fix FTBFS due to missing BuildRequires gcc (bz 1603712)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 5.0a-27
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0a-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 31 2010 Christian Iseli <Christian.Iseli@licr.org> - 5.0a-14
- fix description wrt FHS cleanup patch

* Wed Mar 31 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0a-13
- cleanup FHS patch and spec to properly use /var/lib/crack/run

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Christian Iseli <Christian.Iseli@licr.org> - 5.0a-10
- Rebuild for F-11

* Tue Nov 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0a-9
- rework spec file so that it meets FHS

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.0a-8
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Christian Iseli <Christian.Iseli@licr.org> 5.0a-7
- Mark License tag as "Artistic clarified"

* Wed Aug 22 2007 Christian Iseli <Christian.Iseli@licr.org> 5.0a-6
- add BR: gawk
- Rebuild for BuildID

* Thu May 10 2007 Christian Iseli <Christian.Iseli@licr.org> 5.0a-5
- Fix #239575: crack uses obsolete sort option syntax

* Tue Sep 05 2006 Christian Iseli <Christian.Iseli@licr.org> 5.0a-4
- rebuild for FE 6

* Tue Feb 14 2006 Christian Iseli <Christian.Iseli@licr.org> 5.0a-3
- rebuild for FE 5

* Fri Dec 23 2005 Christian Iseli <Christian.Iseli@licr.org> 5.0a-2
- rebuild with gcc-4.1

* Tue Sep 06 2005 Tom "spot" Callaway <tcallawa@redhat.com> 5.0a-1
- use words to make a richer dict 1

* Tue Sep 06 2005 Christian Iseli <Christian.Iseli@licr.org> 5.0a-0
- Created spec file.
