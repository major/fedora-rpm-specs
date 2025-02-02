Name:		packmol
Version:	20.15.3
Release:	1%{?dist}
Summary:	Packing optimization for molecular dynamics simulations
License:	MIT
URL:		http://m3g.iqm.unicamp.br/packmol/
Source0:	https://github.com/m3g/packmol/archive/v%{version}/packmol-%{version}.tar.gz
# Example files
Source2:        https://m3g.github.io/packmol/examples/examples.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-gfortran

%description
Packmol creates an initial point for molecular dynamics simulations by
packing molecules in defined regions of space. The packing guarantees
that short range repulsive interactions do not disrupt the
simulations.

The great variety of types of spatial constraints that can be
attributed to the molecules, or atoms within the molecules, makes it
easy to create ordered systems, such as lamellar, spherical or tubular
lipid layers.

The user must provide only the coordinates of one molecule of each
type, the number of molecules of each type and the spatial constraints
that each type of molecule must satisfy.

The package is compatible with input files of PDB, TINKER, XYZ and
MOLDY formats.


%prep
%setup -q
find . -name \*.o -delete
tar zxvf %{SOURCE2}

%build
export FC=gfortran
%cmake
%cmake_build

%install
%cmake_install
install -D -p -m 755 solvate.tcl %{buildroot}%{_bindir}/packmol_solvate

%check
cd examples
for f in interface.inp; do
    out=$(basename $f .inp).out
    ../redhat-linux-build/packmol < $f | tee  $out
    ok=$(grep "Success" $out|wc -l)
    if(( ! $ok )); then
	echo "Example failed to run"
	exit
    fi
done

%files
%doc AUTHORS
%license LICENSE
%{_bindir}/packmol
%{_bindir}/packmol_solvate

%changelog
* Fri Jan 31 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.15.3-1
- Update to 20.15.3.

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 17 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.15.1-1
- Update to 20.15.1.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.14.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.14.2-1
- Update to 20.14.2.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.11.1-1
- Update to 20.11.1.

* Thu Nov 10 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.11.0-1
- Update to 20.11.0.

* Fri Nov 04 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.3.6-1
- Update to 20.3.6.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.010-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.010-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.010-5
- Adapt to new CMake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.010-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.010-1
- Update to 20.010.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.013-1
- Update to 18.013.
- License changes to MIT.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.217-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.217-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.217-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 15.217-3
- Rebuilt for libgfortran soname bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 15.217-1
- Update to 15.217.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.243-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.243-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.243-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 05 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 13.243-1
- Update to 13.243.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.2.023-1
- Update to 1.1.2.023.

* Sat Jan 21 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.2.017-1
- Update to 1.1.2.017.

* Tue Sep 27 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.1.258-1
- Initial release.
