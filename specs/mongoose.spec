Name:		mongoose
Summary:	An easy-to-use self-sufficient web server
Version:	3.1
Release:	28%{?dist}
License:	MIT
URL:		http://code.google.com/p/mongoose
Source0:	http://mongoose.googlecode.com/files/mongoose-%{version}.tgz
Source1:	mongoose.conf
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	openssl-devel

# Build changes:
# http://code.google.com/p/mongoose/issues/detail?id=372 
Patch0:		mongoose-fix-libmongoose-so-build.patch
# http://code.google.com/p/mongoose/issues/detail?id=371
Patch1:		mongoose-fix-no-ssl-dl-build-error.patch


%description
Mongoose web server executable is self-sufficient, it does not depend on 
anything to start serving requests. If it is copied to any directory and 
executed, it starts to serve that directory on port 8080 (so to access files, 
go to http://localhost:8080). If some additional configuration is required - 
for example, different listening port or IP-based access control, then a 
'mongoose.conf' file with respective options can be created in the same 
directory where executable lives. This makes Mongoose perfect for all sorts 
of demos, quick tests, file sharing, and Web programming.

%package lib
Summary:	Shared Object for applications that use %{name} embedded

%description lib
This package contains the shared library required by applications that
are using %{name}'s embeddable API to provide web services. 

%ldconfig_scriptlets lib

%package devel
Summary:	Header files and development libraries for %{name}
Requires:	%{name}-lib = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs embedding %{name} on them,
you will need to install %{name}-devel and check %{name}'s API at its
comprisable header file.

%prep
%setup -q -n %{name}
%patch -P0 -p1 -b .solib-build
%patch -P1 -p1 -b .nossldl-build
%{__install} -p -m 0644  %{SOURCE1} .

%build
export VERSION=%{version}
%{__make} %{?_smp_mflags} VER="$VERSION" SOVER="${VERSION%.?}" \
			CFLAGS="%{optflags} -lssl -lcrypto -DNO_SSL_DL" linux 

%install
%{__rm} -rf %{buildroot}
%{__install} -D -p -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
%{__install} -D -p -m 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
# -lib subpackage
export VERSION=%{version}
%{__install} -D -p -m 0755 lib%{name}.so.%{version} \
		%{buildroot}/%{_libdir}/lib%{name}.so.$VERSION
ln -s %{_libdir}/lib%{name}.so.$VERSION \
		%{buildroot}/%{_libdir}/lib%{name}.so.${VERSION%.?}
# -devel subpackage
%{__install} -D -p -m 0644 %{name}.h %{buildroot}/%{_includedir}/%{name}.h
ln -s %{_libdir}/lib%{name}.so.$VERSION \
		%{buildroot}/%{_libdir}/lib%{name}.so

%files
%doc %{name}.conf LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files lib
%{_libdir}/lib%{name}.so.* 

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.1-20
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul  5 2012 Rafael Azenha Aquini <aquini at linux dot com> - 3.1-1
- Packaged mongoose's upstream 3.1 release.
- Introduced -lib -devel sub-packages (804843)
- Change build option to -DNO_SSL_DL (804844)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 27 2011 Rafael Azenha Aquini <aquini at linux dot com> - 3.0-2
- Add upstream patch to fix CVE-2011-2900 (729146) 

* Mon Jul 25 2011 Rafael Azenha Aquini <aquini at linux dot com> - 3.0-1
- Rebuilt for Fedora's inclusion, after scracth-build successful tests. 

* Mon Jul 25 2011 Rafael Azenha Aquini <aquini at linux dot com> - 3.0-0
- Packaged mongoose's upstream 3.0 release. 

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Rafael Azenha Aquini <aquini at linux dot com> - 2.11-0
- Packaged the mongoose's upstream 2.11 release. 

* Wed Jul 21 2010 Rafael Azenha Aquini <aquini at linux dot com> - 2.8-6
- Adjust the approach to grab correct OpenSSL versioned shared libs in 
  build time, as suggested by Toshio Ernie Kuratomi (592670#c25)
- Open an upstream issue asking for shipping a license file within mongoose's
  .tar file (http://code.google.com/p/mongoose/issues/detail?id=159)

* Tue Jul 13 2010 Rafael Azenha Aquini <aquini at linux dot com> - 2.8-5
- Get dinamically the correct OpenSSL versioned shared libs in build time, 
  as suggested by Douglas Schilling Landgraf (592670#c21)

* Wed May 19 2010 Rafael Azenha Aquini <aquini at linux dot com> - 2.8-4
- Drop off all source files from doc dir, including the examples
- Add patch to define correct OpenSSL versioned shared libs in build time, 
  as suggested by Ralf Corsepius (592670#c19)

* Tue May 18 2010 Rafael Azenha Aquini <aquini at linux dot com> - 2.8-3
- Several improvements to the Spec, by Terje RÃ¸sten's review (592670#c3)
- Added /examples dir to docs, as suggested by Chen Lei's review (592670#c4)

* Mon May 17 2010 Rafael Azenha Aquini <aquini at linux dot com> - 2.8-2
- Set of fixes to the Spec file, suggested by Chen Lei's review (592670#c1)

* Sat May 15 2010 Rafael Azenha Aquini <aquini at linux dot com> - 2.8-1
- initial packaging.

