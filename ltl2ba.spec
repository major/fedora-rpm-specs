Name:		ltl2ba
Version:	1.3
Release:	6%{?dist}
Summary:	Fast translation from LTL formulas to Buchi automata

License:	GPLv2+
URL:		http://www.lsv.fr/~gastin/ltl2ba/
Source0:	%{url}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	help2man
BuildRequires:	make

%description
Translate from Linear temporal logic (LTL) formulas to Buchi automata.
LTL is a type of formal logic that extends formal logic with
qualifiers involving time.
A Buchi automaton is the extension of a finite state automaton
to infinite inputs, and are useful for specifying behavior
of non-terminating systems (such as hardware or operating systems).
A Buchi automaton accepts an infinite input sequence if and only if
there exists a run of the automaton which visits at least one of the
final states infinitely often.

The implementation is based on the translation algorithm by Gastin and Oddoux,
presented at the CAV Conference, held in 2001, Paris, France 2001.

%prep
%autosetup -p0

# Fix encoding
iconv -f latin1 -t utf8 README > README.utf8
mv README.utf8 README

%build
%make_build CFLAGS="%{build_cflags} -DNXT %{build_ldflags}"
help2man -N --version-string=%{version} ./ltl2ba > ltl2ba.1

%check
# Trivial test, primarily to make sure it compiled into something executable:
./ltl2ba -f "true"

%install
# Install the binary
mkdir -p %{buildroot}%{_bindir}
cp -p ltl2ba %{buildroot}%{_bindir}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p ltl2ba.1 %{buildroot}%{_mandir}/man1

%files
%doc README
%license LICENSE
%{_bindir}/ltl2ba
%{_mandir}/man1/ltl2ba.1*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Jerry James <loganjerry@gmail.com> - 1.3-1
- Version 1.3
- All patches have been upstreamed
- Link with RPM_LD_FLAGS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 1.2-5
- Add -common patch to fix build with GCC 10
- Add man page

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  9 2018 Jerry James <loganjerry@gmail.com> - 1.2-1
- New upstream version

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Jerry James <loganjerry@gmail.com> - 1.1-11
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec  9 2013 Jerry James <loganjerry@gmail.com> - 1.1-8
- Add -warning patch (bz 1037182)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 1.1-3
- Rebuild for GCC 4.7
- Minor spec file cleanups

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug   5 2010 David A. Wheeler <dwheeler@dwheeler.com> 1.1-2
- Changed spelling of "Buchi" to use only ASCII characters (per Mark Rader)
- Added simple "check" section to detect inability to execute

* Fri Jul  30 2010 David A. Wheeler <dwheeler@dwheeler.com> 1.1-1
- Initial packaging

