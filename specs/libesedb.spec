Name:           libesedb
Version:        20240420
Release:        4%{?dist}
Summary:        Library to access the Extensible Storage Engine (ESE) Database File (EDB) format
License:        LGPL-3.0-or-later
URL:            https://github.com/libyal/libesedb
VCS:            https://github.com/libyal/libesedb
# Releases      https://github.com/libyal/libesedb/releases

%global         common_description %{expand:
Library and tools to access the Extensible Storage Engine (ESE) Database File
(EDB) format. ESEDB is used in may different applications like Windows Search,
Windows Mail, Exchange, Active Directory, etc.}


%global         gituser         libyal
%global         gitname         libesedb
%global         gitdate         20240420
%global         commit          24ae2ff47365adb5f1dcdce315ac7dd16b972836
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

# Build with python3 package by default
%bcond_without  python3


# Source0:      %%{url}/archive/%%{commit}/%%{name}-%%{version}-%%{shortcommit}.tar.gz
Source0:        %{url}/releases/download/%{version}/%{gitname}-experimental-%{version}.tar.gz

# Patch build to use the shared system libraries rather than using embedded ones
# Patch0:         %%{name}-libs.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# autoreconf here needs autopoint from gettext-devel
BuildRequires:  gettext-devel


%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# if with_python3
%endif

Provides: bundled(libbfio)      = 20240420
Provides: bundled(libcdata)     = 20240420
Provides: bundled(libcerror)    = 20240420
Provides: bundled(libcfile)     = 20240420
Provides: bundled(libclocale)   = 20240420
Provides: bundled(libcnotify)   = 20240420
Provides: bundled(libcpath)     = 20240420
Provides: bundled(libcsplit)    = 20240420
Provides: bundled(libcthreads)  = 20240420
Provides: bundled(libfcache)    = 20240420
Provides: bundled(libfdata)     = 20240420
Provides: bundled(libfdatetime) = 20240420
Provides: bundled(libfguid)     = 20240420
Provides: bundled(libfmapi)     = 20240420
Provides: bundled(libfvalue)    = 20240420
Provides: bundled(libfwnt)      = 20240420
Provides: bundled(libmapidb)    = 20240420
Provides: bundled(libuna)       = 20240420

%description
%{common_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%{common_description}


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-pyesedb
Summary:        Python3 binding for the library reading of esedb format
%{?python_provide:%python_provide python%{python3_pkgversion}-pyesedb}

%description -n python%{python3_pkgversion}-pyesedb
Python3 binding for the library reading of esedb format
%{common_description}
%endif


%prep
%autosetup -n %{gitname}-%{version}
#./autogen.sh
autoreconf --force --install
aclocal


%build
%configure --disable-static \
%if 0%{?with_python3}
           --enable-python \
%endif
           --enable-wide-character-type \
           --enable-multi-threading-support

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{_bindir}/esedbexport
%{_bindir}/esedbinfo
%{_mandir}/man1/esedbinfo.1.*
%{_mandir}/man3/libesedb.3.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libesedb.pc

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-pyesedb
%{python3_sitearch}/pyesedb*
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20240420-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240420-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 20240420-2
- Rebuilt for Python 3.13

* Wed May 29 2024 Michal Ambroz <rebus at, seznam.cz> - 20240420-1
- update to 20240420

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20181229-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 20181229-12
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20181229-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20181229-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 20181229-9
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20181229-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20181229-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20181229-6
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20181229-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20181229-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20181229-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20181229-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Michal Ambroz <rebus at, seznam.cz> - 20181229-1
- update to 20181229, provide python3 binding

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120102-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120102-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120102-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120102-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120102-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120102-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120102-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 21 2016 Michal Ambroz <rebus at, seznam.cz> 20120102-10
- backport patch the libuna build for inline on gcc - #1239642 FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20120102-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120102-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120102-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120102-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120102-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Michal Ambroz <rebus at, seznam.cz> 20120102-3
- updates based on the review of Mario Blättermann

* Sat Oct 06 2012 Michal Ambroz <rebus at, seznam.cz> 20120102-2
- updates based on the review of Mario Blättermann

* Sun May 13 2012 Michal Ambroz <rebus at, seznam.cz> 20120102-1
- initial build for Fedora
