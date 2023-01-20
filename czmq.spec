Name:           czmq
Version:        4.2.1
Release:        6%{?dist}
Summary:        High-level C binding for 0MQ (ZeroMQ)

License:        MPLv2.0
URL:            http://czmq.zeromq.org
Source0:        https://github.com/zeromq/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  zeromq-devel
# --with-docs
BuildRequires:  perl-interpreter
BuildRequires:  perl(File::Basename)
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  gcc-c++ cmake

%description
CZMQ has the following goals:
  i) To wrap the ZeroMQ core API in semantics that are natural and lead to
     shorter, more readable applications.
 ii) To hide the differences between versions of ZeroMQ.
iii) To provide a space for development of more sophisticated API semantics.


%package devel
Summary:        Development files for the czmq package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files needed to develop applications using czmq.


%prep
%autosetup -p1

%build
# As of August 2021, the CMake build does not generate
# the documentation (man pages).
%configure --with-docs
%make_build

# Override the binary objects genrated by Autotools with CMake-built ones
%cmake -DCZMQ_BUILD_STATIC:BOOL=OFF
%cmake_build

%install
# For the doc and zproject - But it installs everything
%make_install install-dist_apiDATA

rm -f %{buildroot}%{_libdir}/libczmq.{a,la}

# Override the installation with CMake-build
%cmake_install

%check
#%%ctest


%files
%doc AUTHORS NEWS LICENSE
%{_libdir}/*.so.4*

%files devel
%doc CONTRIBUTING.md README.md
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/%{name}/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*
%{_datarootdir}/zproject/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.2.1-3
- Added CMake build to avoid RPATH issue - BZ#1987416

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 01 2021 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.2.1-1
- Upstream upgrade (to 4.2.1)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.2.0-1
- Merged with EPEL 8 version: upgrade to 4.2.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.1-1
- Update to latest version
- Modernize some bits of the spec

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 4.0.2-3
- Add upstream patches for gcc 7 (0001-Problem-build-error-in-zsys-with-GCC7.patch
  and 0002-Problem-build-error-with-GCC7-in-zgossip_engine.inc.patch)
- Add perl to the build requirements list (required by doc/mkman)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan  5 2017 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 4.0.2-1
- Update to 4.0.2.

* Fri Nov 11 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 4.0.1-1
- Update to 4.0.1.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 3.0.2-2
- Disable the test suite for the moment (requires network access)

* Sat Jun 27 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 3.0.2-1
- Update to 3.0.2.
- License: MPLv2.0 (Mozilla Public License Version 2.0).
- Man pages installation patch (0001-Problem-does-not-install-man-pages-if-BUILD_DOC-is-o.patch)

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-7
- rebuilt for new zeromq 4.1.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar  2 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-5
- Patch to fix sha1 on bigendian machines (#1196994)

* Fri Feb 27 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-4
- Renamed /usr/bin/makecert to avoid a file conflict (#1196483)

* Fri Feb 20 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-3
- Build against ZeroMQ v4

* Fri Feb 20 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-2
- Add upstream patch eebf66a (0001-Use-_DEFAULT_SOURCE-instead-of-_BSD_SOURCE.patch)

* Tue Feb 17 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-1
- Update to 2.2.0.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May  1 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.1-1
- Update to 1.4.1.

* Tue Apr 30 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.0-1
- Update to 1.4.0.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.2-1
- Improve the description.

* Wed Dec 12 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.2-0
- Update to 1.3.2.

* Sun Oct 28 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.1-1
- Update to 1.3.1.

* Thu Oct 25 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.0-0
- Rename to libczmq.
- Update to v1.3.0 git snapshot.

* Tue Oct 23 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2.0-3
- Make czmq-devel require zeromq3-devel.

* Sat Oct 20 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2.0-2
- Build against limzmq v3.x (BR zeromq3-devel instead of zeromq-devel).

* Sat Oct 20 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2.0-1
- First Fedora build.

# vim:set ai ts=4 sw=4 sts=4 et:
