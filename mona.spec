%global upver 1.4
%global uprel 18

Name:           mona
Version:        %{upver}r%{uprel}
Release:        8%{?dist}
Summary:        A decision procedure for the WS1S and WS2S logics

License:        GPL-2.0-or-later
URL:            https://www.brics.dk/mona/
Source0:        https://www.brics.dk/mona/download/%{name}-%{upver}-%{uprel}.tar.gz
Source1:        https://www.brics.dk/mona/mona14.pdf
# Make an intentionally-undefined symbol ("guide") weak
Patch0:         %{name}-weak-guide.patch

BuildRequires:  emacs
BuildRequires:  emacs-el
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  make
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# This can be removed when Fedora 39 reaches EOL
Obsoletes:      %{name}-xemacs < 1.4r18-5

%description
MONA is a tool that translates formulas in the logics WS1S or WS2S into
finite-state automata represented by BDDs.  The formulas may express search
patterns, temporal properties of reactive systems, parse tree constraints,
etc.  MONA also analyzes the automaton resulting from the compilation, and
determines whether the formula is valid and, if the formula is not valid,
generates a counterexample.

%package libs
# GPL-2.0-or-later: the project as a whole
# CC-PDDC: Mem/dlmalloc.{c,h}
License:        GPL-2.0-or-later AND CC-PDDC
Summary:        Supporting libraries for Mona

%description libs
Supporting libraries for Mona.

%package devel
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# URW: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Header files for developing applications with Mona
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications that use the Mona libraries.

%package examples
Summary:        Example Mona source files and C programs
Requires:       %{name}-libs = %{version}-%{release}
BuildArch:      noarch

%description examples
Example Mona source files, for use with the mona executable, and also sample C
programs that access the Mona library interfaces.

%package emacs
Summary:        Emacs mode for editing Mona files
Requires:       %{name}-libs = %{version}-%{release}
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
BuildArch:      noarch

%description emacs
Emacs mode for editing Mona files.

%prep
%autosetup -n %{name}-%{upver} -p1
cp -p %{SOURCE1} .

# Do not override Fedora build flags
sed -i 's/ -O3//g' configure

%build
%configure --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

# Get rid of the .la files; we don't want them
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Install the examples
cp -p Examples/bdd_example $RPM_BUILD_ROOT%{_bindir}
cp -p Examples/gta_example $RPM_BUILD_ROOT%{_bindir}
cp -p Examples/presburger_analysis $RPM_BUILD_ROOT%{_bindir}
cp -p Examples/presburger_transduction $RPM_BUILD_ROOT%{_bindir}

# Move the Emacs lisp file to the right places
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/mona

cd $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/mona
mv $RPM_BUILD_ROOT%{_datadir}/mona-mode.el .
%_emacs_bytecompile mona-mode.el

%files
%{_bindir}/mona
%{_bindir}/dfa2dot
%{_bindir}/gta2dot
%{_mandir}/man1/mona.1*

%files devel
%doc mona14.pdf
%{_includedir}/mona
%{_libdir}/libmona*.so

%files examples
%doc Examples/*.mona Examples/bdd_volatility
%{_bindir}/bdd_example
%{_bindir}/gta_example
%{_bindir}/presburger_analysis
%{_bindir}/presburger_transduction

%files libs
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/libmona*.so.1*

%files emacs
%dir %{_emacs_sitelispdir}/mona
%{_emacs_sitelispdir}/mona/mona-mode.el*

%changelog
* Thu Mar 16 2023 Jerry James <loganjerry@gmail.com> - 1.4r18-8
- Correct License tag: CC-PDDC instead of public domain

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.4r18-7
- Move the manual to the devel subpackage
- Convert License tags to SPDX
- Do not override Fedora build flags

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 1.4r18-5
- Drop XEmacs support

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Jerry James <loganjerry@gmail.com> - 1.4r18-1
- Update to 1.4-18

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1.4r17-9
- Fix inline vs static inline issue for gcc-10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 28 2016 Jerry James <loganjerry@gmail.com> - 1.4r17-1
- Update to 1.4-17

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4r16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct  8 2015 Jerry James <loganjerry@gmail.com> - 1.4r16-1
- Update to 1.4-16

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4r15-6
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 10 2015 Jerry James <loganjerry@gmail.com> - 1.4r15-5
- Add -inline patch to fix a build failure with gcc 5.0
- Use the license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  2 2013 Jerry James <loganjerry@gmail.com> - 1.4r15-1
- Update to 1.4-15

* Mon Apr 29 2013 Jerry James <loganjerry@gmail.com> - 1.4r14-1
- Update to 1.4-14
- Make "guide", which is undefined on purpose, a weak symbol

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 1.4r13-5
- Rebuild for GCC 4.7
- Spec file cleanups

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 29 2010 Jerry James <loganjerry@gmail.com> - 1.4r13-4
- Move COPYING and other docs to -libs, which is required by the main package.
- Remove unnecessary libtool BR.
- Remove BuildRoot tag.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4r13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Jerry James <loganjerry@gmail.com> - 1.4r13-1
- Update to 1.4-13

* Tue Jun 17 2008 Jerry James <loganjerry@gmail.com> - 1.4r11-1
- Update to 1.4-11
- Add the user manual to the main package docs

* Mon Mar 10 2008 Jerry James <loganjerry@gmail.com> - 1.4r10-1
- Initial RPM
