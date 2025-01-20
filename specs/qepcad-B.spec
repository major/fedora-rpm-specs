Name:           qepcad-B
Version:        1.74
Release:        10%{?dist}
Summary:        Quantifier elimination tool

License:        ISC
URL:            https://www.usna.edu/Users/cs/wcbrown/qepcad/B/QEPCAD.html
Source:         https://www.usna.edu/Users/cs/wcbrown/qepcad/INSTALL/%{name}.%{version}.tgz
# Don't require users to set the "qe" or "SINGULARPATH" environment variables.
# Not for upstream.
Patch:          %{name}-env.patch
# Add gcc attributes for better efficiency and warnings. Upstream: 20 Nov 2013.
Patch:          %{name}-attr.patch
# Fix use of uninitialized variables. Upstream: 20 Nov 2013.
Patch:          %{name}-uninit.patch
# Fix a non-void function where control can fall off the end. Upstream:
# 20 Nov 2013.
Patch:          %{name}-return.patch
# Fix abstract base classes with non-virtual destructors. Upstream:
# 20 Nov 2013.
Patch:          %{name}-destructor.patch
# Add parentheses to disambiguate mixed boolean operators. Upstream:
# 20 Nov 2013.
Patch:          %{name}-parens.patch
# Fix some mixed signed/unsigned operations. Upstream: 20 Nov 2013.
Patch:          %{name}-signed.patch
# Fix syntactically incorrect expressions. Upstream: 20 Nov 2013.
Patch:          %{name}-syntax.patch
# Remove unused variables and static functions.
Patch:          %{name}-unused.patch
# Tell Singular not to steal the TTY (bz 1257471)
Patch:          %{name}-tty.patch
# Adapt to GCC 6
Patch:          %{name}-gcc6.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(xext)
BuildRequires:  saclib-devel

# Subprocesses are spawned to run executables from these packages
Requires:       bash
Requires:       coreutils
Requires:       Singular

%description
QEPCAD is an implementation of quantifier elimination by partial
cylindrical algebraic decomposition due originally to Hoon Hong, and
subsequently added on to by many others.  It is an interactive
command-line program written in C/C++, and based on the SACLIB library.
This is QEPCAD B version 1.x, the "B" designating a substantial
departure from the original QEPCAD and distinguishing it from any
development of the original that may proceed in a different direction.

%prep
%autosetup -n qesource -p0

%conf
# Adapt to the Fedora saclib package
sed -i 's,\${saclib}/lib/saclib.\.a,-lsaclib,' source/Makefile cad2d/Makefile

# Embed the library path
sed -i 's,@LIBDIR@,%{_libdir},' source/main/BEGINQEPCAD.c

# Use the right build flags
sed -i 's|-O4|%{build_cxxflags} -Wno-unused-label %{build_ldflags}|' plot2d/Makefile

%build
# FIXME: %%{?_smp_mflags} doesn't work
export saclib=%{_prefix}
export qe=$PWD
export CCo=g++
export FLAGS='%{build_cxxflags} -I%{_includedir}/saclib -Wno-unused-label'
export FLAGSo="$FLAGS"
export SPECIFLAGS="-I%{_includedir}/saclib"
export SPECLFLAGS='%{build_ldflags}'
make -C extensions/sfext
make -C extensions/adj2d
make -C extensions/rend
make -C extensions/newadj
make -C extensions/lift2D
make -C source opt FLAGSo="$FLAGS"
make -C plot2d
make -C cad2d opt FLAGSo="$FLAGS"

%install
#Install the binaries
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 source/qepcad %{buildroot}%{_bindir}
install -p -m 0755 plot2d/ADJ2D_plot %{buildroot}%{_bindir}
install -p -m 0755 cad2d/cad2d %{buildroot}%{_bindir}

# Install the default settings file
mkdir -p %{buildroot}%{_datadir}/qepcad
sed 's,^#S.*,SINGULAR %{_libdir}/Singular,' default.qepcadrc > \
  %{buildroot}%{_datadir}/qepcad/default.qepcadrc
touch -r default.qepcadrc %{buildroot}%{_datadir}/qepcad/default.qepcadrc

# Install qepcad.help and the expected symbolic links
mkdir -p %{buildroot}%{_datadir}/qepcad/bin
cp -p source/qepcad.help %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/ADJ2D_plot %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/cad2d %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/qepcad %{buildroot}%{_datadir}/qepcad/bin

%files
%doc LOG
%license LICENSE
%{_bindir}/qepcad
%{_bindir}/ADJ2D_plot
%{_bindir}/cad2d
%{_datadir}/qepcad/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Jerry James <loganjerry@gmail.com> - 1.74-8
- Stop building for 32-bit x86
- Minor spec file simplifications

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 1.74-4
- Convert License tag to SPDX and correct it to ISC

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  2 2021 Jerry James <loganjerry@gmail.com> - 1.74-1
- Version 1.74

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Jerry James <loganjerry@gmail.com> - 1.72-6
- Drop unneeded -freeglut patch
- Add BR on pkgconfig(xext) to fix FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.72-5
- Rebuilt for new freeglut

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.72-3
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Jerry James <loganjerry@gmail.com> - 1.72-1
- New upstream version
- Updated URLs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.69-13
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.69-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep  3 2015 Jerry James <loganjerry@gmail.com> - 1.69-11
- Run Singular in a separate session so it doesn't steal the TTY (bz 1257471)
- Don't send data to bash through the (supposedly) Singular pipe

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Jerry James <loganjerry@gmail.com> - 1.69-9
- Rebuild for C++ ABI change

* Wed Jan  7 2015 Jerry James <loganjerry@gmail.com> - 1.69-8
- Update URLs
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Jerry James <loganjerry@gmail.com> - 1.69-5
- Fix default.qepcadrc so that it requires Singular on all architectures

* Thu Mar 20 2014 Jerry James <loganjerry@gmail.com> - 1.69-4
- Singular is now available for all architectures

* Sat Feb 15 2014 Jerry James <loganjerry@gmail.com> - 1.69-3
- Singular is currently available for x86 architectures only

* Thu Feb 13 2014 Jerry James <loganjerry@gmail.com> - 1.69-2
- Install qepcad.help

* Thu Nov 21 2013 Jerry James <loganjerry@gmail.com> - 1.69-1
- Initial RPM
