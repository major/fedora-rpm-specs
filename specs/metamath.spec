Name:           metamath
Version:        0.198
Release:        9%{?dist}
Summary:        Construct mathematics from basic axioms

License:        GPL-2.0-or-later
URL:            https://us.metamath.org/
VCS:            site:https://github.com/metamath/metamath-exe.git
Source0:        https://us.metamath.org/downloads/%{name}.tar.bz2
Source1:        https://us.metamath.org/latex/%{name}.tex

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(makecell.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(tabu.sty)

Suggests:       rlwrap

%description
Metamath is a tiny language that can express theorems in abstract
mathematics, accompanied by proofs that can be verified by a computer
program.  Metamath lets you see mathematics developed in complete detail
from first principles, with absolute rigor.

%package        theories
Summary:        Existing mathematical theories in the metamath format
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

# peano.mm is GPL-2.0-or-later; all other theory files are CC0
License:        GPL-2.0-or-later AND CC0-1.0

%description    theories
This package contains metamath theory files for several branches of
mathematics, such as ZFC set theory, HOL, and Peano arithmetic.

%package        doc
# The content is CC0-1.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:        CC0-1.0 AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
Summary:        The Metamath book
BuildArch:      noarch

%description    doc
This package contains The Metamath book, which provides an in-depth
understanding of the Metamath language and program.  The first part of
the book also includes an easy-to-read informal discussion of abstract
mathematics and computers, with references to other proof verifiers and
automated theorem provers.

%prep
%autosetup -n %{name}

%conf
cp -p %{SOURCE1} .
touch special-settings.sty

# Remove prebuilt objects
rm metamath.exe

# Do not override our choice of CFLAGS
sed -i '/Try to optimize/,/^$/d' configure.ac

# Generate the configure script
autoreconf -fi

%build
%configure CFLAGS="%{build_cflags} -DINLINE=inline -fwrapv"
%make_build

# Build the manual
touch metamath.ind
pdflatex metamath
pdflatex metamath
bibtex metamath
makeindex metamath.idx
pdflatex metamath
pdflatex metamath
pdflatex metamath

%install
%make_install

# Install all of the theories
cp -p *.mm %{buildroot}%{_datadir}/metamath

# Install the manual
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -p %{name}.pdf %{buildroot}%{_docdir}/%{name}

%check
# Check proof validity
run_verify() {
./metamath << EOF
read $1
set scroll continuous
verify proof *
quit
EOF
}

for fil in *.mm; do
  run_verify $fil
done

%files
%doc README.TXT
%license LICENSE.TXT
%{_bindir}/metamath
%{_mandir}/man1/metamath.1*

%files theories
%{_datadir}/metamath/

%files doc
%license LICENSE.TXT
%dir %{_docdir}/metamath/
%{_docdir}/metamath/metamath.pdf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.198-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.198-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.198-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.198-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0.198-5
- Stop building for 32-bit x86

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.198-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.198-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 0.198-3
- Convert License tags to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.198-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 0.198-2
- Add %%check script

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.198-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug  8 2021 Jerry James <loganjerry@gmail.com> - 0.198-1
- Version 0.198

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.196-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.196-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Jerry James <loganjerry@gmail.com> - 0.196-1
- Version 0.196

* Mon Dec 28 2020 Jerry James <loganjerry@gmail.com> - 0.194-1
- Version 0.194

* Thu Sep 17 2020 Jerry James <loganjerry@gmail.com> - 0.193-1
- Version 0.193

* Mon Sep  7 2020 Jerry James <loganjerry@gmail.com> - 0.192-1
- Version 0.192

* Mon Aug 24 2020 Jerry James <loganjerry@gmail.com> - 0.188-1
- Version 0.188

* Tue Aug 18 2020 Jerry James <loganjerry@gmail.com> - 0.187-1
- Version 0.187

* Sun Aug  9 2020 Jerry James <loganjerry@gmail.com> - 0.186-1
- Version 0.186

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.184-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Jerry James <loganjerry@gmail.com> - 0.184-1
- Version 0.184

* Wed Jul  1 2020 Jerry James <loganjerry@gmail.com> - 0.183-1
- Version 0.183

* Mon Apr 13 2020 Jerry James <loganjerry@gmail.com> - 0.182-1
- Version 0.182

* Thu Feb 13 2020 Jerry James <loganjerry@gmail.com> - 0.181-1
- Version 0.181

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.180-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Jerry James <loganjerry@gmail.com> - 0.180-1
- Version 0.180

* Sat Nov 30 2019 Jerry James <loganjerry@gmail.com> - 0.179-1
- Version 0.179

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 0.178-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.177-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Jerry James <loganjerry@gmail.com> - 0.177-1
- New upstream version

* Tue Mar 26 2019 Jerry James <loganjerry@gmail.com> - 0.176-1
- New upstream version

* Sat Mar  9 2019 Jerry James <loganjerry@gmail.com> - 0.175-1
- New upstream version

* Sat Feb 23 2019 Jerry James <loganjerry@gmail.com> - 0.174-1
- New upstream version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.172-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 0.172-1
- New upstream version

* Wed Jan  2 2019 Jerry James <loganjerry@gmail.com> - 0.171-1
- New upstream version

* Tue Dec 11 2018 Jerry James <loganjerry@gmail.com> - 0.168-1
- New upstream version

* Mon Nov 19 2018 Jerry James <loganjerry@gmail.com> - 0.167-1
- New upstream version

* Sat Nov 10 2018 Jerry James <loganjerry@gmail.com> - 0.166-1
- New upstream version

* Mon Oct 29 2018 Jerry James <loganjerry@gmail.com> - 0.165-1
- New upstream version

* Sat Sep 22 2018 Jerry James <loganjerry@gmail.com> - 0.164-1
- New upstream version

* Sat Aug  4 2018 Jerry James <loganjerry@gmail.com> - 0.163-1
- New upstream version (bz 1612479)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.162-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Jerry James <loganjerry@gmail.com> - 0.162-1
- New upstream version (bz 1585859)

* Tue Feb  6 2018 Jerry James <loganjerry@gmail.com> - 0.161-1
- New upstream version (bz 1541620)

* Thu Jan 25 2018 Jerry James <loganjerry@gmail.com> - 0.160-1
- New upstream version (bz 1538606)

* Thu Jan 18 2018 Jerry James <loganjerry@gmail.com> - 0.157-1
- New upstream version (bz 1536242)

* Tue Dec 19 2017 Jerry James <loganjerry@gmail.com> - 0.156-1
- New upstream version (bz 1527497)

* Mon Oct 23 2017 Jerry James <loganjerry@gmail.com> - 0.155-1
- New upstream version (bz 1504397)

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 0.152-1
- New upstream version (bz 1497491)

* Tue Sep 26 2017 Jerry James <loganjerry@gmail.com> - 0.151-1
- New upstream version (bz 1495184)

* Sat Sep  2 2017 Jerry James <loganjerry@gmail.com> - 0.150-1
- New upstream version (bz 1485749)

* Wed Aug 23 2017 Jerry James <loganjerry@gmail.com> - 0.149-1
- New upstream version (bz 1484389)

* Thu Aug 17 2017 Jerry James <loganjerry@gmail.com> - 0.148-1
- New upstream version (bz 1482724)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.146-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.146-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul  3 2017 Jerry James <loganjerry@gmail.com> - 0.146-1
- New upstream version (bz 1467070)

* Tue Jun 27 2017 Jerry James <loganjerry@gmail.com> - 0.145-1
- New upstream version (bz 1462574)

* Tue May 16 2017 Jerry James <loganjerry@gmail.com> - 0.144-1
- New upstream version (bz 1450652)

* Mon May  8 2017 Jerry James <loganjerry@gmail.com> - 0.141-1
- New upstream version (bz 1448745)

* Tue Feb 14 2017 Jerry James <loganjerry@gmail.com> - 0.139-1
- New upstream version (bz 1406763)
- Install all of the theories (bz 1422091)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.138-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Jerry James <loganjerry@gmail.com> - 0.138-1
- New upstream version (bz 1406763)

* Mon Sep 19 2016 Jerry James <loganjerry@gmail.com> - 0.135-1
- New upstream version (bz 1377308)

* Sat Aug 27 2016 Jerry James <loganjerry@gmail.com> - 0.134-1
- New upstream version (bz 1370745)

* Fri Aug 19 2016 Jerry James <loganjerry@gmail.com> - 0.133-1
- New upstream version

* Mon Jul 18 2016 Jerry James <loganjerry@gmail.com> - 0.132-1
- New upstream version

* Tue Jun 21 2016 Jerry James <loganjerry@gmail.com> - 0.131-1
- New upstream version

* Wed May 11 2016 Jerry James <loganjerry@gmail.com> - 0.125-2
- Fix unowned directory
- Add the manual

* Fri May  6 2016 Jerry James <loganjerry@gmail.com> - 0.125-1
- Initial RPM
