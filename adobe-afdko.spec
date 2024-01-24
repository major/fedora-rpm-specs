%global archivename afdko

Name:		adobe-afdko
Version:	3.6.1
Release:	9%{?dist}
Summary:	Adobe Font Development Kit for OpenType
# ExternalAntlr4Cpp.cmake is BSD-3-clause
# c/makeotf/makeotf_lib/build/hotpccts/pccts/* is ANTLR-PD
# afdko-3.6.1/python/afdko/pdflib/pdfgen.py is Python-2.0.1
# python/afdko/resources/ is BSD-3-Clause
License:	Apache-2.0 AND BSD-3-clause AND ANTLR-PD AND Python-2.0.1
URL:		https://github.com/adobe-type-tools/afdko
Source0:	https://github.com/adobe-type-tools/%{archivename}/releases/download/%{version}/%{archivename}-%{version}.tar.gz
Patch0: adobe-afdko-c99-1.patch
Patch1: adobe-afdko-c99-2.patch
BuildRequires:	gcc
BuildRequires:	make

%description
Adobe Font Development Kit for OpenType (AFDKO).
The AFDKO is a set of tools for building OpenType font files
from PostScript and TrueType font data.

%prep
%autosetup -p1 -n %{archivename}-%{version}

%build
%set_build_flags
pushd c
sh buildalllinux.sh release
popd

%install
install -m 0755 -d %{buildroot}/%{_bindir}
pushd c/build_all
find ./ -type f -executable -exec install -p -m 0755 "{}" \
	%{buildroot}/%{_bindir} ";"

%files
%license LICENSE.md
%doc docs/ README.md NEWS.md
%{_bindir}/*

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 3.6.1-7
- Fix C compatibility issues

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.6.1-1
- Build for latest 3.6.1 release

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.5.1-1
- Build for latest release 3.5.1

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.4.0-1
- Build for latest release 3.4.0

* Mon May 18 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.3.0-1
- Build for latest release 3.3.0

* Sat May 09 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.2.0-2
- undo the change 'Rename makeotfexe to makeotf'

* Fri Apr 3 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.2.0-1
- Build for latest release

* Mon Mar 23 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-4
- rename package name afdko to adobe-afdko

* Mon Mar 9 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-3
- Added %%set_build_flags
- Updated install script

* Mon Mar 2 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-2
- Added build dependency gcc, make
- Removed unused build dependency
- Rename makeotfexe to makeotf

* Fri Dec 13 2019 Peng Wu <pwu@redhat.com> - 3.0.1-1
- Initial Version
