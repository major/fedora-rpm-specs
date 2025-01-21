##
# Original RPM Specification file from the Dries repository:
#   http://svn.rpmforge.net/svn/trunk/rpms/wsdlpull/wsdlpull.spec
# Original author: Dries Verachtert <dries@ulyssis.org>
##
#
%global mydocs __tmp_docdir
#
Name: wsdlpull
Version: 1.23
Release: 32%{?dist}

Summary: C++ Web Services client library

License: LGPL-2.0-or-later AND MIT
URL: http://%{name}.sourceforge.net

Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
%{?el5:BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
# That patch will be submitted upstream
Patch0: wsdlpull-%{version}-fix-gcc43-compatibility.patch
# That patch will be submitted upstream
Patch1: wsdlpull-%{version}-add-man-pages.patch
# That patch will be submitted upstream
Patch2: wsdlpull-%{version}-fix-gnu-autotools-compatibility.patch

%description
%{name} is a C++ web services client library. It includes a WSDL
Parser, a XSD Schema Parser and Validator and XML Parser and serializer
and an API and command line tool for dynamic WSDL inspection and
invocation.

%{name} comes with a generic web service client. Using %{name} tools,
you can invoke most Web services from command line without writing any
code. See http://wsdlpull.sourceforge.net for usage.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary: HTML documentation for the %{name} library
%if 0%{?fedora} >= 10
BuildArch: noarch
%endif
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: doxygen

%description doc
This package contains the documentation in the HTML format of the %{name}
library. The documentation is the same as at the %{name} web page.

%prep
%setup -q

# Apply the g++ 4.3 compatibility patch
%patch -P0 -p1

# Create a directory for man pages
%{__mkdir} man

# Apply the man page patch
%patch -P1 -p1

# Remove any CVS sub-directory (they should not be delivered with the tar-ball)
find . -name 'CVS' -print | xargs -r %{__rm} -rf

# Remove any a.out binary (they should not be delivered with the tar-ball)
find . -name 'a.out' -print | xargs -r %{__rm} -f

# Remove the generated HTML documentation (it should not be delivered
# with the tar-ball, as it is generated)
if [ -d docs/html ]; then
  %{__rm} -rf docs/html
fi

# Adapt a little bit the structure, so as to be more compliant with
# GNU Autotools
%{__mkdir} config
%{__mv} config.guess config.sub depcomp install-sh ltmain.sh missing config
%{__mv} config.h.in src

# Rename the standard documentation files
%{__mv} AUTHORS.txt AUTHORS
sed -i -e 's/\r$//' AUTHORS
%{__mv} CHANGES.txt CHANGES
%{__mv} COPYING.txt COPYING
%{__mv} README.txt README

# Apply the GNU Autotools compatibility patch
%patch -P2 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Remove unpackaged files from the buildroot
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.la
%{__rm} -rf %{mydocs} && %{__mkdir_p} %{mydocs}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html %{mydocs}

%ldconfig_scriptlets


%files
%doc AUTHORS CHANGES COPYING README
%{_bindir}/%{name}
%{_bindir}/%{name}-schema
%{_libdir}/lib*.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man1/%{name}-schema.1.*
%{_datadir}/%{name}

%files devel
%{_includedir}/schemaparser
%{_includedir}/wsdlparser
%{_includedir}/xmlpull
%{_libdir}/lib*.so

%files doc
%doc AUTHORS CHANGES COPYING README
%doc %{mydocs}/html


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.23-12
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-6
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 14 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.23-3
- Integrated Patrick Monnerat's remarks
  (https://bugzilla.redhat.com/show_bug.cgi?id=502686#c13)

* Tue Jul 11 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.23-2
- Integrated Patrick Monnerat's remarks
  (https://bugzilla.redhat.com/show_bug.cgi?id=502686#c6)

* Tue Jun 26 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 1.23-1
- Initial package, thanks to Dries Verachtert <dries@ulyssis.org>
