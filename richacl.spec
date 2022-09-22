%global commit 12ab188b745a3e56047d7120138213b4446a3a5f

Name: richacl
Summary: Rich Access Control List utilities
Version: 1.12
Release: 15%{?dist}
Requires: librichacl%{?_isa} = %{version}-%{release}
BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: libattr-devel
Source: https://github.com/andreas-gruenbacher/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

License: GPLv2+
URL: https://github.com/andreas-gruenbacher/richacl

%description
The getrichacl and setrichacl utilities allow to manage Rich Access
Control Lists (richacls) from the command line.

Richacls are an implementation of NFSv4 ACLs which has been extended by
file masks to better fit the standard POSIX file permission model.  They
provide a consistent file permission model locally as well as over
various remote file system protocols like NFSv4 and CIFS/Samba.

%package -n librichacl
Summary: Dynamic library for Rich Access Control List support
License: LGPLv2

%description -n librichacl
The librichacl.so dynamic library provides functions for manipulating
Rich Access Control Lists and for converting between their different
representations.

%package -n librichacl-devel
Summary: Files needed for building programs with librichacl
License: LGPLv2
Requires: librichacl%{?_isa} = %{version}-%{release}
Requires: libattr-devel%{?_isa}

# Required because of the directories those packages contain:
Requires: pkgconfig%{?_isa}
%ifarch s390x
Requires: glibc-headers-s390
%else
%ifarch i686 || %ifarch x86_64
Requires: glibc-headers-x86
%else
Requires: glibc-devel
%endif
%endif

%description -n librichacl-devel
Header files and documentation needed to develop programs which make use
of the Rich Access Control List programming interface.

%prep
%setup -qn %{name}-%{commit}

# Upstream, the version is determined by git tags.  There is no information
# about tags in the github snapshot though; we have to fill in the version
# manually:
echo %{version} > .tarball-version

%build
autoreconf -vi
%configure
make %{?_smp_mflags}

%check
if ./src/setrichacl --modify `whoami`:rwpCo::allow .; then
    make tests || exit $?
    if test 0 = `id -u`; then
        make root-tests || exit $?
    fi
else
    echo '*** Richacls are probably not supported by the file system,' \
         'the test-suite will NOT run ***'
fi

%install
%make_install

## get rid of librichacl.a and librichacl.la
rm -f %{buildroot}%{_libdir}/librichacl.a
rm -f %{buildroot}%{_libdir}/librichacl.la

# drop already installed documentation, we will use an RPM macro to install it
#rm -rf %{buildroot}%{_docdir}/%{name}*

%ldconfig_scriptlets -n librichacl

%files
%license doc/COPYING-GPLv2
%{_bindir}/getrichacl
%{_bindir}/setrichacl
%{_mandir}/man1/*
%{_mandir}/man7/*

%files -n librichacl-devel
%{_libdir}/librichacl.so
%{_includedir}/sys/richacl.h
%{_libdir}/pkgconfig/librichacl.pc

%files -n librichacl
%license doc/COPYING-LGPLv2
%{_libdir}/librichacl.so.*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Anoop C S <anoopcs@redhat.com> - 1.12-11
- resolves #1871616

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 20 2016 Anoop C S <anoopcs@redhat.com> - 1.12-1
- Update to version 1.12 (#1358062)

* Thu Jun 16 2016 Anoop C S <anoopcs@redhat.com> - 1.11-1
- Update to version 1.11 (#1347069)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Niels de Vos <ndevos@redhat.com> 1.10-1
- Update to version 1.10 (#1246069)

* Fri Jul 24 2015 Andreas Gruenbacher <agruenba@redhat.com> 1.7-0
- Update from upstream

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 6 2015 Andreas Gruenbacher <agruenba@redhat.com> 1.5-2
- Switch to github snapshot + autotools in the package

* Tue May 5 2015 Andreas Gruenbacher <agruenba@redhat.com> 1.5-1
- Update from upstream
- Some minor spec file "beautification"

* Mon May 4 2015 Andreas Gruenbacher <agruenba@redhat.com> 1.4-3
- Update from upstream

* Wed Apr 29 2015 Andreas Gruenbacher <agruenba@redhat.com> 1.4-1
- Update to upstream version

* Thu Mar 26 2015 Niels de Vos <ndevos@redhat.com> 1.3-1
- Initial packaging
