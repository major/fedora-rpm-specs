Summary:        The GNU Portable Threads library extended with semaphore support
Name:           pthsem
Version:        2.0.7
Release:        27%{?dist}
License:        LGPLv2+
URL:            http://www.auto.tuwien.ac.at/~mkoegler/index.php/pth
Source:         http://downloads.sourceforge.net/bcusdk/pthsem_%{version}.tar.gz
Patch1:         pth-2.0.7-dont-remove-gcc-g.patch
Patch2:         pth-2.0.7-config-script.patch
Patch3:         pthsem-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  /usr/bin/iconv

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

pthsem is an extend version, with support for semaphores added. It can
be installed parallel to a normal pth. The header file is called pthsem.h, 
the configuration program pthsem-config and the autoconf macro
AC_CHECK_PTHSEM.

%package devel
Summary:        Development headers and libraries for Pthsem
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and libraries for pthsem.


%prep
%setup -q
%patch1 -p1 -b .dont-remove-gcc-g
%patch2 -p1 -b .config-script
%patch3 -p1
for f in ChangeLog README THANKS; do
    iconv -f ISO-8859-1 -t UTF-8 $f -o $f.new && mv $f.new $f
done



%build
%configure --disable-static ac_cv_func_sigstack='no'

# Work around multiarch conflicts in the pth-config script in order
# to complete patch2. Make the script choose between /usr/lib and
# /usr/lib64 at run-time.
if [ "%_libdir" == "/usr/lib64" ] ; then
    if grep -e '^pth_libdir="/usr/lib64"' pth-config ; then
        sed -i -e 's!^pth_libdir="/usr/lib64"!pth_libdir="/usr/lib"!' pth-config
    else
        echo "ERROR: Revisit the multiarch pth_libdir fixes for pth-config!"
        exit 1
    fi
fi
if grep -e "$RPM_OPT_FLAGS" pth-config ; then
    # Remove our extra CFLAGS from the pth-config script, since they
    # don't belong in there.
    sed -i -e "s!$RPM_OPT_FLAGS!!g" pth-config
else
    echo "ERROR: Revisit the multiarch CFLAGS fix for pth-config!"
    exit 1
fi

# this is necessary; without it make -j fails
make pth_p.h
make %{?_smp_mflags}


%check
make test
l=$($(pwd)/pth-config --libdir)
%ifarch x86_64 ppc64
    [ "$l" == "/usr/lib64" ]
%endif


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la



%ldconfig_scriptlets


%files
%doc ANNOUNCE AUTHORS COPYING ChangeLog HISTORY NEWS PORTING README
%doc SUPPORT TESTS THANKS USERS
%{_libdir}/*.so.*

%files devel
%doc HACKING
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/*/*
%{_datadir}/aclocal/*


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Florian Weimer <fweimer@redhat.com> - 2.0.7-26
- Port configure script to C99 (#2155421)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Andreas Thienemann <athienem@redhat.com> - 2.0.7-1
- Rolled initial spec based on the pth-2.0.7.spec from mschwendt
