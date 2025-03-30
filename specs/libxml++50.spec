%global api_ver 5.0

Name:           libxml++50
Version:        5.4.0
Release:        3%{?dist}
Summary:        C++ wrapper for the libxml2 XML parser library
License:        LGPL-2.1-or-later
URL:            https://libxmlplusplus.github.io/libxmlplusplus/
Source:         https://github.com/libxmlplusplus/libxmlplusplus/releases/download/%{version}/libxml++-%{version}.tar.xz
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen, graphviz
BuildRequires:  gcc-c++
BuildRequires:  meson, python3
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  /usr/bin/xsltproc

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library. Its original
author is Ari Johnson and it is currently maintained by Christophe de Vienne
and Murray Cumming.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
License:	MIT AND LGPL-2.1-or-later
Requires:       glibmm24-doc

%description    doc
This package contains the full API documentation for %{name}.


%prep
%autosetup -n libxml++-%{version} -p1


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install

%check
%meson_test


%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libxml++-%{api_ver}.so.1*

%files devel
%{_includedir}/libxml++-%{api_ver}/
%{_libdir}/libxml++-%{api_ver}.so
%{_libdir}/libxml++-%{api_ver}/
%{_libdir}/pkgconfig/libxml++-%{api_ver}.pc

%files doc
%license COPYING
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books
%{_datadir}/devhelp/books/libxml++-%{api_ver}
%{_docdir}/libxml++-%{api_ver}


%changelog
* Fri Mar 28 2025 Tom Callaway <spot@fedoraproject.org> - 5.4.0-3
- pull license file into -doc subpackage

* Tue Mar 25 2025 Tom Callaway <spot@fedoraproject.org> - 5.4.0-2
- add %%check section
- update license tag for -doc subpackage

* Mon Mar 24 2025 Tom Callaway <spot@fedoraproject.org> - 5.4.0-1
- Initial Fedora packaging (based on libxml++30)
