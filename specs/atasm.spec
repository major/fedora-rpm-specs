Name:           atasm
Version:        1.25
Release:        3%{?dist}
Summary:        6502 cross-assembler

License:        GPL-2.0-or-later
URL:            https://github.com/CycoPH/atasm
Source0:        %{url}/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
# upstream fixes
Patch0:         %{name}-1.25-fixes.patch

BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  make


%description
ATasm is a 6502 command-line cross-assembler that is compatible with the
original Mac/65 macro-assembler released by OSS software.  Code
development can now be performed using "modern" editors and compiles
with lightning speed.


%prep
%autosetup -p1


%build
pushd src
%make_build CFLAGS="%{build_cflags} -DZLIB_CAPABLE -DUNIX" L="%{build_ldflags} -lz -lm"
sed -e 's|\%\%DOCDIR\%\%|%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}|g' %{name}.1.in > %{name}.1
popd


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

pushd src
install -p -m 755 %{name} %{buildroot}%{_bindir}
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1
popd


%check
pushd tests
make test
popd


%files
%license LICENSE
%doc VERSION.TXT README.md docs/atasm.blurb docs/atasm.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 07 2024 Dan Horák <dan[at]danny.cz> - 1.25-1
- update to 1.25 (rhbz#2279371)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 01 2024 Dan Horák <dan[at]danny.cz> - 1.23-1
- update to 1.23 from an active fork

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Dan Horák <dan[at]danny.cz> - 1.09-1
- update to 1.09 - CVE-2019-19785 CVE-2019-19786 CVE-2019-19787

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Dan Horák <dan[at]danny.cz> - 1.08-7
- pass correct linker flags

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.08-5
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Dan Horák <dan[at]danny.cz> - 1.08-1
- update to 1.08

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Dan Horák <dan[at]danny.cz> - 1.07d-7
- spec file cleanup

* Sat Jul 27 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.07d-6
- Honor %%{_pkgdocdir} where available.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 25 2010 Dan Horák <dan[at]danny.cz> - 1.07d-1
- update to 1.07d

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr  7 2009 Dan Horák <dan[at]danny.cz> - 1.06-2
- don't compress the man page

* Thu Mar 19 2009 Dan Horák <dan[at]danny.cz> - 1.06-1
- update to 1.06

* Sun Oct  7 2007 Dan Horák <dan[at]danny.cz> - 1.05-0.1.beta
- initial Fedora version
