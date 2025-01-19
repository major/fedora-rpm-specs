%global myname minisat

Name:           minisat2
Version:        2.2.1
Release:        21%{?dist}
Summary:        Minimalistic SAT solver

License:        MIT
URL:            http://minisat.se/
# Debian has a newer version than the latest provided by upstream
Source0:        http://ftp.debian.org/debian/pool/main/m/%{name}/%{name}_%{version}.orig.tar.gz
#Source0:        http://minisat.se/downloads/%%{myname}-%%{version}.tar.gz
# Sent sources, test, patches (below) to upstream via email on 2008-07-08:
Source1:        http://www.dwheeler.com/essays/minisat-user-guide-1.0.html
Source2:        minisat2-test.in
# Man page courtesy of Debian
Source3:        minisat.1
# Debian patch to require a nonzero memory limit
Patch0:         %{name}-memory-limit.patch
# Debian patch to fix C++ syntax (for clang, but g++ needs it now too)
Patch1:         %{name}-clang-build.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
MiniSat is a minimalistic, open-source Boolean satisfiability problem
(SAT) solver, developed to help researchers and developers alike to get
started on SAT.  Together with SatELite, MiniSat was recently awarded in
the three industrial categories and one of the "crafted" categories of
the SAT 2005 competition.

A SAT solver can determine if it is possible to find assignments to
boolean variables that would make a given expression true, if the
expression is written with only AND, OR, NOT, parentheses, and boolean
variables.  If the expression is satisfiable, MiniSAT can also produce a
set of assignments that make the expression true.  Although the problem
is NP-complete, SAT solvers (like this one) are often able to decide
this problem in a reasonable time frame.

%package libs
Summary:        Minimalistic SAT solver library

%description libs
The MiniSat library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       zlib-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

# Fix a small C++11 infelicity
for fil in minisat/utils/Options.h minisat/simp/Main.cc; do
  sed -i.orig 's/"\(PRI[[:alnum:]]*\)/" \1 /' $fil
  touch -r $fil.orig $fil
  rm -f $fil.orig
done

# Use fPIC instead of fpic ... just in case
sed -i 's/fpic/fPIC/' Makefile

cp -p %{SOURCE1} minisat-user-guide.html
cp -p %{SOURCE2} .

%build
# %%{?_smp_mflags} leads to sporadic build failures
make lsh sh prefix=%{_prefix} libdir=%{_libdir} VERB=

# Test "minisat2-test.in" is a brief quote from
# http://www.satcompetition.org/2004/format-solvers2004.html
# Exit value is 10 for satisfiable, 20 for unsatisfiable
export LD_LIBRARY_PATH=$PWD/build/dynamic/lib
build/dynamic/bin/minisat minisat2-test.in minisat2-test.out || true

%install
%make_install prefix=%{_prefix} libdir=%{_libdir}

# We don't want the static library
rm %{buildroot}%{_libdir}/libminisat.a

# Fix permissions on the shared library
chmod a+x %{buildroot}%{_libdir}/libminisat.so.2.*

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 -p %{SOURCE3} %{buildroot}%{_mandir}/man1

%check
echo "RESULTS:"
cat minisat2-test.out
result=`head -1 minisat2-test.out`
if [ "$result" = "SAT" ]; then
  echo "SUCCESS - Correctly found that it was satisfiable"
  true
else
  echo "Failed test."
  false
fi

%ldconfig_scriptlets libs

%files
%doc doc/ReleaseNotes-2.2.0.txt
%doc minisat-user-guide.html
%doc minisat2-test.in
%doc minisat2-test.out
%{_bindir}/%{myname}
%{_mandir}/man1/minisat.1*

%files libs
%license LICENSE
%{_libdir}/lib%{myname}.so.2*

%files devel
%{_includedir}/%{myname}/
%{_libdir}/lib%{myname}.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 2.2.1-15
- Do not glob the library name

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 2.2.1-1
- Switch to Debian sources

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Jerry James <loganjerry@gmail.com> - 2.2.0-11
- The -devel subpackage needs to Requires zlib-devel

* Fri Feb 20 2015 Jerry James <loganjerry@gmail.com> - 2.2.0-10
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  1 2013 Jerry James <loganjerry@gmail.com> - 2.2.0-6
- Fix a race between %%check and assembling the files to package

* Fri Mar  1 2013 Jerry James <loganjerry@gmail.com> - 2.2.0-5
- Add a man page, courtesy of the Debian maintainers
- Build a shared library, and add -devel and -libs packages (bz 912190)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 2.2.0-2
- Rebuild for GCC 4.7
- Use the canonical source URL
- Drop the use of -ffloat-store, since the code sets the FPU mode

* Wed Jun 22 2011 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- New upstream version
- Drop upstreamed template patch
- Drop unnecessary spec file elements (BuildRoot, etc.)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10.20070721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9.20070721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8.20070721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 7 2008 David A. Wheeler <dwheeler at, dwheeler.com> 2.0-7.20070721
- Removed code for switching between -O2 and -O3, per reviewer request.

* Thu Aug 7 2008 David A. Wheeler <dwheeler at, dwheeler.com> 2.0-6.20070721
- Timing tests found -O3 was unhelpful; switched back to -O2, but left stub
  in case a switch to another -O level would help in the future.
  -O3 real 0m35.714s, 0m35.714s, 0m35.834s vs. -O2 real 0m35.296s, 0m35.301s

* Tue Jul 8 2008 David A. Wheeler <dwheeler at, dwheeler.com> 2.0-5.20070721
- Moved to higher optimization level (-O3); speed is critical for this app.

* Tue Jul 8 2008 David A. Wheeler <dwheeler at, dwheeler.com> 2.0-4.20070721
- Different version number convention to better conform to Fedora guidelines
- Made macro use consistent (not used for simple commands)
- Documented when patches and documentation sent upstream

* Sat Jun 28 2008 David A. Wheeler <dwheeler at, dwheeler.com> 2.0-3.20070721
- Use "make r" instead of "make" to create "released" version
- Wrote brief user guide, included as part of this package.

* Fri Jun 27 2008 David A. Wheeler <dwheeler at, dwheeler.com> 2.0-2.20070721
- Switched from minimal "core" to more-capable "simp" (simplifier)
- Change "make" invocation so CFLAGS includes %%{optflags}
- Add test file and %%check section (so we'd know if it worked!)
- Modified description for people who don't know what SAT solvers are.

* Thu Jun 26 2008 Earl Sammons <esammons at, hush.com> 2.0-1.20070721
- Initial build
- Include Debian patches minisat2-FPU.patch and minisat2-template.patch
