
Summary: Automated theorem prover for first-order equational logic
Name: eqp
Version: 09e
Release: 19%{?dist}
License: Public Domain
URL: http://www.cs.unm.edu/~mccune/eqp/
Source0: http://www.cs.unm.edu/~mccune/old-ftp/eqp-09e.tar.gz
# file to clarify the software license
Patch0: eqp-09e-license.patch
# patches for some missing function prototypes
Patch1: eqp-09e-missing-proto.patch
# patches for printing of pointer variables
Patch2: eqp-09e-printf.patch
# patches for duplicate definition of the Clocks global
Patch3: eqp-09e-clocks.patch

BuildRequires:  gcc
BuildRequires: make
%description
EQP is an automated theorem proving program for first-order equational
logic. Its strengths are good implementations of associative-commutative
unification and matching, a variety of strategies for equational
reasoning, and fast search. It seems to perform well on many
problems about lattice-like structures.

EQP is not a stable and polished production theorem prover like Otter
or Prover9. Since it has obtained several interesting results, it was
decided to make it available (including the source code) to everyone, with
no restrictions (and of course no warranty either). EQP's documentation
is not great, but if you already know Otter, you probably will not have
great difficulty in learning to use EQP.

In the early 1930's, it was postulated that every Robbin's Algebra,
(named after Herbert Ellis Robbins), must also be a Boolean Algebra. Many
human mathematicians attempted to find a proof, or a counter-example
of this conjecture, but failed. The EQP automated theorem prover
(and its author William McCune) made history by providing the first
known proof in 1996. The EQP input files for proving Robbin's
Conjecture can be found in the package documentation directory
%{_docdir}/%{name}-%{version}/examples/robbins/

%prep
%setup -q
%patch0 -p1 -b .license
%patch1 -p1 -b .missing-proto
%patch2 -p1 -b .printf
%patch3 -p1 -b .clocks

%build
# upstream does not use autoconf, just run make
make %{?_smp_mflags} CFLAGS="%{optflags} -DTP_RUSAGE" eqp

%install
# install the executable as "eqp"
install -d                   ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 eqp%{version} ${RPM_BUILD_ROOT}%{_bindir}/eqp
# remove the "go" shell script from the examples subdir (no executables in doc!)
rm -f examples/go

%check
# define a function to run the eqp executable and test if a proof was found
run_eqp( )
{
  # if a proof is found, eqp will return status = 10
  { ./eqp%{version} < ${1} > /dev/null 2>&1 ; RC=${?} ; } || true
  # check the return status to see if a proof was found
  test ${RC} -eq 10
}
# run some of the simple examples as rudimentary tests of the executable,
# proofs should be found quickly in all of these examples provided with eqp
run_eqp "examples/ortholattice/e2.in"
run_eqp "examples/ring/x2.in"
run_eqp "examples/robbins/eqp-lemma0.in"

%files
%doc ChangeLog Manual.txt README basic.doc examples
%license LICENSE
%attr(0755,root,root) %{_bindir}/eqp

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 09e-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 09e-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 09e-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 09e-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 09e-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 John C. Peterson <jcp@eskimo.com> - 09e-14
- Added a patch to remove a duplicate definition of the Clocks global variable

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 09e-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 09e-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 09e-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 09e-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 09e-9
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 09e-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 09e-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 09e-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 John C. Peterson <jcp@eskimo.com> - 09e-5
- Added copies of the emails I received from ANL to the LICENSE file
- Moved the LICENSE file from %%doc to the new %%license macro
- Added a %%check section that runs some of the simple examples

* Wed Jan  6 2016 John C. Peterson <jcp@eskimo.com> - 09e-4
- Changed the license terms to "Public Domain" as per ruling by Fedora Legal
- Added the _smp_mflags macro to the make command
- Removed the examples/go script
- Rebuild for Fedora 23

* Thu Nov 01 2012 John C. Peterson <jcp@eskimo.com> - 09e-3
- Removed the defattr line (as it is now obsolete)

* Fri Dec 23 2011 John C. Peterson <jcp@eskimo.com> - 09e-2
- Changed license terms to "Freely redistributable without restriction"
- Eliminated the makefile patch and adjusted the make command accordingly
- Eliminated the lont-int patch and crafted a new one (eqp-09e-printf.patch)
  that uses the pointer conversion flag in the relevant printf statements
- Removed all execute permission bits from the examples/go script
- Some minor, cosmetic changes to the spec file

* Sat Dec 17 2011 John C. Peterson <jcp@eskimo.com> - 09e-1
- Initial package spec file for Fedora / Red Hat Enterprise Linux
- Patches for some missing function prototypes
- Patches for long int on 64 bit architectures

