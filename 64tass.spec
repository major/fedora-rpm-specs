%global revision 2900

Name:		64tass
Version:	1.57.%{revision}
Release:	1%{?dist}
Summary:	6502 assembler
License:	GPLv2+
URL:		http://tass64.sourceforge.net/
BuildRequires:	gcc
BuildRequires:	w3m
BuildRequires:	make
Source0:	http://sourceforge.net/projects/tass64/files/source/%{name}-%{version}-src.zip

%description
64tass is a multi-pass optimizing macro assembler for the 65xx series of
processors. It supports the 6502, 65C02, R65C02, W65C02, 65CE02, 65816,
DTV, and 65EL02, using a syntax similar to that of Omicron TASS and TASM.

%prep
%autosetup -n %{name}-%{version}-src
rm README  # will be built

# be verbose during build
sed -i -e 's/.SILENT://' Makefile

%build
%make_build CFLAGS='%{build_cflags} -DREVISION="\""%{revision}"\""' LDFLAGS="%{build_ldflags}"

%install
# install binaries
install -d %{buildroot}%{_bindir}/
install -m 755 64tass %{buildroot}%{_bindir}/
# install man page
install -d %{buildroot}%{_mandir}/man1
install -m 644 64tass.1 %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc README.html
%doc LICENSE-GPL-2.0
%doc LICENSE-LGPL-2.0 LICENSE-LGPL-2.1
%doc LICENSE-my_getopt

%changelog
* Fri Jan 06 2023 Dan Horák <dan[at]danny.cz> - 1.57.2900-1
- Update to 1.57.2900 (rhbz#2140305)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.2625-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.2625-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.56.2625-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Dan Horák <dan[at]danny.cz> - 1.56.2625-1
- Update to 1.56.2625 (#1953379)
- Use distro-wide compiler/linker flags

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.55.2200-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.55.2200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 07 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.55.2200-1
- Update to 1.55.2200 fixes rhbz#1821925

* Mon Apr 06 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.55.2176-4
- Update to 1.55.2176 fixes rhbz#1816374

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.54.1900-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.54.1900-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.54.1900-1
- Rebuilt for new upstream release 1.54.1900, fixes rhbz #1672124

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.53.1515-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.53.1515-4
- spec cleanup and modernization

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.53.1515-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.53.1515-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 05 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.53.1515-1
- Rebuilt for new upstream release 1.53.1515, fixes rhbz #1447034

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.1237-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.1237-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52.1237-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.52.1237-1
- Rebuilt for new upstream release 1.52.1237, fixes rhbz #1063717

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.727-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.51.727-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 29 2014 Eric Smith <brouhaha@fedoraproject.org> 1.51.727-1
- Update to latest upstream

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.51.716-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Eric Smith <brouhaha@fedoraproject.org> 1.51.716-1
- Update to latest upstream

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50.486-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 11 2013 Eric Smith <brouhaha@fedoraproject.org> 1.50.486-1
- Initial version
