Name:           makeself
Version:        2.5.0
Release:        7%{?dist}
BuildArch:      noarch
Summary:        Make self-extractable archives on Unix

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://%{name}.io/
Source:         https://github.com/megastep/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz

Patch0:         https://github.com/megastep/makeself/pull/303.patch

BuildRequires:  %{_bindir}/iconv
BuildRequires:  sed

Requires:       gzip

Recommends:     gnupg
Recommends:     openssl

Suggests:       bzip2
Suggests:       gzip
Suggests:       lz4
Suggests:       pigz
Suggests:       xz
Suggests:       zstd


%description
makeself.sh is a shell script that generates a self-extractable
tar.gz archive from a directory. The resulting file appears as a shell
script, and can be launched as is. The archive will then uncompress
itself to a temporary directory and an arbitrary command will be
executed (for example an installation script). This is pretty similar
to archives generated with WinZip Self-Extractor in the Windows world.


%prep
%autosetup -p1 -n %{name}-release-%{version}


%build
iconv --from-code=ISO-8859-1 --to-code=UTF-8 %{name}.1 | gzip > %{name}.1.gz
sed -i 's:^HEADER=.*:HEADER=/usr/libexec/makeself-header.sh:' makeself.sh


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_mandir}/man1

install -p -m755 %{name}.sh %{buildroot}%{_bindir}
install -p -m644 %{name}-header.sh %{buildroot}%{_libexecdir}
install -p -m644 %{name}.1.gz %{buildroot}%{_mandir}/man1
ln -s %{name}.sh %{buildroot}%{_bindir}/%{name}


%files
%doc README.md COPYING
%{_mandir}/man1/*
%{_libexecdir}/*
%{_bindir}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.0-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 24 2023 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.5.0-1
- Bump version to 2.5.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.4.5-1
- Bump version to 2.4.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.4.4-1
- Bump version to 2.4.4
- Patch the header script location with sed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.4.3-1
- Bump version to 2.4.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.4.2-1
- Bump version to 2.4.2
- Require gzip (default compression)
- Suggest other compression packages

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.4.0-1
- Bump version to 2.4.0
- Change the Source URL to get %%{name}-%%{version}.tar.gz
- Ship the script as makeself.sh as per upstream documentation
- Add a symbolic link to the previous script name (just makeself)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.3.1-1
- Bump version to 2.3.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.3.0-1
- Bump version to 2.3.0
- Update the URL
- Rename the patch
- Use more macros
- Require iconv
- Install the LSM file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.2.0-2
- Preserve timestamps during installation

* Sun Jul 07 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.2.0-1
- GPLv2 license update

* Mon Jun 24 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.2.0-1
- Initial spec
