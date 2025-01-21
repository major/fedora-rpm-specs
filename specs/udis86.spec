%global gitrev 56ff6c8

Name:           udis86
Version:        1.7.2
Release:        26.%{gitrev}%{?dist}
Summary:        A disassembler library for x86 and x86-64

License:        BSD-2-Clause
URL:            https://github.com/vmt/udis86
Source0:        %{name}-%{gitrev}.tar.xz
Patch0:         udis86-ud_opcode.patch
Patch1:         udis86-symresolve.patch
Patch2:         udis86-ax_prog_sphinx_version.patch
Patch3:         udis86-docs_manual_Makefile.am.patch

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  python
BuildRequires:  yasm
BuildRequires:  python3-sphinx

%description
udis86 is a disassembler library (libudis86) for x86 and x86-64.
The primary intent is to aid binary code analysis.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{gitrev}
%patch -P0 -p1 -b .ud_opcode
%patch -P1 -p1 -b .symresolve
%patch -P2 -p1 -b .origm4
%patch -P3 -p1 -b .automake
find '(' -name '*.c' -or -name '*.h' ')' -exec chmod 644 {} \;

%build
./autogen.sh
%configure --disable-static \
           --enable-shared \
           --disable-silent-rules \
           --with-python=%{_bindir}/python3 \
           --with-yasm=%{_bindir}/yasm \
           --with-sphinx-build=%{_bindir}/sphinx-build-3
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
make -C docs/manual html-local


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# udis86 overrides "docdir" from automake to datadir/docs
rm -rf %{buildroot}%{_datadir}/docs
rm -rf %{buildroot}%{_docdir}


%ldconfig_scriptlets

%files
%{_bindir}/udcli
%{_libdir}/*.so.*

%files devel
%doc docs/x86/optable.* docs/manual/html/*.html docs/manual/html/_static
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-26.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-25.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-24.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-23.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-22.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 David Cantrell <dcantrell@redhat.com> - 1.7.2-21.56ff6c8
- Change License to BSD-2-Clause (SPDX expression)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-20.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-19.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-18.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-17.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-16.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-15.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-14.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 David Cantrell <dcantrell@redhat.com> - 1.7.2-13.56ff6c8
- Fix building package on rawhide (#1676171)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-12.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-9.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-5.56ff6c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Scott Tsai <scottt.tw@gmail.com> - 1.7.2-4.56ff6c8
- Package post 1.7.2 snapshot 56ff6c8

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Scott Tsai <scottt.tw@gmail.com> 1.7.2-1
- upstream 1.7.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Scott Tsai <scottt.tw@gmail.com> 1.7.1-1
- upstream 1.7.1

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-8.5c60189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Scott Tsai <scottt.tw@gmail.com> 1.7-7
- Upstream 5c60189

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 04 2009 Scott Tsai <scottt.tw@gmail.com> 1.7-3
- Actually remove commented out requires line
- Move check section after install section
- Place udcli in the main package instead of -devel
- Fix source file permissions

* Thu Dec 03 2009 Scottt Tsai <scottt.tw@gmail.com> 1.7-2
- Fix source url
- Remove commented out requires line
- Fix summary
- Move "make check" to check section
- Mark doc files instead of relying on make install

* Thu Dec 03 2009 Scott Tsai <scottt.tw@gmail.com> 1.7-1
- upstream 1.7
